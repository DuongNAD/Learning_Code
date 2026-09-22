"""
Safety Guardrails & Self-Correction Critic Agent.
Performs independent verification of agronomic physical boundaries,
schema integrity, and pump motor safety limits.
Implements Reflexion self-correction loop (max 3 retries) and circuit breaker.
Conforms strictly to PROJECT.md § Multi-Agent Engine and ORIGINAL_REQUEST.md § Acceptance Criteria.
"""

import math
from typing import Dict, Any, Optional
from core.agents.state import AgentState


def evaluate_plan_by_critic(dispatch_plan: Dict[str, Any], retry_count: int = 0) -> Dict[str, Any]:
    """
    Evaluates dispatch plan against deterministic agronomic safety boundaries.

    Checks:
        1. Schema validation: dispatch_plan must be a non-null dictionary.
        2. Numeric type validation: rejects None, boolean, NaN, and unparsable strings.
        3. Physical water boundaries: 0.0 <= water_needed_mm <= 60.0mm (FAO-56 limit).
        4. Mandatory field presence: 'duration_minutes' must be present.
        5. Physical duration boundaries: 0 <= duration_minutes <= 480 mins (8h motor safety).

    Returns:
        Dict with:
            approved (bool), retry_count (int), feedback (str)
    """
    if not isinstance(dispatch_plan, dict):
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: Dispatch plan must be a valid dictionary structure."
        }

    # 1. Water Needed Sanitization & Bounds
    raw_water = dispatch_plan.get("water_needed_mm", 0.0)
    if raw_water is None or isinstance(raw_water, bool):
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: 'water_needed_mm' must be a valid non-boolean numeric value."
        }

    try:
        water_mm = float(raw_water)
    except (ValueError, TypeError, OverflowError):
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": f"REJECT: Invalid non-numeric water dosage '{raw_water}'."
        }

    if math.isnan(water_mm) or math.isinf(water_mm):
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: 'water_needed_mm' cannot be NaN or Infinite."
        }

    if water_mm < 0.0:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": f"REJECT: Negative water dosage {water_mm}mm violates physical boundary (water_needed_mm >= 0.0)."
        }

    if water_mm > 60.0:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": f"REJECT: Water dosage {water_mm}mm violates FAO-56 maximum single-event limit (60mm). Reduce duration."
        }

    # 2. Duration Minutes Mandatory Presence & Bounds
    if "duration_minutes" not in dispatch_plan:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: Dispatch plan missing mandatory 'duration_minutes' field."
        }

    raw_duration = dispatch_plan.get("duration_minutes")
    if raw_duration is None or isinstance(raw_duration, bool):
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: 'duration_minutes' must be a valid non-boolean numeric value."
        }

    try:
        duration = int(round(float(raw_duration)))
    except (ValueError, TypeError, OverflowError):
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": f"REJECT: Invalid non-numeric pump duration '{raw_duration}'."
        }

    if duration < 0:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": f"REJECT: Negative pump duration {duration} minutes violates physical boundary (duration_minutes >= 0)."
        }

    if duration > 480:
        return {
            "approved": False,
            "retry_count": retry_count + 1,
            "feedback": "REJECT: Continuous pumping over 8 hours risks pump motor burnout. Split into shifts."
        }

    # All safety criteria satisfied
    return {
        "approved": True,
        "retry_count": retry_count,
        "feedback": "APPROVED: Plan within safe agronomic boundaries."
    }


def critic_agent_node(state: AgentState) -> AgentState:
    """
    Safety Critic Node:
    Audits the current dispatch plan, updates the verdict, and manages
    the retry counter and circuit breaker.
    """
    dispatch_plan = state.get("dispatch_plan", {})
    prior_verdict = state.get("critic_verdict", {})
    current_retry = int(prior_verdict.get("retry_count", 0))

    verdict = evaluate_plan_by_critic(dispatch_plan=dispatch_plan, retry_count=current_retry)
    state["critic_verdict"] = verdict
    state["current_step"] = state.get("current_step", 0) + 1

    # Thought / Reflection logging
    state["thoughts"].append({
        "agent": "SafetyCritic",
        "step": "critic_review",
        "critique": verdict["feedback"],
        "approved": verdict["approved"],
        "retry_count": verdict["retry_count"]
    })

    # Circuit breaker handling if retry count >= 3
    if not verdict["approved"] and verdict["retry_count"] >= 3:
        abort_msg = "Circuit breaker triggered after 3 retries: SAFE_ABORT_OPERATOR_NOTIFIED. Defaulting to safe fallback."
        state["errors"].append(abort_msg)
        state["thoughts"].append({
            "agent": "SafetyCritic",
            "step": "circuit_breaker",
            "thought": abort_msg
        })

    return state
