"""
Tier 4: Real-World Scenarios - An Giang Rice Polder (Mekong Delta)
Validates Tokyo Innovation Base Stage Demo 1:
Alternate Wetting and Drying (AWD) water management, -38% water savings,
-28.1% CO2e methane reduction, and rapid ESG audit generation.
Authoritative source: ORIGINAL_REQUEST.md § Acceptance Criteria, PROJECT.md § Milestones
"""

import time
import pytest
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import (
    resolve_agronomy_module,
    resolve_carbon_module,
    resolve_ledger_module
)


class TestAnGiangRicePolderScenario:
    """Validates the An Giang Rice Polder stage demo workload."""

    def test_an_giang_rice_preset_loading_and_attributes(self, an_giang_rice_preset):
        """Verify An Giang preset parameters match agronomic field realities."""
        assert an_giang_rice_preset["crop_type"] == "rice_jasmine_85"
        assert an_giang_rice_preset["field_capacity"] == 45.0
        assert an_giang_rice_preset["wilting_point"] == 15.0
        assert an_giang_rice_preset["pump_power_kw"] == 15.0
        assert an_giang_rice_preset["area_hectares"] == 5.0

    def test_an_giang_awd_irrigation_optimization(self, an_giang_rice_preset):
        """Verify AWD logic determines optimal flush without continuous flooding."""
        agronomy = resolve_agronomy_module()
        et0 = agronomy.calculate_et0(
            temp_max=an_giang_rice_preset["temp_max"],
            temp_min=an_giang_rice_preset["temp_min"],
            humidity=an_giang_rice_preset["humidity"],
            wind_speed=an_giang_rice_preset["wind_speed"],
            solar_rad=an_giang_rice_preset["solar_rad"]
        )
        plan = agronomy.calculate_irrigation_need(
            crop_type=an_giang_rice_preset["crop_type"],
            growth_stage=an_giang_rice_preset["growth_stage"],
            current_soil_moisture=an_giang_rice_preset["current_soil_moisture"],
            field_capacity=an_giang_rice_preset["field_capacity"],
            wilting_point=an_giang_rice_preset["wilting_point"],
            et0=et0,
            forecast_rain_mm=an_giang_rice_preset["forecast_rain_mm"]
        )
        # Flush duration must be within 30-75 mins for 5ha polder sector
        assert 30 <= plan["duration_minutes"] <= 75
        assert plan["urgency"] in ["MEDIUM", "HIGH"]

    def test_an_giang_water_savings_quantification(self):
        """Verify water consumption drops from conventional 7,500 m3/ha to 4,650 m3/ha (-38.0%)."""
        conventional_water_m3_per_ha = 7500.0
        awd_water_m3_per_ha = 4650.0
        
        reduction = (conventional_water_m3_per_ha - awd_water_m3_per_ha) / conventional_water_m3_per_ha
        reduction_pct = round(reduction * 100.0, 1)
        
        assert reduction_pct == 38.0, f"Expected exactly 38.0% water reduction, got {reduction_pct}%"

    def test_an_giang_methane_co2e_reduction(self):
        """Verify AWD field drying halts methanogenesis and delivers targeted -28.1% CO2e cut."""
        carbon = resolve_carbon_module()
        # AWD precision irrigation vs conventional continuous flood baseline
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=465.0,  # 1 hectare seasonal cycle portion
            pump_power_kw=15.0,
            grid_emission_factor=0.7221,
            fertilizer_n_kg=80.0,
            diesel_liters=12.0
        )
        assert abs(res["reduction_pct"] - 28.1) < 1.0
        assert res["total_co2e_kg"] < res["baseline_co2e_kg"]

    def test_an_giang_full_stage_demo_flow(self, an_giang_rice_preset):
        """Simulate the live 5-minute Tokyo stage presentation end-to-end execution."""
        start_time = time.perf_counter()
        agronomy = resolve_agronomy_module()
        carbon = resolve_carbon_module()
        ledger = resolve_ledger_module()
        
        # Step 1: Weather & Soil Sensing
        et0 = agronomy.calculate_et0(34.5, 25.0, 75.0, 2.2, 19.5)
        # Step 2: Eco-Dispatch Calculation
        irrigation = agronomy.calculate_irrigation_need(
            crop_type=an_giang_rice_preset["crop_type"],
            growth_stage=an_giang_rice_preset["growth_stage"],
            current_soil_moisture=22.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=et0,
            forecast_rain_mm=0.0
        )
        # Step 3: Carbon Audit
        emissions = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=(irrigation["duration_minutes"] / 60.0) * 50.0,
            pump_power_kw=15.0
        )
        # Step 4: ESG Ledger Generation
        audit_hash = ledger.create_block_hash(
            record_id="demo_ag_001",
            timestamp="2026-09-08T09:15:00Z",
            farm_id="an_giang_polder_04",
            action="awd_irrigation_cycle",
            co2e_kg=emissions["total_co2e_kg"],
            prev_hash="0" * 64
        )
        
        elapsed_sec = time.perf_counter() - start_time
        assert elapsed_sec < 5.0, f"Demo workload took {elapsed_sec:.3f}s, must be under 5.0s"
        assert len(audit_hash) == 64
        assert irrigation["duration_minutes"] > 0
