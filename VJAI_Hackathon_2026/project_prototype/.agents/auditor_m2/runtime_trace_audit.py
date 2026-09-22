import sys
import os
sys.path.insert(0, os.path.abspath("."))
import time
from core.agents.state import create_initial_agent_state
from core.agents.supervisor import supervisor_node, route_supervisor_decision
from core.agents.sensing_agent import sensing_agent_node
from core.agents.dispatch_agent import dispatch_agent_node
from core.agents.carbon_agent import carbon_agent_node
from core.agents.critic_agent import evaluate_plan_by_critic, critic_agent_node
from core.tools.ledger_tool import record_esg_audit_entry
from core.tools.weather_tool import get_weather_forecast
from core.tools.telemetry_tool import query_sensor_telemetry
from core.tools.carbon_tool import calculate_agricultural_emissions
from core.memory.short_term import ShortTermMemory
from core.memory.vector_store import LongTermVectorMemory

print("=== 1. SUPERVISOR DECOMPOSITION & ROUTING TRACE ===")
s1 = create_initial_agent_state("t1", "an_giang_rice_001", "Plan irrigation for rice")
print("Initial plan length:", len(s1["plan"]))
print("Initial route:", route_supervisor_decision(s1))

s1["weather_data"] = {"temp_max": 33.0, "et0": 4.5}
s1["sensor_telemetry"] = {"soil_moisture_pct": 22.0}
print("Route after sensing:", route_supervisor_decision(s1))

s1["dispatch_plan"] = {"water_needed_mm": 25.0, "duration_minutes": 60}
print("Route after dispatch:", route_supervisor_decision(s1))

s1["carbon_report"] = {"total_co2e_kg": 15.0, "reduction_pct": 28.1}
print("Route after carbon:", route_supervisor_decision(s1))

s1["critic_verdict"] = {"approved": False, "retry_count": 1, "feedback": "REJECT"}
print("Route on critic rejection:", route_supervisor_decision(s1))

s1["critic_verdict"] = {"approved": True, "retry_count": 1, "feedback": "APPROVED"}
print("Route on critic approval:", route_supervisor_decision(s1))

print("\n=== 2. DYNAMIC TOOL QUERIES & COMPUTATION ===")
# Weather tool perturbation
w_live = get_weather_forecast(10.3842, 105.0125, use_cache=False)
w_cache = get_weather_forecast(10.3842, 105.0125, use_cache=True)
print(f"Weather live source: {w_live['source']}, temp_max={w_live['temp_max']}, rain={w_live['forecast_rain_mm']}")
print(f"Weather cache source: {w_cache['source']}, temp_max={w_cache['temp_max']}, rain={w_cache['forecast_rain_mm']}")

# Telemetry tool perturbation
t1 = query_sensor_telemetry("sensor_polder_04", "an_giang_rice_001")
t2 = query_sensor_telemetry("sensor_custom", "farm_custom")
print(f"Telemetry preset: {t1['soil_moisture_pct']}%, source={t1['source']}")
print(f"Telemetry synthetic: {t2['soil_moisture_pct']}%, source={t2['source']}")

# Carbon tool perturbation
c1 = calculate_agricultural_emissions(50.0, 15.0, fertilizer_n_kg=10.0)
c2 = calculate_agricultural_emissions(100.0, 15.0, fertilizer_n_kg=20.0)
print(f"Emissions 50m3: {c1['total_co2e_kg']} kg CO2e, reduction={c1['reduction_pct']}%")
print(f"Emissions 100m3: {c2['total_co2e_kg']} kg CO2e, reduction={c2['reduction_pct']}%")
assert c2['total_co2e_kg'] > c1['total_co2e_kg'], "Emissions should increase with volume & fertilizer"

# Ledger tool perturbation
l1 = record_esg_audit_entry("rec_01", "farm_01", "act", 10.0)
l2 = record_esg_audit_entry("rec_01", "farm_01", "act", 10.1) # tiny perturbation
print(f"Ledger hash 1: {l1['hash']}")
print(f"Ledger hash 2: {l2['hash']}")
assert l1['hash'] != l2['hash'], "Hash must change with perturbed input"
assert len(l1['hash']) == 64

print("\n=== 3. DYNAMIC CRITIC BOUNDARY EVALUATION ===")
v_pass = evaluate_plan_by_critic({"water_needed_mm": 55.0, "duration_minutes": 120})
v_overdose = evaluate_plan_by_critic({"water_needed_mm": 65.0, "duration_minutes": 120})
v_overtime = evaluate_plan_by_critic({"water_needed_mm": 30.0, "duration_minutes": 500})
v_missing = evaluate_plan_by_critic({"water_needed_mm": 30.0})

print(f"Pass case: approved={v_pass['approved']}, feedback={v_pass['feedback']}")
print(f"Overdose case: approved={v_overdose['approved']}, feedback={v_overdose['feedback']}")
print(f"Overtime case: approved={v_overtime['approved']}, feedback={v_overtime['feedback']}")
print(f"Missing field: approved={v_missing['approved']}, feedback={v_missing['feedback']}")

assert v_pass['approved'] is True
assert v_overdose['approved'] is False and "violates FAO-56" in v_overdose['feedback']
assert v_overtime['approved'] is False and "motor burnout" in v_overtime['feedback']
assert v_missing['approved'] is False and "duration_minutes" in v_missing['feedback']

print("\n=== 4. REPRODUCING ROUTING DEADLOCK (CHALLENGER 1 FINDING) ===")
# Trace what happens in route_supervisor_decision when dispatch re-executes after rejection
state_loop = create_initial_agent_state("loop_test", "an_giang_rice_001", "Test loop")
state_loop["weather_data"] = {"et0": 4.5}
state_loop["sensor_telemetry"] = {"soil_moisture_pct": 20.0}
state_loop["dispatch_plan"] = {"water_needed_mm": 75.0, "duration_minutes": 120} # Rejected proposal
state_loop["carbon_report"] = {"total_co2e_kg": 20.0}
state_loop["critic_verdict"] = evaluate_plan_by_critic(state_loop["dispatch_plan"], retry_count=0)
print(f"Initial critic verdict: approved={state_loop['critic_verdict']['approved']}, retry={state_loop['critic_verdict']['retry_count']}")

# Router decides to send to dispatch_agent:
next_step = route_supervisor_decision(state_loop)
print(f"Router decision 1: {next_step}")
assert next_step == "dispatch_agent"

# dispatch_agent executes and updates the plan:
state_loop = dispatch_agent_node(state_loop)
print(f"Dispatch revised water: {state_loop['dispatch_plan']['water_needed_mm']}mm")

# Supervisor checks router again:
next_step_after_dispatch = route_supervisor_decision(state_loop)
print(f"Router decision 2 (after dispatch revision): {next_step_after_dispatch}")
if next_step_after_dispatch == "dispatch_agent":
    print("CONFIRMED DEFECT: Router stuck in infinite loop returning 'dispatch_agent'!")
else:
    print(f"Router proceeded to: {next_step_after_dispatch}")

print("\nALL EMPIRICAL TRACES COMPLETE.")
