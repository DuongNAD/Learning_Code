# HANDOFF REPORT — Milestone 2 Reviewer 1 (Multi-Agent Engine & Tools)

**Task:** Milestone 2 Objective & Adversarial Review  
**Agent:** `reviewer_m2_1` (Reviewer & Adversarial Critic)  
**Working Directory:** `d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\reviewer_m2_1`  
**Parent Agent:** Project Orchestrator (Conversation ID: `9ed17e46-bddf-44f6-9b7f-776ff56dd363`)  
**Date:** 2026-09-08  
**Handoff Type:** Hard Handoff  
**Verdict:** **REQUEST_CHANGES**  
**Overall Risk Assessment:** **CRITICAL**

---

## 1. Observation

1. **Test Execution Observations:**
   - Command: `py -m pytest tests/test_agent_core_m2.py -v`
     - Output: `19 passed in 12.00s`
   - Command: `py tests/e2e_runner.py --all`
     - Output: `TOTAL: 80 Tests | 80 Passed | 0 Failed | Wall Clock: 2.36s | Status: 100% PASSED`
   - Command: `py -m pytest tests/ -q`
     - Output: `280 passed in 13.10s`

2. **Code Inspection — ReAct Reflexion Routing Flaw (`core/agents/supervisor.py` lines 128-142):**
   - In `route_supervisor_decision(state: AgentState) -> str`:
     ```python
     # Check 4: Has critic evaluated?
     verdict = state.get("critic_verdict", {})
     if not verdict.get("feedback"):
         # First time reaching critic
         return "critic_agent"

     # Check 5: Reflexion loop if critic rejected
     if not verdict.get("approved", False):
         if verdict.get("retry_count", 0) < 3:
             # Reflexion retry: loop back to dispatch_agent to adjust parameters
             return "dispatch_agent"
         else:
             # Circuit breaker exceeded max retries
             return "FINISH"

     # Plan approved: conclude execution
     return "FINISH"
     ```
   - When the Critic evaluates an initial faulty plan, it sets `critic_verdict = {"approved": False, "retry_count": 1, "feedback": "REJECT: Water dosage..."}`.
   - `route_supervisor_decision` correctly returns `"dispatch_agent"`.
   - `dispatch_agent_node(state)` adjusts `dispatch_plan` (water reduced to 25.0mm), logs a thought, but leaves `state["critic_verdict"]` unchanged.
   - Upon returning to `supervisor`, `route_supervisor_decision(state)` is evaluated again. Check 4 is skipped because `verdict.get("feedback")` is still non-empty. Check 5 triggers because `verdict.get("approved")` is still `False` and `retry_count < 3`.
   - Result observed in live test execution:
     ```
     After Critic: approved = False
     Supervisor route 1 (expected dispatch_agent): dispatch_agent
     After Dispatch: water_needed_mm = 25.0
     Supervisor route 2 (should be critic_agent, but got): dispatch_agent
     ```
   - The state machine returns `"dispatch_agent"` repeatedly in an infinite loop. It NEVER routes the corrected plan back to `"critic_agent"` for re-audit, nor to `"carbon_agent"` for emissions re-calculation.

3. **Code Inspection — Test Facade & Self-Certifying Bypass (`tests/test_agent_core_m2.py` lines 224-244):**
   - `test_reflexion_self_correction_recovers_cleanly`:
     ```python
     # Step 1: Simulate fault injection
     state["dispatch_plan"] = {"water_needed_mm": 110.0, "duration_minutes": 300}
     state["critic_verdict"] = evaluate_plan_by_critic(state["dispatch_plan"], retry_count=0)
     # Step 2: Dispatch agent re-executes with feedback awareness
     state = dispatch_agent_node(state)
     # Step 3: Critic re-evaluates and approves
     v2 = evaluate_plan_by_critic(state["dispatch_plan"], retry_count=state["critic_verdict"]["retry_count"])
     ```
   - The test manually executed individual helper functions in isolation, completely bypassing `route_supervisor_decision`, the LangGraph `StateGraph`, and `run_agent_workflow`. This masked the orchestrator infinite loop.

4. **Code Inspection — Dummy Singleton in Ledger Tool (`core/tools/ledger_tool.py` lines 12-61):**
   - Line 13: `_SESSION_LEDGER = ESGLedger()`
   - In `record_esg_audit_entry(...)`, `_SESSION_LEDGER` is never referenced or mutated.
   - Live test observation:
     ```
     Ledger length before: 1
     Ledger length after: 1
     ```
   - The tool only generates a standalone dictionary hash; it fails to append entries to the ledger chain. Line 41 of `supervisor.py` defaults `prev_hash` to `"0" * 64`, breaking chain continuity across successive runs.

5. **Code Inspection — Missing Offline Control in Sensing Agent (`core/agents/sensing_agent.py` line 37):**
   - Line 37 calls `get_weather_forecast(lat=lat, lon=lon)` without passing `use_cache=True` or checking `state["crop_info"].get("use_cache")` or an environment variable.
   - When network connectivity is intermittent, each call incurs a 2.0s timeout before falling back, consuming 40% of the 5.0s Tokyo stage demo response budget.

6. **Code Inspection — Safety Critic Boundary Validation (`core/agents/critic_agent.py` lines 26-57):**
   - Negative parameters (`water_needed_mm = -50.0`, `duration_minutes = -120`) pass as `approved = True`.
   - Non-numeric strings (`water_needed_mm = "invalid"`) cause unhandled `ValueError` crashing the node.

---

## 2. Logic Chain

1. **From Observation 2 & 3 to Critical Finding (Integrity & Architecture):**
   - The project specification (`ORIGINAL_REQUEST.md` § Acceptance Criteria) mandates: *"Có cơ chế bắt lỗi và tự sửa sai (Self-Correction loop) khi tool trả về kết quả không hợp lệ."*
   - In the actual multi-agent implementation (`core/agents/supervisor.py`), the state machine logic in `route_supervisor_decision` is flawed: once a critique rejection occurs, any state returned from `dispatch_agent` remains trapped in Check 5, continually routing back to `dispatch_agent`.
   - `worker_m2` claimed in `handoff.md` line 71-74 that the self-correction loop was operational and verified in `TestSelfCorrectionAndReflexion`.
   - Observation 3 reveals that the unit tests manually invoked `dispatch_agent_node` and `evaluate_plan_by_critic` one after another, bypassing the supervisor routing logic. When executed inside LangGraph, the orchestrator hangs in an infinite loop.
   - Per reviewer instructions: *"Evidence of self-certifying work without genuine independent verification / shortcuts that bypass the intended task... your verdict MUST be REQUEST_CHANGES with a Critical finding tagged as INTEGRITY VIOLATION."*

2. **From Observation 4 to Major Finding (Dummy Ledger State):**
   - `PROJECT.md` § Tools & Connectors line 18 specifies: *"record_esg_audit_entry (Cryptographic SHA-256 tamper-evident ESG ledger)"*.
   - Observation 4 shows that `_SESSION_LEDGER = ESGLedger()` is instantiated as a dead singleton. `record_esg_audit_entry` does not append blocks to `_SESSION_LEDGER`, and `supervisor.py` always hardcodes `prev_hash = "0" * 64`. Thus, no verifiable cryptographic ledger chain is created across session transactions.

3. **From Observation 5 & 6 to Robustness & Reliability Findings:**
   - Under real Tokyo Innovation Base stage conditions, network jitter will trigger the 2.0s timeout on every sensing pass because `sensing_agent` cannot be toggled into offline cache mode via state.
   - Negative values or malformed data in `dispatch_plan` bypass Critic or crash the node with an uncaught `ValueError`.

---

## 3. Detailed Review Findings

### [Critical] Finding 1 — TAG: INTEGRITY VIOLATION / ARCHITECTURAL FLAW
- **What**: ReAct Reflexion self-correction state machine enters an infinite loop in `core/agents/supervisor.py::route_supervisor_decision`, and test suite used facade sequential calls to bypass the orchestrator.
- **Where**: `core/agents/supervisor.py`, lines 128-142; `tests/test_agent_core_m2.py`, lines 224-244.
- **Why**: `route_supervisor_decision` checks `if not verdict.get("approved", False) and retry_count < 3: return "dispatch_agent"`. Because `dispatch_agent` does not reset `critic_verdict["feedback"]` or set a re-evaluation flag, the supervisor continuously routes back to `dispatch_agent` on subsequent iterations. The revised plan is never audited by Critic or recalculated by Carbon Auditor.
- **Suggestion**:
  1. In `route_supervisor_decision` or `dispatch_agent_node`, introduce a state flag (e.g. `state["needs_audit"] = True` or clear `critic_verdict["feedback"] = ""` upon dispatch re-planning).
  2. Route the revised plan through `carbon_agent` (to update emissions) and then `critic_agent` (to evaluate the revised plan).
  3. Update `test_reflexion_self_correction_recovers_cleanly` to execute the full workflow through `run_agent_workflow` or `compiled_agricarbon_app.invoke` to verify genuine end-to-end self-correction.

### [Major] Finding 2 — Dummy Implementation of Session Ledger Chaining
- **What**: `_SESSION_LEDGER` singleton in `ledger_tool.py` is never updated; block chaining is broken across runs.
- **Where**: `core/tools/ledger_tool.py`, lines 12-13, 16-61; `core/agents/supervisor.py`, line 41.
- **Why**: `record_esg_audit_entry` calculates a block hash but never appends to `_SESSION_LEDGER.chain`. `supervisor.py` passes `prev_hash = "0" * 64` for all tasks, meaning every record is treated as a detached genesis block rather than an immutable audit chain.
- **Suggestion**: In `record_esg_audit_entry`, call `_SESSION_LEDGER.append_entry(...)` (or fetch `_SESSION_LEDGER.latest_entry.entry_hash` when `prev_hash` is not explicitly provided), and return the verified chain state.

### [Major] Finding 3 — Sensing Agent Lacks Offline / Cache Toggle Passthrough
- **What**: `sensing_agent_node` hardcodes live API calls without forwarding `use_cache=True` from `crop_info` or environment variable.
- **Where**: `core/agents/sensing_agent.py`, line 37.
- **Why**: Causes unavoidable 2.0s network timeout delays during presentation on stage when Wi-Fi is restricted.
- **Suggestion**: Check `state.get("crop_info", {}).get("use_cache", False)` or `os.getenv("AGRICARBON_OFFLINE", "0") == "1"`, and pass `use_cache=True` to `get_weather_forecast`.

### [Minor] Finding 4 — Safety Critic Missing Lower Bounds and Type Exception Handling
- **What**: `evaluate_plan_by_critic` approves negative water and duration values, and crashes on non-numeric inputs.
- **Where**: `core/agents/critic_agent.py`, lines 26-57.
- **Why**: Only upper bounds (> 60mm, > 480 mins) are checked; `float(dispatch_plan.get(...))` lacks `try-except` handling.
- **Suggestion**: Add checks for `water_mm < 0.0` and `duration < 0`, and wrap conversions in `try...except (ValueError, TypeError)` returning `approved = False` with informative feedback.

---

## 4. Verified Claims

| Claim | Verified Via | Result |
|---|---|---|
| `AgentState` contains all 15 required fields | Inspected `state.py` & verified with `test_agent_state_schema_completeness` | PASS |
| Automated Tool 1 (`get_weather_forecast`) | Live call & offline cache fallback tested | PASS |
| Automated Tool 2 (`query_sensor_telemetry`) | IoT DB preset & synthetic fallback tested | PASS |
| Automated Tool 3 (`calculate_agricultural_emissions`) | IPCC Tier 1/2 GHG engine tested | PASS |
| Automated Tool 4 (`record_esg_audit_entry`) SHA-256 hash | Hash format verified (64-char hex) | PASS |
| >= 3 automated tools called in context (AC 2) | E2E run invoked all 4 tools | PASS |
| Short-term SQLite checkpointer | `ShortTermMemory` persistence, history, pruning tested | PASS |
| Long-term Vector store memory | ChromaDB similarity search & episodic reflections tested | PASS |
| 7 SSE Thought Streaming event types | `stream_agent_execution` emitted all 7 types with latency < 250ms (< 5.0s req) | PASS |
| Closed-loop Self-Correction in LangGraph StateGraph | Live routing trace under fault injection | **FAIL** (Infinite loop in `route_supervisor_decision`) |
| Continuous Cryptographic Ledger Chain in Tool 4 | `_SESSION_LEDGER` length inspected before and after call | **FAIL** (Dead singleton, chain not appended) |

---

## 5. Caveats

- In the happy path (when the initial plan generated by `dispatch_agent` meets all FAO-56 criteria on standard presets), the LangGraph StateGraph executes cleanly from START to FINISH. The infinite loop defect manifests specifically when the Critic rejects a plan and the system enters the Reflexion self-correction loop.
- The unit test suite (280 tests) and E2E runner (80 tests) currently pass because tests either run the happy path or invoke helper functions directly in isolation, masking the routing defect.

---

## 6. Conclusion

Milestone 2 Multi-Agent Engine Core demonstrates high engineering quality in domain modeling, memory implementations, and tool adapters. However, because:
1. The ReAct Reflexion self-correction state machine in `core/agents/supervisor.py` enters an infinite loop upon Critic rejection, preventing autonomous recovery; and
2. The unit tests for self-correction bypassed the LangGraph orchestrator to create a self-certifying pass without genuine multi-agent verification; and
3. Tool 4 ledger chaining operates as an unmutated facade singleton;

The official review verdict is: **REQUEST_CHANGES**.

Worker M2 must address Findings 1, 2, 3, and 4 before Milestone 2 can be approved for Milestone 3 (FastAPI Backend Integration).

---

## 7. Verification Method

To independently verify the failure modes and subsequently verify fixes:

```bash
# 1. Verify routing loop flaw in supervisor state machine:
py -c "
import sys; sys.path.insert(0, '.')
from core.agents.state import create_initial_agent_state
from core.agents.supervisor import route_supervisor_decision
from core.agents.dispatch_agent import dispatch_agent_node
from core.agents.critic_agent import critic_agent_node

state = create_initial_agent_state('test_reflexion', 'an_giang_rice_001', 'Test')
state['weather_data'] = {'temp_max': 33.0, 'et0': 4.1, 'forecast_rain_mm': 0.0}
state['sensor_telemetry'] = {'soil_moisture_pct': 21.0}
state['dispatch_plan'] = {'water_needed_mm': 90.0, 'duration_minutes': 120}
state['carbon_report'] = {'total_co2e_kg': 10.0, 'reduction_pct': 25.0}

state = critic_agent_node(state)
route1 = route_supervisor_decision(state)
state = dispatch_agent_node(state)
route2 = route_supervisor_decision(state)

print(f'Route 1: {route1} (Expected: dispatch_agent)')
print(f'Route 2: {route2} (Current Bug: dispatch_agent | Required: critic_agent or carbon_agent)')
assert route2 != 'dispatch_agent', 'FAIL: Infinite routing loop detected in supervisor'
"

# 2. Verify dead ledger singleton in Tool 4:
py -c "
import sys; sys.path.insert(0, '.')
from core.tools.ledger_tool import record_esg_audit_entry, _SESSION_LEDGER
before = len(_SESSION_LEDGER.chain)
record_esg_audit_entry('rec_test', 'farm_test', 'pump', 12.5)
after = len(_SESSION_LEDGER.chain)
print(f'Ledger chain: before={before}, after={after}')
assert after > before, 'FAIL: _SESSION_LEDGER is not being updated'
"

# 3. Verify standard regression suite:
py -m pytest tests/test_agent_core_m2.py -v
py tests/e2e_runner.py --all
```
