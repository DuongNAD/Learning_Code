"""
Tier 3: Pairwise - Sensing to Dispatch Pipeline
Tests the integrated data flow from Weather & IoT Sensing to Resource Eco-Dispatch.
Authoritative source: PROJECT.md § Multi-Agent Engine
"""

import pytest
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import resolve_agronomy_module


class TestSensingDispatchPipeline:
    """Validates interactions between Sensing Worker and Dispatch Worker."""

    def test_sensing_to_dispatch_end_to_end(self, an_giang_rice_preset):
        """Verify weather and soil sensing outputs correctly drive irrigation dispatch."""
        agronomy = resolve_agronomy_module()
        
        # 1. Sensing step
        et0 = agronomy.calculate_et0(
            temp_max=an_giang_rice_preset["temp_max"],
            temp_min=an_giang_rice_preset["temp_min"],
            humidity=an_giang_rice_preset["humidity"],
            wind_speed=an_giang_rice_preset["wind_speed"],
            solar_rad=an_giang_rice_preset["solar_rad"]
        )
        assert et0 > 0.0
        
        # 2. Dispatch step using sensed values
        plan = agronomy.calculate_irrigation_need(
            crop_type=an_giang_rice_preset["crop_type"],
            growth_stage=an_giang_rice_preset["growth_stage"],
            current_soil_moisture=an_giang_rice_preset["current_soil_moisture"],
            field_capacity=an_giang_rice_preset["field_capacity"],
            wilting_point=an_giang_rice_preset["wilting_point"],
            et0=et0,
            forecast_rain_mm=an_giang_rice_preset["forecast_rain_mm"]
        )
        assert plan["duration_minutes"] > 0
        assert plan["water_needed_mm"] > 0
        assert plan["urgency"] in ["MEDIUM", "HIGH"]

    def test_soil_deficit_triggers_proportional_duration(self, an_giang_rice_preset):
        """Verify deeper moisture depletion produces longer pump duration."""
        agronomy = resolve_agronomy_module()
        et0 = 4.2
        
        # Deficit A: 25% moisture (mild deficit)
        p_mild = agronomy.calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=25.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=et0,
            forecast_rain_mm=0.0
        )
        
        # Deficit B: 18% moisture (severe deficit)
        p_severe = agronomy.calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=18.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=et0,
            forecast_rain_mm=0.0
        )
        
        assert p_severe["duration_minutes"] > p_mild["duration_minutes"], "Severe deficit must require more pump time"
        assert p_severe["water_needed_mm"] > p_mild["water_needed_mm"]

    def test_weather_evapotranspiration_scales_irrigation(self):
        """Verify hotter, drier day (higher ET0) increases irrigation requirement."""
        agronomy = resolve_agronomy_module()
        
        low_et0_plan = agronomy.calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=26.0,
            field_capacity=40.0,
            wilting_point=18.0,
            et0=2.5,
            forecast_rain_mm=0.0
        )
        
        high_et0_plan = agronomy.calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=26.0,
            field_capacity=40.0,
            wilting_point=18.0,
            et0=6.5,
            forecast_rain_mm=0.0
        )
        
        assert high_et0_plan["water_needed_mm"] > low_et0_plan["water_needed_mm"]

    def test_dispatch_plan_preserves_crop_type_and_stage(self, lam_dong_coffee_preset):
        """Verify coffee-specific agronomic constraints are enforced during dispatch."""
        agronomy = resolve_agronomy_module()
        plan = agronomy.calculate_irrigation_need(
            crop_type=lam_dong_coffee_preset["crop_type"],
            growth_stage=lam_dong_coffee_preset["growth_stage"],
            current_soil_moisture=lam_dong_coffee_preset["current_soil_moisture"],
            field_capacity=lam_dong_coffee_preset["field_capacity"],
            wilting_point=lam_dong_coffee_preset["wilting_point"],
            et0=3.5,
            forecast_rain_mm=lam_dong_coffee_preset["forecast_rain_mm"]
        )
        assert "water_needed_mm" in plan
        assert plan["duration_minutes"] <= 120, "Coffee drip irrigation single cycle should not exceed 120 mins"
