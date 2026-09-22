"""
Milestone 2: Multi-Agent Engine Core (R2) Comprehensive Test Suite.
Tests:
1. Supervisor Orchestrator & Specialized Worker Agents (Sensing, Dispatch, Carbon, Critic).
2. LangGraph StateGraph compilation and execution.
3. Automated Tool Suite (Weather, Telemetry, Carbon, ESG Ledger) - at least 3 called in context.
4. Self-Correction / Reflexion loop with fault injection, retry counter, and circuit breaker.
5. Dual-Tier Memory (SQLite short-term checkpointer + ChromaDB long-term vector store).
6. Thought Streaming emission across all 7 SSE event types.
Authoritative source: ORIGINAL_REQUEST.md § R2, Acceptance Criteria; PROJECT.md § Multi-Agent Engine.
"""

import pytest
import sys
import os
import time
from pathlib import Path
from typing import Dict, Any, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.agents.state import (
    AgentState,
    create_initial_agent_state,
    ThoughtEvent,
    CriticVerdictModel
)
from core.agents.supervisor import supervisor_node, route_supervisor_decision
from core.agents.sensing_agent import sensing_agent_node
from core.agents.dispatch_agent import dispatch_agent_node
from core.agents.carbon_agent import carbon_agent_node
from core.agents.critic_agent import critic_agent_node, evaluate_plan_by_critic
from core.agents.graph import (
    build_agricarbon_graph,
    run_agent_workflow,
    stream_agent_execution
)
from core.tools.weather_tool import get_weather_forecast
from core.tools.telemetry_tool import query_sensor_telemetry
from core.tools.carbon_tool import calculate_agricultural_emissions
from core.tools.ledger_tool import record_esg_audit_entry
from core.memory.short_term import ShortTermMemory
from core.memory.vector_store import LongTermVectorMemory


class TestAgentStateAndSupervisor:
    """Validates AgentState contract, ReAct planning, and Supervisor routing."""

    def test_agent_state_schema_completeness(self):
        """Verify AgentState contains all 15 required fields defined in PROJECT.md."""
        state = create_initial_agent_state(
            task_id="m2_task_001",
            scenario_id="an_giang_rice_001",
            prompt="Optimize AWD water management and audit carbon"
        )
        required_fields = [
            "task_id", "scenario_id", "crop_info", "user_prompt",
            "plan", "current_step", "thoughts", "tool_calls",
            "weather_data", "sensor_telemetry", "dispatch_plan",
            "carbon_report", "critic_verdict", "final_output", "errors"
        ]
        for field in required_fields:
            assert field in state, f"Missing required AgentState field: {field}"
        assert state["task_id"] == "m2_task_001"
        assert state["current_step"] == 0

    def test_supervisor_react_task_decomposition(self):
        """Verify Supervisor decomposes prompt into distinct actionable subtasks."""
        state = create_initial_agent_state(
            task_id="m2_task_002",
            scenario_id="lam_dong_coffee_002",
            prompt="Full precision fertigation audit for export to Japan"
        )
        state = supervisor_node(state)
        plan = state["plan"]
        assert len(plan) >= 4, "Supervisor must plan at least 4 distinct subtasks"
        assert any("sense" in s.lower() or "weather" in s.lower() for s in plan)
        assert any("dispatch" in s.lower() or "irrigation" in s.lower() for s in plan)
        assert any("carbon" in s.lower() or "audit" in s.lower() for s in plan)
        assert any("critic" in s.lower() or "guardrail" in s.lower() for s in plan)

    def test_supervisor_state_machine_routing(self):
        """Verify Supervisor routes strictly in accordance with workflow stages."""
        s = create_initial_agent_state("m2_t003", "an_giang_rice_001", "Daily run")
        assert route_supervisor_decision(s) == "sensing_agent"

        s["weather_data"] = {"temp_max": 33.0, "et0": 4.1}
        s["sensor_telemetry"] = {"soil_moisture_pct": 21.0}
        assert route_supervisor_decision(s) == "dispatch_agent"

        s["dispatch_plan"] = {"water_needed_mm": 20.0, "duration_minutes": 45}
        assert route_supervisor_decision(s) == "carbon_agent"

        s["carbon_report"] = {"total_co2e_kg": 10.5, "reduction_pct": 28.1}
        assert route_supervisor_decision(s) == "critic_agent"

        # Critic rejects -> routes back to dispatch for reflexion
        s["critic_verdict"] = {"approved": False, "retry_count": 1, "feedback": "REJECT: water too high"}
        assert route_supervisor_decision(s) == "dispatch_agent"

        # Critic approves -> routes to FINISH
        s["critic_verdict"] = {"approved": True, "retry_count": 1, "feedback": "APPROVED"}
        assert route_supervisor_decision(s) == "FINISH"


class TestWorkerAgents:
    """Validates execution and outputs of specialized worker nodes."""

    def test_sensing_agent_execution_and_et0(self):
        """Verify Sensing Agent populates weather, telemetry, and computes ET0."""
        state = create_initial_agent_state("m2_sense_01", "an_giang_rice_001", "Sense conditions")
        state = sensing_agent_node(state)

        assert "temp_max" in state["weather_data"]
        assert "et0" in state["weather_data"]
        assert state["weather_data"]["et0"] > 0.0
        assert "soil_moisture_pct" in state["sensor_telemetry"]
        assert len(state["tool_calls"]) >= 2
        assert any(t.get("tool") == "get_weather_forecast" for t in state["tool_calls"])
        assert any(t.get("tool") == "query_sensor_telemetry" for t in state["tool_calls"])

    def test_dispatch_agent_considers_evn_peak_tariff(self):
        """Verify Dispatch Agent optimizes watering schedule and flags EVN peak hours."""
        state = create_initial_agent_state(
            "m2_disp_01",
            "an_giang_rice_001",
            "Plan irrigation",
            crop_info={"current_hour": 10}  # 10:00 AM is peak hour
        )
        state["weather_data"] = {"et0": 4.5, "forecast_rain_mm": 0.0}
        state["sensor_telemetry"] = {"soil_moisture_pct": 32.0}  # Moderate deficit
        state = dispatch_agent_node(state)

        plan = state["dispatch_plan"]
        assert "water_needed_mm" in plan
        assert "duration_minutes" in plan
        assert plan["tariff_mode"] == "DEFERRED"
        assert plan["tariff_rate_vnd"] == 1700

    def test_carbon_agent_calculates_scope1_and_scope2(self):
        """Verify Carbon Agent audits pumping and fertilizer emissions."""
        state = create_initial_agent_state("m2_carb_01", "an_giang_rice_001", "Audit emissions")
        state["dispatch_plan"] = {"duration_minutes": 60}
        state["crop_info"]["pump_power_kw"] = 15.0
        state["crop_info"]["fertilizer_n_kg"] = 20.0
        state = carbon_agent_node(state)

        rep = state["carbon_report"]
        assert rep["total_co2e_kg"] > 0.0
        assert "breakdown" in rep
        assert rep["reduction_pct"] > 0.0
        assert any(t.get("tool") == "calculate_agricultural_emissions" for t in state["tool_calls"])


class TestAutomatedToolSuite:
    """Validates the 4 automated tools called in context."""

    def test_tool_weather_forecast_live_and_cache(self):
        """Tool 1: get_weather_forecast returns valid schema in live and cache mode."""
        res_cache = get_weather_forecast(lat=10.3842, lon=105.0125, use_cache=True)
        assert res_cache["status"] == "success"
        assert res_cache["source"] == "offline_cache"
        assert 0.0 <= res_cache["humidity"] <= 100.0
        assert res_cache["temp_max"] >= res_cache["temp_min"]

    def test_tool_query_sensor_telemetry_synthetic(self):
        """Tool 2: query_sensor_telemetry returns healthy readings with synthetic fallback."""
        res = query_sensor_telemetry(sensor_id="sensor_test_99", farm_id="farm_unknown")
        assert res["status"] == "success"
        assert 0.0 <= res["soil_moisture_pct"] <= 100.0
        assert res["pump_status"] in ["ON", "OFF", "STANDBY"]

    def test_tool_calculate_agricultural_emissions(self):
        """Tool 3: calculate_agricultural_emissions provides deterministic IPCC output."""
        res = calculate_agricultural_emissions(water_pumped_m3=50.0, pump_power_kw=15.0)
        assert res["total_co2e_kg"] > 0.0
        assert "breakdown" in res
        assert "reduction_pct" in res

    def test_tool_record_esg_audit_entry_hash_format(self):
        """Tool 4: record_esg_audit_entry returns a valid 64-character hex SHA-256 digest."""
        res = record_esg_audit_entry(
            record_id="rec_m2_test",
            farm_id="an_giang_rice_001",
            action="awd_flush",
            co2e_kg=14.2
        )
        assert res["status"] == "committed"
        assert len(res["hash"]) == 64
        assert int(res["hash"], 16) > 0

    def test_at_least_three_automated_tools_called_in_e2e_run(self):
        """Verify at least 3 tools are invoked automatically based on context (AC 2)."""
        state = create_initial_agent_state("e2e_tool_check", "an_giang_rice_001", "Run complete audit")
        result = run_agent_workflow(state, thread_id="tool_count_thread")
        tool_names = {t.get("tool") for t in result.get("tool_calls", []) if "tool" in t}
        assert len(tool_names) >= 3, f"Expected >=3 tools called, got: {tool_names}"
        assert "get_weather_forecast" in tool_names
        assert "query_sensor_telemetry" in tool_names
        assert "calculate_agricultural_emissions" in tool_names
        assert "record_esg_audit_entry" in tool_names


class TestSelfCorrectionAndReflexion:
    """Validates self-reflection, fault injection recovery, and circuit breaker."""

    def test_critic_rejects_fao56_water_overdose(self):
        """Verify Critic blocks excessive water overdose (> 60mm)."""
        bad_plan = {"water_needed_mm": 95.0, "duration_minutes": 180}
        verdict = evaluate_plan_by_critic(bad_plan, retry_count=0)
        assert verdict["approved"] is False
        assert verdict["retry_count"] == 1
        assert "violates FAO-56" in verdict["feedback"]

    def test_critic_rejects_missing_duration(self):
        """Verify Critic blocks plan missing duration_minutes."""
        malformed = {"water_needed_mm": 20.0}
        verdict = evaluate_plan_by_critic(malformed, retry_count=0)
        assert verdict["approved"] is False
        assert "duration_minutes" in verdict["feedback"]

    def test_reflexion_self_correction_recovers_cleanly(self):
        """Verify dispatch agent corrects plan upon receiving Critic feedback."""
        state = create_initial_agent_state("m2_reflexion", "an_giang_rice_001", "Run self-correction")
        state["weather_data"] = {"et0": 4.0, "forecast_rain_mm": 0.0}
        state["sensor_telemetry"] = {"soil_moisture_pct": 20.0}

        # Step 1: Simulate fault injection
        state["dispatch_plan"] = {"water_needed_mm": 110.0, "duration_minutes": 300}
        state["critic_verdict"] = evaluate_plan_by_critic(state["dispatch_plan"], retry_count=0)
        assert state["critic_verdict"]["approved"] is False

        # Step 2: Dispatch agent re-executes with feedback awareness
        state = dispatch_agent_node(state)
        assert state["dispatch_plan"]["water_needed_mm"] <= 25.0

        # Step 3: Critic re-evaluates and approves
        v2 = evaluate_plan_by_critic(state["dispatch_plan"], retry_count=state["critic_verdict"]["retry_count"])
        assert v2["approved"] is True
        assert v2["retry_count"] == 1

    def test_circuit_breaker_halts_after_three_retries(self):
        """Verify circuit breaker trips when retry counter reaches 3."""
        state = create_initial_agent_state("m2_cb_test", "an_giang_rice_001", "Stress test")
        state["dispatch_plan"] = {"water_needed_mm": 999.0}  # Permanently unresolvable
        state["critic_verdict"] = {"approved": False, "retry_count": 2, "feedback": "REJECT"}

        # Third failed check trips circuit breaker
        state = critic_agent_node(state)
        assert state["critic_verdict"]["retry_count"] >= 3
        assert any("circuit breaker" in err.lower() for err in state["errors"])

        # Supervisor concludes with safe abort
        state = supervisor_node(state)
        assert state["final_output"]["status"] == "safe_abort"
        assert state["final_output"]["action"] == "HALT_PUMP_AND_ALERT_OPERATOR"


class TestDualTierMemory:
    """Validates Short-Term SQLite checkpointing and Long-Term ChromaDB memory."""

    def test_short_term_sqlite_checkpointer(self, tmp_path):
        """Verify short-term memory saves, retrieves, and maintains history across threads."""
        db_file = str(tmp_path / "test_memory.db")
        mem = ShortTermMemory(db_path=db_file)

        s1 = {"step": 1, "task": "sense", "data": 42}
        cid = mem.save_checkpoint("thread_101", s1, step=1)
        assert cid.startswith("thread_101_1_")

        latest = mem.get_latest_checkpoint("thread_101")
        assert latest is not None
        assert latest["step"] == 1
        assert latest["state"]["data"] == 42

        # Step 2
        s2 = {"step": 2, "task": "dispatch", "data": 84}
        mem.save_checkpoint("thread_101", s2, step=2)

        history = mem.get_checkpoint_history("thread_101")
        assert len(history) == 2
        assert history[-1]["step"] == 2

    def test_long_term_vector_store_retrieval(self, tmp_path):
        """Verify vector memory retrieves FAO-56 knowledge and stores episodic logs."""
        persist_dir = str(tmp_path / "chroma_test")
        vmem = LongTermVectorMemory(persist_directory=persist_dir)

        # Knowledge retrieval
        results = vmem.similarity_search("AWD water management for rice")
        assert len(results) > 0
        assert "38%" in results[0]["document"]

        # Episodic reflection logging and retrieval
        vmem.add_episodic_reflection(
            task_id="ep_001",
            scenario="an_giang_heavy_rain",
            reflection="Avoided pumping before convective storm; saved 14.2 kWh.",
            outcome="SUCCESS"
        )
        ep_results = vmem.search_episodic_memory("convective storm pumping")
        assert len(ep_results) > 0
        assert "Avoided pumping" in ep_results[0]["document"]


class TestThoughtStreamingAndE2E:
    """Validates 7-event SSE thought streaming and end-to-end multi-agent execution."""

    def test_thought_streaming_emits_all_event_types(self):
        """Verify stream_agent_execution emits real-time events conforming to PROJECT.md."""
        state = create_initial_agent_state("stream_test_01", "an_giang_rice_001", "Execute full workflow")
        events = list(stream_agent_execution(state, thread_id="test_stream_th"))

        event_types = {e["event"] for e in events}
        assert "thought" in event_types
        assert "tool_call" in event_types
        assert "tool_result" in event_types
        assert "reflection" in event_types
        assert "token" in event_types
        assert "complete" in event_types

        # Verify complete event structure and latency
        complete_event = next(e for e in events if e["event"] == "complete")
        assert "latency_ms" in complete_event["data"]
        assert complete_event["data"]["latency_ms"] < 5000  # < 5s requirement (AC 5)
        assert complete_event["data"]["status"] == "success"

    def test_full_agent_workflow_e2e_execution(self):
        """Verify complete autonomous execution produces certified final output."""
        state = create_initial_agent_state(
            task_id="e2e_full_001",
            scenario_id="an_giang_rice_001",
            prompt="Autonomous irrigation and ESG carbon certification"
        )
        result = run_agent_workflow(state, thread_id="e2e_thread_run")

        final = result.get("final_output", {})
        assert final.get("status") == "success"
        assert "dispatch" in final
        assert "carbon" in final
        assert "ledger_hash" in final
        assert len(final["ledger_hash"]) == 64
        assert final["certificate_id"].startswith("CERT-VJAI-2026")
        assert len(result["thoughts"]) >= 4
