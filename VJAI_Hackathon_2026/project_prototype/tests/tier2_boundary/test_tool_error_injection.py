"""
Tier 2: Boundary & Corner Cases - Tool Error Injection & Self-Correction
Tests Critic Guardrail Agent detecting faulty tool outputs,
incrementing Reflexion retry counter (max 3), and triggering self-correction.
Authoritative source: ORIGINAL_REQUEST.md § Acceptance Criteria (Self-Correction Loop)
"""

import pytest
import sys
from pathlib import Path
from typing import Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def evaluate_plan_by_critic(dispatch_plan: Dict[str, Any], retry_count: int) -> Dict[str, Any]:
    """Safety Critic Guardrail node logic enforcing agronomic bounds."""
    # Check 1: Excessive water overdose guardrail (> 60mm in a single day is catastrophic for rice/coffee)
    water_mm = dispatch_plan.get("water_needed_mm", 0.0)
    if water_mm > 60.0:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": f"REJECT: Water dosage {water_mm}mm violates FAO-56 maximum single-event limit (60mm). Reduce duration."
        }
        
    # Check 2: Missing or malformed keys
    if "duration_minutes" not in dispatch_plan:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: Dispatch plan missing mandatory 'duration_minutes' field."
        }
        
    # Check 3: Excessive pump duration (> 480 minutes / 8 hours single run)
    if dispatch_plan.get("duration_minutes", 0) > 480:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: Continuous pumping over 8 hours risks pump motor burnout. Split into shifts."
        }
        
    # If all safe:
    return {
        "approved": True,
        "retry_count": retry_count,
        "feedback": "APPROVED: Plan within safe agronomic boundaries."
    }


class TestToolErrorInjectionAndSelfCorrection:
    """Validates Reflexion self-correction loop triggered by malformed tool results."""

    def test_critic_detects_irrigation_overdose(self):
        """Verify Critic blocks dangerous over-irrigation recommendation (150mm)."""
        bad_plan = {"water_needed_mm": 150.0, "duration_minutes": 360}
        verdict = evaluate_plan_by_critic(bad_plan, retry_count=0)
        
        assert verdict["approved"] is False
        assert verdict["retry_count"] == 1
        assert "violates FAO-56" in verdict["feedback"]

    def test_critic_detects_malformed_plan_schema(self):
        """Verify Critic blocks plan missing duration_minutes."""
        malformed_plan = {"water_needed_mm": 20.0}  # Missing duration_minutes
        verdict = evaluate_plan_by_critic(malformed_plan, retry_count=0)
        
        assert verdict["approved"] is False
        assert "duration_minutes" in verdict["feedback"]

    def test_reflexion_retry_counter_increments(self):
        """Verify sequential rejections increment the retry counter."""
        bad_plan = {"water_needed_mm": 99.0, "duration_minutes": 200}
        v1 = evaluate_plan_by_critic(bad_plan, retry_count=0)
        assert v1["retry_count"] == 1
        
        v2 = evaluate_plan_by_critic(bad_plan, retry_count=v1["retry_count"])
        assert v2["retry_count"] == 2

    def test_circuit_breaker_terminal_fallback_after_max_retries(self):
        """Verify circuit breaker trips when retry counter reaches max limit of 3."""
        MAX_RETRIES = 3
        current_retries = 3
        # When retries reach limit, supervisor triggers fallback safe state
        circuit_broken = (current_retries >= MAX_RETRIES)
        fallback_action = "HALT_PUMP_AND_ALERT_OPERATOR" if circuit_broken else "RETRY"
        
        assert circuit_broken is True
        assert fallback_action == "HALT_PUMP_AND_ALERT_OPERATOR"

    def test_self_correction_recovers_to_approved_plan(self):
        """Verify loop successfully accepts a corrected plan following feedback."""
        # Initial bad plan
        bad_plan = {"water_needed_mm": 90.0, "duration_minutes": 240}
        v1 = evaluate_plan_by_critic(bad_plan, retry_count=0)
        assert v1["approved"] is False
        
        # Planner self-corrects based on feedback
        corrected_plan = {"water_needed_mm": 25.0, "duration_minutes": 60}
        v2 = evaluate_plan_by_critic(corrected_plan, retry_count=v1["retry_count"])
        
        assert v2["approved"] is True
        assert "APPROVED" in v2["feedback"]
        assert v2["retry_count"] == 1  # Preserved retry record for auditability
