"""
Resource Eco-Dispatch Worker Agent.
Optimizes precision irrigation schedules and fertigation dosages using FAO-56 water balance,
rain avoidance suppression, and EVN TOU peak electricity tariff avoidance.
Conforms strictly to PROJECT.md § Multi-Agent Engine and ORIGINAL_REQUEST.md § R2.
"""

from typing import Dict, Any
from core.agents.state import AgentState
from core.domain.agronomy import calculate_irrigation_need


def dispatch_agent_node(state: AgentState) -> AgentState:
    """
    Eco-Dispatch Worker Node:
    Computes precision irrigation prescription, adjusts for rain avoidance,
    and applies self-correction adjustments if Critic rejected prior plan.
    """
    crop_info = state.get("crop_info", {})
    weather = state.get("weather_data", {})
    telemetry = state.get("sensor_telemetry", {})
    critic_verdict = state.get("critic_verdict", {})

    crop_type = crop_info.get("crop_type", "rice_jasmine_85")
    growth_stage = crop_info.get("growth_stage", "vegetative_tillering")
    field_capacity = float(crop_info.get("field_capacity", 45.0))
    wilting_point = float(crop_info.get("wilting_point", 15.0))

    current_moisture = float(telemetry.get("soil_moisture_pct", 22.0))
    et0 = float(weather.get("et0", 4.2))
    rain_mm = float(weather.get("forecast_rain_mm", 0.0))

    # Base calculation from FAO-56 domain model
    prescription = calculate_irrigation_need(
        crop_type=crop_type,
        growth_stage=growth_stage,
        current_soil_moisture=current_moisture,
        field_capacity=field_capacity,
        wilting_point=wilting_point,
        et0=et0,
        forecast_rain_mm=rain_mm
    )

    # Reflexion / Self-Correction Handling:
    # If Critic had rejected the previous plan, analyze feedback and enforce safe guardrails
    if critic_verdict and not critic_verdict.get("approved", True) and critic_verdict.get("feedback"):
        feedback = critic_verdict.get("feedback", "").lower()
        if "fao-56" in feedback or "violates" in feedback or "water dosage" in feedback:
            # Scale down excessive water to safe compliant quota
            prescription["water_needed_mm"] = min(25.0, prescription["water_needed_mm"])
            prescription["duration_minutes"] = 48 if "rice" in crop_type.lower() else 45
            prescription["urgency"] = "MEDIUM"
        if "duration_minutes" in feedback:
            prescription["duration_minutes"] = max(30, min(75, int(prescription.get("water_needed_mm", 20.0) * 1.5)))
        if "pump motor burnout" in feedback or "8 hours" in feedback:
            prescription["duration_minutes"] = min(120, prescription.get("duration_minutes", 60))

        # Reset carbon report and critique feedback so downstream nodes re-audit the revised plan
        state["carbon_report"] = {}
        if isinstance(state.get("critic_verdict"), dict):
            state["critic_verdict"]["feedback"] = ""

    # EVN Tariff Optimization
    current_hour = int(crop_info.get("current_hour", 14))
    is_peak = current_hour in [9, 10, 17, 18, 19]
    if is_peak and prescription["urgency"] != "HIGH" and prescription["duration_minutes"] > 0:
        tariff_mode = "DEFERRED"
        tariff_rate = 1700
        tariff_note = "Deferred to avoid peak tariff (3,100 VND/kWh) and protect farmer margins."
    else:
        tariff_mode = "IMMEDIATE"
        tariff_rate = 3100 if is_peak else (1100 if current_hour in [22, 23, 0, 1, 2, 3] else 1700)
        tariff_note = "Emergency irrigation authorized" if is_peak else "Optimal run window"

    prescription["tariff_mode"] = tariff_mode
    prescription["tariff_rate_vnd"] = tariff_rate
    prescription["tariff_note"] = tariff_note

    # Update state
    state["dispatch_plan"] = prescription
    state["current_step"] = state.get("current_step", 0) + 1

    thought_msg = (
        f"Calculated dispatch plan: {prescription['water_needed_mm']}mm water needed, "
        f"duration {prescription['duration_minutes']} mins (Urgency: {prescription['urgency']}). "
        f"Avoid reason: {prescription.get('avoid_reason')}. Tariff: {tariff_mode} ({tariff_rate} VND/kWh)."
    )
    state["thoughts"].append({
        "agent": "DispatchWorker",
        "step": "dispatch_planning",
        "thought": thought_msg
    })

    return state
