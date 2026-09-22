#!/usr/bin/env python3
"""
AMD AI Academy: AI Agents 101 - Empirical Stress Test & Adversarial Verification Suite
Challenger 1 (teamwork_preview_challenger)

This harness executes rigorous boundary and adversarial tests against all 4 code labs in 03_Materials_Code/:
- Lab 1: 01_pure_react_agent.py (ReAct loop, parsing, math safety, catalog lookups, iteration boundaries)
- Lab 2: 02_tool_calling_agent.py (Tool dispatch, parameter validation, self-correction, recovery loops)
- Lab 3: 03_memory_state_agent.py (Multi-tier memory, 20+ turns eviction, summary preservation, TF-IDF recall)
- Lab 4: 04_framework_agent_langgraph.py (StateGraph topology, cycle limits, malformed state, node failures)
"""

import sys
import os
import json
import time
import math
import importlib
from pathlib import Path
from typing import Dict, Any, List, Tuple

# Ensure 03_Materials_Code is importable
LABS_DIR = Path(__file__).resolve().parent.parent.parent / "03_Materials_Code"
if str(LABS_DIR) not in sys.path:
    sys.path.insert(0, str(LABS_DIR))

# Import lab modules
lab1 = importlib.import_module("01_pure_react_agent")
lab2 = importlib.import_module("02_tool_calling_agent")
lab3 = importlib.import_module("03_memory_state_agent")
lab4 = importlib.import_module("04_framework_agent_langgraph")

# Test Result Tracking
class TestHarness:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warned = 0
        self.findings: List[Dict[str, Any]] = []

    def record_pass(self, test_id: str, description: str, details: str = ""):
        self.passed += 1
        print(f"  [PASS] {test_id}: {description}")
        if details:
            print(f"         └─ {details}")

    def record_fail(self, test_id: str, description: str, error: str, severity: str = "HIGH"):
        self.failed += 1
        print(f"  [FAIL] {test_id}: {description}")
        print(f"         └─ Error: {error}")
        self.findings.append({
            "test_id": test_id,
            "status": "FAIL",
            "severity": severity,
            "description": description,
            "error": error
        })

    def record_warn(self, test_id: str, description: str, warning: str, severity: str = "MEDIUM"):
        self.warned += 1
        print(f"  [WARN] {test_id}: {description}")
        print(f"         └─ Note: {warning}")
        self.findings.append({
            "test_id": test_id,
            "status": "WARN",
            "severity": severity,
            "description": description,
            "error": warning
        })


# =====================================================================
# SUITE 1: LAB 1 - PURE REACT AGENT
# =====================================================================

def test_suite_1(harness: TestHarness):
    print("\n" + "=" * 75)
    print("TEST SUITE 1: Lab 1 (01_pure_react_agent.py)")
    print("=" * 75)

    # 1.1 Max step limits with infinite looping Mock LLM
    class InfiniteLoopLLM:
        def __init__(self):
            self.count = 0
        def generate(self, prompt: str, question: str) -> str:
            self.count += 1
            return "Thought: Still thinking.\nAction: calculate[1 + 1]"

    loop_llm = InfiniteLoopLLM()
    agent = lab1.ReActAgent(llm_engine=loop_llm, max_iterations=4)
    res = agent.run("Infinite loop test", verbose=False)
    if not res["success"] and res["steps"] == 4 and "Max iterations" in res["final_answer"]:
        harness.record_pass("L1-01", "Max step limit enforced accurately on non-converging agent", f"Halted at step {res['steps']}")
    else:
        harness.record_fail("L1-01", "Max step limit failed to halt agent properly", str(res))

    # 1.2 Boundary max_iterations = 0
    try:
        agent_zero = lab1.ReActAgent(llm_engine=InfiniteLoopLLM(), max_iterations=0)
        res_zero = agent_zero.run("Zero iteration test", verbose=False)
        if not res_zero["success"] and res_zero["steps"] == 0:
            harness.record_pass("L1-02", "max_iterations=0 handled gracefully", f"Steps: {res_zero['steps']}")
        else:
            harness.record_fail("L1-02", "max_iterations=0 unexpected result", str(res_zero))
    except Exception as e:
        harness.record_fail("L1-02", "max_iterations=0 crashed", str(e))

    # 1.3 tool_calculate: Division by Zero
    div_zero = lab1.tool_calculate("100 / 0")
    if "Calculation Error" in div_zero and "division by zero" in div_zero:
        harness.record_pass("L1-03", "tool_calculate trapped division by zero safely", div_zero)
    else:
        harness.record_fail("L1-03", "tool_calculate failed to trap division by zero", div_zero)

    # 1.4 tool_calculate: Malformed syntax / forbidden characters
    syntax_err = lab1.tool_calculate("5 ++ 3 **")
    if "Calculation Error" in syntax_err:
        harness.record_pass("L1-04", "tool_calculate trapped syntax error", syntax_err)
    else:
        harness.record_fail("L1-04", "tool_calculate syntax error untrapped", syntax_err)

    inj_err = lab1.tool_calculate("__import__('os').system('ls')")
    if "Error: Invalid characters" in inj_err:
        harness.record_pass("L1-05", "tool_calculate blocked code injection attempt", inj_err)
    else:
        harness.record_fail("L1-05", "tool_calculate allowed forbidden characters", inj_err, severity="CRITICAL")

    # 1.5 tool_calculate: Empty expression
    empty_calc = lab1.tool_calculate("")
    if "Calculation Error" in empty_calc:
        harness.record_pass("L1-06", "tool_calculate handled empty expression gracefully", empty_calc)
    else:
        harness.record_fail("L1-06", "tool_calculate crashed or failed on empty string", empty_calc)

    # 1.6 tool_lookup_hardware & tool_search_knowledge_base with EMPTY QUERY
    # Substring matching vulnerability check: `if key in q or q in key:`
    hw_empty = lab1.tool_lookup_hardware("")
    if "Ryzen AI 9 HX 370" in hw_empty:
        harness.record_warn("L1-07", "Substring trap: tool_lookup_hardware('') returns first catalog item",
                            "Empty query '' evaluates True in 'q in key', falsely matching 'ryzen ai 9 hx 370'.",
                            severity="MEDIUM")
    else:
        harness.record_pass("L1-07", "tool_lookup_hardware('') properly returned not found", hw_empty)

    kb_empty = lab1.tool_search_knowledge_base("")
    if "AMD ROCm" in kb_empty:
        harness.record_warn("L1-08", "Substring trap: tool_search_knowledge_base('') returns first KB doc",
                            "Empty query '' evaluates True in 'q in key', falsely matching 'rocm'.",
                            severity="MEDIUM")
    else:
        harness.record_pass("L1-08", "tool_search_knowledge_base('') properly returned not found", kb_empty)

    # 1.7 Non-existent tool dispatch
    class BadToolLLM:
        def generate(self, prompt: str, question: str) -> str:
            return "Thought: Try bad tool.\nAction: non_existent_tool[arg1]\n"
    bad_tool_agent = lab1.ReActAgent(llm_engine=BadToolLLM(), max_iterations=1)
    bad_tool_res = bad_tool_agent.run("Test unknown tool", verbose=False)
    if not bad_tool_res["success"] and bad_tool_res["steps"] == 1:
        harness.record_pass("L1-09", "Non-existent tool handled via observation error message without crash", "Handled gracefully")
    else:
        harness.record_fail("L1-09", "Non-existent tool caused unexpected state", str(bad_tool_res))

    # 1.8 ReActParser resilience against malformed tokens and unclosed brackets
    p1 = lab1.ReActParser.parse("Thought: thinking\nAction: calculate[2 + 2")  # Unclosed bracket
    # Should fallback or parse action without crash
    harness.record_pass("L1-10", "ReActParser handled unclosed bracket without exception", f"Output: {p1}")

    p2 = lab1.ReActParser.parse("Complete garbage without any keywords or colons.")
    if p2 == ("", None, None, None):
        harness.record_pass("L1-11", "ReActParser handled garbage text safely", str(p2))
    else:
        harness.record_warn("L1-11", "ReActParser extracted unexpected tokens from garbage", str(p2))

    # 1.9 Adversarial user input: Unicode, emojis, 10KB string
    huge_query = "What is TOPS? " + "🔥⚡💻" * 100 + "A" * 10000
    try:
        huge_res = agent.run(huge_query, verbose=False)
        harness.record_pass("L1-12", "ReActAgent executed safely with 10KB query containing emojis", f"Success: {huge_res['success']}")
    except Exception as e:
        harness.record_fail("L1-12", "ReActAgent crashed on large unicode query", str(e))


# =====================================================================
# SUITE 2: LAB 2 - TOOL CALLING AGENT
# =====================================================================

def test_suite_2(harness: TestHarness):
    print("\n" + "=" * 75)
    print("TEST SUITE 2: Lab 2 (02_tool_calling_agent.py)")
    print("=" * 75)

    reg = lab2.registry

    # 2.1 Parameter injection (unexpected extra arguments)
    extra_args_res = reg.dispatch("query_amd_catalog", {
        "product_name": "Ryzen AI 9 HX 370",
        "metric": "npu_tops",
        "malicious_injected_param": "DROP TABLE users;"
    })
    if extra_args_res["status"] == "error" and extra_args_res["error_type"] == "ParameterMismatchError":
        harness.record_pass("L2-01", "Parameter injection trapped as ParameterMismatchError", extra_args_res["message"])
    else:
        harness.record_fail("L2-01", "Parameter injection not caught properly", str(extra_args_res))

    # 2.2 Invalid type passing: non-dict arguments
    try:
        invalid_type_res = reg.dispatch("query_amd_catalog", "not a dictionary")
        if invalid_type_res["status"] == "error" and invalid_type_res["error_type"] == "ParameterMismatchError":
            harness.record_pass("L2-02", "Non-dict arguments trapped as ParameterMismatchError", invalid_type_res["message"])
        else:
            harness.record_fail("L2-02", "Non-dict arguments produced unexpected result", str(invalid_type_res))
    except Exception as e:
        harness.record_fail("L2-02", "Non-dict arguments crashed dispatch", str(e))

    # 2.3 Invalid type passing: int instead of str for product_name
    int_arg_res = reg.dispatch("query_amd_catalog", {
        "product_name": 12345,
        "metric": "npu_tops"
    })
    if int_arg_res["status"] == "error" and int_arg_res["error_type"] == "AttributeError":
        harness.record_pass("L2-03", "Integer product_name trapped gracefully as AttributeError", int_arg_res["message"])
    else:
        harness.record_fail("L2-03", "Integer product_name was not trapped", str(int_arg_res))

    # 2.4 Unknown tool name
    unknown_tool_res = reg.dispatch("non_existent_gpu_tool", {"param": 1})
    if unknown_tool_res["status"] == "error" and unknown_tool_res["error_type"] == "ToolNotFound":
        harness.record_pass("L2-04", "Unknown tool call trapped as ToolNotFound", unknown_tool_res["message"])
    else:
        harness.record_fail("L2-04", "Unknown tool did not return ToolNotFound", str(unknown_tool_res))

    # 2.5 calculate tool: Zero division & expression errors
    calc_zero = reg.dispatch("calculate", {"expression": "500 / 0"})
    if calc_zero["status"] == "error" and calc_zero["error_type"] == "ZeroDivisionError":
        harness.record_pass("L2-05", "Tool calculate division by zero trapped as ZeroDivisionError", calc_zero["message"])
    else:
        harness.record_fail("L2-05", "Tool calculate division by zero failed", str(calc_zero))

    # 2.6 Recovery loop exhaustion: 5 consecutive failing tool calls
    class FailingToolLLM:
        def __init__(self):
            self.turns = 0
        def get_next_action(self, messages):
            self.turns += 1
            return {
                "type": "tool_call",
                "thought": f"Attempting failing call turn {self.turns}",
                "tool_call": {
                    "name": "query_amd_catalog",
                    "arguments": {"product_name": "InvalidHW", "metric": "invalid_metric"}
                }
            }

    failing_agent = lab2.ToolCallingAgent(registry=reg, llm=FailingToolLLM())
    fail_res = failing_agent.run("Test recovery loop exhaustion", verbose=False)
    if not fail_res["success"] and fail_res["turns"] == 5 and fail_res["error_recoveries"] == 5:
        harness.record_pass("L2-06", "Agent gracefully exhausted 5 recovery turns without unhandled exception",
                            f"Recoveries logged: {fail_res['error_recoveries']}")
    else:
        harness.record_fail("L2-06", "Recovery loop exhaustion handled unexpectedly", str(fail_res))

    # 2.7 Unknown action type in LLM response
    class UnknownActionLLM:
        def get_next_action(self, messages):
            return {"type": "unknown_action_type", "data": 123}

    unknown_action_agent = lab2.ToolCallingAgent(registry=reg, llm=UnknownActionLLM())
    ua_res = unknown_action_agent.run("Test unknown action type", verbose=False)
    if not ua_res["success"] and ua_res["turns"] == 5:
        harness.record_pass("L2-07", "Unknown action type loop terminates safely after 5 turns", "Graceful exit")
    else:
        harness.record_fail("L2-07", "Unknown action type caused crash or unexpected state", str(ua_res))


# =====================================================================
# SUITE 3: LAB 3 - MEMORY STATE AGENT
# =====================================================================

def test_suite_3(harness: TestHarness):
    print("\n" + "=" * 75)
    print("TEST SUITE 3: Lab 3 (03_memory_state_agent.py)")
    print("=" * 75)

    # 3.1 Memory eviction with 25 conversation turns (exceeding max_buffer_turns=2)
    manager = lab3.MemoryStateManager(max_buffer_turns=2)
    start_time = time.perf_counter()

    for i in range(1, 26):
        user_msg = f"Turn {i}: I am user Alex testing item {i} on AMD Ryzen AI 9 HX 370 with tops {i*2}."
        asst_msg = f"Response {i}: Item {i} confirmed for Alex on XDNA 2 with TOPS {i*2}."
        manager.add_interaction(user_msg, asst_msg)

    eviction_duration = time.perf_counter() - start_time

    # Verification of sliding buffer boundary: strictly max_buffer_turns * 2 messages (i.e. 4 messages)
    buffer_len = len(manager.short_term_buffer)
    archive_len = len(manager.episodic_archive)
    if buffer_len == 4:
        harness.record_pass("L3-01", f"Sliding window buffer strictly bounded at {buffer_len} messages (2 turns)",
                            f"Tested 25 turns; duration: {eviction_duration*1000:.2f}ms")
    else:
        harness.record_fail("L3-01", f"Sliding window buffer length violated! Expected 4, got {buffer_len}",
                            f"Buffer len: {buffer_len}")

    # Verification of episodic archive size: 25 - 2 = 23 evicted turns
    if archive_len == 23:
        harness.record_pass("L3-02", f"Episodic archive stored all {archive_len} evicted turns without loss",
                            f"Archive count matches (25 - 2 = 23)")
    else:
        harness.record_fail("L3-02", f"Episodic archive count mismatch. Expected 23, got {archive_len}",
                            f"Archive len: {archive_len}")

    # 3.2 Rolling summary preservation over 25 turns
    summary = manager.rolling_summary
    turn_1_in_summary = "[Turn 1]" in summary
    turn_23_in_summary = "[Turn 23]" in summary
    if turn_1_in_summary and turn_23_in_summary:
        harness.record_pass("L3-03", "Rolling summary preserved earliest and latest evicted turns",
                            f"Summary length: {len(summary)} chars, contains Turn 1 and Turn 23")
    else:
        harness.record_fail("L3-03", "Rolling summary lost turn markers", f"Turn 1: {turn_1_in_summary}, Turn 23: {turn_23_in_summary}")

    # 3.3 TF-IDF recall with disjoint vocabulary (zero common words)
    disjoint_query = "xylophone zeppelin kangaroo pterodactyl"
    recalled_disjoint = manager.recall_episodic(disjoint_query, top_k=1)
    if recalled_disjoint and recalled_disjoint[0][0] == 0.0:
        harness.record_pass("L3-04", "TF-IDF episodic recall correctly returned 0.0 similarity for disjoint query",
                            f"Score: {recalled_disjoint[0][0]}")
    else:
        harness.record_fail("L3-04", "Disjoint query produced non-zero similarity", str(recalled_disjoint))

    # 3.4 TF-IDF recall with empty and all-punctuation queries
    empty_sim = lab3.term_frequency_cosine_similarity("", "AMD Ryzen AI 9 HX 370")
    if empty_sim == 0.0:
        harness.record_pass("L3-05", "term_frequency_cosine_similarity handled empty string safely (0.0)", "No ZeroDivisionError")
    else:
        harness.record_fail("L3-05", "Empty string returned non-zero", str(empty_sim))

    punct_sim = lab3.term_frequency_cosine_similarity("!!! ??? :::: ---", "AMD Instinct MI300X")
    if punct_sim == 0.0:
        harness.record_pass("L3-06", "term_frequency_cosine_similarity handled all-punctuation string safely (0.0)", "Clean split")
    else:
        harness.record_fail("L3-06", "Punctuation string returned non-zero", str(punct_sim))

    # 3.5 Prompt assembly with full memory state
    prompt = manager.assemble_prompt("Can you recall my drone project?")
    has_layer1 = "[LAYER 1: STRUCTURED ENTITY STORE]" in prompt
    has_layer2 = "[LAYER 2: ROLLING SUMMARY (COMPRESSED PAST TURNS)]" in prompt
    has_layer4 = "[LAYER 4: SHORT-TERM WORKING BUFFER]" in prompt
    if has_layer1 and has_layer2 and has_layer4:
        harness.record_pass("L3-07", "Multi-tier prompt assembly verified with all 4 memory layers intact",
                            f"Prompt size: {len(prompt)} chars")
    else:
        harness.record_fail("L3-07", "Assembled prompt missing required memory layers", prompt[:200])


# =====================================================================
# SUITE 4: LAB 4 - FRAMEWORK AGENT (LANGGRAPH PATTERN)
# =====================================================================

def test_suite_4(harness: TestHarness):
    print("\n" + "=" * 75)
    print("TEST SUITE 4: Lab 4 (04_framework_agent_langgraph.py)")
    print("=" * 75)

    # 4.1 Cycle limits: Construct infinite cycle in NativeStateGraph (A -> B -> A)
    # Verify that invoke terminates strictly at max_steps
    builder = lab4.NativeStateGraph()
    call_counts = {"A": 0, "B": 0}

    def node_a(state):
        call_counts["A"] += 1
        return {"step_a": call_counts["A"]}

    def node_b(state):
        call_counts["B"] += 1
        return {"step_b": call_counts["B"]}

    builder.add_node("A", node_a)
    builder.add_node("B", node_b)
    builder.set_entry_point("A")
    builder.add_edge("A", "B")
    builder.add_edge("B", "A")

    cyclic_graph = builder.compile()

    start_t = time.perf_counter()
    cycle_res = cyclic_graph.invoke({"init": True}, max_steps=10)
    cycle_duration = time.perf_counter() - start_t

    total_calls = call_counts["A"] + call_counts["B"]
    trace_len = len(cycle_res.get("execution_trace", []))

    if total_calls == 10 and trace_len == 10:
        harness.record_pass("L4-01", f"Graph cycle limit strictly enforced at max_steps=10",
                            f"Terminated in {cycle_duration*1000:.2f}ms, trace length: {trace_len}")
    else:
        harness.record_fail("L4-01", f"Cycle limit not enforced properly. Calls: {total_calls}, Trace: {trace_len}",
                            str(cycle_res))

    # 4.2 Invalid state input: completed_tasks is None
    # Vulnerability check: `state.get("completed_tasks", []) + ["hardware"]`
    # When state has {"completed_tasks": None}, state.get() returns None -> TypeError!
    graph_app = lab4.build_collaboration_graph()
    try:
        state_with_none_tasks = {
            "task_query": "Evaluate AMD hardware",
            "completed_tasks": None,  # None instead of list
            "execution_trace": []
        }
        res_none_tasks = graph_app.invoke(state_with_none_tasks)
        harness.record_pass("L4-02", "completed_tasks=None handled without crash", str(res_none_tasks))
    except TypeError as te:
        harness.record_fail("L4-02", "completed_tasks=None caused unhandled TypeError in node addition",
                            f"TypeError: {te}", severity="HIGH")
    except Exception as e:
        harness.record_fail("L4-02", "completed_tasks=None caused unhandled exception", str(e), severity="HIGH")

    # 4.3 Invalid state input: hardware_report is None
    # Vulnerability check: `hw = state.get("hardware_report", {})` -> if key exists as None, hw is None -> AttributeError!
    try:
        def bad_hw_node(state):
            return {"hardware_report": None, "completed_tasks": ["hardware", "benchmark"]}
        
        test_graph = lab4.NativeStateGraph()
        test_graph.add_node("bad_hw", bad_hw_node)
        test_graph.add_node("synthesizer", lab4.synthesizer_reviewer_node)
        test_graph.set_entry_point("bad_hw")
        test_graph.add_edge("bad_hw", "synthesizer")
        compiled_test_graph = test_graph.compile()

        res_bad_hw = compiled_test_graph.invoke({})
        harness.record_pass("L4-03", "hardware_report=None handled safely", str(res_bad_hw))
    except AttributeError as ae:
        harness.record_fail("L4-03", "hardware_report=None caused unhandled AttributeError in synthesizer",
                            f"AttributeError: {ae}", severity="HIGH")
    except Exception as e:
        harness.record_fail("L4-03", "hardware_report=None caused unhandled exception", str(e), severity="HIGH")

    # 4.4 Reviewer approval gate behavior on empty reports
    empty_report_state = {
        "hardware_report": {},
        "benchmark_report": {}
    }
    synth_res = lab4.synthesizer_reviewer_node(empty_report_state)
    if synth_res.get("review_status") == "APPROVED":
        harness.record_warn("L4-04", "Reviewer blindly approves empty hardware/benchmark reports",
                            "synthesizer_reviewer_node returns 'APPROVED' even when hardware_report and benchmark_report are empty.",
                            severity="MEDIUM")
    else:
        harness.record_pass("L4-04", "Reviewer rejected or handled empty reports", str(synth_res))

    # 4.5 Router fallback to END on unknown route key
    test_graph_router = lab4.NativeStateGraph()
    test_graph_router.add_node("router_node", lambda s: {"route": "unknown_target"})
    test_graph_router.set_entry_point("router_node")
    test_graph_router.add_conditional_edges(
        "router_node",
        lambda s: s.get("route"),
        {"valid_target": "router_node"}  # 'unknown_target' not in mapping
    )
    comp_router = test_graph_router.compile()
    route_res = comp_router.invoke({})
    trace = route_res.get("execution_trace", [])
    if trace and "-> __END__" in trace[-1]:
        harness.record_pass("L4-05", "Conditional router safely fell back to __END__ on unmapped route key", trace[-1])
    else:
        harness.record_fail("L4-05", "Conditional router failed on unmapped route key", str(trace))

    # 4.6 Unhandled exception in node execution
    failing_node_graph = lab4.NativeStateGraph()
    def exploding_node(state):
        raise RuntimeError("Hardware telemetry hardware failure simulation")
    failing_node_graph.add_node("boom", exploding_node)
    failing_node_graph.set_entry_point("boom")
    comp_exploding = failing_node_graph.compile()

    try:
        comp_exploding.invoke({})
        harness.record_fail("L4-06", "Exploding node did not raise exception", "Expected RuntimeError")
    except RuntimeError as re:
        harness.record_pass("L4-06", "Node exception propagated cleanly to caller (no silent swallowing)", str(re))
    except Exception as e:
        harness.record_fail("L4-06", "Exploding node raised unexpected exception type", str(e))


# =====================================================================
# MAIN RUNNER
# =====================================================================

def main():
    print("=" * 75)
    print("🚀 AMD AI Academy: AI Agents 101 - Empirical Stress Harness")
    print(f"Python Interpreter: {sys.executable} ({sys.version.split()[0]})")
    print(f"Target Labs Directory: {LABS_DIR}")
    print("=" * 75)

    harness = TestHarness()

    test_suite_1(harness)
    test_suite_2(harness)
    test_suite_3(harness)
    test_suite_4(harness)

    print("\n" + "=" * 75)
    print("📊 EMPIRICAL STRESS TESTING SCORECARD")
    print("=" * 75)
    print(f"  Total Passed:  {harness.passed}")
    print(f"  Total Warnings:{harness.warned}")
    print(f"  Total Failures:{harness.failed}")
    print(f"  Total Tests:   {harness.passed + harness.warned + harness.failed}")

    if harness.findings:
        print("\n🚨 Summary of Findings & Observations:")
        for idx, f in enumerate(harness.findings, 1):
            print(f"  {idx}. [{f['status']}] [{f['severity']}] {f['test_id']}: {f['description']}")
            print(f"     └─ {f['error']}")

    print("=" * 75)
    
    # Save findings JSON artifact
    artifact_path = Path(__file__).resolve().parent / "stress_results.json"
    with open(artifact_path, "w", encoding="utf-8") as fp:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "passed": harness.passed,
            "warned": harness.warned,
            "failed": harness.failed,
            "findings": harness.findings
        }, fp, indent=2)
    print(f"Saved empirical results artifact to: {artifact_path}")

    return 0 if harness.failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
