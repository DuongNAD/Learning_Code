"""
Tool 3: calculate_agricultural_emissions
Deterministic IPCC Tier 1/2 GHG computation engine for CO2e, CH4, and N2O.
Conforms strictly to PROJECT.md § Tools & Connectors and tests/tier1_feature/test_tools.py.
"""

from typing import Dict, Any, Optional
from core.domain.carbon_models import (
    calculate_scope1_scope2_emissions as domain_calc_emissions,
    calculate_scope3_logistics,
    calculate_methane_emissions_tier2
)


def calculate_agricultural_emissions(
    water_pumped_m3: float,
    pump_power_kw: float,
    fertilizer_n_kg: float = 0.0,
    diesel_liters: float = 0.0,
    grid_emission_factor: float = 0.7221,
    electricity_kwh: Optional[float] = None,
    baseline_co2e_override: Optional[float] = None
) -> Dict[str, Any]:
    """
    Computes agricultural GHG footprint according to IPCC 2006/2019 guidelines.

    Returns:
        Dict with:
            total_co2e_kg, breakdown (electricity_co2e, fertilizer_n2o_co2e, fuel_co2e),
            baseline_co2e_kg, reduction_pct, methodology
    """
    res = domain_calc_emissions(
        water_pumped_m3=water_pumped_m3,
        pump_power_kw=pump_power_kw,
        grid_emission_factor=grid_emission_factor,
        fertilizer_n_kg=fertilizer_n_kg,
        diesel_liters=diesel_liters,
        electricity_kwh=electricity_kwh,
        baseline_co2e_override=baseline_co2e_override
    )
    res["methodology"] = "IPCC 2006 / 2019 Refinement AFOLU Tier 1/2"
    return res
