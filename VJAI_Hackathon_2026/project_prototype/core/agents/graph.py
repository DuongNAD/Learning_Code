"""
LangGraph StateGraph Builder & Multi-Agent Execution Engine.
Orchestrates Supervisor, Sensing, Dispatch, Carbon Auditor, and Critic Agents.
Supports ReAct planning, Reflexion self-correction loop, and 7-event SSE thought streaming.
Conforms strictly to PROJECT.md § Multi-Agent Engine and ORIGINAL_REQUEST.md § R2.
"""

import time
from typing import Dict, Any, Generator, Optional
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from core.agents.state import AgentState, create_initial_agent_state
from core.agents.supervisor import supervisor_node, route_supervisor_decision
from core.agents.sensing_agent import sensing_agent_node
from core.agents.dispatch_agent import dispatch_agent_node
from core.agents.carbon_agent import carbon_agent_node
from core.agents.critic_agent import critic_agent_node
from core.memory.short_term import ShortTermMemory


def build_agricarbon_graph(checkpointer=None):
    """
    Constructs and compiles the hierarchical LangGraph StateGraph.
    """
    workflow = StateGraph(AgentState)

    # 1. Register specialized agent nodes
    workflow.add_node("supervisor", supervisor_node)
    workflow.add_node("sensing_agent", sensing_agent_node)
    workflow.add_node("dispatch_agent", dispatch_agent_node)
    workflow.add_node("carbon_agent", carbon_agent_node)
    workflow.add_node("critic_agent", critic_agent_node)

    # 2. Entry point: route to supervisor
    workflow.add_edge(START, "supervisor")

    # 3. Conditional routing from supervisor to workers or finish
    workflow.add_conditional_edges(
        "supervisor",
        route_supervisor_decision,
        {
            "sensing_agent": "sensing_agent",
            "dispatch_agent": "dispatch_agent",
            "carbon_agent": "carbon_agent",
            "critic_agent": "critic_agent",
            "FINISH": END,
        }
    )

    # 4. Pipeline execution edges:
    # Forward execution pipeline eliminates redundant supervisor ping-pong,
    # ensuring that 3-retry Reflexion with circuit breaker completes strictly within
    # 14 steps (<= 15 recursion limit), and 1-retry self-correction within 10 steps.
    workflow.add_edge("sensing_agent", "dispatch_agent")
    workflow.add_edge("dispatch_agent", "carbon_agent")
    workflow.add_edge("carbon_agent", "critic_agent")
    workflow.add_edge("critic_agent", "supervisor")

    # Compile graph with checkpointer
    if checkpointer is None:
        checkpointer = MemorySaver()

    compiled_app = workflow.compile(checkpointer=checkpointer)
    return compiled_app


# Global compiled default graph application
_DEFAULT_CHECKPOINTER = MemorySaver()
compiled_agricarbon_app = build_agricarbon_graph(checkpointer=_DEFAULT_CHECKPOINTER)


def run_agent_workflow(
    initial_state: AgentState,
    thread_id: str = "default_thread",
    checkpointer=None
) -> AgentState:
    """
    Executes the multi-agent workflow to completion.
    """
    app = build_agricarbon_graph(checkpointer=checkpointer) if checkpointer else compiled_agricarbon_app
    config = {"configurable": {"thread_id": thread_id}}

    result = app.invoke(initial_state, config=config)
    return result


def stream_agent_execution(
    initial_state: AgentState,
    thread_id: str = "stream_thread",
    max_steps: int = 15
) -> Generator[Dict[str, Any], None, None]:
    """
    Generator yielding Server-Sent Events (SSE) thought stream in real-time.
    Supports 7 event types defined in PROJECT.md:
    1. thought: Reasoning progression
    2. tool_call: Tool invocation with arguments
    3. tool_result: Tool response
    4. reflection: Critic approval / critique feedback
    5. token: Streamed explanation tokens
    6. complete: Final verified result & latency
    7. error: Error or circuit breaker alerts
    """
    start_time = time.time()
    state = dict(initial_state)

    # Initial token streaming event
    yield {
        "event": "token",
        "data": {"chunk": f"Initiating autonomous AgriCarbon agent workflow for scenario: {state.get('scenario_id', 'custom')}..."}
    }

    # Supervisor initial planning
    state = supervisor_node(state)
    yield {
        "event": "thought",
        "data": {
            "step": "planning",
            "content": f"Decomposed user prompt into {len(state.get('plan', []))} subtasks."
        }
    }

    steps = 0
    while steps < max_steps:
        steps += 1
        next_node = route_supervisor_decision(state)

        if next_node == "FINISH":
            # Conclude with supervisor final synthesis
            state = supervisor_node(state)
            break

        elif next_node == "sensing_agent":
            yield {
                "event": "thought",
                "data": {"step": "sensing", "content": "Querying ambient weather forecast and IoT soil telemetry..."}
            }
            # Capture tool calls count before node execution
            prior_tools = len(state.get("tool_calls", []))
            state = sensing_agent_node(state)
            new_tools = state.get("tool_calls", [])[prior_tools:]

            for t in new_tools:
                if "args" in t:
                    yield {"event": "tool_call", "data": t}
                elif "result" in t:
                    yield {"event": "tool_result", "data": t}

            state = supervisor_node(state)

        elif next_node == "dispatch_agent":
            yield {
                "event": "thought",
                "data": {"step": "dispatch", "content": "Computing precision irrigation demand and EVN peak tariff schedule..."}
            }
            state = dispatch_agent_node(state)
            plan = state.get("dispatch_plan", {})
            yield {
                "event": "token",
                "data": {"chunk": f"Optimal watering schedule: {plan.get('water_needed_mm')}mm, duration {plan.get('duration_minutes')} mins."}
            }
            state = supervisor_node(state)

        elif next_node == "carbon_agent":
            yield {
                "event": "thought",
                "data": {"step": "carbon_audit", "content": "Calculating Scope 1-3 GHG footprint using IPCC AFOLU equations..."}
            }
            prior_tools = len(state.get("tool_calls", []))
            state = carbon_agent_node(state)
            new_tools = state.get("tool_calls", [])[prior_tools:]

            for t in new_tools:
                if "args" in t:
                    yield {"event": "tool_call", "data": t}
                elif "result" in t:
                    yield {"event": "tool_result", "data": t}

            report = state.get("carbon_report", {})
            yield {
                "event": "token",
                "data": {"chunk": f"Audited emissions: {report.get('total_co2e_kg')} kg CO2e ({report.get('reduction_pct')}% reduction)."}
            }
            state = supervisor_node(state)

        elif next_node == "critic_agent":
            yield {
                "event": "thought",
                "data": {"step": "guardrail_verification", "content": "Evaluating agronomic safety limits and FAO-56 compliance..."}
            }
            state = critic_agent_node(state)
            verdict = state.get("critic_verdict", {})
            yield {
                "event": "reflection",
                "data": {
                    "approved": verdict.get("approved", False),
                    "critique": verdict.get("feedback", ""),
                    "retry_count": verdict.get("retry_count", 0)
                }
            }
            state = supervisor_node(state)

    # Any errors recorded?
    if state.get("errors"):
        for err in state["errors"]:
            yield {
                "event": "error",
                "data": {"message": err}
            }

    # Final complete event
    latency_ms = int((time.time() - start_time) * 1000)
    final_output = state.get("final_output", {})

    yield {
        "event": "complete",
        "data": {
            "final_result": final_output,
            "status": final_output.get("status", "success"),
            "latency_ms": latency_ms
        }
    }
