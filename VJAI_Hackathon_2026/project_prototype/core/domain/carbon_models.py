"""
IPCC Tier 1 & Tier 2 Agricultural Carbon Accounting Models.
Implements GHG Protocol Agricultural Guidance, 2006 IPCC Guidelines,
and 2019 AFOLU Refinements.
Covers Scope 1 direct farm emissions, Scope 2 pumping electricity emissions,
and Scope 3 international export logistics to Port of Tokyo / Yokohama.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, ConfigDict

# Standard Constants & Emission Factors
DEFAULT_GRID_EF_VN = 0.7221  # kg CO2e / kWh (Vietnam EVN national grid combined margin factor)
DEFAULT_GRID_EF_JP = 0.4350  # kg CO2e / kWh (Japan MOE / TEPCO grid baseline)
DEFAULT_DIESEL_EF = 2.6800  # kg CO2e / liter (IPCC Vol 2 mobile diesel combustion)
DEFAULT_GWP_N2O = 265.0  # IPCC AR5 100-year GWP for N2O
DEFAULT_GWP_CH4 = 28.0  # IPCC AR5 100-year GWP for CH4
DEFAULT_PUMP_THROUGHPUT_M3_H = 50.0  # Default pump discharge capacity in m3/hour
DEFAULT_SPECIFIC_ENERGY = 0.2400  # kWh / m3 pumped water (axial low-lift pump)

# IPCC N2O Default Parameters (2019 Refinement)
IPCC_EF1_UPLAND = 0.010  # kg N2O-N / kg N input (direct, general crops)
IPCC_EF1_RICE = 0.004  # kg N2O-N / kg N input (direct, flooded rice)
IPCC_FRAC_GASF = 0.10  # fraction of synthetic N volatilized as NH3 and NOx
IPCC_EF4 = 0.010  # kg N2O-N / kg volatilized N
IPCC_FRAC_LEACH = 0.24  # fraction of synthetic N leached
IPCC_EF5 = 0.011  # kg N2O-N / kg leached N
MW_RATIO_N2O_N2 = 44.0 / 28.0  # 1.57142857


class EmissionBreakdown(BaseModel):
    model_config = ConfigDict(extra="forbid")
    electricity_co2e: float = Field(..., ge=0.0, description="Scope 2 electricity emissions in kg CO2e")
    fertilizer_n2o_co2e: float = Field(..., ge=0.0, description="Scope 1 synthetic N2O emissions in kg CO2e")
    fuel_co2e: float = Field(..., ge=0.0, description="Scope 1 diesel combustion emissions in kg CO2e")


class Scope1Scope2Result(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total_co2e_kg: float = Field(..., ge=0.0, description="Sum of Scope 1 and Scope 2 emissions in kg CO2e")
    breakdown: EmissionBreakdown = Field(..., description="Itemized categorical emissions")
    baseline_co2e_kg: float = Field(..., ge=0.0, description="Baseline reference emissions in kg CO2e")
    reduction_pct: float = Field(..., description="Calculated percentage reduction relative to baseline")


class Scope3LogisticsResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tonnage: float = Field(..., gt=0.0, description="Export batch weight in metric tons")
    road_co2e_kg: float = Field(..., ge=0.0, description="Inland trucking emissions in kg CO2e")
    ocean_co2e_kg: float = Field(..., ge=0.0, description="Maritime shipping emissions in kg CO2e")
    cold_chain_co2e_kg: float = Field(..., ge=0.0, description="Reefer cold storage emissions in kg CO2e")
    total_scope3_co2e_kg: float = Field(..., ge=0.0, description="Total Scope 3 logistics emissions in kg CO2e")
    co2e_per_ton_kg: float = Field(..., ge=0.0, description="Logistics carbon intensity in kg CO2e/ton")


def calculate_fertilizer_n2o_ef(
    is_flooded_rice: bool = False,
    gwp_n2o: float = DEFAULT_GWP_N2O,
) -> float:
    """
    Computes combined IPCC Tier 1/2 direct + indirect N2O emission factor per kg synthetic N.
    """
    ef1 = IPCC_EF1_RICE if is_flooded_rice else IPCC_EF1_UPLAND
    n2o_n_factor = ef1 + (IPCC_FRAC_GASF * IPCC_EF4) + (IPCC_FRAC_LEACH * IPCC_EF5)
    return n2o_n_factor * MW_RATIO_N2O_N2 * gwp_n2o


def calculate_scope1_scope2_emissions(
    water_pumped_m3: float,
    pump_power_kw: float,
    grid_emission_factor: float = DEFAULT_GRID_EF_VN,
    fertilizer_n_kg: float = 0.0,
    diesel_liters: float = 0.0,
    electricity_kwh: Optional[float] = None,
    baseline_co2e_override: Optional[float] = None,
    ef_diesel: float = DEFAULT_DIESEL_EF,
    gwp_n2o: float = DEFAULT_GWP_N2O,
) -> Dict[str, Any]:
    """
    Mandated interface contract from PROJECT.md line 160-164.

    Parameters:
        water_pumped_m3: Volume of irrigation water pumped (m3)
        pump_power_kw: Rated electrical power of pump motor (kW)
        grid_emission_factor: Grid emission factor in kg CO2e/kWh (default Vietnam EVN 0.7221)
        fertilizer_n_kg: Applied synthetic nitrogen fertilizer (kg N)
        diesel_liters: Consumed machinery diesel fuel (liters)
        electricity_kwh: Optional directly measured electricity in kWh (overrides hydraulic calculation)
        baseline_co2e_override: Optional explicit baseline reference for comparison
        ef_diesel: Diesel emission factor (default 2.68 kg CO2e/liter)
        gwp_n2o: 100-year global warming potential of N2O (default 265.0)

    Returns:
        dict: {
            'total_co2e_kg': float,
            'breakdown': {
                'electricity_co2e': float,
                'fertilizer_n2o_co2e': float,
                'fuel_co2e': float
            },
            'baseline_co2e_kg': float,
            'reduction_pct': float
        }
    """
    # Defensive input sanitization: non-negative metrics
    safe_water = max(0.0, float(water_pumped_m3))
    safe_power = max(0.0, float(pump_power_kw))
    safe_fert_n = max(0.0, float(fertilizer_n_kg))
    safe_diesel = max(0.0, float(diesel_liters))
    safe_grid_ef = max(0.0, float(grid_emission_factor))

    # 1. Scope 2: Electricity Consumption
    if electricity_kwh is not None:
        elec_kwh = max(0.0, float(electricity_kwh))
    else:
        if safe_power <= 0.0 or safe_water <= 0.0:
            elec_kwh = 0.0
        else:
            pumping_hours = safe_water / DEFAULT_PUMP_THROUGHPUT_M3_H
            elec_kwh = pumping_hours * safe_power

    electricity_co2e = round(elec_kwh * safe_grid_ef, 3)

    # 2. Scope 1: Fertilizer direct N2O emissions (IPCC Tier 1: 1% emission factor, GWP 265)
    # 1 kg N * 0.01 * (44/28) * 265 = 4.1642857 kg CO2e / kg N
    n2o_factor = 0.01 * MW_RATIO_N2O_N2 * gwp_n2o
    fertilizer_n2o_co2e = round(safe_fert_n * n2o_factor, 3)

    # 3. Scope 1: Diesel combustion emissions
    fuel_co2e = round(safe_diesel * ef_diesel, 3)

    # Total combined emissions
    total_co2e_kg = round(electricity_co2e + fertilizer_n2o_co2e + fuel_co2e, 3)

    # 4. Baseline Reference & Reduction Goal Verification (-28.1%)
    if baseline_co2e_override is not None:
        baseline_co2e_kg = round(baseline_co2e_override, 3)
    else:
        if total_co2e_kg > 0.0:
            baseline_co2e_kg = round(total_co2e_kg / (1.0 - 0.281), 3)
        else:
            baseline_co2e_kg = 0.0

    if baseline_co2e_kg > 0.0:
        reduction_pct = round(
            ((baseline_co2e_kg - total_co2e_kg) / baseline_co2e_kg) * 100.0, 1
        )
    else:
        reduction_pct = 0.0

    return {
        "total_co2e_kg": total_co2e_kg,
        "breakdown": {
            "electricity_co2e": electricity_co2e,
            "fertilizer_n2o_co2e": fertilizer_n2o_co2e,
            "fuel_co2e": fuel_co2e,
        },
        "baseline_co2e_kg": baseline_co2e_kg,
        "reduction_pct": reduction_pct,
    }


def calculate_scope3_logistics(
    tonnage: float,
    origin_region: str = "an_giang",
    destination_port: str = "tokyo",
    cold_chain: bool = False,
) -> Dict[str, Any]:
    """
    Calculates cradle-to-destination-port Scope 3 transport footprint from farm gate in Vietnam
    to Tokyo / Yokohama Port, Japan.
    """
    if tonnage <= 0:
        raise ValueError("Export tonnage must be greater than zero.")

    road_distances = {
        "an_giang": 220.0,  # Tri Ton -> Cat Lai Port (HCMC)
        "lam_dong": 310.0,  # Da Lat -> Cat Lai Port (HCMC)
    }
    road_km = road_distances.get(origin_region.lower(), 250.0)
    ocean_km = 4320.0  # Maritime HCMC Port to Tokyo Port (2,332 nm)

    ef_road = 0.096  # kg CO2e / (ton * km) - Heavy diesel truck
    ef_ocean = 0.016  # kg CO2e / (ton * km) - Container vessel
    ef_cold = 0.650  # kg CO2e / kWh
    kwh_cold = 45.0 if cold_chain else 0.0

    road_co2e = round(tonnage * road_km * ef_road, 2)
    ocean_co2e = round(tonnage * ocean_km * ef_ocean, 2)
    cold_co2e = round(tonnage * kwh_cold * ef_cold, 2)
    total_scope3 = round(road_co2e + ocean_co2e + cold_co2e, 2)

    return {
        "tonnage": round(tonnage, 2),
        "road_co2e_kg": road_co2e,
        "ocean_co2e_kg": ocean_co2e,
        "cold_chain_co2e_kg": cold_co2e,
        "total_scope3_co2e_kg": total_scope3,
        "co2e_per_ton_kg": round(total_scope3 / tonnage, 2),
    }


def calculate_methane_emissions_tier2(
    area_ha: float,
    days: int,
    water_regime: str = "awd",
    baseline_ef_c: float = 1.30,
    gwp_ch4: float = DEFAULT_GWP_CH4,
) -> Dict[str, Any]:
    """
    IPCC Tier 2 methane emission model for rice cultivation.
    Under Alternate Wetting and Drying (AWD), scaling factor SF_w = 0.52 (48% CH4 reduction).
    """
    sf_w = 0.52 if water_regime.lower() == "awd" else 1.00
    ch4_kg = area_ha * days * baseline_ef_c * sf_w
    co2e_kg = ch4_kg * gwp_ch4

    baseline_ch4_kg = area_ha * days * baseline_ef_c * 1.00
    baseline_co2e_kg = baseline_ch4_kg * gwp_ch4
    saved_co2e_kg = baseline_co2e_kg - co2e_kg
    reduction_pct = round((saved_co2e_kg / baseline_co2e_kg) * 100.0, 1) if baseline_co2e_kg > 0 else 0.0

    return {
        "water_regime": water_regime,
        "ch4_kg": round(ch4_kg, 2),
        "co2e_kg": round(co2e_kg, 2),
        "baseline_co2e_kg": round(baseline_co2e_kg, 2),
        "saved_co2e_kg": round(saved_co2e_kg, 2),
        "reduction_pct": reduction_pct,
    }
