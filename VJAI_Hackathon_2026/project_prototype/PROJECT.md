# Project: AgriCarbon Agent — Vietnam Japan AI Hackathon 2026

## Architecture
Autonomous Multi-Agent System for Precision Irrigation, Fertilizer Optimization, and Supply Chain Carbon Footprint Auditing (Scope 1-3) in Vietnam-Japan Agri-Export.

### System Components & Data Flow
1. **Domain Layer (`core/domain/`)**: Agronomic formulas (FAO-56 Penman-Monteith, IPCC Tier 1/2 GHG calculations, ESG ledger schema).
2. **Multi-Agent Engine (`core/agents/`)**:
   - **Supervisor Orchestrator Node**: ReAct planning, task routing, intent dispatch.
   - **SensingAndWeatherAgent**: Weather forecasts (Open-Meteo) & soil IoT telemetry analysis.
   - **ResourceEcoDispatchAgent**: Precision irrigation & fertilizer scheduling optimization.
   - **CarbonAuditorAgent**: Scope 1, 2, 3 carbon footprint calculation & SHA-256 audit ledger entry.
   - **SafetyAndGuardrailsCritic**: Self-reflection, agronomic boundary validation, fault injection handling, circuit breaker (<= 3 retries).
3. **Tools & Connectors (`core/tools/`)**:
   - `get_weather_forecast` (Open-Meteo API + offline cache adapter)
   - `query_sensor_telemetry` (IoT Sensor DB + synthetic farm telemetry generator)
   - `calculate_agricultural_emissions` (Deterministic IPCC Tier 1/2 GHG engine)
   - `record_esg_audit_entry` (Cryptographic SHA-256 tamper-evident ESG ledger)
4. **Memory Layer (`core/memory/`)**:
   - Short-term: LangGraph `SqliteSaver` thread checkpointer and context buffer.
   - Long-term: ChromaDB local vector store indexing FAO-56 guidelines, IPCC emission factors, and episodic reflection logs.
5. **Backend Service (`backend/`)**:
   - FastAPI server with lifespan management, CORS, structured logging.
   - SSE streaming endpoint: `/api/v1/agent/stream` (7 event types: thought, tool_call, tool_result, reflection, token, complete, error).
   - Preset demo endpoints (`/api/v1/demo/{preset_id}`) responding in <5.0 seconds.
   - Healthcheck: `/healthz`.
6. **Frontend Web UI (`frontend/`)**:
   - Streamlit interactive dashboard with real-time agent thought streaming feed, preset scenario selector, interactive sensor gauges, and bilingual (VN/JA) ESG carbon certificate export.
7. **Presentation & Stage Assets (`presentation/`)**:
   - 10-slide TiB Tokyo pitch deck (`pitch_deck.md`, `pitch_deck.html`).
   - 60-second backup video script & storyboard (`backup_demo_60s.md`).
   - TiB Judge Q&A Defense Playbook (`judge_qa_defense.md`).
8. **E2E Test Suite (`tests/`)**:
   - Tier 1: Feature Coverage tests.
   - Tier 2: Boundary & Corner Case tests.
   - Tier 3: Cross-Feature interaction tests.
   - Tier 4: Real-World Tokyo Stage Workload tests.
   - Tier 5: Adversarial stress testing.

## Code Layout
```
project_prototype/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py        # REST and SSE streaming endpoints
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── models.py        # Pydantic v2 request/response models
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── engine_service.py # Bridge between API and Multi-Agent Core
├── core/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── agronomy.py          # FAO-56 evapotranspiration & irrigation models
│   │   ├── carbon_models.py     # IPCC Tier 1/2 GHG emission calculation models
│   │   └── esg_ledger.py        # Cryptographic ESG audit entry schemas
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── state.py             # AgentState TypedDict definition
│   │   ├── supervisor.py        # Supervisor Orchestrator Node
│   │   ├── sensing_agent.py     # Weather & IoT sensing worker
│   │   ├── dispatch_agent.py    # Irrigation & fertilizer dispatch worker
│   │   ├── carbon_agent.py      # Carbon footprint auditing worker
│   │   ├── critic_agent.py      # Guardrails & self-reflection worker
│   │   └── graph.py             # LangGraph StateGraph builder & compiler
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── weather_tool.py      # get_weather_forecast tool
│   │   ├── telemetry_tool.py    # query_sensor_telemetry tool
│   │   ├── carbon_tool.py       # calculate_agricultural_emissions tool
│   │   ├── ledger_tool.py       # record_esg_audit_entry tool
│   │   └── mock_data.py         # Offline mock datasets for TiB demo resilience
│   └── memory/
│       ├── __init__.py
│       ├── short_term.py        # SQLite / Memory checkpointer
│       └── vector_store.py      # ChromaDB retrieval store for domain knowledge
├── frontend/
│   ├── app.py                   # Streamlit web application
│   └── components/
│       ├── __init__.py
│       ├── thought_stream.py    # Real-time thought rendering component
│       ├── metrics_dashboard.py # Water/Carbon/Cost gauge cards
│       └── esg_exporter.py      # Bilingual ESG report generator
├── presentation/
│   ├── pitch_deck.md            # 10-slide standard pitch deck
│   ├── pitch_deck.html          # Interactive slide presentation
│   ├── backup_demo_60s.md       # 60-second backup demo plan and script
│   └── judge_qa_defense.md      # Judge Q&A 30s defense playbook
├── tests/
│   ├── conftest.py
│   ├── e2e_runner.py            # Central E2E test runner CLI
│   ├── tier1_feature/           # Feature coverage tests
│   ├── tier2_boundary/          # Boundary and error-recovery tests
│   ├── tier3_pairwise/          # Cross-feature combination tests
│   ├── tier4_scenarios/         # Real-world TiB demo scenario tests
│   └── tier5_adversarial/       # Adversarial stress tests
├── data/
│   ├── presets/                 # Preset farm scenarios (An Giang Rice, Lam Dong Coffee)
│   └── vector_kb/               # Knowledge base documents for vector memory
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation & execution guide
```

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Track & Problem Statement Definition | Finalize Track 3 AgriCarbon Agent specification, beneficiary profiles, and regulatory compliance alignment (GX Japan, EU CBAM). | M1 | Survey 1, ORIGINAL_REQUEST §R1 |
| 2 | Quantitative Sustainable Impact Formulas | Mathematical models for -38% water, -28.1% CO2e, -30.5% fertilizer savings, and 3min vs 21 days audit time. | M1 | Survey 1, ORIGINAL_REQUEST §Acceptance |
| 3 | Preset Farm Scenarios & Telemetry Data | An Giang Rice Polder & Lam Dong Arabica Coffee preset datasets with weather, soil moisture, and electricity tariff mocks. | M1 | Survey 1, Survey 3, Spec Miner |
| 4 | Supervisor Orchestrator Node | LangGraph central routing node performing ReAct task decomposition, worker assignment, and state aggregation. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 5 | Sensing & Weather Worker Agent | Evaluates ambient weather (rain probability, ET0) and soil moisture telemetry to determine watering urgency. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 6 | Resource Eco-Dispatch Worker Agent | Optimizes pump schedules, valve durations, and nitrogen dosages to minimize resource usage and peak electricity costs. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 7 | Carbon Footprint Auditor Worker Agent | Calculates Scope 1-3 GHG emissions (fuel, grid electricity, fertilizer N2O) and generates audit entries. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 8 | Safety Guardrails & Self-Correction Critic | Detects invalid tool outputs, out-of-bounds agronomic commands, initiates Reflexion retry loop (max 3 retries). | M2 | Survey 2, ORIGINAL_REQUEST §Acceptance |
| 9 | Tool 1: `get_weather_forecast` | Open-Meteo REST API client with automatic fallback to offline cached forecasts. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 10 | Tool 2: `query_sensor_telemetry` | Database/Telemetry connector querying soil moisture, NPK, temperature, and pump status. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 11 | Tool 3: `calculate_agricultural_emissions` | Deterministic IPCC Tier 1/2 computation engine for CO2e, CH4, and N2O. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 12 | Tool 4: `record_esg_audit_entry` | Appends cryptographically hashed (SHA-256) audit records into tamper-evident JSON/SQLite ledger. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 13 | Short-Term Context Memory Buffer | State checkpointing via SQLite thread storage for multi-turn conversation and recovery. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 14 | Long-Term Vector Store Memory | ChromaDB local vector store embedding FAO-56/IPCC/MARD standards and historical decision reflections. | M2 | Survey 2, ORIGINAL_REQUEST §R2 |
| 15 | FastAPI Backend Service | Modular FastAPI app with CORS, structured logging, Lifespan handler, and error middleware. | M3 | Survey 3, ORIGINAL_REQUEST §R3 |
| 16 | SSE Thought Streaming Endpoint | Server-Sent Events `/api/v1/agent/stream` publishing 7 thought event types in real-time. | M3 | Survey 3, ORIGINAL_REQUEST §R3 |
| 17 | Preset Demo Endpoints (<5s latency) | High-speed cached endpoints `/api/v1/demo/{preset_id}` guaranteed to respond in < 5.0 seconds. | M3 | Survey 3, ORIGINAL_REQUEST §Acceptance |
| 18 | Health & System Status APIs | `/healthz` and `/api/v1/status` reporting multi-agent readiness, tool health, and memory stats. | M3 | Survey 3, ORIGINAL_REQUEST §R3 |
| 19 | Interactive Streamlit Web UI | Streamlit dashboard visualizing farm telemetry, real-time agent thought streaming feed, and action control. | M3 | Survey 3, ORIGINAL_REQUEST §R3 |
| 20 | Bilingual ESG Carbon Certificate Export | One-click generation of export-grade ESG carbon audit reports in Vietnamese and Japanese. | M3 | Survey 3, ORIGINAL_REQUEST §R3 |
| 21 | 10-Slide TiB Tokyo Pitch Deck | Complete international standard pitch deck covering all 10 required hackathon rubrics. | M4 | Survey 3, ORIGINAL_REQUEST §R4 |
| 22 | TiB 60s Backup Demo Plan & Script | Three-tier fail-safe plan (Live App -> Offline Cache -> Video MP4) with second-by-second stage script. | M4 | Survey 3, ORIGINAL_REQUEST §R3 |
| 23 | TiB Judge Q&A Defense Playbook | 30-second bulletproof responses to Hallucination, Token Cost, Data Privacy, and Legal Co-pilot questions. | M4 | Survey 3, Handbook Part 9 |
| 24 | E2E Test Suite & Test Runner CLI | Automated test harness executing Tier 1 to 4 test suites with pass/fail exit code reporting. | E2E Track | ORIGINAL_REQUEST §Acceptance |
| 25 | 100% E2E Test Pass (Tiers 1-4) | Verification of all 6 acceptance criteria across 24+ test cases. | Final M (P1) | ORIGINAL_REQUEST §Acceptance |
| 26 | Adversarial Hardening (Tier 5) | Stress testing tool error injection, extreme weather bounds, malformed inputs, and recovery loops. | Final M (P2) | Project Pattern Guidelines |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Problem Framing, Domain Models & Data Presets | Domain models (`agronomy.py`, `carbon_models.py`, `esg_ledger.py`), baseline impact metrics, and preset datasets (`An Giang Rice`, `Lam Dong Coffee`). | None | DONE |
| M2 | Multi-Agent Core Engine, Tools & Dual-Tier Memory | LangGraph supervisor stategraph, 4 worker agents, ReAct loop, guardrails critic, 4 automated tools, SQLite checkpointer, ChromaDB vector store. | M1 | DONE |
| M3 | FastAPI Backend Service & Streaming Web UI | FastAPI app, SSE thought streaming `/api/v1/agent/stream`, preset demo endpoints (<5s), Streamlit dashboard with real-time thought timeline, ESG certificate export. | M2 | DONE |
| M4 | TiB Pitch Deck, 60s Demo Plan & Judge Defense | 10-slide pitch deck (Markdown & HTML), 60s backup video script, and TiB judge Q&A defense playbook. | M1, M2, M3 | DONE |
| Final | 100% E2E Test Pass & Adversarial Hardening | Phase 1: 100% pass on Tiers 1-4 E2E tests. Phase 2: Tier 5 adversarial stress testing and coverage hardening. | M1, M2, M3, M4, TEST_READY | DONE |

## Interface Contracts

### `core/domain/agronomy.py` ↔ `core/agents/sensing_agent.py` & `dispatch_agent.py`
```python
def calculate_et0(temp_max: float, temp_min: float, humidity: float, wind_speed: float, solar_rad: float) -> float:
    """Calculates reference evapotranspiration (mm/day) using FAO-56 Penman-Monteith."""

def calculate_irrigation_need(crop_type: str, growth_stage: str, current_soil_moisture: float, field_capacity: float, wilting_point: float, et0: float, forecast_rain_mm: float) -> dict:
    """Returns: {'water_needed_mm': float, 'duration_minutes': int, 'urgency': str, 'avoid_reason': str | None}"""
```

### `core/domain/carbon_models.py` ↔ `core/agents/carbon_agent.py` & `core/tools/carbon_tool.py`
```python
def calculate_scope1_scope2_emissions(water_pumped_m3: float, pump_power_kw: float, grid_emission_factor: float, fertilizer_n_kg: float, diesel_liters: float) -> dict:
    """Returns: {'total_co2e_kg': float, 'breakdown': {'electricity_co2e': float, 'fertilizer_n2o_co2e': float, 'fuel_co2e': float}, 'baseline_co2e_kg': float, 'reduction_pct': float}"""
```

### `core/agents/graph.py` (Supervisor AgentState)
```python
from typing import TypedDict, Annotated, List, Dict, Any

class AgentState(TypedDict):
    task_id: str
    scenario_id: str
    crop_info: Dict[str, Any]
    user_prompt: str
    plan: List[str]
    current_step: int
    thoughts: List[Dict[str, Any]]
    tool_calls: List[Dict[str, Any]]
    weather_data: Dict[str, Any]
    sensor_telemetry: Dict[str, Any]
    dispatch_plan: Dict[str, Any]
    carbon_report: Dict[str, Any]
    critic_verdict: Dict[str, Any]  # {'approved': bool, 'retry_count': int, 'feedback': str}
    final_output: Dict[str, Any]
    errors: List[str]
```

### `backend/app/api/routes.py` ↔ Frontend / Clients
- `POST /api/v1/agent/run` -> `AgentRunResponse`: Synchronous execution (with timeout fallback).
- `GET /api/v1/agent/stream?scenario_id=...` -> `text/event-stream`: SSE thought events:
  - `event: thought`, `data: {"step": "...", "content": "..."}`
  - `event: tool_call`, `data: {"tool": "...", "args": {...}}`
  - `event: tool_result`, `data: {"tool": "...", "result": {...}}`
  - `event: reflection`, `data: {"approved": bool, "critique": "..."}`
  - `event: token`, `data: {"chunk": "..."}`
  - `event: complete`, `data: {"final_result": {...}, "latency_ms": int}`
  - `event: error`, `data: {"message": "..."}`
- `GET /api/v1/demo/{preset_id}` -> `DemoPresetResponse`: Instant pre-computed / cached scenario (<5s).
- `GET /healthz` -> `{"status": "ok", "service": "agricarbon-backend", "version": "1.0.0"}`
