"""
AgriCarbon Agent Tools and External Connectors Package.
Provides automated tools:
1. get_weather_forecast: Open-Meteo REST API adapter + offline cache.
2. query_sensor_telemetry: IoT soil telemetry query + synthetic generator.
3. calculate_agricultural_emissions: Deterministic IPCC Tier 1/2 GHG engine.
4. record_esg_audit_entry: Cryptographic SHA-256 tamper-evident ledger entry.
"""

from core.tools.weather_tool import get_weather_forecast
from core.tools.telemetry_tool import query_sensor_telemetry
from core.tools.carbon_tool import calculate_agricultural_emissions
from core.tools.ledger_tool import record_esg_audit_entry
from core.tools.mock_data import get_mock_weather, get_mock_telemetry

TOOL_REGISTRY = {
    "get_weather_forecast": get_weather_forecast,
    "query_sensor_telemetry": query_sensor_telemetry,
    "calculate_agricultural_emissions": calculate_agricultural_emissions,
    "record_esg_audit_entry": record_esg_audit_entry,
}

__all__ = [
    "get_weather_forecast",
    "query_sensor_telemetry",
    "calculate_agricultural_emissions",
    "record_esg_audit_entry",
    "get_mock_weather",
    "get_mock_telemetry",
    "TOOL_REGISTRY",
]
