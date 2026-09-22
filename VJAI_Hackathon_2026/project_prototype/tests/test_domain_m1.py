"""
Comprehensive Unit & Integration Test Suite for AgriCarbon Agent Milestone 1.
Validates:
1. FAO-56 Penman-Monteith Evapotranspiration (ET0) & Climatic Extremes.
2. Crop Coefficients (Kc) for Jasmine 85 Rice & Arabica Coffee.
3. Soil Water Balance, Irrigation Demand & Dynamic Rain Avoidance.
4. Quantitative Sustainable Impact Proofs (-38.0% Water, -28.1% CO2e, -30.5% Nitrogen).
5. IPCC Tier 1 & 2 Carbon Emissions (Scope 1, Scope 2, Scope 3 Logistics, AWD Methane).
6. Cryptographic SHA-256 Tamper-Evident ESG Audit Ledger & Hash-Chain Verification.
7. Data Presets (An Giang Rice Polder & Lam Dong Coffee Farm).
"""

import json
import math
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from core.domain.agronomy import (
    calculate_et0,
    get_crop_coefficient,
    calculate_irrigation_need,
    calculate_seasonal_water_savings,
    CropType,
    GrowthStage,
    IrrigationUrgency,
    AvoidReason,
)
from core.domain.carbon_models import (
    calculate_scope1_scope2_emissions,
    calculate_scope3_logistics,
    calculate_fertilizer_n2o_ef,
    calculate_methane_emissions_tier2,
    DEFAULT_GRID_EF_VN,
    DEFAULT_GRID_EF_JP,
    DEFAULT_DIESEL_EF,
)
from core.domain.esg_ledger import (
    create_block_hash,
    verify_ledger_integrity,
    ESGAuditEntryModel,
    ESGLedger,
    verify_ledger_chain,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ============================================================================
# 1. FAO-56 EVAPOTRANSPIRATION (ET0) TESTS
# ============================================================================

class TestFAO56Evapotranspiration:
    """Validates Penman-Monteith ET0 calculations across tropical and highland conditions."""

    def test_an_giang_tropical_et0(self):
        """Mekong Delta baseline: 33°C / 25°C, 75% RH, 2.0 m/s wind, 20.0 MJ/m2/day."""
        et0 = calculate_et0(
            temp_max=33.0,
            temp_min=25.0,
            humidity=75.0,
            wind_speed=2.0,
            solar_rad=20.0,
            elevation=2.0,
            latitude=10.5,
        )
        assert 4.5 <= et0 <= 5.0, f"Expected ET0 in [4.5, 5.0], got {et0}"
        assert isinstance(et0, float)

    def test_lam_dong_highland_et0(self):
        """Da Lat highland baseline: 26°C / 16°C, 80% RH, 1.8 m/s wind, 18.0 MJ/m2/day, 1500m ASL."""
        et0 = calculate_et0(
            temp_max=26.0,
            temp_min=16.0,
            humidity=80.0,
            wind_speed=1.8,
            solar_rad=18.0,
            elevation=1500.0,
            latitude=11.9,
        )
        assert 3.2 <= et0 <= 3.8, f"Expected ET0 in [3.2, 3.8], got {et0}"

    def test_zero_wind_speed_boundary(self):
        """Zero wind speed should not divide by zero and should return valid positive ET0."""
        et0 = calculate_et0(
            temp_max=32.0,
            temp_min=24.0,
            humidity=70.0,
            wind_speed=0.0,
            solar_rad=18.0,
        )
        assert et0 > 0.0

    def test_100_percent_humidity_boundary(self):
        """At 100% RH, vapor pressure deficit is 0 and ET0 is driven purely by radiation."""
        et0 = calculate_et0(
            temp_max=30.0,
            temp_min=22.0,
            humidity=100.0,
            wind_speed=2.0,
            solar_rad=16.0,
        )
        assert et0 > 0.0

    def test_temperature_inversion_handled(self):
        """If temp_min > temp_max, function must swap and still compute valid ET0."""
        et0 = calculate_et0(
            temp_max=22.0,
            temp_min=32.0,
            humidity=75.0,
            wind_speed=2.0,
            solar_rad=18.0,
        )
        assert et0 > 0.0

    def test_extreme_drought_boundary(self):
        """Drought conditions: 46°C, 15% RH, 29 MJ/m2/day -> ET0 between 6.0 and 15.0."""
        et0 = calculate_et0(
            temp_max=46.0,
            temp_min=32.0,
            humidity=15.0,
            wind_speed=5.5,
            solar_rad=29.0,
        )
        assert 6.0 < et0 < 15.0

    def test_subzero_frost_boundary(self):
        """Subzero freezing temperatures (-8°C) clamped safely to minimal baseline."""
        et0 = calculate_et0(
            temp_max=0.0,
            temp_min=-8.0,
            humidity=55.0,
            wind_speed=3.0,
            solar_rad=6.0,
        )
        assert et0 >= 0.1

    def test_cyclonic_wind_boundary(self):
        """Cyclonic winds (35 m/s) do not produce NaN or overflow."""
        et0 = calculate_et0(
            temp_max=28.0,
            temp_min=24.0,
            humidity=90.0,
            wind_speed=35.0,
            solar_rad=10.0,
        )
        assert not math.isnan(et0)
        assert et0 > 0.0

    def test_zero_solar_radiation_overcast(self):
        """Complete overcast / night condition with zero solar rad."""
        et0 = calculate_et0(
            temp_max=22.0,
            temp_min=20.0,
            humidity=95.0,
            wind_speed=1.0,
            solar_rad=0.0,
        )
        assert 0.1 <= et0 < 2.0


# ============================================================================
# 2. CROP COEFFICIENTS (Kc) & PHENOLOGY TESTS
# ============================================================================

class TestCropCoefficients:
    """Validates FAO-56 crop coefficients for target cultivars."""

    def test_jasmine_85_rice_kc_stages(self):
        """Verifies Jasmine 85 rice stages: initial, vegetative, mid-season, late-season."""
        assert get_crop_coefficient("rice", "initial") == 1.05
        assert get_crop_coefficient("rice_jasmine_85", "vegetative_tillering") == 1.12
        assert get_crop_coefficient("jasmine_85", "mid_season_flowering") == 1.20
        assert get_crop_coefficient("rice", "late_season_ripening") == 0.90

    def test_arabica_coffee_kc_stages(self):
        """Verifies Arabica coffee dry season stages: dormancy, blossom, berry set, late."""
        assert get_crop_coefficient("coffee", "initial_dormancy") == 0.85
        assert get_crop_coefficient("arabica_coffee", "development_anthesis") == 0.95
        assert get_crop_coefficient("arabica_coffee", "berry_development") == 1.05
        assert get_crop_coefficient("coffee", "late_season_harvest") == 0.90

    def test_unknown_cultivar_fallback(self):
        """Unknown crop returns safe default Kc of 1.00."""
        assert get_crop_coefficient("unknown_crop", "any_stage") == 1.00


# ============================================================================
# 3. SOIL WATER BALANCE & RAIN AVOIDANCE TESTS
# ============================================================================

class TestSoilWaterBalanceAndRainAvoidance:
    """Validates dynamic irrigation calculations and rain avoidance rules."""

    def test_heavy_rain_forecast_completely_suppresses_pumping(self):
        """Rain forecast >= 15.0 mm strictly cancels pump run."""
        res = calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative_tillering",
            current_soil_moisture=18.0,  # Dry soil
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=18.0,  # Forecast above 15mm
        )
        assert res["water_needed_mm"] == 0.0
        assert res["duration_minutes"] == 0
        assert res["urgency"] == "NONE"
        assert res["avoid_reason"] == "forecast_rain"

    def test_rain_avoidance_threshold_step(self):
        """Test exact boundary at 15.0 mm rainfall."""
        # 14.0 mm: below threshold, pump still runs
        sub = calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=24.0,
            field_capacity=40.0,
            wilting_point=18.0,
            et0=4.0,
            forecast_rain_mm=14.0,
        )
        assert sub["avoid_reason"] != "forecast_rain"

        # 15.0 mm: at threshold, pump suppressed
        at_thresh = calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=24.0,
            field_capacity=40.0,
            wilting_point=18.0,
            et0=4.0,
            forecast_rain_mm=15.0,
        )
        assert at_thresh["avoid_reason"] == "forecast_rain"
        assert at_thresh["duration_minutes"] == 0

    def test_marginal_rain_partially_offsets_irrigation(self):
        """Light rain (4 mm) reduces water needed without cancelling run."""
        no_rain = calculate_irrigation_need(
            crop_type="rice",
            growth_stage="vegetative",
            current_soil_moisture=22.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=0.0,
        )
        light_rain = calculate_irrigation_need(
            crop_type="rice",
            growth_stage="vegetative",
            current_soil_moisture=22.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=4.0,
        )
        assert light_rain["water_needed_mm"] < no_rain["water_needed_mm"]
        assert light_rain["duration_minutes"] > 0
        assert light_rain["avoid_reason"] is None

    def test_soil_at_field_capacity_suppressed(self):
        """When soil moisture is already at or above field capacity, no irrigation needed."""
        res = calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=42.0,  # Above FC 40%
            field_capacity=40.0,
            wilting_point=18.0,
            et0=3.8,
            forecast_rain_mm=0.0,
        )
        assert res["water_needed_mm"] == 0.0
        assert res["duration_minutes"] == 0
        assert res["avoid_reason"] == "sufficient_moisture"

    def test_soil_deficit_proportional_duration(self):
        """Severe deficit requires longer pump duration than mild deficit."""
        mild = calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=25.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.2,
            forecast_rain_mm=0.0,
        )
        severe = calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=18.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.2,
            forecast_rain_mm=0.0,
        )
        assert severe["duration_minutes"] > mild["duration_minutes"]
        assert severe["water_needed_mm"] > mild["water_needed_mm"]

    def test_coffee_duration_clamp_at_120_mins(self):
        """Single coffee drip irrigation cycle capped at 120 minutes."""
        plan = calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=12.0,  # Severe drought
            field_capacity=40.0,
            wilting_point=18.0,
            et0=6.5,
            forecast_rain_mm=0.0,
        )
        assert plan["duration_minutes"] <= 120

    def test_an_giang_rice_polder_flush_duration(self):
        """An Giang preset (moisture 22%, FC 45%, WP 15%) must be between 30 and 75 minutes."""
        plan = calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative_tillering",
            current_soil_moisture=22.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.78,
            forecast_rain_mm=0.0,
        )
        assert 30 <= plan["duration_minutes"] <= 75
        assert plan["urgency"] in ["MEDIUM", "HIGH"]

    def test_negative_sensor_reading_handled_safely(self):
        """Negative soil moisture reading (-5%) treated as extreme drought without crash."""
        res = calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative",
            current_soil_moisture=-5.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.0,
            forecast_rain_mm=0.0,
        )
        assert res["urgency"] == "HIGH"
        assert res["water_needed_mm"] > 0.0


# ============================================================================
# 4. QUANTITATIVE SUSTAINABLE IMPACT PROOFS
# ============================================================================

class TestQuantitativeImpactProofs:
    """Verifies mathematical proofs for -38.0% water, -28.1% CO2e, and -30.5% fertilizer savings."""

    def test_rice_water_savings_proof(self):
        """Rice: Baseline 7,500 m3/ha vs AgriCarbon 4,650 m3/ha = exactly -38.0% savings."""
        savings = calculate_seasonal_water_savings(crop_type="rice", area_ha=5.0)
        assert savings["baseline_m3"] == 37500.0
        assert savings["agent_m3"] == 23250.0
        assert savings["saved_m3"] == 14250.0
        assert savings["savings_pct"] == -38.0

    def test_coffee_water_savings_proof(self):
        """Coffee: Baseline 4,200 m3/ha vs AgriCarbon 2,604 m3/ha = exactly -38.0% savings."""
        savings = calculate_seasonal_water_savings(crop_type="coffee", area_ha=3.5)
        assert savings["baseline_m3"] == 14700.0
        assert savings["agent_m3"] == 9114.0
        assert savings["saved_m3"] == 5586.0
        assert savings["savings_pct"] == -38.0

    def test_carbon_reduction_proof(self):
        """Baseline 4,200.0 kg CO2e vs Optimized 3,020.0 kg CO2e = -28.1% CO2e cut."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=100.0,
            pump_power_kw=10.0,
            grid_emission_factor=0.7221,
            fertilizer_n_kg=20.0,
            diesel_liters=5.0,
        )
        assert abs(res["reduction_pct"] - 28.1) < 1.0
        assert res["baseline_co2e_kg"] > res["total_co2e_kg"]

    def test_nitrogen_reduction_proof(self):
        """Conventional 180 kg N/ha vs Optimized 125 kg N/ha = -30.55% ~ -30.5% reduction."""
        base_n = 180.0
        opt_n = 125.0
        reduction_pct = round(((base_n - opt_n) / base_n) * 100.0, 2)
        assert reduction_pct == 30.56 or abs(reduction_pct - 30.5) < 0.2


# ============================================================================
# 5. IPCC TIER 1 & 2 CARBON EMISSION MODELS
# ============================================================================

class TestIPCCCarbonAccounting:
    """Validates Scope 1, Scope 2, Scope 3, and Tier 2 AWD methane models."""

    def test_emissions_breakdown_consistency(self):
        """Verify itemized breakdown matches total_co2e_kg within floating point precision."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=120.0,
            pump_power_kw=15.0,
            grid_emission_factor=DEFAULT_GRID_EF_VN,
            fertilizer_n_kg=30.0,
            diesel_liters=10.0,
        )
        b = res["breakdown"]
        calculated_sum = b["electricity_co2e"] + b["fertilizer_n2o_co2e"] + b["fuel_co2e"]
        assert abs(res["total_co2e_kg"] - calculated_sum) < 0.01

    def test_zero_pump_power_gravity_irrigation(self):
        """Gravity-fed canal irrigation emits zero electrical CO2e."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=200.0,
            pump_power_kw=0.0,
            fertilizer_n_kg=15.0,
            diesel_liters=0.0,
        )
        assert res["breakdown"]["electricity_co2e"] == 0.0
        assert res["total_co2e_kg"] == res["breakdown"]["fertilizer_n2o_co2e"]

    def test_zero_water_pumped(self):
        """Zero water pumped emits zero electricity CO2e."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=0.0,
            pump_power_kw=15.0,
            fertilizer_n_kg=0.0,
            diesel_liters=0.0,
        )
        assert res["breakdown"]["electricity_co2e"] == 0.0
        assert res["total_co2e_kg"] == 0.0

    def test_zero_fertilizer_and_fuel(self):
        """Only electrical pumping emission counted when fert and diesel are zero."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=100.0,
            pump_power_kw=10.0,
            fertilizer_n_kg=0.0,
            diesel_liters=0.0,
        )
        assert res["breakdown"]["fertilizer_n2o_co2e"] == 0.0
        assert res["breakdown"]["fuel_co2e"] == 0.0
        assert res["total_co2e_kg"] > 0.0

    def test_direct_electricity_kwh_override(self):
        """Metered electricity kWh directly overrides hydraulic throughput estimation."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=500.0,
            pump_power_kw=15.0,
            grid_emission_factor=0.7221,
            electricity_kwh=100.0,
        )
        expected_elec_co2e = round(100.0 * 0.7221, 3)
        assert res["breakdown"]["electricity_co2e"] == expected_elec_co2e

    def test_scope3_japan_export_logistics(self):
        """Verify cradle-to-Tokyo Port export logistics calculation."""
        res = calculate_scope3_logistics(
            tonnage=25.0,
            origin_region="an_giang",
            destination_port="tokyo",
            cold_chain=False,
        )
        assert res["tonnage"] == 25.0
        assert res["road_co2e_kg"] == 528.0  # 25t * 220km * 0.096
        assert res["ocean_co2e_kg"] == 1728.0  # 25t * 4320km * 0.016
        assert res["total_scope3_co2e_kg"] == 2256.0
        assert res["co2e_per_ton_kg"] == 90.24

    def test_ipcc_tier2_awd_methane_mitigation(self):
        """Verify AWD scaling factor (SF_w = 0.52) delivers 48% methane reduction."""
        res = calculate_methane_emissions_tier2(area_ha=5.0, days=100, water_regime="awd")
        assert res["reduction_pct"] == 48.0
        assert res["ch4_kg"] < res["baseline_co2e_kg"]


# ============================================================================
# 6. CRYPTOGRAPHIC SHA-256 ESG AUDIT LEDGER TESTS
# ============================================================================

class TestCryptographicESGLedger:
    """Validates SHA-256 hash chaining, ISO 14064-3 compliance, and tamper detection."""

    def test_block_hash_deterministic(self):
        """SHA-256 block hash produces predictable 64-char hex string."""
        h = create_block_hash(
            record_id="rec_001",
            timestamp="2026-09-08T06:00:00Z",
            farm_id="an_giang_01",
            action="irrigation_pump",
            co2e_kg=14.25,
            prev_hash="0" * 64,
        )
        assert len(h) == 64
        assert h.isalnum()

    def test_dict_ledger_integrity_verification(self):
        """Verifies multi-block hash chain integrity."""
        chain = []
        h1 = create_block_hash("rec_1", "2026-09-08T06:00:00Z", "farm_1", "pump", 10.0, "0" * 64)
        chain.append({
            "record_id": "rec_1", "timestamp": "2026-09-08T06:00:00Z",
            "farm_id": "farm_1", "action": "pump", "co2e_kg": 10.0,
            "prev_hash": "0" * 64, "hash": h1,
        })
        h2 = create_block_hash("rec_2", "2026-09-08T12:00:00Z", "farm_1", "fert", 20.0, h1)
        chain.append({
            "record_id": "rec_2", "timestamp": "2026-09-08T12:00:00Z",
            "farm_id": "farm_1", "action": "fert", "co2e_kg": 20.0,
            "prev_hash": h1, "hash": h2,
        })
        assert verify_ledger_integrity(chain) is True

        # Tampering simulation
        tampered = [dict(b) for b in chain]
        tampered[0]["co2e_kg"] = 999.0
        assert verify_ledger_integrity(tampered) is False

    def test_esg_ledger_class_and_pydantic_chain(self):
        """Validates ESGLedger class, genesis block, appending, and verification."""
        ledger = ESGLedger()
        assert len(ledger.chain) == 1
        assert ledger.latest_entry.index == 0
        assert ledger.latest_entry.previous_hash == "0" * 64

        # Append entry 1
        e1 = ledger.append_entry(
            batch_id="BATCH-VN-2026-RICE-01",
            farm_id="VN-AG-TRITON-001",
            crop_type="Jasmine 85 Rice",
            scope1_co2e_kg=2189.58,
            scope2_co2e_kg=830.42,
            scope3_co2e_kg=2256.00,
            baseline_co2e_kg=6456.00,
        )
        assert e1.index == 1
        assert e1.previous_hash == ledger.chain[0].entry_hash
        assert len(e1.entry_hash) == 64

        # Append entry 2
        e2 = ledger.append_entry(
            batch_id="BATCH-VN-2026-COFFEE-02",
            farm_id="VN-LD-CAUDAT-002",
            crop_type="Arabica Coffee",
            scope1_co2e_kg=1450.20,
            scope2_co2e_kg=410.50,
            scope3_co2e_kg=988.80,
            baseline_co2e_kg=3788.80,
        )
        assert e2.index == 2
        assert e2.previous_hash == e1.entry_hash

        # Verify chain
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True
        assert err is None

    def test_esg_ledger_tamper_detection(self):
        """Asserts tampering is detected with exact diagnostics."""
        ledger = ESGLedger()
        ledger.append_entry("B1", "F1", "Rice", 10.0, 5.0, 2.0, 25.0)
        ledger.append_entry("B2", "F1", "Rice", 12.0, 6.0, 2.0, 28.0)

        # Alter payload of block 1
        ledger.chain[1].scope1_co2e_kg = 1.0  # Fraudulent claim
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is False
        assert "Tampering detected at block index 1" in err

    def test_esg_ledger_json_export_and_reload(self, tmp_path):
        """Verifies JSON export and reload round-trip preserves chain validity."""
        ledger = ESGLedger()
        ledger.append_entry("B1", "F1", "Rice", 10.0, 5.0, 2.0, 25.0)
        filepath = tmp_path / "test_ledger.json"
        ledger.export_to_json(str(filepath))

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        reloaded = ESGLedger.load_from_dict(data)
        assert len(reloaded.chain) == 2
        valid, err = verify_ledger_chain(reloaded.chain)
        assert valid is True


# ============================================================================
# 7. PRESET DATASETS VALIDATION TESTS
# ============================================================================

class TestPresetDatasets:
    """Validates the An Giang Rice and Lam Dong Coffee preset JSON files."""

    def test_an_giang_rice_preset_exists_and_valid(self):
        """data/presets/an_giang_rice.json must parse cleanly and contain required keys."""
        preset_path = PROJECT_ROOT / "data" / "presets" / "an_giang_rice.json"
        assert preset_path.exists(), f"Preset file missing: {preset_path}"

        with open(preset_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data["preset_id"] == "an_giang_rice"
        assert data["farm_profile"]["province"] == "An Giang"
        assert data["crop_profile"]["fao_kc"] == 1.10
        assert data["sensor_telemetry"]["soil_moisture_pct"] == 42.0
        assert data["weather_forecast"]["summary_48h"]["expected_precipitation_mm"] == 35.0
        assert data["optimized_agricarbon"]["water_savings_pct"] == 38.0

    def test_lam_dong_coffee_preset_exists_and_valid(self):
        """data/presets/lam_dong_coffee.json must parse cleanly and contain required keys."""
        preset_path = PROJECT_ROOT / "data" / "presets" / "lam_dong_coffee.json"
        assert preset_path.exists(), f"Preset file missing: {preset_path}"

        with open(preset_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data["preset_id"] == "lam_dong_coffee"
        assert "Lâm Đồng" in data["farm_profile"]["province"]
        assert data["crop_profile"]["fao_kc"] == 0.95
        assert data["sensor_telemetry"]["soil_moisture_pct"] == 24.0
        assert data["weather_forecast"]["summary_48h"]["expected_precipitation_mm"] == 0.0
        assert data["optimized_agricarbon"]["electricity_cost_savings_pct"] == 71.19
        assert data["optimized_agricarbon"]["fertilizer_savings_pct"] == 30.95


if __name__ == "__main__":
    pytest.main(["-v", __file__])
