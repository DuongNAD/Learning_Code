"""
Tier 5 Adversarial Stress Testing: Agronomic & Carbon Boundary Robustness.
Authoritative source: Milestone 1 Verification Protocol (Challenger 1).
Exhaustively stresses core/domain/agronomy.py and core/domain/carbon_models.py under:
- Climatic extremes: extreme heat (up to 100°C), subzero frost (down to -80°C), cyclonic winds (up to 100 m/s),
  zero wind (0.0 m/s), 100% relative humidity, dark overcast (0 radiation).
- Irrigation boundaries: negative rainfall, extreme deluge (5000 mm), fractional vs percentage soil moisture,
  subzero soil moisture readings, saturation conditions.
- Carbon accounting boundaries: extreme nitrogen rates (up to 1,000,000 kg N), negative diesel/water/power inputs,
  zero inputs, electricity kWh overrides.
- Invariant verification: No NaN, No Inf, No negative irrigation demand, No unhandled exceptions.
"""

import math
import random
import pytest
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.domain.agronomy import (
    calculate_et0,
    calculate_irrigation_need,
    calculate_seasonal_water_savings,
    get_crop_coefficient,
    CropType,
    GrowthStage,
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


class TestAgronomyClimaticExtremes:
    """Stress tests FAO-56 Penman-Monteith ET0 against extreme physical and non-physical bounds."""

    @pytest.mark.parametrize("tmax, tmin", [
        (45.0, 35.0),
        (55.0, 42.0),
        (65.0, 50.0),
        (80.0, 60.0),
        (100.0, 80.0),
    ])
    def test_extreme_heat_bounds(self, tmax, tmin):
        """Extreme heat (45°C - 100°C) must produce finite ET0 clamped to [0.1, 14.5] mm/day."""
        et0 = calculate_et0(
            temp_max=tmax,
            temp_min=tmin,
            humidity=30.0,
            wind_speed=3.0,
            solar_rad=25.0,
        )
        assert isinstance(et0, float)
        assert not math.isnan(et0)
        assert not math.isinf(et0)
        assert 0.1 <= et0 <= 14.5

    @pytest.mark.parametrize("tmax, tmin", [
        (0.0, -5.0),
        (-5.0, -15.0),
        (-20.0, -35.0),
        (-50.0, -70.0),
        (-80.0, -90.0),
    ])
    def test_subzero_frost_bounds(self, tmax, tmin):
        """Deep subzero frost down to -90°C must not produce NaN, negative numbers or crash."""
        et0 = calculate_et0(
            temp_max=tmax,
            temp_min=tmin,
            humidity=60.0,
            wind_speed=2.0,
            solar_rad=5.0,
        )
        assert isinstance(et0, float)
        assert not math.isnan(et0)
        assert not math.isinf(et0)
        assert et0 >= 0.1

    @pytest.mark.parametrize("wind", [0.0, 0.00001, -1.0, -50.0, 35.0, 60.0, 100.0])
    def test_wind_speed_boundaries(self, wind):
        """Wind speeds from zero, negative (sensor bug), up to category 5 hurricane (100 m/s)."""
        et0 = calculate_et0(
            temp_max=32.0,
            temp_min=24.0,
            humidity=70.0,
            wind_speed=wind,
            solar_rad=18.0,
        )
        assert isinstance(et0, float)
        assert not math.isnan(et0)
        assert not math.isinf(et0)
        assert 0.1 <= et0 <= 14.5

    @pytest.mark.parametrize("humidity", [-50.0, 0.0, 0.01, 50.0, 99.9, 100.0, 105.0, 200.0])
    def test_relative_humidity_boundaries(self, humidity):
        """Relative humidity from negative, zero, 100% condensation, to supersaturation."""
        et0 = calculate_et0(
            temp_max=30.0,
            temp_min=22.0,
            humidity=humidity,
            wind_speed=2.0,
            solar_rad=16.0,
        )
        assert isinstance(et0, float)
        assert not math.isnan(et0)
        assert not math.isinf(et0)
        assert 0.1 <= et0 <= 14.5

    @pytest.mark.parametrize("solar_rad", [-20.0, 0.0, 0.001, 15.0, 35.0, 50.0, 100.0])
    def test_solar_radiation_boundaries(self, solar_rad):
        """Solar radiation from negative, total darkness (0.0), to extreme extraterrestrial levels."""
        et0 = calculate_et0(
            temp_max=28.0,
            temp_min=20.0,
            humidity=65.0,
            wind_speed=2.0,
            solar_rad=solar_rad,
        )
        assert isinstance(et0, float)
        assert not math.isnan(et0)
        assert not math.isinf(et0)
        assert 0.1 <= et0 <= 14.5

    def test_et0_monte_carlo_fuzzing(self):
        """10,000 randomized Monte Carlo simulations across all atmospheric input dimensions."""
        random.seed(42)
        for _ in range(10000):
            t1 = random.uniform(-60.0, 70.0)
            t2 = random.uniform(-60.0, 70.0)
            tmax, tmin = max(t1, t2), min(t1, t2)
            rh = random.uniform(-30.0, 150.0)
            ws = random.uniform(-10.0, 80.0)
            rs = random.uniform(-10.0, 45.0)
            elev = random.uniform(-100.0, 4000.0)
            lat = random.uniform(-80.0, 80.0)
            doy = random.randint(1, 365)

            et0 = calculate_et0(
                temp_max=tmax,
                temp_min=tmin,
                humidity=rh,
                wind_speed=ws,
                solar_rad=rs,
                elevation=elev,
                latitude=lat,
                day_of_year=doy,
            )
            assert not math.isnan(et0), f"NaN produced for inputs: {tmax}, {tmin}, {rh}, {ws}, {rs}"
            assert not math.isinf(et0), f"Inf produced for inputs: {tmax}, {tmin}, {rh}, {ws}, {rs}"
            assert 0.1 <= et0 <= 14.5, f"Out of bounds ET0: {et0}"


class TestAgronomyIrrigationBoundaries:
    """Stress tests irrigation need calculation under precipitation, soil moisture, and crop bounds."""

    @pytest.mark.parametrize("rain", [
        -1000.0, -100.0, -1.0, -0.001, 0.0,
        5.0, 14.9, 14.999, 15.0, 15.001, 30.0, 100.0, 500.0, 5000.0
    ])
    def test_rainfall_boundary_spectrum(self, rain):
        """Exhaustive rainfall spectrum from negative (sensor glitch) to typhoon (5000 mm)."""
        res = calculate_irrigation_need(
            crop_type="rice_jasmine_85",
            growth_stage="vegetative_tillering",
            current_soil_moisture=20.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.5,
            forecast_rain_mm=rain,
        )
        assert isinstance(res, dict)
        assert res["water_needed_mm"] >= 0.0, f"Negative water needed: {res['water_needed_mm']}"
        assert res["duration_minutes"] >= 0, f"Negative duration: {res['duration_minutes']}"
        assert not math.isnan(res["water_needed_mm"])

        if rain >= 15.0:
            assert res["water_needed_mm"] == 0.0
            assert res["duration_minutes"] == 0
            assert res["urgency"] == "NONE"
            assert res["avoid_reason"] == "forecast_rain"
        elif rain <= 0.0:
            # Negative rain sanitized to 0.0, demand remains positive for dry soil
            assert res["water_needed_mm"] > 0.0
            assert res["duration_minutes"] > 0
            assert res["avoid_reason"] is None

    @pytest.mark.parametrize("sm", [
        -50.0, -5.0, -0.001, 0.0, 0.05, 0.15, 0.25, 0.40,
        5.0, 15.0, 25.0, 40.0, 45.0, 50.0, 75.0, 100.0, 150.0
    ])
    def test_soil_moisture_normalization_and_saturation(self, sm):
        """Covers fractional inputs, percentage inputs, negative sensor anomalies, and supersaturation."""
        res = calculate_irrigation_need(
            crop_type="arabica_coffee",
            growth_stage="berry_development",
            current_soil_moisture=sm,
            field_capacity=40.0,
            wilting_point=18.0,
            et0=4.0,
            forecast_rain_mm=0.0,
        )
        assert res["water_needed_mm"] >= 0.0
        assert res["duration_minutes"] >= 0
        assert not math.isnan(res["water_needed_mm"])

        # Moisture at or above field capacity must require 0 water
        # If sm is fraction > 0.40 or percentage >= 40.0
        is_above_fc = (sm >= 40.0) or (0.40 <= sm <= 1.0)
        if is_above_fc:
            assert res["water_needed_mm"] == 0.0
            assert res["duration_minutes"] == 0
            assert res["avoid_reason"] == "sufficient_moisture"

    @pytest.mark.parametrize("crop, stage", [
        ("", ""),
        ("unknown_alien_crop", "unknown_stage"),
        ("rice", "invalid_phase"),
        ("coffee", ""),
        ("JASMINE_85", "MID_SEASON_FLOWERING"),
        ("Arabica", "BERRY_DEVELOPMENT"),
    ])
    def test_unrecognized_crop_and_stage_fallbacks(self, crop, stage):
        """Unrecognized cultivars or stages gracefully fall back without crashing."""
        kc = get_crop_coefficient(crop, stage)
        assert isinstance(kc, float)
        assert kc > 0.0

        res = calculate_irrigation_need(
            crop_type=crop,
            growth_stage=stage,
            current_soil_moisture=20.0,
            field_capacity=45.0,
            wilting_point=15.0,
            et0=4.0,
            forecast_rain_mm=0.0,
        )
        assert res["water_needed_mm"] >= 0.0
        assert res["duration_minutes"] >= 0

    def test_irrigation_need_monte_carlo_fuzzing(self):
        """5,000 randomized Monte Carlo simulations across soil water parameters."""
        random.seed(99)
        for _ in range(5000):
            crop = random.choice(["rice", "coffee", "rice_jasmine_85", "arabica_coffee", "unknown"])
            stage = random.choice(["initial", "vegetative", "mid_season", "late_season", "unknown"])
            sm = random.uniform(-20.0, 100.0)
            fc = random.uniform(20.0, 60.0)
            wp = random.uniform(5.0, min(fc - 1.0, 35.0))
            et0 = random.uniform(0.1, 15.0)
            rain = random.uniform(-10.0, 50.0)

            res = calculate_irrigation_need(
                crop_type=crop,
                growth_stage=stage,
                current_soil_moisture=sm,
                field_capacity=fc,
                wilting_point=wp,
                et0=et0,
                forecast_rain_mm=rain,
            )
            assert res["water_needed_mm"] >= 0.0
            assert res["duration_minutes"] >= 0
            assert not math.isnan(res["water_needed_mm"])
            assert res["urgency"] in ["CRITICAL", "HIGH", "MEDIUM", "MODERATE", "LOW", "NONE", "DEFERRED"]


class TestCarbonModelsStressBoundaries:
    """Stress tests IPCC Tier 1/2 GHG calculations and Scope 1-3 carbon accounting."""

    @pytest.mark.parametrize("fert_n", [
        -500.0, -1.0, 0.0, 1.0, 100.0, 500.0, 10000.0, 100000.0, 1_000_000.0
    ])
    def test_extreme_nitrogen_rates(self, fert_n):
        """Nitrogen rates from negative (sanitized) to massive industrial mega-applications."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=100.0,
            pump_power_kw=10.0,
            grid_emission_factor=DEFAULT_GRID_EF_VN,
            fertilizer_n_kg=fert_n,
            diesel_liters=5.0,
        )
        assert res["total_co2e_kg"] >= 0.0
        assert res["breakdown"]["fertilizer_n2o_co2e"] >= 0.0
        assert not math.isnan(res["total_co2e_kg"])
        assert not math.isinf(res["total_co2e_kg"])

        if fert_n <= 0.0:
            assert res["breakdown"]["fertilizer_n2o_co2e"] == 0.0
        else:
            assert res["breakdown"]["fertilizer_n2o_co2e"] > 0.0

    @pytest.mark.parametrize("water, power, diesel", [
        (-100.0, 10.0, 5.0),
        (100.0, -10.0, 5.0),
        (100.0, 10.0, -5.0),
        (-50.0, -50.0, -50.0),
        (0.0, 0.0, 0.0),
        (1e7, 1e4, 1e5),
    ])
    def test_hydraulic_and_fuel_negative_and_extreme_bounds(self, water, power, diesel):
        """Negative and extreme water/power/fuel inputs sanitized without crash or negative emissions."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=water,
            pump_power_kw=power,
            grid_emission_factor=DEFAULT_GRID_EF_VN,
            fertilizer_n_kg=20.0,
            diesel_liters=diesel,
        )
        assert res["total_co2e_kg"] >= 0.0
        assert res["breakdown"]["electricity_co2e"] >= 0.0
        assert res["breakdown"]["fuel_co2e"] >= 0.0
        assert not math.isnan(res["total_co2e_kg"])

    @pytest.mark.parametrize("elec_override", [-50.0, 0.0, 100.0, 1e6])
    def test_electricity_kwh_override_boundaries(self, elec_override):
        """Direct electricity kWh override bounds."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=100.0,
            pump_power_kw=10.0,
            electricity_kwh=elec_override,
        )
        assert res["breakdown"]["electricity_co2e"] >= 0.0
        if elec_override <= 0.0:
            assert res["breakdown"]["electricity_co2e"] == 0.0

    @pytest.mark.parametrize("baseline_override", [-100.0, 0.0, 50.0, 1000.0])
    def test_baseline_override_boundaries(self, baseline_override):
        """Baseline reference override bounds."""
        res = calculate_scope1_scope2_emissions(
            water_pumped_m3=100.0,
            pump_power_kw=10.0,
            baseline_co2e_override=baseline_override,
        )
        assert not math.isnan(res["reduction_pct"])
        assert not math.isinf(res["reduction_pct"])

    def test_carbon_monte_carlo_fuzzing(self):
        """5,000 randomized Monte Carlo simulations for carbon accounting."""
        random.seed(123)
        for _ in range(5000):
            water = random.uniform(-100.0, 5000.0)
            power = random.uniform(-20.0, 100.0)
            grid_ef = random.uniform(0.0, 1.5)
            fert_n = random.uniform(-50.0, 1000.0)
            diesel = random.uniform(-50.0, 500.0)

            res = calculate_scope1_scope2_emissions(
                water_pumped_m3=water,
                pump_power_kw=power,
                grid_emission_factor=grid_ef,
                fertilizer_n_kg=fert_n,
                diesel_liters=diesel,
            )
            assert res["total_co2e_kg"] >= 0.0
            assert res["breakdown"]["electricity_co2e"] >= 0.0
            assert res["breakdown"]["fertilizer_n2o_co2e"] >= 0.0
            assert res["breakdown"]["fuel_co2e"] >= 0.0
            assert not math.isnan(res["total_co2e_kg"])
            assert not math.isnan(res["reduction_pct"])

    @pytest.mark.parametrize("tonnage", [-100.0, -1.0, 0.0])
    def test_scope3_logistics_non_positive_tonnage_rejected(self, tonnage):
        """Scope 3 logistics must reject zero and negative export tonnage with ValueError."""
        with pytest.raises(ValueError, match="greater than zero"):
            calculate_scope3_logistics(tonnage=tonnage)

    @pytest.mark.parametrize("tonnage", [0.001, 1.0, 25.0, 1000.0, 100000.0])
    def test_scope3_logistics_positive_tonnage_validity(self, tonnage):
        """Scope 3 logistics calculates positive, non-NaN footprint for valid tonnage."""
        res = calculate_scope3_logistics(tonnage=tonnage, cold_chain=True)
        assert res["total_scope3_co2e_kg"] > 0.0
        assert res["co2e_per_ton_kg"] > 0.0
        assert not math.isnan(res["total_scope3_co2e_kg"])

    @pytest.mark.parametrize("area, days, regime", [
        (0.0, 100, "awd"),
        (5.0, 0, "awd"),
        (5.0, 100, "continuous"),
        (10.0, 120, "other"),
        (1000.0, 365, "awd"),
    ])
    def test_methane_tier2_boundaries(self, area, days, regime):
        """AWD Methane model calculates valid bounds without division by zero or NaN."""
        res = calculate_methane_emissions_tier2(area_ha=area, days=days, water_regime=regime)
        assert res["ch4_kg"] >= 0.0
        assert res["co2e_kg"] >= 0.0
        assert not math.isnan(res["reduction_pct"])
        assert not math.isinf(res["reduction_pct"])
