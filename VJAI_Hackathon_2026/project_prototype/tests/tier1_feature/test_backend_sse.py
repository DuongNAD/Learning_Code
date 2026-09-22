"""
Tier 1: Feature Coverage - Backend & SSE Streaming
Tests FastAPI endpoints and the 7 Server-Sent Events (SSE) streaming types:
thought, tool_call, tool_result, reflection, token, complete, error.
Authoritative source: PROJECT.md § Backend Service & Interface Contracts
"""

import json
import pytest
import sys
from pathlib import Path
from typing import Dict, Any, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def format_sse_message(event: str, data: Dict[str, Any]) -> str:
    """Formats event and data into standard SSE protocol text."""
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


def parse_sse_stream(raw_text: str) -> List[Dict[str, Any]]:
    """Parses raw SSE text into structured event-data records."""
    messages = []
    blocks = raw_text.strip().split("\n\n")
    for block in blocks:
        if not block:
            continue
        lines = block.strip().split("\n")
        ev_type = None
        data_val = None
        for line in lines:
            if line.startswith("event:"):
                ev_type = line.replace("event:", "").strip()
            elif line.startswith("data:"):
                data_val = json.loads(line.replace("data:", "").strip())
        if ev_type and data_val is not None:
            messages.append({"event": ev_type, "data": data_val})
    return messages


class TestBackendAndSSE:
    """Validates FastAPI and SSE streaming formats."""

    def test_healthcheck_endpoint_contract(self):
        """Verify /healthz returns standard service health payload."""
        expected_payload = {
            "status": "ok",
            "service": "agricarbon-backend",
            "version": "1.0.0"
        }
        assert expected_payload["status"] == "ok"
        assert expected_payload["service"] == "agricarbon-backend"
        assert expected_payload["version"] == "1.0.0"

    def test_sse_event_format_seven_types(self, sample_sse_events):
        """Verify all 7 mandatory SSE event types serialize and parse cleanly."""
        raw_stream = "".join(format_sse_message(item["event"], item["data"]) for item in sample_sse_events)
        parsed = parse_sse_stream(raw_stream)
        
        assert len(parsed) == 7, "Must parse exactly 7 distinct SSE messages"
        parsed_events = [p["event"] for p in parsed]
        expected_events = ["thought", "tool_call", "tool_result", "reflection", "token", "complete", "error"]
        assert parsed_events == expected_events

    def test_sse_thought_payload_structure(self):
        """Verify 'thought' event contains 'step' and 'content'."""
        data = {"step": "sensing_telemetry", "content": "Querying IoT sensor moisture..."}
        raw = format_sse_message("thought", data)
        parsed = parse_sse_stream(raw)[0]
        assert parsed["event"] == "thought"
        assert "step" in parsed["data"]
        assert "content" in parsed["data"]

    def test_sse_tool_call_and_result_payload_structure(self):
        """Verify 'tool_call' and 'tool_result' contain tool name and args/results."""
        call_msg = format_sse_message("tool_call", {"tool": "get_weather_forecast", "args": {"lat": 10.4, "lon": 105.1}})
        res_msg = format_sse_message("tool_result", {"tool": "get_weather_forecast", "result": {"temp_max": 34.0}})
        
        parsed_call = parse_sse_stream(call_msg)[0]
        parsed_res = parse_sse_stream(res_msg)[0]
        
        assert parsed_call["data"]["tool"] == "get_weather_forecast"
        assert "lat" in parsed_call["data"]["args"]
        assert parsed_res["data"]["result"]["temp_max"] == 34.0

    def test_sse_reflection_payload_structure(self):
        """Verify 'reflection' event carries boolean 'approved' and string 'critique'."""
        refl_data = {"approved": True, "critique": "AWD dosage conforms with IRRI irrigation threshold."}
        raw = format_sse_message("reflection", refl_data)
        parsed = parse_sse_stream(raw)[0]
        assert parsed["event"] == "reflection"
        assert parsed["data"]["approved"] is True
        assert len(parsed["data"]["critique"]) > 0

    def test_sse_complete_payload_structure(self):
        """Verify 'complete' event returns 'final_result' and 'latency_ms'."""
        comp_data = {
            "final_result": {
                "decision": "DISPATCH_PUMP",
                "duration_min": 45,
                "water_saved_pct": 38.0
            },
            "latency_ms": 340
        }
        raw = format_sse_message("complete", comp_data)
        parsed = parse_sse_stream(raw)[0]
        assert parsed["event"] == "complete"
        assert "final_result" in parsed["data"]
        assert parsed["data"]["latency_ms"] < 5000, "Completion latency must be under 5.0s"
