"""
Supervisor Orchestrator Node.
Performs ReAct task decomposition, intent dispatch, dynamic worker routing,
and final state synthesis with SHA-256 ESG audit ledger commitment.
Conforms strictly to PROJECT.md § Multi-Agent Engine and ORIGINAL_REQUEST.md § R2.
"""

from typing import Dict, Any, List
from core.agents.state import AgentState
from core.tools.ledger_tool import record_esg_audit_entry, _SESSION_LEDGER


def supervisor_node(state: AgentState) -> AgentState:
    """
    Supervisor Node:
    Monitors progress against execution plan, manages worker transitions,
    and seals the cryptographic ESG ledger upon approval.
    """
    # 1. Initialize or maintain task decomposition plan
    if not state.get("plan"):
        state["plan"] = [
            "1. Sense ambient weather and soil telemetry",
            "2. Optimize irrigation and fertigation schedule",
            "3. Audit carbon footprint (Scope 1-3)",
            "4. Validate agronomic guardrails via Critic",
            "5. Commit SHA-256 ESG audit entry"
        ]

    critic_verdict = state.get("critic_verdict") or {}
    approved = critic_verdict.get("approved", False)
    retries = critic_verdict.get("retry_count", 0)

    # 2. Final Synthesis when plan is approved or circuit breaker tripped
    if approved:
        # Commit Tool 4: record_esg_audit_entry
        task_id = state.get("task_id", "task_001")
        farm_id = state.get("crop_info", {}).get("farm_id", state.get("scenario_id", "farm_001"))
        crop_type = state.get("crop_info", {}).get("crop_type", "rice_jasmine_85")
        carbon_co2e = float(state.get("carbon_report", {}).get("total_co2e_kg", 12.8))

        prev_hash = (
            state.get("crop_info", {}).get("prev_hash")
            or _SESSION_LEDGER.latest_entry.entry_hash
        )

        ledger_entry = record_esg_audit_entry(
            record_id=f"rec_{task_id}",
            farm_id=farm_id,
            action="precision_irrigation_optimization",
            co2e_kg=carbon_co2e,
            prev_hash=prev_hash,
            crop_type=crop_type,
            metadata={
                "water_needed_mm": state.get("dispatch_plan", {}).get("water_needed_mm"),
                "duration_minutes": state.get("dispatch_plan", {}).get("duration_minutes"),
                "reduction_pct": state.get("carbon_report", {}).get("reduction_pct")
            }
        )
        state["tool_calls"].append({
            "tool": "record_esg_audit_entry",
            "args": {"record_id": f"rec_{task_id}", "farm_id": farm_id, "co2e_kg": carbon_co2e},
            "result": {"hash": ledger_entry["hash"], "certificate_id": ledger_entry["certificate_id"]}
        })

        state["final_output"] = {
            "status": "success",
            "task_id": task_id,
            "scenario_id": state.get("scenario_id"),
            "dispatch": state.get("dispatch_plan"),
            "carbon": state.get("carbon_report"),
            "critic": critic_verdict,
            "ledger_entry": ledger_entry,
            "ledger_hash": ledger_entry["hash"],
            "certificate_id": ledger_entry["certificate_id"]
        }

        thought_msg = (
            f"All worker subtasks verified and approved by Critic. "
            f"Committed SHA-256 ESG audit entry (Hash: {ledger_entry['hash'][:16]}...). "
            f"Workflow successfully completed."
        )
        state["thoughts"].append({
            "agent": "SupervisorOrchestrator",
            "step": "final_synthesis",
            "thought": thought_msg
        })

    elif retries >= 3:
        # Circuit breaker terminal fallback
        state["final_output"] = {
            "status": "safe_abort",
            "action": "HALT_PUMP_AND_ALERT_OPERATOR",
            "retry_count": retries,
            "reason": "Max retries (3) reached without passing Critic guardrails."
        }
        state["thoughts"].append({
            "agent": "SupervisorOrchestrator",
            "step": "circuit_breaker_terminal",
            "thought": "Terminal circuit breaker activated: halted pumping and alerted human operator."
        })

    else:
        # In-progress supervisor assessment
        step_num = state.get("current_step", 0)
        thought_msg = f"Supervisor evaluated progress at step {step_num}. Routing to next specialist worker."
        state["thoughts"].append({
            "agent": "SupervisorOrchestrator",
            "step": "plan_coordination",
            "thought": thought_msg
        })

    return state


def route_supervisor_decision(state: AgentState) -> str:
    """
    Conditional routing function determining the next execution node.
    """
    # Check 1: Has sensing run?
    if not state.get("weather_data") or not state.get("sensor_telemetry"):
        return "sensing_agent"

    # Check 2: Has dispatch run?
    if not state.get("dispatch_plan"):
        return "dispatch_agent"

    # Check 3: Has carbon auditing run?
    if not state.get("carbon_report"):
        return "carbon_agent"

    # Check 4: Has critic evaluated?
    verdict = state.get("critic_verdict") or {}
    if not verdict.get("feedback"):
        # First time reaching critic
        return "critic_agent"

    # Check 5: Reflexion loop if critic rejected
    if not verdict.get("approved", False):
        if verdict.get("retry_count", 0) < 3:
            # Reflexion retry: loop back to dispatch_agent to adjust parameters
            return "dispatch_agent"
        else:
            # Circuit breaker exceeded max retries
            return "FINISH"

    # Plan approved: conclude execution
    return "FINISH"
