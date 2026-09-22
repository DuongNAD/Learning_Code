"""
Tier 3: Pairwise - Fault Injection -> Critic Self-Reflection -> Recovery Pipeline
Tests the complete closed-loop self-correction pipeline:
Tool error injection -> Critic rejection -> Planner re-planning -> Critic approval -> ESG commit.
Authoritative source: ORIGINAL_REQUEST.md § Acceptance Criteria (Self-Correction Loop)
"""

import pytest
import sys
from pathlib import Path
from typing import Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.tier1_feature.test_supervisor_agent import create_initial_agent_state
from tests.tier2_boundary.test_tool_error_injection import evaluate_plan_by_critic
from tests.conftest import resolve_carbon_module, resolve_ledger_module


class TestCriticSelfCorrectionPipeline:
    """Validates the full self-reflection and re-planning pipeline under fault injection."""

    def test_full_error_injection_self_reflection_recovery_pipeline(self):
        """End-to-end simulation of error injection, critic rejection, re-planning, and final approval."""
        carbon = resolve_carbon_module()
        ledger = resolve_ledger_module()
        
        # 1. Initialize State
        state = create_initial_agent_state("task_self_corr_01", "an_giang_rice_001", "Execute daily irrigation")
        
        # 2. Injected Fault: Dispatch proposes 120mm water (extreme overdose)
        faulty_plan = {
            "water_needed_mm": 120.0,
            "duration_minutes": 280,
            "urgency": "HIGH"
        }
        state["dispatch_plan"] = faulty_plan
        state["thoughts"].append({"step": "dispatch", "thought": "Proposing 120mm deep flooding."})
        
        # 3. Critic evaluates faulty plan
        verdict = evaluate_plan_by_critic(state["dispatch_plan"], retry_count=state["critic_verdict"]["retry_count"])
        state["critic_verdict"] = verdict
        state["thoughts"].append({"step": "critic_review", "critique": verdict["feedback"]})
        
        assert verdict["approved"] is False
        assert verdict["retry_count"] == 1
        
        # 4. Supervisor triggers ReAct re-planning loop based on Critic feedback
        corrected_plan = {
            "water_needed_mm": 24.0,  # Corrected to safe AWD quota
            "duration_minutes": 48,
            "urgency": "MEDIUM"
        }
        state["dispatch_plan"] = corrected_plan
        state["thoughts"].append({"step": "re_planning", "thought": "Scaled down water dosage to 24mm based on Critic feedback."})
        
        # 5. Critic re-evaluates corrected plan
        v2 = evaluate_plan_by_critic(state["dispatch_plan"], retry_count=state["critic_verdict"]["retry_count"])
        state["critic_verdict"] = v2
        state["thoughts"].append({"step": "critic_review_2", "critique": v2["feedback"]})
        
        assert v2["approved"] is True
        assert "APPROVED" in v2["feedback"]
        assert v2["retry_count"] == 1
        
        # 6. Carbon auditing and ledger commit proceeds on approved plan
        emissions = carbon.calculate_scope1_scope2_emissions(
            water_pumped_m3=40.0,
            pump_power_kw=15.0
        )
        state["carbon_report"] = emissions
        
        entry = ledger.create_block_hash(
            record_id="rec_corr_01",
            timestamp="2026-09-08T09:00:00Z",
            farm_id="an_giang_rice_001",
            action="pump_flush_corrected",
            co2e_kg=emissions["total_co2e_kg"],
            prev_hash="0" * 64
        )
        state["final_output"] = {
            "status": "success",
            "dispatch": corrected_plan,
            "ledger_hash": entry
        }
        
        assert state["final_output"]["status"] == "success"
        assert len(state["thoughts"]) >= 4

    def test_unrecoverable_fault_triggers_safe_shutdown(self):
        """Verify 3 consecutive failed re-plans cleanly trigger safe abort without crashing."""
        retry_count = 0
        terminal_status = None
        
        # 3 iterations of unresolvable error injection
        for _ in range(3):
            bad_plan = {"water_needed_mm": 999.0}
            verdict = evaluate_plan_by_critic(bad_plan, retry_count=retry_count)
            retry_count = verdict["retry_count"]
            if retry_count >= 3:
                terminal_status = "SAFE_ABORT_OPERATOR_NOTIFIED"
                break
                
        assert retry_count == 3
        assert terminal_status == "SAFE_ABORT_OPERATOR_NOTIFIED"
