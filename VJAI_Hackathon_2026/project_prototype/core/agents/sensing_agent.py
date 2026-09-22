"""
Sensing & Weather Worker Agent.
Retrieves real-time weather forecasts and IoT soil telemetry via Tool Calling.
Computes reference evapotranspiration (ET0) using FAO-56 Penman-Monteith.
Conforms strictly to PROJECT.md § Multi-Agent Engine and ORIGINAL_REQUEST.md § R2.
"""

import os
from typing import Dict, Any
from core.agents.state import AgentState
from core.tools.weather_tool import get_weather_forecast
from core.tools.telemetry_tool import query_sensor_telemetry
from core.domain.agronomy import calculate_et0


def sensing_agent_node(state: AgentState) -> AgentState:
    """
    Sensing Worker Node:
    Calls get_weather_forecast and query_sensor_telemetry tools,
    computes FAO-56 ET0, and populates state.
    Supports offline cache toggle via state or environment variables.
    """
    crop_info = state.get("crop_info", {})
    scenario_id = state.get("scenario_id", "default_scenario")

    # Determine coordinates
    lat = float(crop_info.get("latitude", 10.3842 if "an_giang" in scenario_id else 11.9404))
    lon = float(crop_info.get("longitude", 105.0125 if "an_giang" in scenario_id else 108.4583))
    sensor_id = crop_info.get("sensor_id", "sensor_polder_04" if "an_giang" in scenario_id else "sensor_coffee_02")
    farm_id = crop_info.get("farm_id", scenario_id)

    # Determine offline cache / network fallback mode
    env_offline = os.getenv("AGRICARBON_OFFLINE", "0").lower() in ("1", "true", "yes")
    env_cache = os.getenv("AGRICARBON_USE_CACHE", "0").lower() in ("1", "true", "yes")
    use_cache = bool(
        crop_info.get("use_cache", False)
        or crop_info.get("offline_mode", False)
        or state.get("use_cache", False)
        or env_offline
        or env_cache
    )

    simulate_db_disconnect = bool(
        crop_info.get("simulate_db_disconnect", False)
        or os.getenv("AGRICARBON_SIMULATE_DB_DISCONNECT", "0").lower() in ("1", "true", "yes")
    )

    # 1. Tool Call: get_weather_forecast
    tool_call_weather = {
        "tool": "get_weather_forecast",
        "args": {"lat": lat, "lon": lon, "forecast_hours": 48, "use_cache": use_cache}
    }
    state["tool_calls"].append(tool_call_weather)

    weather_data = get_weather_forecast(lat=lat, lon=lon, use_cache=use_cache, forecast_hours=48)
    state["tool_calls"].append({
        "tool": "get_weather_forecast",
        "result": {
            "temp_max": weather_data["temp_max"],
            "temp_min": weather_data["temp_min"],
            "humidity": weather_data["humidity"],
            "forecast_rain_mm": weather_data["forecast_rain_mm"],
            "rain_probability": weather_data.get("rain_probability", 0),
            "source": weather_data.get("source", "open_meteo_api"),
            "fallback_engaged": weather_data.get("fallback_engaged", False)
        }
    })

    # 2. Tool Call: query_sensor_telemetry
    tool_call_telemetry = {
        "tool": "query_sensor_telemetry",
        "args": {"sensor_id": sensor_id, "farm_id": farm_id, "simulate_db_disconnect": simulate_db_disconnect}
    }
    state["tool_calls"].append(tool_call_telemetry)

    sensor_data = query_sensor_telemetry(
        sensor_id=sensor_id,
        farm_id=farm_id,
        simulate_db_disconnect=simulate_db_disconnect
    )
    state["tool_calls"].append({
        "tool": "query_sensor_telemetry",
        "result": {
            "soil_moisture_pct": sensor_data["soil_moisture_pct"],
            "soil_temperature_c": sensor_data["soil_temperature_c"],
            "pump_status": sensor_data["pump_status"],
            "source": sensor_data.get("source", "synthetic_generator"),
            "fallback_engaged": sensor_data.get("fallback_engaged", False)
        }
    })

    # 3. Compute reference evapotranspiration (ET0) via FAO-56 Penman-Monteith
    computed_et0 = calculate_et0(
        temp_max=weather_data["temp_max"],
        temp_min=weather_data["temp_min"],
        humidity=weather_data["humidity"],
        wind_speed=weather_data["wind_speed"],
        solar_rad=weather_data["solar_rad"]
    )
    weather_data["et0"] = computed_et0

    # 4. State updates & thought logging
    state["weather_data"] = weather_data
    state["sensor_telemetry"] = sensor_data
    state["current_step"] = state.get("current_step", 0) + 1

    source_label = weather_data.get("source", "open_meteo_api")
    thought_msg = (
        f"Observed ambient weather via {source_label} (Tmax={weather_data['temp_max']}°C, "
        f"Rain={weather_data['forecast_rain_mm']}mm, ET0={computed_et0}mm/day). "
        f"Soil moisture at {sensor_data['soil_moisture_pct']}%. "
        f"Telemetry gathered successfully."
    )
    state["thoughts"].append({
        "agent": "SensingWorker",
        "step": "sensing_telemetry",
        "thought": thought_msg
    })

    return state
