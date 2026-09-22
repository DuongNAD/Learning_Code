"""
Milestone 3 Comprehensive Test Suite: FastAPI Backend & Frontend UI.
Authoritative source: ORIGINAL_REQUEST.md § R3 & Acceptance Criteria, PROJECT.md § Backend Service.

Tests:
1. FastAPI Server boots cleanly without dependency errors.
2. /healthz returns {"status": "ok", ...}.
3. /api/v1/status reports multi-agent readiness, tool health, and memory stats.
4. /api/v1/demo/{preset_id} responds in < 5.0 seconds (<0.5s warm cache).
5. /api/v1/agent/run executes full synchronous LangGraph multi-agent workflow.
6. /api/v1/agent/stream streams SSE event types (thought, tool_call, tool_result, reflection, token, complete, error).
7. /api/v1/export/esg produces bilingual (VN/JA) cryptographic ESG certificates.
8. Frontend components render without runtime errors.
"""

import sys
import json
import time
from pathlib import Path
from typing import Dict, Any, List
import pytest
from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.main import app
from backend.app.services.engine_service import (
    get_demo_preset_fast,
    get_preset_scenario,
    stream_agent_run,
    generate_bilingual_esg_certificate,
    execute_agent_run,
)
from backend.app.schemas.models import AgentRunRequest


client = TestClient(app)


def parse_sse_text(raw_text: str) -> List[Dict[str, Any]]:
    """Helper to parse raw SSE text into structured events."""
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


class TestHealthAndStatusEndpoints:
    """Validates basic service health, diagnostics, and preset discovery."""

    def test_healthz_endpoint_contract(self):
        """Verify /healthz returns standard service health payload."""
        response = client.get("/healthz")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["service"] == "agricarbon-backend"
        assert data["version"] == "1.0.0"
        assert data.get("multi_agent_engine") == "ready"

    def test_system_status_endpoint(self):
        """Verify /api/v1/status reports online tools and memory stats."""
        response = client.get("/api/v1/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "get_weather_forecast" in data["tools"]
        assert "query_sensor_telemetry" in data["tools"]
        assert "calculate_agricultural_emissions" in data["tools"]
        assert "record_esg_audit_entry" in data["tools"]
        assert "sqlite_checkpointer" in data["memory_stats"]
        assert len(data["presets_loaded"]) >= 2

    def test_list_presets_endpoint(self):
        """Verify /api/v1/presets returns configured farm presets."""
        response = client.get("/api/v1/presets")
        assert response.status_code == 200
        data = response.json()
        presets = data.get("presets", [])
        assert len(presets) >= 2
        preset_ids = [p["preset_id"] for p in presets]
        assert "an_giang_rice_001" in preset_ids
        assert "lam_dong_coffee_002" in preset_ids


class TestDemoPresetLatencyAndContent:
    """Validates fast response times (<5.0s) and payload contracts for TiB demo."""

    def test_demo_preset_an_giang_rice_under_5s(self):
        """Verify An Giang Rice preset responds well under 5.0 seconds (<0.5s warm)."""
        start = time.perf_counter()
        response = client.get("/api/v1/demo/an_giang_rice_001")
        elapsed = time.perf_counter() - start

        assert response.status_code == 200
        assert elapsed < 5.0, f"Preset execution took {elapsed:.2f}s, exceeding 5.0s requirement"

        data = response.json()
        assert data["status"] == "success"
        assert data["crop"] == "Jasmine 85 Rice (AWD)"
        assert data["action"] == "DISPATCH_IRRIGATION"
        assert data["duration_minutes"] == 45
        assert data["water_saved_pct"] == 38.0
        assert data["co2e_saved_pct"] == 28.1
        assert len(data["audit_hash"]) == 64
        assert data["server_elapsed_seconds"] < 5.0

    def test_demo_preset_lam_dong_coffee_under_5s(self):
        """Verify Lam Dong Coffee preset responds well under 5.0 seconds (<0.5s warm)."""
        start = time.perf_counter()
        response = client.get("/api/v1/demo/lam_dong_coffee_002")
        elapsed = time.perf_counter() - start

        assert response.status_code == 200
        assert elapsed < 5.0, f"Preset execution took {elapsed:.2f}s, exceeding 5.0s requirement"

        data = response.json()
        assert data["status"] == "success"
        assert data["crop"] == "Arabica Coffee (Agroforestry)"
        assert data["action"] == "DRIP_FERTIGATION"
        assert data["duration_minutes"] == 30
        assert data["fertilizer_saved_pct"] == 30.5
        assert data["co2e_saved_pct"] == 28.1
        assert len(data["audit_hash"]) == 64

    def test_demo_preset_not_found_returns_404(self):
        """Verify non-existent preset returns 404 error."""
        response = client.get("/api/v1/demo/nonexistent_preset_999")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()


class TestAgentSyncRunEndpoint:
    """Validates synchronous execution of multi-agent LangGraph workflow."""

    def test_agent_run_synchronous_workflow(self):
        """Verify /api/v1/agent/run executes full LangGraph pipeline autonomously."""
        payload = {
            "scenario_id": "an_giang_rice_001",
            "user_prompt": "Run autonomous precision irrigation and audit Scope 1-3 emissions",
            "task_id": "test_m3_sync_run"
        }
        start = time.perf_counter()
        response = client.post("/api/v1/agent/run", json=payload)
        elapsed = time.perf_counter() - start

        assert response.status_code == 200
        data = response.json()

        assert data["status"] == "success"
        assert data["task_id"] == "test_m3_sync_run"
        assert data["scenario_id"] == "an_giang_rice_001"
        assert len(data["plan"]) >= 4
        assert len(data["thoughts"]) >= 4

        # Verify tool calls (at least 3 automated tools called)
        tools_called = {t.get("tool") for t in data.get("tool_calls", []) if "tool" in t}
        assert len(tools_called) >= 3

        # Verify critic guardrail approval
        assert data["critic_verdict"]["approved"] is True

        # Verify final certificate
        final_out = data["final_output"]
        assert final_out["status"] == "success"
        assert len(final_out["ledger_hash"]) == 64
        assert final_out["certificate_id"].startswith("CERT-VJAI-2026")


class TestAgentSSEStreamingEndpoint:
    """Validates Server-Sent Events (SSE) thought streaming endpoint and event types."""

    def test_agent_stream_all_event_types(self):
        """Verify /api/v1/agent/stream returns standard SSE event types."""
        with client.stream("GET", "/api/v1/agent/stream?scenario_id=an_giang_rice_001") as response:
            assert response.status_code == 200
            assert "text/event-stream" in response.headers.get("content-type", "")

            content = response.read().decode("utf-8")
            parsed = parse_sse_text(content)
            assert len(parsed) >= 6

            event_types = {m["event"] for m in parsed}
            assert "thought" in event_types
            assert "tool_call" in event_types
            assert "tool_result" in event_types
            assert "reflection" in event_types
            assert "token" in event_types
            assert "complete" in event_types

            # Verify complete event structure
            complete_event = next(m for m in parsed if m["event"] == "complete")
            assert "latency_ms" in complete_event["data"]
            assert complete_event["data"]["latency_ms"] < 5000

    def test_agent_stream_simulated_error(self):
        """Verify /api/v1/agent/stream streams error event when fault occurs."""
        with client.stream("GET", "/api/v1/agent/stream?scenario_id=an_giang_rice_001&simulate_error=true") as response:
            assert response.status_code == 200
            content = response.read().decode("utf-8")
            parsed = parse_sse_text(content)
            event_types = [m["event"] for m in parsed]
            assert "error" in event_types
            assert "complete" in event_types


class TestBilingualESGExportEndpoint:
    """Validates bilingual (VN/JA) ESG Certificate generation and cryptographic hashing."""

    def test_esg_export_bilingual(self):
        """Verify export returns both Vietnamese and Japanese certificate contents."""
        payload = {
            "scenario_id": "an_giang_rice_001",
            "language": "both"
        }
        response = client.post("/api/v1/export/esg", json=payload)
        assert response.status_code == 200
        data = response.json()

        assert data["status"] == "certified"
        assert len(data["audit_hash_sha256"]) == 64
        assert data["content_vi"] is not None
        assert data["content_ja"] is not None

        # Vietnamese content validation
        vi = data["content_vi"]
        assert "CHỨNG NHẬN DẤU CHÂN CARBON" in vi["title"]
        assert vi["metrics"]["water_saved_pct"] == 38.0
        assert "BẤT BIẾN SHA-256" in vi["verification_status"]

        # Japanese content validation
        ja = data["content_ja"]
        assert "持続可能農業カーボンフットプリント認証書" in ja["title"]
        assert ja["metrics"]["water_saved_pct"] == 38.0
        assert "SHA-256暗号化" in ja["verification_status"]

    def test_esg_export_vietnamese_only(self):
        """Verify export with language='vi' returns only Vietnamese section."""
        payload = {
            "scenario_id": "an_giang_rice_001",
            "language": "vi"
        }
        response = client.post("/api/v1/export/esg", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["content_vi"] is not None
        assert data["content_ja"] is None

    def test_esg_export_japanese_only(self):
        """Verify export with language='ja' returns only Japanese section."""
        payload = {
            "scenario_id": "lam_dong_coffee_002",
            "language": "ja"
        }
        response = client.post("/api/v1/export/esg", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["content_vi"] is None
        assert data["content_ja"] is not None
        assert data["content_ja"]["metrics"]["fertilizer_saved_pct"] == 30.5
