"""
Tier 3: Pairwise - Weather Rain Forecast & Irrigation Suppression Interaction
Tests cross-feature interactions between quantitative rainfall forecasts and pump dispatch suppression.
Authoritative source: PROJECT.md § Multi-Agent Engine (Sensing & Dispatch)
"""

import pytest
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import resolve_agronomy_module


class TestWeatherRainSuppressionInteraction:
    """Validates how quantitative rain forecasts dynamically suppress or modify irrigation."""

    def test_marginal_rain_partially_reduces_irrigation(self):
        """Marginal rain (4mm) reduces water deficit without completely canceling pump run."""
        agronomy = resolve_agronomy_module()
        
        plan_no_rain = agronomy.calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=22.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=0.0
        )
        
        plan_light_rain = agronomy.calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=22.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=4.0
        )
        
        assert plan_light_rain["water_needed_mm"] < plan_no_rain["water_needed_mm"]
        assert plan_light_rain["duration_minutes"] > 0, "Light rain should not cancel run when deficit remains"
        assert plan_light_rain["avoid_reason"] is None

    def test_heavy_rain_threshold_completely_suppresses_irrigation(self):
        """Forecast rain >= 15mm strictly cancels pumping to prevent waterlogging and energy waste."""
        agronomy = resolve_agronomy_module()
        
        plan = agronomy.calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=18.0,  # Dry soil
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=18.0  # Above 15mm threshold
        )
        
        assert plan["water_needed_mm"] == 0.0
        assert plan["duration_minutes"] == 0
        assert plan["avoid_reason"] == "forecast_rain"
        assert plan["urgency"] == "NONE"

    def test_rain_suppression_boundary_step(self):
        """Test boundary transition at 15.0mm rain threshold."""
        agronomy = resolve_agronomy_module()
        
        # Sub-threshold: 14.0mm
        sub = agronomy.calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry",
            current_soil_moisture=24.0,
            field_capacity=40.0,
            wilting_point=18.0,
            et0=4.0,
            forecast_rain_mm=14.0
        )
        assert sub["avoid_reason"] != "forecast_rain"
        
        # At threshold: 15.0mm
        at_thresh = agronomy.calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry",
            current_soil_moisture=24.0,
            field_capacity=40.0,
            wilting_point=18.0,
            et0=4.0,
            forecast_rain_mm=15.0
        )
        assert at_thresh["avoid_reason"] == "forecast_rain"
        assert at_thresh["duration_minutes"] == 0
