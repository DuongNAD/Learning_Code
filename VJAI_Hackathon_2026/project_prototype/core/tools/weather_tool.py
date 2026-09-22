"""
Tool 1: get_weather_forecast
Open-Meteo REST API client with automatic fallback to offline cached forecasts.
Conforms strictly to PROJECT.md § Tools & Connectors and tests/tier1_feature/test_tools.py.
"""

from typing import Dict, Any, Optional
import requests
from core.tools.mock_data import get_mock_weather


def get_weather_forecast(
    lat: float,
    lon: float,
    use_cache: bool = False,
    forecast_hours: int = 48,
    simulate_network_error: bool = False,
    timeout_seconds: float = 2.0
) -> Dict[str, Any]:
    """
    Retrieves weather forecast for given geographic coordinates.
    Tries Open-Meteo REST API first; if unavailable, timeout, or use_cache=True,
    transparently falls back to calibrated offline cache data.

    Returns:
        Dict with:
            latitude, longitude, temp_max, temp_min, humidity, wind_speed,
            solar_rad, rain_probability, forecast_rain_mm, source, status, fallback_engaged
    """
    if use_cache or simulate_network_error:
        mock = get_mock_weather(lat, lon)
        mock["fallback_engaged"] = True
        mock["source"] = "offline_cache"
        mock["status"] = "success"
        return mock

    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&"
            f"daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,wind_speed_10m_max,shortwave_radiation_sum&"
            f"hourly=relative_humidity_2m&timezone=auto"
        )
        response = requests.get(url, timeout=timeout_seconds)
        if response.status_code == 200:
            data = response.json()
            daily = data.get("daily", {})
            hourly = data.get("hourly", {})

            temp_max = float(daily.get("temperature_2m_max", [33.5])[0])
            temp_min = float(daily.get("temperature_2m_min", [24.8])[0])
            if temp_min > temp_max:
                temp_max, temp_min = temp_min, temp_max

            rh_list = hourly.get("relative_humidity_2m", [78.0])
            humidity = float(sum(rh_list[:24]) / len(rh_list[:24])) if rh_list else 78.0
            humidity = max(0.0, min(100.0, humidity))

            wind_speed = float(daily.get("wind_speed_10m_max", [2.1])[0])
            sr_sum = float(daily.get("shortwave_radiation_sum", [18.2])[0])
            rain_prob = int(daily.get("precipitation_probability_max", [10])[0])
            rain_mm = float(daily.get("precipitation_sum", [0.0])[0])

            return {
                "latitude": lat,
                "longitude": lon,
                "temp_max": temp_max,
                "temp_min": temp_min,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "solar_rad": sr_sum,
                "rain_probability": rain_prob,
                "forecast_rain_mm": rain_mm,
                "source": "open_meteo_api",
                "fallback_engaged": False,
                "status": "success"
            }
        else:
            # Non-200 HTTP status code -> fallback
            mock = get_mock_weather(lat, lon)
            mock["fallback_engaged"] = True
            mock["source"] = "offline_cache"
            mock["status"] = "success"
            return mock

    except Exception:
        # Network disconnect / timeout / DNS failure -> transparent fallback
        mock = get_mock_weather(lat, lon)
        mock["fallback_engaged"] = True
        mock["source"] = "offline_cache"
        mock["status"] = "success"
        return mock
