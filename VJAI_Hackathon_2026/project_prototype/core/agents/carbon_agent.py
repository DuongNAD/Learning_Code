"""
Carbon Footprint Auditor Worker Agent.
Calculates Scope 1, 2, and 3 agricultural greenhouse gas emissions
conforming to 2006/2019 IPCC Guidelines and GHG Protocol Agricultural Guidance.
Conforms strictly to PROJECT.md § Multi-Agent Engine and ORIGINAL_REQUEST.md § R2.
"""

from typing import Dict, Any
from core.agents.state import AgentState
from core.tools.carbon_tool import calculate_agricultural_emissions
from core.domain.carbon_models import calculate_scope3_logistics


def carbon_agent_node(state: AgentState) -> AgentState:
    """
    Carbon Auditor Worker Node:
    Calls calculate_agricultural_emissions tool and records Scope 1-3 audit metrics.
    """
    dispatch_plan = state.get("dispatch_plan", {})
    crop_info = state.get("crop_info", {})

    duration_mins = float(dispatch_plan.get("duration_minutes", 0))
    pump_power_kw = float(crop_info.get("pump_power_kw", 15.0))
    fertilizer_n_kg = float(crop_info.get("fertilizer_n_kg", 0.0))
    diesel_liters = float(crop_info.get("diesel_liters", 0.0))

    # Hydraulic volume pumped (assuming 50 m3/hr standard flow rate)
    pumping_hours = duration_mins / 60.0
    water_pumped_m3 = pumping_hours * 50.0

    # 1. Tool Call: calculate_agricultural_emissions
    tool_call = {
        "tool": "calculate_agricultural_emissions",
        "args": {
            "water_pumped_m3": round(water_pumped_m3, 2),
            "pump_power_kw": pump_power_kw,
            "fertilizer_n_kg": fertilizer_n_kg,
            "diesel_liters": diesel_liters
        }
    }
    state["tool_calls"].append(tool_call)

    carbon_report = calculate_agricultural_emissions(
        water_pumped_m3=water_pumped_m3,
        pump_power_kw=pump_power_kw,
        fertilizer_n_kg=fertilizer_n_kg,
        diesel_liters=diesel_liters
    )

    state["tool_calls"].append({
        "tool": "calculate_agricultural_emissions",
        "result": {
            "total_co2e_kg": carbon_report["total_co2e_kg"],
            "reduction_pct": carbon_report["reduction_pct"],
            "baseline_co2e_kg": carbon_report["baseline_co2e_kg"]
        }
    })

    # Optional Scope 3 export logistics if export tonnage specified
    tonnage = crop_info.get("export_tonnage")
    if tonnage:
        scope3 = calculate_scope3_logistics(
            tonnage=float(tonnage),
            origin_region="an_giang" if "rice" in crop_info.get("crop_type", "") else "lam_dong"
        )
        carbon_report["scope3_logistics"] = scope3

    state["carbon_report"] = carbon_report
    state["current_step"] = state.get("current_step", 0) + 1

    thought_msg = (
        f"Audited carbon emissions: {carbon_report['total_co2e_kg']} kg CO2e "
        f"vs baseline {carbon_report['baseline_co2e_kg']} kg CO2e "
        f"({carbon_report['reduction_pct']}% reduction achieved)."
    )
    state["thoughts"].append({
        "agent": "CarbonAuditorWorker",
        "step": "carbon_auditing",
        "thought": thought_msg
    })

    return state
