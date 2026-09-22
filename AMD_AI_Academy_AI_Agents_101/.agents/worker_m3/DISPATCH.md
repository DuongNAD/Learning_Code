# Dispatch: Worker M3 (Python Code Labs & Execution Specialist)

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT
hardcode test results, create dummy/facade implementations, or
circumvent the intended task. A teamwork_preview_auditor will independently
verify your work. Integrity violations WILL be detected and your
work WILL be rejected.

## Task Objective
You are Worker M3 (`teamwork_preview_worker`), the Python Code Labs Implementation & Zero-Defect Execution Specialist.

Your working directory is:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m3`

Read the authoritative requirements at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md`
and Explorer 3's complete code designs and handoff report at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_3/handoff.md`

### Write Ownership
You exclusively own all files in:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/`
Specifically:
- `03_Materials_Code/requirements.txt`
- `03_Materials_Code/01_pure_react_agent.py`
- `03_Materials_Code/02_tool_calling_agent.py`
- `03_Materials_Code/03_memory_state_agent.py`
- `03_Materials_Code/04_framework_agent_langgraph.py`
- `03_Materials_Code/verify_labs.py`
- `03_Materials_Code/README.md`

### Detailed Instructions:
1. Implement all 4 Python labs and testing harness based on the verified designs in Explorer 3's handoff report:
   - `01_pure_react_agent.py`: 100% Python standard library ReAct agent executing Thought -> Action -> Observation -> Final Answer with terminal formatting, AMD hardware knowledge base (Ryzen AI NPU TOPS vs M3, ROCm Instinct MI300X), and deterministic execution mode.
   - `02_tool_calling_agent.py`: Pydantic / JSON Schema validated tool calling agent with execution dispatcher, self-reflection error recovery on parameter validation failures, and realistic system tools.
   - `03_memory_state_agent.py`: 4-tier memory manager (sliding short-term window, rolling summarization, structured entity store, TF-IDF episodic recall) with multi-turn conversation simulation demonstrating zero context loss.
   - `04_framework_agent_langgraph.py`: Dual-mode state graph workflow (Supervisor -> Hardware Specialist -> Benchmark Analyst -> Synthesizer -> END) featuring native fallback `NativeStateGraph` that runs out-of-the-box in the host Python environment while maintaining LangGraph API compatibility.
   - `requirements.txt`: Clear listing of core libraries, optional LLM extensions, and AMD ROCm PyTorch installation commands.
   - `verify_labs.py`: Automated verification script that checks `py_compile` on all 4 scripts, executes each script end-to-end, validates semantic output tokens, and prints a test report with exit code 0.
   - `README.md` inside `03_Materials_Code/`: Complete guide explaining each lab, concept mapping, how to run individually or via `python3 verify_labs.py`.
2. Run testing and verification:
   - Run `python3 -m py_compile 03_Materials_Code/*.py`
   - Run `python3 03_Materials_Code/verify_labs.py`
   - Ensure 100% pass rate with 0 runtime errors.
3. Write your completion report in `handoff.md` in your working directory with full command execution logs and verification evidence.

## 2026-09-22T11:54:20Z
You are Worker M3 (teamwork_preview_worker), the Python Code Labs Implementation & Zero-Defect Execution Specialist.
Your working directory is: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m3
Read your instructions in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m3/DISPATCH.md
and the authoritative request in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md

Implement all 4 Python labs in 03_Materials_Code/ (01_pure_react_agent.py, 02_tool_calling_agent.py, 03_memory_state_agent.py, 04_framework_agent_langgraph.py), requirements.txt, verify_labs.py, and 03_Materials_Code/README.md based on Explorer 3's verified handoff. Execute py_compile and verify_labs.py to guarantee zero defect runtime execution. Write your completion report to handoff.md in your working directory and notify via send_message when done.

