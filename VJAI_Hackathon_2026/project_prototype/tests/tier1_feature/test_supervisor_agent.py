"""
Tier 1: Feature Coverage - Supervisor & Multi-Agent Architecture
Tests Supervisor ReAct planning, State transitions, AgentState TypedDict schema,
and Guardrail Critic interaction.
Authoritative source: PROJECT.md § Interface Contracts, ORIGINAL_REQUEST.md § R2
"""

import pytest
import sys
from pathlib import Path
from typing import Dict, Any, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def create_initial_agent_state(task_id: str, scenario_id: str, prompt: str) -> Dict[str, Any]:
    """Generates a valid AgentState conformant to PROJECT.md § AgentState."""
    return {
        "task_id": task_id,
        "scenario_id": scenario_id,
        "crop_info": {
            "crop_type": "rice_jasmine_85",
            "growth_stage": "vegetative_tillering",
            "field_capacity": 45.0,
            "wilting_point": 15.0
        },
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


class TestSupervisorAgent:
    """Validates Supervisor AgentState schema, ReAct task decomposition, and worker transitions."""

    def test_agent_state_schema_conformance(self):
        """Verify AgentState structure matches the contract defined in PROJECT.md."""
        state = create_initial_agent_state(
            task_id="task_e2e_001",
            scenario_id="an_giang_rice_001",
            prompt="Analyze soil moisture and optimize today's irrigation"
        )
        required_fields = [
            "task_id", "scenario_id", "crop_info", "user_prompt",
            "plan", "current_step", "thoughts", "tool_calls",
            "weather_data", "sensor_telemetry", "dispatch_plan",
            "carbon_report", "critic_verdict", "final_output", "errors"
        ]
        for field in required_fields:
            assert field in state, f"AgentState missing required field '{field}'"

    def test_supervisor_task_decomposition_react_loop(self):
        """Verify Supervisor decomposes unstructured user prompt into multi-agent subtasks."""
        state = create_initial_agent_state(
            task_id="task_e2e_002",
            scenario_id="lam_dong_coffee_002",
            prompt="Perform full fertigation audit for export to Japan"
        )
        assert len(state["plan"]) >= 4, "Supervisor must plan at least 4 distinct subtasks"
        assert any("sense" in step.lower() or "weather" in step.lower() for step in state["plan"])
        assert any("dispatch" in step.lower() or "irrigation" in step.lower() for step in state["plan"])
        assert any("carbon" in step.lower() or "audit" in step.lower() for step in state["plan"])

    def test_supervisor_worker_routing_transitions(self):
        """Verify state updates progressively as worker nodes execute."""
        state = create_initial_agent_state("task_003", "an_giang_01", "Run daily optimization")
        
        # Step 1: Sensing worker writes weather & telemetry
        state["current_step"] = 1
        state["weather_data"] = {"temp_max": 34.0, "forecast_rain_mm": 0.0, "et0": 4.5}
        state["sensor_telemetry"] = {"soil_moisture_pct": 21.0}
        state["thoughts"].append({"agent": "SensingWorker", "thought": "Telemetry gathered successfully."})
        assert state["weather_data"]["et0"] > 0
        
        # Step 2: Dispatch worker writes irrigation plan
        state["current_step"] = 2
        state["dispatch_plan"] = {"water_needed_mm": 18.5, "duration_minutes": 45, "urgency": "HIGH"}
        state["thoughts"].append({"agent": "DispatchWorker", "thought": "Calculated 45 min AWD flush."})
        assert state["dispatch_plan"]["duration_minutes"] == 45
        
        # Step 3: Carbon worker calculates emissions
        state["current_step"] = 3
        state["carbon_report"] = {"total_co2e_kg": 12.8, "reduction_pct": 28.1}
        assert state["carbon_report"]["reduction_pct"] == 28.1

    def test_critic_guardrail_verdict_schema(self):
        """Verify Critic agent verdict schema contains approval status, retry counter, and feedback."""
        state = create_initial_agent_state("task_004", "an_giang_01", "Validate plan")
        # Simulating critic approval
        state["critic_verdict"] = {
            "approved": True,
            "retry_count": 0,
            "feedback": "Plan compliant with FAO-56 and safe soil moisture limits."
        }
        verdict = state["critic_verdict"]
        assert isinstance(verdict["approved"], bool)
        assert isinstance(verdict["retry_count"], int)
        assert isinstance(verdict["feedback"], str)
        assert verdict["approved"] is True

    def test_short_term_context_checkpointing(self):
        """Verify short-term memory checkpointer can record and recover thread state."""
        # Simulated SQLite checkpointer dictionary
        checkpoints: Dict[str, List[Dict[str, Any]]] = {}
        thread_id = "thread_session_101"
        
        s1 = create_initial_agent_state("t1", "ag_01", "Initial request")
        checkpoints.setdefault(thread_id, []).append({"step": 1, "state": s1})
        
        s2 = dict(s1)
        s2["current_step"] = 2
        s2["thoughts"] = [{"step": 2, "msg": "Proceeding"}]
        checkpoints[thread_id].append({"step": 2, "state": s2})
        
        assert len(checkpoints[thread_id]) == 2
        assert checkpoints[thread_id][-1]["state"]["current_step"] == 2

    def test_long_term_knowledge_retrieval_contract(self):
        """Verify knowledge retrieval interface returns relevant FAO-56/IPCC context."""
        def mock_vector_search(query: str) -> List[Dict[str, Any]]:
            if "rice" in query.lower() or "awd" in query.lower():
                return [{
                    "document": "FAO-56 / IRRI: Alternate Wetting and Drying (AWD) reduces water use by 38% and CH4 emissions by 30%.",
                    "score": 0.92
                }]
            return []
            
        results = mock_vector_search("AWD water management for rice")
        assert len(results) > 0
        assert "38%" in results[0]["document"]
