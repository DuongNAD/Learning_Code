"""
Tier 3: Pairwise - Dispatch to Carbon Auditor to ESG Ledger Pipeline
Tests data flow from dispatch decisions to IPCC carbon auditing and cryptographic ledger recording.
Authoritative source: PROJECT.md § Architecture & Data Flow
"""

import pytest
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import (
    resolve_carbon_module,
    resolve_ledger_module
)


class TestDispatchCarbonLedgerPipeline:
    """Validates interactions between Eco-Dispatch, Carbon Auditor, and ESG Ledger."""

    def test_dispatch_to_carbon_and_ledger_flow(self):
        """Verify dispatch action leads to calculated emissions and committed ledger record."""
        carbon = resolve_carbon_module()
        ledger = resolve_ledger_module()
        
        # 1. Dispatch decision: 45 min pump duration at 15 kW -> ~37.5 m3 pumped
        pump_duration_min = 45
        pump_kw = 15.0
        water_m3 = (pump_duration_min / 60.0) * 50.0  # 37.5 m3
        
        # 2. Carbon auditing
        emissions = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=water_m3,
            pump_power_kw=pump_kw,
            grid_emission_factor=0.7221,
            fertilizer_n_kg=0.0,
            diesel_liters=0.0
        )
        assert emissions["total_co2e_kg"] > 0.0
        
        # 3. Ledger commitment
        h = ledger.create_block_hash(
            record_id="rec_polder_45m",
            timestamp="2026-09-08T08:00:00Z",
            farm_id="an_giang_rice_001",
            action="pump_flush_45min",
            co2e_kg=emissions["total_co2e_kg"],
            prev_hash="0" * 64
        )
        assert len(h) == 64
        assert h.isalnum()

    def test_sequential_dispatch_actions_form_valid_hash_chain(self):
        """Verify sequential dispatch cycles build a tamper-evident audit trail."""
        carbon = resolve_carbon_module()
        ledger = resolve_ledger_module()
        
        chain = []
        # Cycle 1: Morning irrigation
        e1 = carbon.calculate_scope1_scope2_emissions(30.0, 10.0, 0.7221, 0.0, 0.0)
        h1 = ledger.create_block_hash("rec_01", "2026-09-08T06:00:00Z", "farm_01", "morning_irrigation", e1["total_co2e_kg"], "0" * 64)
        chain.append({
            "record_id": "rec_01", "timestamp": "2026-09-08T06:00:00Z",
            "farm_id": "farm_01", "action": "morning_irrigation",
            "co2e_kg": e1["total_co2e_kg"], "prev_hash": "0" * 64, "hash": h1
        })
        
        # Cycle 2: Afternoon fertigation
        e2 = carbon.calculate_scope1_scope2_emissions(20.0, 10.0, 0.7221, 15.0, 2.0)
        h2 = ledger.create_block_hash("rec_02", "2026-09-08T14:00:00Z", "farm_01", "fertigation", e2["total_co2e_kg"], h1)
        chain.append({
            "record_id": "rec_02", "timestamp": "2026-09-08T14:00:00Z",
            "farm_id": "farm_01", "action": "fertigation",
            "co2e_kg": e2["total_co2e_kg"], "prev_hash": h1, "hash": h2
        })
        
        assert ledger.verify_ledger_integrity(chain) is True

    def test_carbon_reduction_pct_recorded_in_audit(self):
        """Verify audited reduction percentage matches target expectations (-28.1%)."""
        carbon = resolve_carbon_module()
        res = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=75.0,
            pump_power_kw=12.0,
            grid_emission_factor=0.7221,
            fertilizer_n_kg=10.0,
            diesel_liters=4.0
        )
        assert res["reduction_pct"] > 25.0
        assert res["baseline_co2e_kg"] > res["total_co2e_kg"]
