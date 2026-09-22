"""
FastAPI Routes for AgriCarbon Multi-Agent Platform.
Implements REST endpoints and SSE Thought Streaming.
Authoritative source: PROJECT.md § Backend Service & Interface Contracts
"""

from typing import Optional, Dict, Any, List
from fastapi import APIRouter, HTTPException, Query, status
from fastapi.responses import StreamingResponse

from backend.app.schemas.models import (
    HealthResponse,
    AgentRunRequest,
    AgentRunResponse,
    DemoPresetResponse,
    SystemStatusResponse,
    ESGExportRequest,
    ESGExportResponse,
)
from backend.app.services.engine_service import (
    execute_agent_run,
    stream_agent_run,
    get_demo_preset_fast,
    get_system_status,
    generate_bilingual_esg_certificate,
    get_preset_scenario,
    _PRESET_CACHE,
)

router = APIRouter()


@router.get(
    "/healthz",
    response_model=HealthResponse,
    summary="Service Healthcheck",
    tags=["System"]
)
def healthcheck():
    """
    Returns the microservice health status conforming to PROJECT.md:
    {"status": "ok", "service": "agricarbon-backend", "version": "1.0.0"}
    """
    return HealthResponse(
        status="ok",
        service="agricarbon-backend",
        version="1.0.0",
        multi_agent_engine="ready"
    )


@router.get(
    "/api/v1/status",
    response_model=SystemStatusResponse,
    summary="System and Multi-Agent Engine Status",
    tags=["System"]
)
def system_status():
    """Returns runtime health of tools, checkpointers, and preset scenarios."""
    return get_system_status()


@router.get(
    "/api/v1/presets",
    summary="List Available Farm Presets",
    tags=["Demo Presets"]
)
def list_presets():
    """Returns metadata for all pre-configured demo scenarios."""
    return {
        "presets": [
            {
                "preset_id": "an_giang_rice_001",
                "title": "An Giang Jasmine 85 AWD Rice Polder (5.0 ha)",
                "province": "An Giang",
                "crop": "Jasmine 85 Rice",
                "water_saving_target": "38.0%",
                "co2e_saving_target": "28.1%"
            },
            {
                "preset_id": "lam_dong_coffee_002",
                "title": "Cau Dat Arabica Agroforestry Estate (3.2 ha)",
                "province": "Lam Dong",
                "crop": "Arabica Coffee",
                "fertilizer_saving_target": "30.5%",
                "co2e_saving_target": "28.1%"
            }
        ]
    }


@router.get(
    "/api/v1/demo/{preset_id}",
    response_model=DemoPresetResponse,
    summary="Instant Cached Demo Preset Execution (<5.0s)",
    tags=["Demo Presets"]
)
def demo_preset(preset_id: str):
    """
    Ultra-fast (<0.5s warm cache, guaranteed <5.0s) endpoint designed for stage demos.
    Retrieves pre-cached farm telemetry, agronomic calculations, and cryptographic ledger hash.
    """
    result = get_demo_preset_fast(preset_id)
    if result.get("status") == "error":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Preset scenario '{preset_id}' not found."
        )
    return DemoPresetResponse(**result)


@router.post(
    "/api/v1/agent/run",
    response_model=AgentRunResponse,
    summary="Synchronous Autonomous Multi-Agent Execution",
    tags=["Multi-Agent Engine"]
)
def agent_run(request: AgentRunRequest):
    """
    Executes the full LangGraph multi-agent workflow:
    Supervisor -> Sensing -> Dispatch -> Carbon Auditor -> Critic Guardrails.
    """
    try:
        response = execute_agent_run(request)
        return response
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent workflow execution error: {str(exc)}"
        )


@router.get(
    "/api/v1/agent/stream",
    summary="Real-time Server-Sent Events (SSE) Thought Streaming",
    tags=["Multi-Agent Engine"]
)
def agent_stream(
    scenario_id: str = Query("an_giang_rice_001", description="Preset scenario ID"),
    prompt: Optional[str] = Query(None, description="Custom agronomist prompt"),
    task_id: Optional[str] = Query(None, description="Execution tracing task ID"),
    simulate_error: bool = Query(False, description="Simulate fault injection for resilience verification")
):
    """
    Streams multi-agent reasoning progression in real-time across 7 SSE event types:
    - thought: Reasoning progression
    - tool_call: Tool invocation with arguments
    - tool_result: Tool output / execution data
    - reflection: Critic approval / critique feedback
    - token: Streamed explanation tokens
    - complete: Final verified result & latency
    - error: Error or circuit breaker alerts
    """
    generator = stream_agent_run(
        scenario_id=scenario_id,
        prompt=prompt,
        task_id=task_id,
        simulate_error=simulate_error
    )
    return StreamingResponse(
        generator,
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
            "Content-Type": "text/event-stream"
        }
    )


@router.post(
    "/api/v1/export/esg",
    response_model=ESGExportResponse,
    summary="Generate Bilingual (VN/JA) ESG Carbon Certificate",
    tags=["ESG Audit"]
)
def export_esg_certificate(request: ESGExportRequest):
    """
    Generates cryptographic tamper-evident ESG carbon footprint certification
    in Vietnamese, Japanese, or bilingual format for Tokyo Green Transformation (GX) compliance.
    """
    return generate_bilingual_esg_certificate(
        scenario_id=request.scenario_id,
        language=request.language,
        producer_name=request.producer_name,
        batch_code=request.batch_code
    )
