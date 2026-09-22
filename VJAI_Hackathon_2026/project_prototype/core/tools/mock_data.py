"""
Offline mock data for AgriCarbon Agent tools.
Ensures 100% resilient execution during TiB Tokyo stage presentations
even under network disconnects or API outages.
"""

import hashlib
from typing import Dict, Any

MOCK_WEATHER_PRESETS: Dict[str, Dict[str, Any]] = {
    "an_giang": {
        "latitude": 10.3842,
        "longitude": 105.0125,
        "temp_max": 33.5,
        "temp_min": 24.8,
        "humidity": 78.0,
        "wind_speed": 2.1,
        "solar_rad": 18.2,
        "rain_probability": 10,
        "forecast_rain_mm": 0.0,
        "condition": "Partly Cloudy",
        "source": "offline_cache",
        "status": "success"
    },
    "an_giang_storm": {
        "latitude": 10.3842,
        "longitude": 105.0125,
        "temp_max": 28.5,
        "temp_min": 23.0,
        "humidity": 92.0,
        "wind_speed": 7.5,
        "solar_rad": 8.5,
        "rain_probability": 88,
        "forecast_rain_mm": 35.0,
        "condition": "Tropical Convective Storm",
        "source": "offline_cache",
        "status": "success"
    },
    "lam_dong": {
        "latitude": 11.9404,
        "longitude": 108.4583,
        "temp_max": 24.5,
        "temp_min": 14.5,
        "humidity": 65.0,
        "wind_speed": 1.8,
        "solar_rad": 17.5,
        "rain_probability": 15,
        "forecast_rain_mm": 2.0,
        "condition": "Mild Highland Sun",
        "source": "offline_cache",
        "status": "success"
    },
    "default": {
        "latitude": 10.5,
        "longitude": 105.5,
        "temp_max": 32.0,
        "temp_min": 24.0,
        "humidity": 75.0,
        "wind_speed": 2.2,
        "solar_rad": 18.0,
        "rain_probability": 10,
        "forecast_rain_mm": 0.0,
        "condition": "Typical Agro-Climate",
        "source": "offline_cache",
        "status": "success"
    }
}

MOCK_SENSOR_PRESETS: Dict[str, Dict[str, Any]] = {
    "an_giang_rice_001": {
        "sensor_id": "sensor_polder_04",
        "farm_id": "an_giang_rice_001",
        "soil_moisture_pct": 21.5,
        "soil_temperature_c": 28.2,
        "nitrogen_ppm": 45.0,
        "phosphorus_ppm": 18.0,
        "potassium_ppm": 120.0,
        "pump_status": "OFF",
        "battery_pct": 94,
        "timestamp": "2026-09-08T06:30:00Z",
        "depth_cm": 20,
        "status": "success"
    },
    "sensor_polder_04": {
        "sensor_id": "sensor_polder_04",
        "farm_id": "an_giang_rice_001",
        "soil_moisture_pct": 21.5,
        "soil_temperature_c": 28.2,
        "nitrogen_ppm": 45.0,
        "phosphorus_ppm": 18.0,
        "potassium_ppm": 120.0,
        "pump_status": "OFF",
        "battery_pct": 94,
        "timestamp": "2026-09-08T06:30:00Z",
        "depth_cm": 20,
        "status": "success"
    },
    "lam_dong_coffee_002": {
        "sensor_id": "sensor_coffee_02",
        "farm_id": "lam_dong_coffee_002",
        "soil_moisture_pct": 26.0,
        "soil_temperature_c": 22.4,
        "nitrogen_ppm": 55.0,
        "phosphorus_ppm": 25.0,
        "potassium_ppm": 140.0,
        "pump_status": "OFF",
        "battery_pct": 92,
        "timestamp": "2026-09-08T06:30:00Z",
        "depth_cm": 30,
        "status": "success"
    }
}


def get_mock_weather(lat: float, lon: float) -> Dict[str, Any]:
    """Resolves the closest mock weather profile or produces a synthetic deterministic reading."""
    if 10.0 <= lat <= 11.0 and 104.5 <= lon <= 106.0:
        base = dict(MOCK_WEATHER_PRESETS["an_giang"])
    elif 11.2 <= lat <= 12.5 and 107.5 <= lon <= 109.0:
        base = dict(MOCK_WEATHER_PRESETS["lam_dong"])
    else:
        base = dict(MOCK_WEATHER_PRESETS["default"])
    base["latitude"] = round(lat, 4)
    base["longitude"] = round(lon, 4)
    return base


def get_mock_telemetry(sensor_id: str, farm_id: str, depth_cm: int = 20) -> Dict[str, Any]:
    """Returns cached sensor reading or generates reproducible synthetic telemetry."""
    if farm_id in MOCK_SENSOR_PRESETS:
        res = dict(MOCK_SENSOR_PRESETS[farm_id])
        res["sensor_id"] = sensor_id
        res["depth_cm"] = depth_cm
        return res
    if sensor_id in MOCK_SENSOR_PRESETS:
        res = dict(MOCK_SENSOR_PRESETS[sensor_id])
        res["farm_id"] = farm_id
        res["depth_cm"] = depth_cm
        return res

    seed_str = f"{sensor_id}:{farm_id}"
    hash_val = int(hashlib.md5(seed_str.encode("utf-8")).hexdigest()[:8], 16)
    pseudo_moisture = round(18.0 + (hash_val % 220) / 10.0, 1)
    pseudo_temp = round(22.0 + ((hash_val >> 4) % 100) / 10.0, 1)
    pseudo_npk_n = round(30.0 + ((hash_val >> 8) % 300) / 10.0, 1)
    pseudo_npk_p = round(15.0 + ((hash_val >> 12) % 150) / 10.0, 1)
    pseudo_npk_k = round(90.0 + ((hash_val >> 16) % 600) / 10.0, 1)
    pseudo_bat = 85 + (hash_val % 15)

    return {
        "sensor_id": sensor_id,
        "farm_id": farm_id,
        "soil_moisture_pct": pseudo_moisture,
        "soil_temperature_c": pseudo_temp,
        "nitrogen_ppm": pseudo_npk_n,
        "phosphorus_ppm": pseudo_npk_p,
        "potassium_ppm": pseudo_npk_k,
        "pump_status": "OFF",
        "battery_pct": pseudo_bat,
        "timestamp": "2026-09-08T06:30:00Z",
        "depth_cm": depth_cm,
        "status": "success"
    }
