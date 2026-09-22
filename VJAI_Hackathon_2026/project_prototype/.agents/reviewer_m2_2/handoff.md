# Milestone 2 Review & Adversarial Challenge Report

**Reviewer**: Milestone 2 Reviewer 2 (Self-Correction & Dual-Tier Memory)  
**Target Milestone**: Milestone 2 (Multi-Agent Core Engine, Tools & Dual-Tier Memory)  
**Parent Orchestrator**: `9ed17e46-bddf-44f6-9b7f-776ff56dd363`  
**Date**: 2026-09-08  
**Verdict**: **REQUEST_CHANGES**

---

## 1. Observation

### Obs 1. Test Suite Results
Direct execution of tests via command line:
1. `py -m pytest tests/test_agent_core_m2.py -v`:
   - Result: 19 passed in 10.11s.
   - All unit tests in `TestAgentStateAndSupervisor`, `TestWorkerAgents`, `TestAutomatedToolSuite`, `TestSelfCorrectionAndReflexion`, `TestDualTierMemory`, and `TestThoughtStreamingAndE2E` passed.
2. `py tests/e2e_runner.py --all`:
   - Result: 80 passed across Tier 1 (35 tests), Tier 2 (20 tests), Tier 3 (15 tests), Tier 4 (10 tests) in 2.41s.
   - Status: 100% PASSED reported by runner.

### Obs 2. Router Infinite Loop under Reflexion Retry (`core/agents/supervisor.py:112-144`)
Inspection of `route_supervisor_decision` in `core/agents/supervisor.py`:
```python
112: def route_supervisor_decision(state: AgentState) -> str:
...
128:     # Check 4: Has critic evaluated?
129:     verdict = state.get("critic_verdict", {})
130:     if not verdict.get("feedback"):
131:         # First time reaching critic
132:         return "critic_agent"
133: 
134:     # Check 5: Reflexion loop if critic rejected
135:     if not verdict.get("approved", False):
136:         if verdict.get("retry_count", 0) < 3:
137:             # Reflexion retry: loop back to dispatch_agent to adjust parameters
138:             return "dispatch_agent"
139:         else:
140:             # Circuit breaker exceeded max retries
141:             return "FINISH"
142: 
143:     # Plan approved: conclude execution
144:     return "FINISH"
```
When `critic_agent` rejects an initial plan (`approved: False, retry_count: 1, feedback: "REJECT: ..."`):
1. `route_supervisor_decision` routes to `dispatch_agent`.
2. `dispatch_agent_node` executes and scales down water prescription, but does NOT reset `state["critic_verdict"]`.
3. Control returns to `supervisor`, which calls `route_supervisor_decision(state)`.
4. `verdict.get("feedback")` is still non-empty string.
5. `verdict.get("approved", False)` is still `False`.
6. `verdict.get("retry_count", 0)` is still `1 < 3`.
7. `route_supervisor_decision` returns `"dispatch_agent"` AGAIN. It NEVER routes to `"critic_agent"` to re-evaluate the corrected plan!

Verification via command reproduction:
```python
# Tested in Python session:
state['dispatch_plan'] = {'water_needed_mm': 100.0, 'duration_minutes': 500}
state = critic_agent_node(state)
print(route_supervisor_decision(state)) # -> 'dispatch_agent'
state = dispatch_agent_node(state)
print(route_supervisor_decision(state)) # -> 'dispatch_agent' (STUCK IN LOOP!)
```
When executed through `stream_agent_execution`, it emitted:
`Thought steps: ['planning', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch', 'dispatch']` (15 repeated dispatch loops until `max_steps` cutoff, never returning to Critic).

### Obs 3. Carbon Emissions Never Re-Audited on Revised Dispatch Plan
In `supervisor_node` and `graph.py`:
When `dispatch_agent` corrects the water needed from 100mm to 25mm, `carbon_agent` is never re-run. If execution were to proceed, the ESG Ledger would commit the carbon emissions calculated from the original faulty 100mm dosage rather than the corrected 25mm dosage.

### Obs 4. Type Safety and Negative Value Gaps in Critic (`core/agents/critic_agent.py:13-58`)
In `evaluate_plan_by_critic`:
```python
27:     water_mm = float(dispatch_plan.get("water_needed_mm", 0.0))
...
44:     duration = int(dispatch_plan.get("duration_minutes", 0))
```
- If `dispatch_plan.get("water_needed_mm")` is `None` or a non-numeric string (e.g. from an upstream tool failure or malformed payload), `float(None)` raises `TypeError` and crashes the agent.
- If `water_needed_mm` is negative (e.g. `-50.0`) or `duration_minutes` is negative (e.g. `-100`), neither triggers `water_mm > 60.0` nor `duration > 480`. The critic approves negative dosages (`approved: True`), which violates physical domain constraints.

### Obs 5. Dual-Tier Memory Fallback Limitation (`core/memory/vector_store.py:180-200`)
In `LongTermVectorMemory`:
ChromaDB is properly integrated (ChromaDB 1.5.9 verified installed).
However, in `_lexical_search_fallback`:
```python
184:         for item in DEFAULT_DOMAIN_DOCUMENTS:
```
The fallback search only indexes `DEFAULT_DOMAIN_DOCUMENTS`. When `collection_name == "episodic_memory"`, fallback search returns domain documents instead of episodic reflections.

### Obs 6. Test Masking of Closed-Loop Reflexion (`tests/test_agent_core_m2.py:224-243`)
In `TestSelfCorrectionAndReflexion`:
`test_reflexion_self_correction_recovers_cleanly` manually called `evaluate_plan_by_critic`, then manually invoked `dispatch_agent_node`, then manually invoked `evaluate_plan_by_critic` again. It never called `run_agent_workflow` or `stream_agent_execution` through a multi-step retry loop. Similarly, `tests/tier3_pairwise/test_critic_self_correction_pipeline.py` manually assigned states and verified functions in isolation. Consequently, the infinite loop defect in `route_supervisor_decision` went undetected.

---

## 2. Logic Chain

1. **Premise 1 (Acceptance Criteria R2 & AC 3)**:
   ORIGINAL_REQUEST.md § Acceptance Criteria mandates: "Agent tự chủ giải quyết luồng công việc từ đầu đến cuối mà không cần can thiệp từng bước của con người" and "Có cơ chế bắt lỗi và tự sửa sai (Self-Correction loop) khi tool trả về kết quả không hợp lệ."
2. **Premise 2 (Obs 2 Observation)**:
   In `core/agents/supervisor.py`, when a plan is rejected by `critic_agent`, `route_supervisor_decision` routes to `dispatch_agent`. After `dispatch_agent` updates the plan, the router is re-evaluated with unchanged `critic_verdict` (`approved == False`).
3. **Deduction 1**:
   Because `critic_verdict["approved"]` remains `False` and `critic_verdict["feedback"]` is non-empty, `route_supervisor_decision` continuously evaluates Check 5 and returns `"dispatch_agent"` infinitely.
4. **Deduction 2**:
   The workflow never returns to `critic_agent` to evaluate the corrected plan, never updates `retry_count`, never trips the circuit breaker through repeated node execution, and never reaches `carbon_agent` or `FINISH`. In LangGraph `app.invoke`, it causes infinite recursion. In `stream_agent_execution`, it burns all steps looping in `dispatch_agent`.
5. **Conclusion**:
   The autonomous self-correction loop does not function end-to-end within the LangGraph orchestrator. This is a critical functional blocker for Milestone 2 acceptance.

---

## 3. Caveats

- ChromaDB is fully functional in the environment (`v1.5.9`) and passes all vector retrieval tests.
- The 4 automated tools (`weather_tool`, `telemetry_tool`, `carbon_tool`, `ledger_tool`) are well-implemented, utilize real calculations (Penman-Monteith, IPCC AFOLU Tier 1/2, SHA-256 hash chaining), and include robust offline fallbacks.
- The isolated unit logic of `critic_agent.py` (`evaluate_plan_by_critic`) and `dispatch_agent.py` correctly handles dosage reductions when called manually.
- The issue is localized strictly to state-machine transition tracking in `core/agents/supervisor.py` (and state synchronization in `core/agents/dispatch_agent.py` / `graph.py`).

---

## 4. Conclusion & Findings

**Verdict**: **REQUEST_CHANGES**

### Critical Findings

#### [Critical] Finding 1: Infinite Routing Loop in Supervisor State Machine during Reflexion
- **Where**: `core/agents/supervisor.py:129-142` (`route_supervisor_decision`) and `core/agents/dispatch_agent.py`.
- **Why**: When `critic_agent` rejects a plan, `dispatch_agent` updates `state["dispatch_plan"]`, but `state["critic_verdict"]` is not marked as needing re-evaluation. `route_supervisor_decision` continues to see `approved == False` and routes to `dispatch_agent` repeatedly.
- **Remediation**:
  1. In `dispatch_agent_node`: When re-planning occurs following a critic rejection, flag the plan as revised (e.g., set `state["critic_verdict"]["pending_review"] = True` or clear `state["critic_verdict"]["feedback"] = ""`).
  2. In `route_supervisor_decision`:
     If `critic_verdict` has `pending_review == True` (or empty feedback), route to `"critic_agent"`.
  3. Re-route approved revised plans through `carbon_agent` before committing to ensure the ESG Ledger records emissions based on the corrected dosage.

### Major Findings

#### [Major] Finding 2: Lack of Input Sanitization and Physical Bound Checking in Critic
- **Where**: `core/agents/critic_agent.py:26-50` (`evaluate_plan_by_critic`).
- **Why**: `float(dispatch_plan.get("water_needed_mm", 0.0))` will crash with `TypeError` if value is `None` or `ValueError` if non-numeric string. Negative values (`water_needed_mm < 0` or `duration_minutes < 0`) pass without error.
- **Remediation**:
  Wrap type casting in a try/except block; validate that `water_needed_mm >= 0.0` and `duration_minutes >= 0`; reject any negative or non-numeric values with explicit feedback.

#### [Major] Finding 3: E2E Test Suite Did Not Exercise Graph-Level Reflexion
- **Where**: `tests/test_agent_core_m2.py:224-243` and `tests/tier3_pairwise/test_critic_self_correction_pipeline.py`.
- **Why**: Tests only validated individual node functions step-by-step, masking the supervisor routing infinite loop.
- **Remediation**:
  Add an integration test that runs `run_agent_workflow(initial_state)` and `list(stream_agent_execution(initial_state))` where the initial conditions force a critic rejection (e.g. `field_capacity` or initial deficit triggering >60mm water requirement), and assert that the workflow completes autonomously with `critic_verdict["approved"] == True` and `retry_count == 1`.

---

## 5. Verification Method

To verify the fixes once implemented:
1. Run standard unit tests:
   ```bash
   py -m pytest tests/test_agent_core_m2.py -v
   ```
2. Run graph-level self-correction test:
   ```python
   from core.agents.state import create_initial_agent_state
   from core.agents.graph import stream_agent_execution
   state = create_initial_agent_state("verify_fix", "an_giang_rice_001", "Test")
   state['dispatch_plan'] = {'water_needed_mm': 100.0, 'duration_minutes': 500}
   from core.agents.critic_agent import critic_agent_node
   state = critic_agent_node(state)
   events = list(stream_agent_execution(state))
   # Assert events include: dispatch -> guardrail_verification (reflection) -> complete
   steps = [e['data']['step'] for e in events if e.get('event') in ('thought', 'reflection')]
   assert "guardrail_verification" in steps
   ```
3. Run complete E2E suite:
   ```bash
   py tests/e2e_runner.py --all
   ```
