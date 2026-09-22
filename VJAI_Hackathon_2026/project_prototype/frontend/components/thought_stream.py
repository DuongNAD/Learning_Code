"""
Streamlit UI Component: Real-Time Agent Thought Stream.
Visualizes the 7 Server-Sent Event (SSE) types in real-time:
thought, tool_call, tool_result, reflection, token, complete, error.
Authoritative source: PROJECT.md § Frontend Web UI & Interface Contracts
"""

import json
from typing import Dict, Any, List
import streamlit as st


EVENT_ICONS = {
    "thought": "🧠",
    "tool_call": "🛠️",
    "tool_result": "📥",
    "reflection": "🛡️",
    "token": "⚡",
    "complete": "✅",
    "error": "⚠️",
}

EVENT_COLORS = {
    "thought": "#2b6cb0",
    "tool_call": "#d69e2e",
    "tool_result": "#319795",
    "reflection": "#805ad5",
    "token": "#4a5568",
    "complete": "#38a169",
    "error": "#e53e3e",
}


def render_thought_event(event_type: str, data: Dict[str, Any]):
    """Renders a single SSE event item into the Streamlit feed."""
    icon = EVENT_ICONS.get(event_type, "📌")
    color = EVENT_COLORS.get(event_type, "#4a5568")

    if event_type == "thought":
        step = data.get("step", "reasoning").upper()
        content = data.get("content", "")
        st.markdown(
            f"""
            <div style="border-left: 4px solid {color}; padding: 8px 12px; margin-bottom: 8px; background: rgba(43, 108, 176, 0.05); border-radius: 4px;">
                <strong style="color: {color};">{icon} THOUGHT [{step}]:</strong>
                <div style="margin-top: 4px; color: #2d3748; font-size: 14px;">{content}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif event_type == "tool_call":
        tool_name = data.get("tool", "unknown_tool")
        args = data.get("args", {})
        st.markdown(
            f"""
            <div style="border-left: 4px solid {color}; padding: 8px 12px; margin-bottom: 8px; background: rgba(214, 158, 46, 0.05); border-radius: 4px;">
                <strong style="color: {color};">{icon} TOOL CALL: <code>{tool_name}</code></strong>
                <pre style="margin-top: 4px; font-size: 12px; background: #f7fafc; padding: 6px; border-radius: 4px;">{json.dumps(args, indent=2)}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif event_type == "tool_result":
        tool_name = data.get("tool", "unknown_tool")
        res = data.get("result", {})
        st.markdown(
            f"""
            <div style="border-left: 4px solid {color}; padding: 8px 12px; margin-bottom: 8px; background: rgba(49, 151, 149, 0.05); border-radius: 4px;">
                <strong style="color: {color};">{icon} TOOL RESULT: <code>{tool_name}</code></strong>
                <pre style="margin-top: 4px; font-size: 12px; background: #f7fafc; padding: 6px; border-radius: 4px;">{json.dumps(res, indent=2)}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif event_type == "reflection":
        approved = data.get("approved", False)
        critique = data.get("critique", "")
        retries = data.get("retry_count", 0)
        badge = "🟢 APPROVED" if approved else f"🔴 REJECTED (Retry {retries})"
        st.markdown(
            f"""
            <div style="border-left: 4px solid {color}; padding: 8px 12px; margin-bottom: 8px; background: rgba(128, 90, 213, 0.05); border-radius: 4px;">
                <strong style="color: {color};">{icon} CRITIC GUARDRAIL [{badge}]:</strong>
                <div style="margin-top: 4px; color: #2d3748; font-size: 14px; font-style: italic;">{critique}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif event_type == "token":
        chunk = data.get("chunk", "")
        st.markdown(
            f"""
            <div style="border-left: 4px solid {color}; padding: 6px 12px; margin-bottom: 8px; background: #f7fafc; border-radius: 4px;">
                <span style="color: #4a5568; font-size: 13px;">{icon} {chunk}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif event_type == "complete":
        final_res = data.get("final_result", {})
        latency = data.get("latency_ms", 0)
        st.markdown(
            f"""
            <div style="border-left: 4px solid {color}; padding: 12px; margin-bottom: 8px; background: rgba(56, 161, 105, 0.08); border-radius: 4px;">
                <strong style="color: {color}; font-size: 16px;">{icon} WORKFLOW COMPLETED ({latency} ms)</strong>
                <div style="margin-top: 6px; font-size: 14px;">Status: <strong>{data.get('status', 'success').upper()}</strong></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif event_type == "error":
        msg = data.get("message", "An unexpected error occurred.")
        st.error(f"{icon} ERROR / CIRCUIT BREAKER: {msg}")


def render_thought_stream(events: List[Dict[str, Any]]):
    """Renders a chronological list of thought stream events."""
    if not events:
        st.info("No agent thoughts yet. Trigger an execution to observe the live ReAct thought stream.")
        return

    st.markdown("### 🧠 Live Agent Thought Timeline (ReAct Loop)")
    for event in events:
        ev_type = event.get("event", "thought")
        ev_data = event.get("data", {})
        render_thought_event(ev_type, ev_data)
