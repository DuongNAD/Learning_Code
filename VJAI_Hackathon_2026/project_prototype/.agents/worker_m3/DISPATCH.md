## 2026-09-08T07:08:47Z
You are Milestone 3 Worker for AgriCarbon Agent (Vietnam Japan AI Hackathon 2026).
Working Directory: d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\worker_m3
Parent: Project Orchestrator (Conversation ID: 9ed17e46-bddf-44f6-9b7f-776ff56dd363)

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

MANDATORY INSTRUCTIONS:
1. Read `d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\ORIGINAL_REQUEST.md` and `d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\PROJECT.md`.
2. Implement production-grade FastAPI backend and Streamlit web interface:
   - `backend/app/__init__.py`, `backend/app/main.py`
   - `backend/app/api/__init__.py`, `backend/app/api/routes.py`
   - `backend/app/schemas/__init__.py`, `backend/app/schemas/models.py`
   - `backend/app/services/__init__.py`, `backend/app/services/engine_service.py`
   - `frontend/app.py`, `frontend/components/thought_stream.py`, `metrics_dashboard.py`, `esg_exporter.py`
3. Ensure:
   - FastAPI server boots cleanly without dependency errors.
   - `/healthz` returns `{"status": "ok", ...}`.
   - `/api/v1/demo/{preset_id}` responds in < 5.0 seconds using pre-cached telemetry and graph execution.
   - `/api/v1/agent/stream` streams 7 SSE event types (`thought`, `tool_call`, `tool_result`, `reflection`, `token`, `complete`, `error`).
   - Streamlit frontend displays real-time agent thought streaming feed, interactive gauges, and bilingual (VN/JA) ESG certificate export.
4. Write tests in `tests/test_backend_m3.py` and execute:
   - `py -m pytest tests/test_backend_m3.py`
   - `py tests/e2e_runner.py --all`
   Verify 100% pass.
5. Write handoff report to `d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\worker_m3\handoff.md`.
6. Send completion message back to Parent (Conversation ID: 9ed17e46-bddf-44f6-9b7f-776ff56dd363).
