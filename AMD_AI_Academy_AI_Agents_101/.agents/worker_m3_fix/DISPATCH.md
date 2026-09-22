# Dispatch: Worker M3 Patch (Code Labs Robustness Hardening)

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT
hardcode test results, create dummy/facade implementations, or
circumvent the intended task. A teamwork_preview_auditor will independently
verify your work. Integrity violations WILL be detected and your
work WILL be rejected.

## Task Objective
You are Worker M3 Patch (`teamwork_preview_worker`), the Code Labs Robustness Hardening Specialist.

Your working directory is:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m3_fix`

Read the authoritative requirements at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md`
and Challenger 1's exact findings at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/challenger_1/handoff.md`

### Write Ownership
You exclusively own:
- `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/01_pure_react_agent.py`
- `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/04_framework_agent_langgraph.py`

### Required Defensive Patches:
1. In `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/01_pure_react_agent.py`:
   - In `search_hardware_specs(query)` and `search_knowledge_base(query)`:
     Add empty query guards:
     ```python
     if not query or not str(query).strip():
         return "Error: Search query cannot be empty or whitespace only."
     ```
     Ensure empty query does not match `"" in key` and falsely return the first catalog item.

2. In `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/04_framework_agent_langgraph.py`:
   - In `supervisor_node(state)`:
     Use `completed = state.get("completed_tasks") or []` (defensive check in case `completed_tasks` is explicitly `None`).
   - In `hardware_specialist_node(state)`:
     Use `completed = list(state.get("completed_tasks") or [])` when appending completed tasks.
   - In `benchmark_analyst_node(state)`:
     Use `completed = list(state.get("completed_tasks") or [])` when appending completed tasks.
   - In `synthesizer_reviewer_node(state)`:
     Use `hw_report = state.get("hardware_report") or {}` and `bench_report = state.get("benchmark_report") or {}`.
     Add validation: If either report is empty (`not hw_report or not bench_report`), set `review_status = "NEEDS_REVISION"` and indicate missing telemetry, rather than unconditionally setting `"APPROVED"`.

### Verification Requirements:
1. Run syntax compilation: `python3 -m py_compile 03_Materials_Code/*.py`
2. Run standard verification: `python3 03_Materials_Code/verify_labs.py`
3. Run Challenger 1's stress test harness: `python3 /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/challenger_1/stress_test.py`
   Ensure all 32/32 tests pass with exit code 0!
4. Write your completion report in `handoff.md` in your working directory.

## 2026-09-22T12:41:07Z

You are Worker M3 Patch (teamwork_preview_worker), the Code Labs Robustness Hardening Specialist.
Your working directory is: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m3_fix
Read your instructions in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m3_fix/DISPATCH.md
and the authoritative request in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md
and Challenger 1's findings in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/challenger_1/handoff.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Apply defensive fixes to 03_Materials_Code/01_pure_react_agent.py and 03_Materials_Code/04_framework_agent_langgraph.py as detailed in DISPATCH.md. Verify with python3 -m py_compile, verify_labs.py, and python3 .agents/challenger_1/stress_test.py. Ensure 100% 32/32 tests pass. Write handoff.md and notify via send_message when done.
