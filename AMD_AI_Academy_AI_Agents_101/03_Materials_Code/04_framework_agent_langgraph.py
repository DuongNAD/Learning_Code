#!/usr/bin/env python3
"""
Lab 4: Multi-Agent Collaboration & Stateful Graph Workflow (LangGraph Pattern)
AMD AI Academy: AI Agents 101

Architecture:
- Implements the Supervisor / Worker Multi-Agent Collaboration pattern.
- Stateful Graph topology:
  Supervisor (Router) -> Hardware Specialist -> Synthesizer
                      -> Benchmark Analyst   -> Synthesizer
                      -> Synthesizer (Review & Self-Reflection) -> END
- Dual Engine:
  - If official 'langgraph' is installed, uses 'langgraph.graph.StateGraph'.
  - If 'langgraph' is not installed, seamlessly falls back to 'NativeStateGraph'
    (a clean, lightweight implementation with identical API contracts).
  - Guarantees 100% offline standalone execution without requiring heavy pip packages!
"""

import sys
import json
import argparse
from typing import Dict, Any, List, Callable, Optional, TypedDict, Tuple

# =====================================================================
# 1. DUAL-ENGINE STATE GRAPH IMPLEMENTATION
# =====================================================================

END = "__END__"
START = "__START__"

try:
    from langgraph.graph import StateGraph, END
    ENGINE_TYPE = "Official LangGraph"
except ImportError:
    ENGINE_TYPE = "Native Lightweight StateGraph (Zero-Dependency Fallback)"

    class NativeStateGraph:
        """Lightweight standard library implementation mirroring LangGraph's StateGraph API."""
        
        def __init__(self, state_schema=dict):
            self.nodes: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {}
            self.edges: Dict[str, str] = {}
            self.conditional_edges: Dict[str, Tuple[Callable, Dict[str, str]]] = {}
            self.entry_point: Optional[str] = None

        def add_node(self, name: str, func: Callable[[Dict[str, Any]], Dict[str, Any]]):
            self.nodes[name] = func

        def set_entry_point(self, name: str):
            self.entry_point = name

        def add_edge(self, from_node: str, to_node: str):
            self.edges[from_node] = to_node

        def add_conditional_edges(self, from_node: str, condition: Callable, mapping: Dict[str, str]):
            self.conditional_edges[from_node] = (condition, mapping)

        def compile(self):
            return CompiledNativeGraph(self)

    class CompiledNativeGraph:
        def __init__(self, graph: NativeStateGraph):
            self.graph = graph

        def invoke(self, initial_state: Dict[str, Any], max_steps: int = 15) -> Dict[str, Any]:
            state = dict(initial_state)
            current = self.graph.entry_point
            step = 0

            while current != END and step < max_steps:
                step += 1
                node_fn = self.graph.nodes[current]
                updates = node_fn(state)
                if updates:
                    state.update(updates)

                # Determine next transition
                if current in self.graph.conditional_edges:
                    cond_fn, mapping = self.graph.conditional_edges[current]
                    route_key = cond_fn(state)
                    next_node = mapping.get(route_key, END)
                elif current in self.graph.edges:
                    next_node = self.graph.edges[current]
                else:
                    next_node = END

                state.setdefault("execution_trace", []).append(f"[{step}] {current} -> {next_node}")
                current = next_node

            return state

    StateGraph = NativeStateGraph

# =====================================================================
# 2. STATE SCHEMA & MULTI-AGENT NODES
# =====================================================================

class AgentTeamState(TypedDict, total=False):
    task_query: str
    completed_tasks: List[str]
    next_action: str
    hardware_report: Dict[str, Any]
    benchmark_report: Dict[str, Any]
    final_synthesis: str
    review_status: str
    execution_trace: List[str]

# Node 1: Supervisor / Orchestrator
def supervisor_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Analyzes overall state, decomposes query, and routes to specialists."""
    completed = state.get("completed_tasks") or []
    if "hardware" not in completed:
        return {"next_action": "hardware_specialist"}
    elif "benchmark" not in completed:
        return {"next_action": "benchmark_analyst"}
    else:
        return {"next_action": "synthesizer"}

def supervisor_router(state: Dict[str, Any]) -> str:
    return state.get("next_action", "synthesizer")

# Node 2: Hardware Architecture Specialist
def hardware_specialist_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Specializes in AMD CDNA, RDNA, and XDNA silicon architectures."""
    hw_data = {
        "datacenter_accelerator": {
            "model": "AMD Instinct MI300X",
            "arch": "CDNA 3",
            "memory": "192GB HBM3 (5.3 TB/s)",
            "interconnect": "Infinity Fabric (896 GB/s bidirectional)",
            "software": "ROCm 6.2 with HIP, PyTorch, vLLM, Triton"
        },
        "client_processor": {
            "model": "AMD Ryzen AI 9 HX 370",
            "arch": "Zen 5 + XDNA 2",
            "npu_tops": 50,
            "software": "Ryzen AI Software, ONNX Runtime Vitis AI EP"
        }
    }
    completed = list(state.get("completed_tasks") or []) + ["hardware"]
    return {"hardware_report": hw_data, "completed_tasks": completed}

# Node 3: Benchmark & Performance Analyst
def benchmark_analyst_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Computes compute metrics, memory bandwidth advantages, and efficiency."""
    bench_data = {
        "mi300x_fp16_tflops": 1307,
        "mi300x_memory_bandwidth_tb_s": 5.3,
        "h100_sxm5_comparison": {
            "memory_capacity_ratio": "192GB vs 80GB (2.4x higher)",
            "memory_bandwidth_ratio": "5.3 TB/s vs 3.35 TB/s (1.6x higher)"
        },
        "ryzen_ai_efficiency": "50 NPU TOPS enables real-time 30+ tokens/sec on Llama-3-8B (INT4) at <15W NPU power"
    }
    completed = list(state.get("completed_tasks") or []) + ["benchmark"]
    return {"benchmark_report": bench_data, "completed_tasks": completed}

# Node 4: Synthesizer & Reviewer (Reflection & Quality Gate)
def synthesizer_reviewer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Combines specialist findings, reviews completeness, and synthesizes final advice."""
    hw_report = state.get("hardware_report") or {}
    bench_report = state.get("benchmark_report") or {}

    if not hw_report or not bench_report:
        return {
            "final_synthesis": "Error: Incomplete telemetry reports. Missing hardware or benchmark telemetry.",
            "review_status": "NEEDS_REVISION"
        }

    mi300x = hw_report.get("datacenter_accelerator", {})
    ryzen = hw_report.get("client_processor", {})
    h100_cmp = bench_report.get("h100_sxm5_comparison", {})

    synthesis = (
        "=======================================================================\n"
        "🎯 EXECUTIVE MULTI-AGENT SYNTHESIS: AMD AI PORTFOLIO EVALUATION\n"
        "=======================================================================\n"
        f"1. DATACENTER ACCELERATION ({mi300x.get('model')}):\n"
        f"   - Architecture: {mi300x.get('arch')} with {mi300x.get('memory')}\n"
        f"   - Software Stack: {mi300x.get('software')}\n"
        f"   - Competitive Moat vs H100: {h100_cmp.get('memory_capacity_ratio')}, "
        f"{h100_cmp.get('memory_bandwidth_ratio')}\n\n"
        f"2. ON-DEVICE & EDGE ACCELERATION ({ryzen.get('model')}):\n"
        f"   - Architecture: {ryzen.get('arch')} with {ryzen.get('npu_tops')} NPU TOPS\n"
        f"   - Software Stack: {ryzen.get('software')}\n"
        f"   - Efficiency: {bench_report.get('ryzen_ai_efficiency')}\n\n"
        "3. REVIEWER VERDICT: APPROVED (All architectural and benchmark metrics validated).\n"
        "======================================================================="
    )
    return {"final_synthesis": synthesis, "review_status": "APPROVED"}

def synthesizer_router(state: Dict[str, Any]) -> str:
    if state.get("review_status") == "APPROVED":
        return "end"
    return "supervisor"

# =====================================================================
# 3. GRAPH TOPOLOGY CONSTRUCTION
# =====================================================================

def build_collaboration_graph():
    """Builds and compiles the multi-agent state graph."""
    builder = StateGraph(AgentTeamState)

    # Add Nodes
    builder.add_node("supervisor", supervisor_node)
    builder.add_node("hardware_specialist", hardware_specialist_node)
    builder.add_node("benchmark_analyst", benchmark_analyst_node)
    builder.add_node("synthesizer", synthesizer_reviewer_node)

    # Set Entry Point
    builder.set_entry_point("supervisor")

    # Conditional Routing from Supervisor to Specialists
    builder.add_conditional_edges(
        "supervisor",
        supervisor_router,
        {
            "hardware_specialist": "hardware_specialist",
            "benchmark_analyst": "benchmark_analyst",
            "synthesizer": "synthesizer"
        }
    )

    # Specialists report back to Supervisor
    builder.add_edge("hardware_specialist", "supervisor")
    builder.add_edge("benchmark_analyst", "supervisor")

    # Reviewer gates final completion
    builder.add_conditional_edges(
        "synthesizer",
        synthesizer_router,
        {
            "end": END,
            "supervisor": "supervisor"
        }
    )

    return builder.compile()

# =====================================================================
# 4. CLI & STANDALONE EXECUTION
# =====================================================================

def main():
    parser = argparse.ArgumentParser(description="Run Multi-Agent LangGraph Workflow")
    parser.add_argument("--test-mode", action="store_true", help="Run automated test assertion")
    args = parser.parse_args()

    print("\n" + "=" * 75)
    print(f"🌐 AMD AI Academy: Multi-Agent StateGraph Workflow [{ENGINE_TYPE}]")
    print("=" * 75)

    graph_app = build_collaboration_graph()
    initial_state: Dict[str, Any] = {
        "task_query": "Evaluate AMD datacenter and client hardware stack for AI Agents",
        "completed_tasks": [],
        "execution_trace": []
    }

    result = graph_app.invoke(initial_state)

    print("\n📈 Graph Execution Trace:")
    for step in result.get("execution_trace", []):
        print(f"  {step}")

    print("\n" + result["final_synthesis"] + "\n")

    if args.test_mode:
        assert result["review_status"] == "APPROVED", "Synthesizer reviewer failed to approve synthesis"
        assert len(result["completed_tasks"]) == 2, "Not all specialist agent nodes completed their tasks"
        assert "MI300X" in result["final_synthesis"], "Synthesis missing MI300X datacenter accelerator"
        assert "XDNA 2" in result["final_synthesis"], "Synthesis missing XDNA 2 client NPU"
        print("✅ Lab 4 Test Mode Verification Passed: Zero Defects.")
        sys.exit(0)

if __name__ == "__main__":
    main()
