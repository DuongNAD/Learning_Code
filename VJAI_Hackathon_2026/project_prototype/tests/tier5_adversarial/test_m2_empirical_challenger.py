"""
Tier 5 Adversarial Stress Test Suite: Milestone 2 Empirical Challenger.
Focus:
1. Tool Error Injection & Network Failover (HTTP 500, 502, 503, 504, 404, ConnectionError, ReadTimeout, SSLError, Malformed JSON).
2. Soil IoT Telemetry DB Disconnect and Synthetic Failover.
3. Sensing Agent node behavior under total network blackout.
4. Critic Rejection on Out-of-Bounds proposals (Water > 60mm, Duration > 480m, Malformed).
5. Reflexion Self-Correction Recovery.
6. Circuit Breaker tripping strictly after 3 retries under unrecoverable fault.
7. LangGraph StateGraph termination and SSE streaming output under circuit breaker trip.
8. Adversarial corner cases (Zero irrigation, boundary values, negative numbers).
"""

import pytest
import sys
import socket
from pathlib import Path
from unittest.mock import patch, MagicMock
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.tools.weather_tool import get_weather_forecast
from core.tools.telemetry_tool import query_sensor_telemetry
from core.tools.carbon_tool import calculate_agricultural_emissions
from core.tools.ledger_tool import record_esg_audit_entry
from core.agents.state import create_initial_agent_state
from core.agents.sensing_agent import sensing_agent_node
from core.agents.dispatch_agent import dispatch_agent_node
from core.agents.carbon_agent import carbon_agent_node
from core.agents.critic_agent import evaluate_plan_by_critic, critic_agent_node
from core.agents.supervisor import supervisor_node, route_supervisor_decision
from core.agents.graph import build_agricarbon_graph, run_agent_workflow, stream_agent_execution


class TestToolErrorInjectionLiveAndMocks:
    """Empirical verification of tool resilience under adverse network conditions."""

    @pytest.mark.parametrize("status_code", [500, 502, 503, 504, 404, 400])
    def test_open_meteo_http_error_codes_fallback_cleanly(self, status_code):
        """Verify HTTP 4xx and 5xx errors from Open-Meteo transparently trigger offline cache."""
        with patch("requests.get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.status_code = status_code
            mock_get.return_value = mock_resp

            res = get_weather_forecast(lat=10.3842, lon=105.0125, simulate_network_error=False)

            assert res["status"] == "success"
            assert res["fallback_engaged"] is True
            assert res["source"] == "offline_cache"
            assert res["temp_max"] >= res["temp_min"]
            assert 0.0 <= res["humidity"] <= 100.0

    @pytest.mark.parametrize("exception_cls", [
        requests.exceptions.ConnectionError,
        requests.exceptions.ReadTimeout,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.SSLError,
        requests.exceptions.ChunkedEncodingError,
        socket.gaierror
    ])
    def test_open_meteo_network_exceptions_fallback_cleanly(self, exception_cls):
        """Verify raw network disconnects and timeouts transparently trigger offline cache."""
        with patch("requests.get") as mock_get:
            mock_get.side_effect = exception_cls("Simulated network breakdown")

            res = get_weather_forecast(lat=10.3842, lon=105.0125, simulate_network_error=False)

            assert res["status"] == "success"
            assert res["fallback_engaged"] is True
            assert res["source"] == "offline_cache"
            assert res["temp_max"] > 0.0

    def test_open_meteo_malformed_empty_json_fallback(self):
        """Verify API 200 OK with empty or malformed JSON falls back without unhandled crash."""
        with patch("requests.get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.status_code = 200
            mock_resp.json.return_value = {}
            mock_get.return_value = mock_resp

            res = get_weather_forecast(lat=10.3842, lon=105.0125, simulate_network_error=False)

            assert res["status"] == "success"
            assert res["temp_max"] >= res["temp_min"]

    def test_telemetry_db_disconnect_engages_synthetic_generator(self):
        """Verify query_sensor_telemetry handles simulated database disconnect."""
        res = query_sensor_telemetry(
            sensor_id="sensor_an_giang_01",
            farm_id="an_giang_rice_001",
            simulate_db_disconnect=True
        )
        assert res["status"] == "success"
        assert res["fallback_engaged"] is True
        assert res["source"] == "synthetic_generator"
        assert 0.0 <= res["soil_moisture_pct"] <= 100.0

    def test_telemetry_unknown_farm_engages_synthetic_generator(self):
        """Verify unmapped farm parcels engage synthetic fallback seamlessly."""
        res = query_sensor_telemetry(
            sensor_id="sensor_unknown_999",
            farm_id="unknown_region_parcel_xyz"
        )
        assert res["status"] == "success"
        assert res["fallback_engaged"] is True
        assert res["source"] == "synthetic_generator"

    def test_telemetry_physical_bounds_normalization(self):
        """Verify soil moisture clamped to [0, 100] and pump status normalized."""
        res = query_sensor_telemetry(
            sensor_id="sensor_bound_test",
            farm_id="custom_farm"
        )
        assert 0.0 <= res["soil_moisture_pct"] <= 100.0
        assert res["pump_status"] in ["ON", "OFF", "STANDBY"]

    def test_sensing_agent_node_resilience_under_dual_network_failure(self):
        """Verify sensing_agent_node executes completely even when both Weather API and DB fail."""
        state = create_initial_agent_state(
            task_id="stress_sense_001",
            scenario_id="unknown_farm_failover",
            prompt="Test sensing under network crash"
        )
        with patch("requests.get") as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError("Total internet outage")
            state = sensing_agent_node(state)

        assert state["weather_data"]["fallback_engaged"] is True
        assert state["sensor_telemetry"]["fallback_engaged"] is True
        assert state["weather_data"]["et0"] > 0.0
        assert len(state["tool_calls"]) >= 2
        assert len(state["thoughts"]) >= 1


class TestCriticRejectionAndReflexion:
    """Empirical verification of Critic rejection, Reflexion recovery, and Circuit Breaker."""

    @pytest.mark.parametrize("water_mm", [60.1, 85.0, 150.0, 999.0])
    def test_critic_rejects_out_of_bounds_water_dosage(self, water_mm):
        """Verify Critic strictly rejects water dosages exceeding FAO-56 60mm limit."""
        plan = {"water_needed_mm": water_mm, "duration_minutes": 120}
        verdict = evaluate_plan_by_critic(plan, retry_count=0)
        assert verdict["approved"] is False
        assert verdict["retry_count"] == 1
        assert "FAO-56" in verdict["feedback"]

    @pytest.mark.parametrize("duration_mins", [481, 600, 1440])
    def test_critic_rejects_excessive_pump_duration(self, duration_mins):
        """Verify Critic strictly rejects pump durations > 480 mins (motor burnout risk)."""
        plan = {"water_needed_mm": 30.0, "duration_minutes": duration_mins}
        verdict = evaluate_plan_by_critic(plan, retry_count=0)
        assert verdict["approved"] is False
        assert verdict["retry_count"] == 1
        assert "motor burnout" in verdict["feedback"].lower()

    def test_critic_rejects_missing_duration_minutes(self):
        """Verify Critic strictly rejects plans missing mandatory duration_minutes."""
        plan = {"water_needed_mm": 25.0}
        verdict = evaluate_plan_by_critic(plan, retry_count=0)
        assert verdict["approved"] is False
        assert verdict["retry_count"] == 1
        assert "duration_minutes" in verdict["feedback"]

    def test_critic_approves_boundary_maximums(self):
        """Verify Critic approves plans exactly at upper safe limits (60mm, 480 mins)."""
        plan = {"water_needed_mm": 60.0, "duration_minutes": 480}
        verdict = evaluate_plan_by_critic(plan, retry_count=0)
        assert verdict["approved"] is True
        assert verdict["retry_count"] == 0

    def test_reflexion_self_correction_recovers_to_valid_plan(self):
        """Verify closed-loop self-correction: Fault -> Rejection -> Correction -> Approval."""
        state = create_initial_agent_state(
            task_id="stress_reflexion_001",
            scenario_id="an_giang_rice_001",
            prompt="Test reflexion loop"
        )
        state["weather_data"] = {"et0": 4.5, "forecast_rain_mm": 0.0}
        state["sensor_telemetry"] = {"soil_moisture_pct": 20.0}
        state["carbon_report"] = {"total_co2e_kg": 15.0}

        # Step 1: Inject out-of-bounds proposal
        state["dispatch_plan"] = {"water_needed_mm": 120.0, "duration_minutes": 360}
        state = critic_agent_node(state)
        assert state["critic_verdict"]["approved"] is False
        assert state["critic_verdict"]["retry_count"] == 1

        # Step 2: Supervisor routes back to dispatch worker for reflexion
        next_step = route_supervisor_decision(state)
        assert next_step == "dispatch_agent", f"Expected dispatch_agent, got {next_step}"

        # Step 3: Dispatch worker consumes critique feedback and adjusts
        state = dispatch_agent_node(state)
        assert state["dispatch_plan"]["water_needed_mm"] <= 25.0

        # Step 4: Routing must NOT loop back to dispatch_agent again; must route to critic_agent (or carbon_agent)
        next_step_after_fix = route_supervisor_decision(state)
        assert next_step_after_fix in ["critic_agent", "carbon_agent"], (
            f"Expected routing to critic_agent or carbon_agent after plan correction, but got: {next_step_after_fix}"
        )

    def test_circuit_breaker_trips_strictly_at_three_retries(self):
        """Verify circuit breaker trips and transitions to safe abort when retries reach 3."""
        state = create_initial_agent_state(
            task_id="stress_cb_001",
            scenario_id="an_giang_rice_001",
            prompt="Test circuit breaker tripping"
        )
        bad_plan = {"water_needed_mm": 999.0, "duration_minutes": 999}
        state["dispatch_plan"] = bad_plan
        state["weather_data"] = {"et0": 4.0}
        state["sensor_telemetry"] = {"soil_moisture_pct": 20.0}
        state["carbon_report"] = {"total_co2e_kg": 10.0}

        # Iteration 1
        state = critic_agent_node(state)
        assert state["critic_verdict"]["retry_count"] == 1
        assert state["critic_verdict"]["approved"] is False
        assert route_supervisor_decision(state) == "dispatch_agent"

        # Iteration 2
        state["dispatch_plan"] = bad_plan
        state = critic_agent_node(state)
        assert state["critic_verdict"]["retry_count"] == 2
        assert state["critic_verdict"]["approved"] is False
        assert route_supervisor_decision(state) == "dispatch_agent"

        # Iteration 3: Terminal failure
        state["dispatch_plan"] = bad_plan
        state = critic_agent_node(state)
        assert state["critic_verdict"]["retry_count"] == 3
        assert state["critic_verdict"]["approved"] is False
        assert any("circuit breaker" in err.lower() for err in state["errors"])

        # Routing check: must route to FINISH, NOT loop to dispatch_agent
        next_step = route_supervisor_decision(state)
        assert next_step == "FINISH"

        # Supervisor concludes with safe abort
        state = supervisor_node(state)
        assert state["final_output"]["status"] == "safe_abort"
        assert state["final_output"]["action"] == "HALT_PUMP_AND_ALERT_OPERATOR"
        assert state["final_output"]["retry_count"] == 3

    def test_langgraph_e2e_circuit_breaker_termination(self):
        """Verify LangGraph execution halts cleanly without recursion/infinite loop when circuit breaker trips."""
        def mock_eval(*args, **kwargs):
            retry = kwargs.get("retry_count", 0)
            return {
                "approved": False,
                "retry_count": retry + 1,
                "feedback": "REJECT: Persistent unresolvable fault."
            }

        with patch("core.agents.critic_agent.evaluate_plan_by_critic", side_effect=mock_eval):
            from core.agents.graph import build_agricarbon_graph
            app = build_agricarbon_graph()
            state = create_initial_agent_state(
                task_id="stress_langgraph_cb",
                scenario_id="an_giang_rice_001",
                prompt="Adversarial circuit breaker test"
            )
            # Must terminate within reasonable recursion limit (<= 15)
            result = app.invoke(state, config={"configurable": {"thread_id": "cb_thread"}, "recursion_limit": 15})

            assert result["final_output"]["status"] == "safe_abort"
            assert result["final_output"]["action"] == "HALT_PUMP_AND_ALERT_OPERATOR"
            assert result["critic_verdict"]["retry_count"] == 3

    def test_sse_stream_circuit_breaker_emission(self):
        """Verify SSE thought stream emits reflection, error, and complete events on safe abort."""
        def mock_eval(*args, **kwargs):
            retry = kwargs.get("retry_count", 0)
            return {
                "approved": False,
                "retry_count": retry + 1,
                "feedback": "REJECT: Persistent unresolvable fault."
            }

        with patch("core.agents.critic_agent.evaluate_plan_by_critic", side_effect=mock_eval):
            state = create_initial_agent_state(
                task_id="stress_stream_cb",
                scenario_id="an_giang_rice_001",
                prompt="Stream circuit breaker test"
            )
            events = list(stream_agent_execution(state, thread_id="stress_stream_cb_th", max_steps=15))

            event_types = [e["event"] for e in events]
            assert "reflection" in event_types
            assert "error" in event_types
            assert "complete" in event_types

            # Verify error message
            error_events = [e for e in events if e["event"] == "error"]
            assert any("circuit breaker" in e["data"]["message"].lower() for e in error_events)

            # Verify complete event
            complete_event = next(e for e in events if e["event"] == "complete")
            assert complete_event["data"]["status"] == "safe_abort"
            assert complete_event["data"]["final_result"]["action"] == "HALT_PUMP_AND_ALERT_OPERATOR"


class TestAdversarialCornerCases:
    """Tests extreme numerical and edge-case inputs."""

    def test_zero_irrigation_due_to_heavy_rain(self):
        """Verify when rain cancels irrigation, water_needed_mm=0 is approved by Critic."""
        zero_plan = {"water_needed_mm": 0.0, "duration_minutes": 0, "avoid_reason": "heavy_rain"}
        verdict = evaluate_plan_by_critic(zero_plan, retry_count=0)
        assert verdict["approved"] is True

    def test_critic_preserves_retry_count_on_approval(self):
        """Verify retry_count in critic verdict preserves historical count on approval."""
        plan = {"water_needed_mm": 20.0, "duration_minutes": 45}
        v = evaluate_plan_by_critic(plan, retry_count=2)
        assert v["approved"] is True
        assert v["retry_count"] == 2
