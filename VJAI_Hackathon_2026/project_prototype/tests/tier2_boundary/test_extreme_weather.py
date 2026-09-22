"""
Tier 2: Boundary & Corner Cases - Extreme Weather
Tests domain models under catastrophic weather conditions:
Drought, typhoon deluge, freezing frost, cyclonic winds, and zero solar radiation.
Authoritative source: PROJECT.md § Interface Contracts
"""

import pytest
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import ReferenceAgronomyOracle, resolve_agronomy_module


class TestExtremeWeatherBoundaries:
    """Validates FAO-56 and irrigation models against severe climatic extremes."""

    def test_extreme_drought_high_evapotranspiration(self):
        """Drought boundary: Temp 46°C, 15% humidity, high radiation."""
        agronomy = resolve_agronomy_module()
        et0 = agronomy.calculate_et0(
            temp_max=46.0,
            temp_min=32.0,
            humidity=15.0,
            wind_speed=5.5,
            solar_rad=29.0
        )
        assert et0 > 6.0, f"Drought ET0 should be high, got {et0} mm/day"
        assert et0 < 25.0, f"ET0 {et0} exceeded physical upper bound"

    def test_typhoon_deluge_irrigation_complete_suppression(self):
        """Typhoon boundary: 220mm forecast precipitation suppresses all pumping."""
        agronomy = resolve_agronomy_module()
        res = agronomy.calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative_tillering",
            current_soil_moisture=12.0,  # Severely dry, but typhoon is coming!
            field_capacity=45.0,
            wilting_point=15.0,
            et0=2.0,
            forecast_rain_mm=220.0
        )
        assert res["water_needed_mm"] == 0.0
        assert res["duration_minutes"] == 0
        assert res["avoid_reason"] == "forecast_rain"
        assert res["urgency"] == "NONE"

    def test_freezing_temperatures_handling(self):
        """Subzero boundary: Freezing temperatures (-5°C) do not break calculation."""
        agronomy = resolve_agronomy_module()
        et0 = agronomy.calculate_et0(
            temp_max=0.0,
            temp_min=-8.0,
            humidity=55.0,
            wind_speed=3.0,
            solar_rad=6.0
        )
        assert et0 >= 0.1, "Subzero ET0 must be non-negative and clamped to safe minimal baseline"

    def test_zero_solar_radiation_dark_overcast(self):
        """Zero solar boundary: Complete overcast / night condition."""
        agronomy = resolve_agronomy_module()
        et0 = agronomy.calculate_et0(
            temp_max=22.0,
            temp_min=20.0,
            humidity=95.0,
            wind_speed=1.0,
            solar_rad=0.0
        )
        assert et0 >= 0.1
        assert et0 < 2.0, "Zero solar radiation should yield minimal ET0"

    def test_cyclonic_wind_speeds(self):
        """Cyclonic wind boundary: Wind speed 35 m/s (Category 1 typhoon)."""
        agronomy = resolve_agronomy_module()
        et0 = agronomy.calculate_et0(
            temp_max=28.0,
            temp_min=24.0,
            humidity=90.0,
            wind_speed=35.0,
            solar_rad=10.0
        )
        assert isinstance(et0, (int, float))
        assert not (et0 != et0), "ET0 must not be NaN"
