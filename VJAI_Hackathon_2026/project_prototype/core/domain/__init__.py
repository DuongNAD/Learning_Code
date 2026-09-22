"""
AgriCarbon Agent Domain Layer.
Provides deterministic biophysical and carbon models:
1. agronomy: FAO-56 Penman-Monteith evapotranspiration & irrigation scheduling.
2. carbon_models: IPCC Tier 1 & 2 GHG calculation & Scope 1-3 auditing.
3. esg_ledger: Cryptographic SHA-256 tamper-evident ESG audit ledger.
"""

from core.domain.agronomy import (
    calculate_et0,
    calculate_irrigation_need,
    get_crop_coefficient,
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
    EmissionBreakdown,
    Scope1Scope2Result,
    Scope3LogisticsResult,
)
from core.domain.esg_ledger import (
    create_block_hash,
    verify_ledger_integrity,
    ESGAuditEntryModel,
    ESGLedger,
    verify_ledger_chain,
)

__all__ = [
    "calculate_et0",
    "calculate_irrigation_need",
    "get_crop_coefficient",
    "calculate_seasonal_water_savings",
    "CropType",
    "GrowthStage",
    "IrrigationUrgency",
    "AvoidReason",
    "calculate_scope1_scope2_emissions",
    "calculate_scope3_logistics",
    "calculate_fertilizer_n2o_ef",
    "EmissionBreakdown",
    "Scope1Scope2Result",
    "Scope3LogisticsResult",
    "create_block_hash",
    "verify_ledger_integrity",
    "ESGAuditEntryModel",
    "ESGLedger",
    "verify_ledger_chain",
]
