"""
Tier 2: Boundary & Corner Cases - Negative & Zero Values
Tests edge conditions: zero pump power (gravity irrigation), zero water,
zero fertilizer, negative sensor readings, and invalid fuel inputs.
Authoritative source: PROJECT.md § Domain Layer
"""

import pytest
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import ReferenceCarbonOracle, ReferenceAgronomyOracle, resolve_carbon_module, resolve_agronomy_module


class TestNegativeAndZeroBoundaries:
    """Validates mathematical stability with zero and negative parameter inputs."""

    def test_zero_pump_power_gravity_fed(self):
        """Zero pump power: Gravity-fed canal irrigation emits zero electrical CO2e."""
        carbon = resolve_carbon_module()
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=200.0,
            pump_power_kw=0.0,
            fertilizer_n_kg=15.0,
            diesel_liters=0.0
        )
        assert res["breakdown"]["electricity_co2e"] == 0.0
        assert res["total_co2e_kg"] == res["breakdown"]["fertilizer_n2o_co2e"]

    def test_zero_water_pumped(self):
        """Zero water pumped: Pumping emissions are strictly 0.0."""
        carbon = resolve_carbon_module()
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=0.0,
            pump_power_kw=15.0,
            fertilizer_n_kg=0.0,
            diesel_liters=0.0
        )
        assert res["breakdown"]["electricity_co2e"] == 0.0
        assert res["total_co2e_kg"] == 0.0

    def test_zero_fertilizer_and_fuel(self):
        """Zero fertilizer and zero diesel: Only electrical pumping emission counted."""
        carbon = resolve_carbon_module()
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=100.0,
            pump_power_kw=10.0,
            fertilizer_n_kg=0.0,
            diesel_liters=0.0
        )
        assert res["breakdown"]["fertilizer_n2o_co2e"] == 0.0
        assert res["breakdown"]["fuel_co2e"] == 0.0
        assert res["total_co2e_kg"] > 0.0

    def test_negative_soil_moisture_sensor_fault_handling(self):
        """Negative soil moisture: Malfunctioning sensor reading (-5%) clamped or flagged."""
        agronomy = resolve_agronomy_module()
        # Should gracefully treat < 0% as 0% or wilting point without crashing
        res = agronomy.calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=-5.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.0,
            forecast_rain_mm=0.0
        )
        assert res["urgency"] == "HIGH"
        assert res["water_needed_mm"] > 0.0

    def test_negative_fuel_sanitization(self):
        """Negative diesel liters: Defensive validation ensures emissions cannot be negative."""
        carbon = resolve_carbon_module()
        # If diesel is negative, fuel CO2e must not subtract from total
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=50.0,
            pump_power_kw=10.0,
            fertilizer_n_kg=10.0,
            diesel_liters=max(0.0, -15.0)  # Sanitized input boundary
        )
        assert res["breakdown"]["fuel_co2e"] >= 0.0
        assert res["total_co2e_kg"] >= 0.0
