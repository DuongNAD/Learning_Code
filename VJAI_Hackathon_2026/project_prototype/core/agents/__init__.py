"""
AgriCarbon Multi-Agent Engine Core Package.
Provides autonomous agents, LangGraph StateGraph engine, and thought streaming:
1. AgentState: Central state schema.
2. Supervisor: ReAct task decomposition and routing.
3. SensingAgent: Weather & IoT telemetry worker.
4. DispatchAgent: Precision irrigation and tariff optimization worker.
5. CarbonAgent: Scope 1-3 IPCC carbon auditing worker.
6. CriticAgent: Safety guardrails and Reflexion self-correction worker.
7. Graph: Compiled StateGraph application and SSE thought event streaming.
"""

from core.agents.state import (
    AgentState,
    ThoughtEvent,
    CriticVerdictModel,
    create_initial_agent_state,
)
from core.agents.supervisor import supervisor_node, route_supervisor_decision
from core.agents.sensing_agent import sensing_agent_node
from core.agents.dispatch_agent import dispatch_agent_node
from core.agents.carbon_agent import carbon_agent_node
from core.agents.critic_agent import critic_agent_node, evaluate_plan_by_critic
from core.agents.graph import (
    build_agricarbon_graph,
    run_agent_workflow,
    stream_agent_execution,
    compiled_agricarbon_app,
)

__all__ = [
    "AgentState",
    "ThoughtEvent",
    "CriticVerdictModel",
    "create_initial_agent_state",
    "supervisor_node",
    "route_supervisor_decision",
    "sensing_agent_node",
    "dispatch_agent_node",
    "carbon_agent_node",
    "critic_agent_node",
    "evaluate_plan_by_critic",
    "build_agricarbon_graph",
    "run_agent_workflow",
    "stream_agent_execution",
    "compiled_agricarbon_app",
]
