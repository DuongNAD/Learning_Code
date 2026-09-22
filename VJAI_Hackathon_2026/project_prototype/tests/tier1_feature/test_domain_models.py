"""
Tier 1: Feature Coverage - Domain Models
Tests core domain mathematical models: FAO-56 Agronomy, IPCC GHG Emissions, and ESG Ledger.
Authoritative source: PROJECT.md § Interface Contracts, ORIGINAL_REQUEST.md § Acceptance
"""

import pytest
import sys
from pathlib import Path

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import (
    ReferenceAgronomyOracle,
    ReferenceCarbonOracle,
    ReferenceLedgerOracle,
    resolve_agronomy_module,
    resolve_carbon_module,
    resolve_ledger_module,
)


class TestDomainAgronomy:
    """Validates FAO-56 Penman-Monteith ET0 and Irrigation Need Calculations."""

    def test_fao56_penman_monteith_et0(self, an_giang_rice_preset):
        """Test FAO-56 ET0 calculation matches tropical Mekong Delta realistic bounds."""
        agronomy = resolve_agronomy_module()
        et0 = agronomy.calculate_et0(
            temp_max=an_giang_rice_preset["temp_max"],
            temp_min=an_giang_rice_preset["temp_min"],
            humidity=an_giang_rice_preset["humidity"],
            wind_speed=an_giang_rice_preset["wind_speed"],
            solar_rad=an_giang_rice_preset["solar_rad"]
        )
        assert isinstance(et0, (int, float)), "ET0 must be a numeric value"
        assert 2.5 <= et0 <= 7.0, f"Tropical ET0 {et0} out of realistic daily range (2.5-7.0 mm/day)"

    def test_irrigation_need_under_soil_deficit(self, an_giang_rice_preset):
        """Test irrigation need computation under soil moisture deficit."""
        agronomy = resolve_agronomy_module()
        et0 = agronomy.calculate_et0(34.0, 25.0, 75.0, 2.0, 19.0)
        res = agronomy.calculate_irrigation_need(
            crop_type=an_giang_rice_preset["crop_type"],
            growth_stage=an_giang_rice_preset["growth_stage"],
            current_soil_moisture=22.0,
            field_capacity=an_giang_rice_preset["field_capacity"],
            wilting_point=an_giang_rice_preset["wilting_point"],
            et0=et0,
            forecast_rain_mm=0.0
        )
        assert "water_needed_mm" in res
        assert "duration_minutes" in res
        assert "urgency" in res
        assert res["water_needed_mm"] > 0, "Deficit must trigger positive irrigation requirement"
        assert res["duration_minutes"] > 0, "Pump duration must be positive"
        assert res["urgency"] in ["HIGH", "MEDIUM", "LOW"]
        assert res["avoid_reason"] is None

    def test_irrigation_need_avoidance_on_forecast_rain(self, an_giang_rice_preset):
        """Test irrigation suppression when upcoming precipitation is forecast >= 15mm."""
        agronomy = resolve_agronomy_module()
        res = agronomy.calculate_irrigation_need(
            crop_type=an_giang_rice_preset["crop_type"],
            growth_stage=an_giang_rice_preset["growth_stage"],
            current_soil_moisture=20.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=25.0  # Heavy rain forecast
        )
        assert res["water_needed_mm"] == 0.0, "Rain forecast must suppress irrigation water requirement"
        assert res["duration_minutes"] == 0, "Pump duration must be 0 minutes during rain"
        assert res["avoid_reason"] == "forecast_rain"
        assert res["urgency"] == "NONE"

    def test_irrigation_need_avoidance_on_field_saturation(self):
        """Test irrigation suppression when soil is already at or above field capacity."""
        agronomy = resolve_agronomy_module()
        res = agronomy.calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=42.0,  # Above FC 40%
            field_capacity=40.0,
            wilting_point=18.0,
            et0=3.8,
            forecast_rain_mm=0.0
        )
        assert res["water_needed_mm"] == 0.0
        assert res["duration_minutes"] == 0
        assert res["avoid_reason"] == "sufficient_moisture"


class TestDomainCarbonAndLedger:
    """Validates IPCC Tier 1/2 GHG Calculation Models and SHA-256 ESG Ledger."""

    def test_ipcc_tier1_emissions_breakdown(self):
        """Test Scope 1 and Scope 2 emission computation and breakdown consistency."""
        carbon = resolve_carbon_module()
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=120.0,
            pump_power_kw=15.0,
            grid_emission_factor=0.7221,
            fertilizer_n_kg=30.0,
            diesel_liters=10.0
        )
        assert "total_co2e_kg" in res
        assert "breakdown" in res
        b = res["breakdown"]
        assert "electricity_co2e" in b
        assert "fertilizer_n2o_co2e" in b
        assert "fuel_co2e" in b

        # Breakdown sum verification within numerical precision
        calculated_sum = b["electricity_co2e"] + b["fertilizer_n2o_co2e"] + b["fuel_co2e"]
        assert abs(res["total_co2e_kg"] - calculated_sum) < 0.01

    def test_sustainable_quant_reduction_goals(self):
        """Verify baseline vs optimized emission reduction formula achieves targeted -28.1%."""
        carbon = resolve_carbon_module()
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=100.0,
            pump_power_kw=10.0,
            grid_emission_factor=0.7221,
            fertilizer_n_kg=20.0,
            diesel_liters=5.0
        )
        assert res["baseline_co2e_kg"] > res["total_co2e_kg"]
        assert abs(res["reduction_pct"] - 28.1) < 1.0, f"Expected reduction ~28.1%, got {res['reduction_pct']}%"

    def test_esg_ledger_sha256_cryptographic_integrity(self):
        """Verify SHA-256 cryptographic chain generation and tamper-evident detection."""
        ledger = resolve_ledger_module()
        chain = []
        
        # Block 1 (Genesis)
        prev_hash = "0" * 64
        h1 = ledger.create_block_hash("rec_001", "2026-09-08T06:00:00Z", "an_giang_01", "irrigation_pump", 14.25, prev_hash)
        chain.append({
            "record_id": "rec_001",
            "timestamp": "2026-09-08T06:00:00Z",
            "farm_id": "an_giang_01",
            "action": "irrigation_pump",
            "co2e_kg": 14.25,
            "prev_hash": prev_hash,
            "hash": h1
        })
        
        # Block 2
        h2 = ledger.create_block_hash("rec_002", "2026-09-08T07:00:00Z", "an_giang_01", "fertilizer_dispense", 22.80, h1)
        chain.append({
            "record_id": "rec_002",
            "timestamp": "2026-09-08T07:00:00Z",
            "farm_id": "an_giang_01",
            "action": "fertilizer_dispense",
            "co2e_kg": 22.80,
            "prev_hash": h1,
            "hash": h2
        })
        
        # Integrity check on untampered chain
        assert ledger.verify_ledger_integrity(chain) is True
        
        # Tamper simulation: mutate action or co2e in block 1
        tampered_chain = [dict(c) for c in chain]
        tampered_chain[0]["co2e_kg"] = 999.99
        assert ledger.verify_ledger_integrity(tampered_chain) is False, "Tampered chain must fail cryptographic validation"
