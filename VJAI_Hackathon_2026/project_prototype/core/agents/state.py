"""
Global Agent State Schema & Data Contracts for AgriCarbon Multi-Agent System.
Conforms strictly to PROJECT.md § Interface Contracts (lines 167-186)
and tests/tier1_feature/test_supervisor_agent.py.
"""

from typing import TypedDict, List, Dict, Any, Optional, Literal
from pydantic import BaseModel, Field


class AgentState(TypedDict, total=False):
    """
    Central shared state object passed across LangGraph nodes.
    """
    task_id: str
    scenario_id: str
    crop_info: Dict[str, Any]
    user_prompt: str
    plan: List[str]
    current_step: int
    thoughts: List[Dict[str, Any]]
    tool_calls: List[Dict[str, Any]]
    weather_data: Dict[str, Any]
    sensor_telemetry: Dict[str, Any]
    dispatch_plan: Dict[str, Any]
    carbon_report: Dict[str, Any]
    critic_verdict: Dict[str, Any]  # {'approved': bool, 'retry_count': int, 'feedback': str}
    final_output: Dict[str, Any]
    errors: List[str]


class ThoughtEvent(BaseModel):
    """
    Structured thought event emitted for real-time SSE streaming.
    Event types: thought, tool_call, tool_result, reflection, token, complete, error
    """
    event: Literal["thought", "tool_call", "tool_result", "reflection", "token", "complete", "error"]
    data: Dict[str, Any]
    timestamp: Optional[str] = None


class CriticVerdictModel(BaseModel):
    """Pydantic validation contract for Critic Agent evaluation output."""
    approved: bool = Field(..., description="Whether the plan meets all agronomic safety rules")
    retry_count: int = Field(default=0, ge=0, description="Cumulative retry attempts")
    feedback: str = Field(..., description="Constructive critique or approval verification")


def create_initial_agent_state(
    task_id: str,
    scenario_id: str,
    prompt: str,
    crop_info: Optional[Dict[str, Any]] = None
) -> AgentState:
    """
    Generates a valid initial AgentState conforming to PROJECT.md § AgentState.
    """
    default_crop = {
        "crop_type": "rice_jasmine_85",
        "growth_stage": "vegetative_tillering",
        "field_capacity": 45.0,
        "wilting_point": 15.0,
        "area_hectares": 5.0,
        "pump_power_kw": 15.0
    }
    if crop_info:
        default_crop.update(crop_info)

    return {
        "task_id": task_id,
        "scenario_id": scenario_id,
        "crop_info": default_crop,
        "user_prompt": prompt,
        "plan": [
            "1. Sense ambient weather and soil telemetry",
            "2. Optimize irrigation and fertigation schedule",
            "3. Audit carbon footprint (Scope 1-3)",
            "4. Validate agronomic guardrails via Critic",
            "5. Commit SHA-256 ESG audit entry"
        ],
        "current_step": 0,
        "thoughts": [],
        "tool_calls": [],
        "weather_data": {},
        "sensor_telemetry": {},
        "dispatch_plan": {},
        "carbon_report": {},
        "critic_verdict": {
            "approved": False,
            "retry_count": 0,
            "feedback": ""
        },
        "final_output": {},
        "errors": []
    }
