# FIX SPECIFICATION — Milestone 2 Remediation Track 1: Reflexion Routing State Machine

**Agent:** Milestone 2 Remediation Explorer 1 (`explorer_m2_fix_1`)  
**Target Files:**
- `core/agents/dispatch_agent.py`
- `core/agents/graph.py`
- `core/agents/supervisor.py`
**Adversarial Benchmark:** `tests/tier5_adversarial/test_m2_empirical_challenger.py`  
**Date:** 2026-09-08  
**Status:** Approved by Empirical Verification (32/32 tests passing)

---

## 1. Executive Summary & Root Cause Analysis

### 1.1 The Failure Mode
In adversarial tests (`test_m2_empirical_challenger.py`), three critical tests failed:
1. `TestCriticRejectionAndReflexion::test_reflexion_self_correction_recovers_to_valid_plan`
   - **Error:** `AssertionError: Expected routing to critic_agent or carbon_agent after plan correction, but got: dispatch_agent`
2. `TestCriticRejectionAndReflexion::test_langgraph_e2e_circuit_breaker_termination`
   - **Error:** `langgraph.errors.GraphRecursionError: Recursion limit of 15 reached without hitting a stop condition.`
3. `TestCriticRejectionAndReflexion::test_sse_stream_circuit_breaker_emission`
   - **Error:** `AssertionError: assert 'error' in event_types` (Stream looped in `dispatch_agent` 15 times, never re-evaluated Critic or tripped circuit breaker).

### 1.2 Mathematical & Architectural Root Cause
Two interconnected design flaws caused this failure:

1. **Stale Feedback Deadlock in `dispatch_agent_node`:**
   - When `critic_agent_node` rejects an invalid proposal (e.g. `water_needed_mm = 120.0`), it populates `state["critic_verdict"] = {"approved": False, "retry_count": 1, "feedback": "REJECT: ..."}`.
   - `route_supervisor_decision` routes control to `dispatch_agent` for Reflexion.
   - `dispatch_agent_node` consumes the feedback and scales down parameters (e.g. `water_needed_mm = 25.0`).
   - However, `dispatch_agent_node` **never cleared or reset** `state["carbon_report"]` and **never cleared** `state["critic_verdict"]["feedback"]`.
   - When control returned to `route_supervisor_decision`:
     - `state["carbon_report"]` was non-empty (stale carbon calculation from 120mm).
     - `state["critic_verdict"]["feedback"]` was non-empty (`"REJECT: ..."`).
     - `verdict["approved"]` was `False`, and `retry_count` was `1 < 3`.
     - Router returned `"dispatch_agent"` again!
   - Result: Infinite loop between `supervisor` and `dispatch_agent`. `critic_agent` was never re-invoked, `carbon_agent` was bypassed, and `retry_count` never incremented past 1.

2. **Graph Topology Superstep Inflation in `build_agricarbon_graph`:**
   - In `core/agents/graph.py`, every worker had a return edge directly to `supervisor`:
     `workflow.add_edge("sensing_agent", "supervisor")`, `workflow.add_edge("dispatch_agent", "supervisor")`, etc.
   - In LangGraph's Pregel engine, each node execution constitutes 1 step.
   - With every worker returning to `supervisor`, every single transition took 2 Pregel steps (worker + supervisor).
   - For an initial cycle (4 workers): $2 \times 4 + 1 = 9$ steps.
   - For 3 retries, each retry required $3 \text{ workers} \times 2 = 6$ steps.
   - Total steps to reach circuit breaker: $9 + 6 \times 3 = 27$ steps!
   - Under `recursion_limit: 15`, LangGraph crashed at Step 15 before retry 2 or 3 could even execute!

---

## 2. Proposed Architecture & State Flow

### 2.1 State Transition Lifecycle
```
[START]
   │
   ▼
[supervisor] ──(route_supervisor_decision)──► [sensing_agent]
                                                     │
                                                     ▼
                                              [dispatch_agent] ◄──────────────┐
                                                     │                        │ (Reflexion
                                                     ▼                        │  if rejected
                                              [carbon_agent]                  │  & retries < 3)
                                                     │                        │
                                                     ▼                        │
                                              [critic_agent]                  │
                                                     │                        │
                                                     ▼                        │
                                              [supervisor] ───────────────────┘
                                                │         │
                   (if approved: commit ledger) │         │ (if retries >= 3: safe_abort)
                                                ▼         ▼
                                              [END]     [END]
```

### 2.2 Step Count Optimization
By chaining workers in a forward execution pipeline (`sensing -> dispatch -> carbon -> critic -> supervisor`), intermediate supervisor ping-pong is eliminated while maintaining full ReAct supervision:
- **Zero-retry Happy Path:** 6 steps (START -> supervisor -> sensing -> dispatch -> carbon -> critic -> supervisor -> END).
- **1-retry Self-Correction:** 10 steps (initial 5 -> supervisor -> dispatch -> carbon -> critic -> supervisor -> END), comfortably below Challenger's $\le 12$ step requirement.
- **3-retry Circuit Breaker Trip:** Exactly 14 steps (well below `recursion_limit: 15`).

---

## 3. Concrete Code Changes

### 3.1 Modification to `core/agents/dispatch_agent.py`

**Target File:** `core/agents/dispatch_agent.py`  
**Target Function:** `dispatch_agent_node(state: AgentState) -> AgentState`  
**Rationale:** Clear stale downstream state upon self-correction adjustment so that `carbon_agent` recalculates emissions and `critic_agent` re-audits the revised proposal.

```python
<<<<
    # Reflexion / Self-Correction Handling:
    # If Critic had rejected the previous plan, analyze feedback and enforce safe guardrails
    if critic_verdict and not critic_verdict.get("approved", True):
        feedback = critic_verdict.get("feedback", "").lower()
        if "fao-56" in feedback or "violates" in feedback or "water dosage" in feedback:
            # Scale down excessive water to safe compliant quota
            prescription["water_needed_mm"] = min(25.0, prescription["water_needed_mm"])
            prescription["duration_minutes"] = 48 if "rice" in crop_type.lower() else 45
            prescription["urgency"] = "MEDIUM"
        if "duration_minutes" in feedback:
            prescription["duration_minutes"] = max(30, min(75, int(prescription.get("water_needed_mm", 20.0) * 1.5)))
        if "pump motor burnout" in feedback or "8 hours" in feedback:
            prescription["duration_minutes"] = min(120, prescription.get("duration_minutes", 60))
====
    # Reflexion / Self-Correction Handling:
    # If Critic had rejected the previous plan, analyze feedback and enforce safe guardrails
    if critic_verdict and not critic_verdict.get("approved", True) and critic_verdict.get("feedback"):
        feedback = critic_verdict.get("feedback", "").lower()
        if "fao-56" in feedback or "violates" in feedback or "water dosage" in feedback:
            # Scale down excessive water to safe compliant quota
            prescription["water_needed_mm"] = min(25.0, prescription["water_needed_mm"])
            prescription["duration_minutes"] = 48 if "rice" in crop_type.lower() else 45
            prescription["urgency"] = "MEDIUM"
        if "duration_minutes" in feedback:
            prescription["duration_minutes"] = max(30, min(75, int(prescription.get("water_needed_mm", 20.0) * 1.5)))
        if "pump motor burnout" in feedback or "8 hours" in feedback:
            prescription["duration_minutes"] = min(120, prescription.get("duration_minutes", 60))

        # Reset carbon report and critique feedback so downstream nodes re-audit the revised plan
        state["carbon_report"] = {}
        if isinstance(state.get("critic_verdict"), dict):
            state["critic_verdict"]["feedback"] = ""
>>>>
```

---

### 3.2 Modification to `core/agents/graph.py`

**Target File:** `core/agents/graph.py`  
**Target Function:** `build_agricarbon_graph(checkpointer=None)`  
**Rationale:** Connect worker nodes in forward pipeline to eliminate redundant supervisor ping-pong, reducing worst-case 3-retry step count from 27 to 14.

```python
<<<<
    # 4. Return edges: workers return control back to supervisor for re-evaluation
    workflow.add_edge("sensing_agent", "supervisor")
    workflow.add_edge("dispatch_agent", "supervisor")
    workflow.add_edge("carbon_agent", "supervisor")
    workflow.add_edge("critic_agent", "supervisor")
====
    # 4. Pipeline execution edges:
    # Forward execution pipeline eliminates redundant supervisor ping-pong,
    # ensuring that 3-retry Reflexion with circuit breaker completes strictly within
    # 14 steps (<= 15 recursion limit), and 1-retry self-correction within 10 steps.
    workflow.add_edge("sensing_agent", "dispatch_agent")
    workflow.add_edge("dispatch_agent", "carbon_agent")
    workflow.add_edge("carbon_agent", "critic_agent")
    workflow.add_edge("critic_agent", "supervisor")
>>>>
```

---

### 3.3 Defensive Hardening to `core/agents/supervisor.py`

**Target File:** `core/agents/supervisor.py`  
**Target Functions:** `supervisor_node(state: AgentState)` and `route_supervisor_decision(state: AgentState)`  
**Rationale:** Defend against `None` values for `critic_verdict`.

```python
<<<<
    critic_verdict = state.get("critic_verdict", {})
====
    critic_verdict = state.get("critic_verdict") or {}
>>>>
```

```python
<<<<
    verdict = state.get("critic_verdict", {})
====
    verdict = state.get("critic_verdict") or {}
>>>>
```

---

## 4. Verification Results & Test Evidence

The proposed fix has been empirically tested across the entire project test bed:

| Test Suite | Scope | Status |
|---|---|---|
| `tests/tier5_adversarial/test_m2_empirical_challenger.py` | 32 tests (HTTP errors, DB disconnects, bounds, Reflexion loop, circuit breaker, SSE streaming) | **32 / 32 PASSED (0 failures)** |
| `tests/test_agent_core_m2.py` | 19 tests (AgentState schema, ReAct decomposition, state machine routing, tools, memory, SSE streaming, E2E) | **19 / 19 PASSED (0 failures)** |
| `tests/tier1_feature/test_supervisor_agent.py` | 6 tests (State schema, ReAct loop, worker routing transitions, critic verdict, checkpoints) | **6 / 6 PASSED (0 failures)** |
| `tests/tier3_pairwise/test_critic_self_correction_pipeline.py` | 2 tests (Error injection self-reflection recovery, safe shutdown) | **2 / 2 PASSED (0 failures)** |
| **Total Verified** | **59 tests** | **100% Pass Rate** |

---

## 5. Implementation Instructions for Implementer Agent

1. Apply the modification in Section 3.1 to `core/agents/dispatch_agent.py`.
2. Apply the modification in Section 3.2 to `core/agents/graph.py`.
3. Apply the defensive hardening in Section 3.3 to `core/agents/supervisor.py`.
4. Run verification command:
   ```bash
   py -m pytest tests/tier5_adversarial/test_m2_empirical_challenger.py -v
   ```
   Verify 32/32 tests pass with 0 errors.
5. Run regression check:
   ```bash
   py -m pytest tests/test_agent_core_m2.py tests/tier1_feature/test_supervisor_agent.py tests/tier3_pairwise/test_critic_self_correction_pipeline.py -v
   ```
   Verify 27/27 tests pass with 0 errors.
