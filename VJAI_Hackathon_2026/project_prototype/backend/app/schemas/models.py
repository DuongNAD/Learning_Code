"""
Pydantic v2 Models and Schemas for AgriCarbon FastAPI Backend.
Authoritative source: PROJECT.md § Backend Service & Interface Contracts
"""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Healthcheck response model for /healthz."""
    status: str = Field(default="ok", description="Service health status")
    service: str = Field(default="agricarbon-backend", description="Microservice name")
    version: str = Field(default="1.0.0", description="API Version")
    multi_agent_engine: str = Field(default="ready", description="LangGraph engine status")
    timestamp: Optional[str] = Field(default=None, description="Current server ISO timestamp")


class AgentRunRequest(BaseModel):
    """Request payload for synchronous multi-agent execution."""
    scenario_id: str = Field(default="an_giang_rice_001", description="Preset or custom scenario identifier")
    user_prompt: Optional[str] = Field(
        default="Autonomous precision irrigation and ESG carbon footprint audit",
        description="Farmer or agronomist execution command"
    )
    task_id: Optional[str] = Field(default=None, description="Unique execution tracing ID")
    crop_info: Optional[Dict[str, Any]] = Field(default=None, description="Optional crop override parameters")


class AgentRunResponse(BaseModel):
    """Response payload returning autonomous execution results."""
    task_id: str
    scenario_id: str
    status: str = Field(description="Execution outcome: success | safe_abort | error")
    execution_time_ms: int = Field(description="Total server wall clock latency in milliseconds")
    plan: List[str] = Field(default_factory=list, description="Supervisor decomposed subtasks")
    thoughts: List[Dict[str, Any]] = Field(default_factory=list, description="Agent ReAct thoughts")
    tool_calls: List[Dict[str, Any]] = Field(default_factory=list, description="Tool invocation logs")
    weather_data: Dict[str, Any] = Field(default_factory=dict, description="Ambient weather & ET0")
    sensor_telemetry: Dict[str, Any] = Field(default_factory=dict, description="IoT sensor readings")
    dispatch_plan: Dict[str, Any] = Field(default_factory=dict, description="Irrigation & fertilizer dispatch")
    carbon_report: Dict[str, Any] = Field(default_factory=dict, description="Scope 1-3 carbon footprint")
    critic_verdict: Dict[str, Any] = Field(default_factory=dict, description="Guardrails verification")
    final_output: Dict[str, Any] = Field(default_factory=dict, description="Synthesized decision and certificate")
    errors: List[str] = Field(default_factory=list, description="Captured errors or warnings")


class DemoPresetResponse(BaseModel):
    """High-speed response model (<5.0s) for Tokyo Innovation Base stage demo."""
    preset_id: str
    crop: str
    action: str
    duration_minutes: int
    water_saved_pct: Optional[float] = None
    fertilizer_saved_pct: Optional[float] = None
    co2e_saved_pct: float
    audit_hash: str
    status: str = "success"
    server_elapsed_seconds: float
    summary: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


class SystemStatusResponse(BaseModel):
    """Comprehensive system diagnostics for /api/v1/status."""
    status: str = "ok"
    service: str = "agricarbon-backend"
    version: str = "1.0.0"
    tools: Dict[str, str] = Field(default_factory=dict, description="Automated tool statuses")
    memory_stats: Dict[str, Any] = Field(default_factory=dict, description="Short-term & vector store stats")
    presets_loaded: List[str] = Field(default_factory=list, description="Available cached scenario presets")


class SSEEventPayload(BaseModel):
    """Standard Server-Sent Event wrapper payload."""
    event: str = Field(description="SSE event name (thought|tool_call|tool_result|reflection|token|complete|error)")
    data: Dict[str, Any] = Field(description="JSON data dictionary")


class ESGExportRequest(BaseModel):
    """Request payload for bilingual ESG Carbon Certificate export."""
    scenario_id: str = "an_giang_rice_001"
    language: str = Field(default="both", description="Target language: vi | ja | both")
    producer_name: Optional[str] = None
    batch_code: Optional[str] = None


class ESGExportResponse(BaseModel):
    """Bilingual ESG Carbon Certificate export response."""
    certificate_id: str
    standard: str
    issuing_entity: str
    timestamp: str
    audit_hash_sha256: str
    language: str
    content_vi: Optional[Dict[str, Any]] = None
    content_ja: Optional[Dict[str, Any]] = None
    status: str = "certified"
