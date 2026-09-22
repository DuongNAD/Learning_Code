# AgriCarbon Agent — E2E Test Infrastructure & Methodology (`TEST_INFRA.md`)
**Project:** AgriCarbon Agent (Vietnam Japan AI Hackathon 2026 — Track 3)  
**Document Version:** 1.0.0  
**Authoritative Reference:** `ORIGINAL_REQUEST.md`, `PROJECT.md`  
**Test Harness Location:** `tests/`  
**Central Test Runner:** `tests/e2e_runner.py`

---

## 1. Overview & Testing Philosophy

AgriCarbon Agent is an autonomous multi-agent system designed for precision agriculture and supply-chain carbon auditing (Scope 1-3) targeting Vietnam-Japan export corridors (An Giang Rice Polder and Lam Dong Coffee Farm).

The End-to-End (E2E) test suite adheres to four foundational pillars:
1. **Requirement-Driven & Opaque-Box**: Tests validate externally observable behaviors, mathematical invariants, schema contracts, and domain rules defined in `ORIGINAL_REQUEST.md` and `PROJECT.md`. Tests do not depend on internal private states.
2. **Progressive Testability**: The harness is designed to execute immediately during milestone development and progressively verify newly implemented components (Milestone 1 domain models, Milestone 2 multi-agent graph & tools, Milestone 3 backend & SSE stream, Milestone 4 presentation assets).
3. **Deterministic Verification with Authoritative Oracles**: Every test derives expected outputs from authoritative specifications: FAO-56 Penman-Monteith evapotranspiration, IPCC Tier 1/2 GHG emission methodologies, Vietnam EVN electricity tariff schedules, and cryptographic SHA-256 audit ledger invariants.
4. **Adversarial Resilience & Fault Injection**: Robust testing of failure modes, out-of-bounds weather, sensor disconnects, and malformed tool outputs triggering the Critic agent's self-correction loop (Reflexion, max 3 retries).

---

## 2. 4-Tier Test Architecture

The test suite is partitioned into four distinct, progressive tiers:

```
tests/
├── conftest.py                      # Shared fixtures, oracles, reference contracts, mock datasets
├── e2e_runner.py                    # Unified CLI runner with formatted tabular summaries
├── tier1_feature/                   # Tier 1: Isolated feature coverage (>=5 tests per area)
│   ├── test_domain_models.py        # Agronomy FAO-56, IPCC Carbon, Cryptographic Ledger
│   ├── test_tools.py                # 4 Core Tools (Weather, Telemetry, Emissions, Ledger)
│   ├── test_supervisor_agent.py     # Supervisor ReAct planning, StateGraph transitions
│   ├── test_backend_sse.py          # FastAPI routes, 7 SSE event types, healthcheck
│   ├── test_demo_latency.py         # Sub-5.0s preset response latency, caching, throughput
│   └── test_presentation_artifacts.py # 10-slide deck, 60s backup video script, judge Q&A
├── tier2_boundary/                  # Tier 2: Boundary conditions & error recovery
│   ├── test_extreme_weather.py      # Drought (ET0>12), typhoon (>200mm), freezing (<0°C)
│   ├── test_negative_zero_values.py # Zero pump kW, negative moisture, zero fertilizer
│   ├── test_network_failures.py     # Open-Meteo 500, IoT sensor timeout, cache fallback
│   └── test_tool_error_injection.py # Schema corruption, Critic rejection, max 3 retries
├── tier3_pairwise/                  # Tier 3: Cross-feature integrations & pipelines
│   ├── test_sensing_dispatch_pipeline.py # Weather + Soil telemetry -> Irrigation plan
│   ├── test_dispatch_carbon_ledger.py    # Dispatch action -> IPCC emissions -> Ledger entry
│   ├── test_weather_rain_suppression.py # Rain forecast >= threshold suppresses irrigation
│   ├── test_peak_tariff_dispatch.py     # EVN peak tariff shifts pump schedules to off-peak
│   └── test_critic_self_correction_pipeline.py # Fault injection -> Critic rejects -> Re-plan
└── tier4_scenarios/                 # Tier 4: Real-world TiB demo stage workloads
    ├── test_an_giang_rice_polder.py   # AWD water management, -38% water, methane cut
    └── test_lam_dong_coffee_farm.py   # Agroforestry drip fertigation, Scope 3 export audit
```

---

## 3. Test Runner CLI (`tests/e2e_runner.py`)

The central test runner provides a standardized CLI interface for automated and manual execution:

### Usage Syntax:
```bash
# Run all tiers (Tier 1 through Tier 4)
python tests/e2e_runner.py --all

# Run specific tier
python tests/e2e_runner.py --tier 1
python tests/e2e_runner.py --tier 2
python tests/e2e_runner.py --tier 3
python tests/e2e_runner.py --tier 4

# Run with verbose output (prints individual test names and docstrings)
python tests/e2e_runner.py --all --verbose

# Run summary mode (default table overview)
python tests/e2e_runner.py --summary
```

### Direct `pytest` Invocation:
```bash
# Run full suite via pytest
pytest tests/ -v

# Run specific tier via pytest
pytest tests/tier1_feature/ -v
pytest tests/tier2_boundary/ -v
pytest tests/tier3_pairwise/ -v
pytest tests/tier4_scenarios/ -v
```

### Exit Codes:
- `0`: All executed tests passed successfully.
- `1`: One or more tests failed or experienced an uncaught error.

---

## 4. Feature Coverage Matrix (26 Features)

| Feature # | Feature Name | Primary Test Tier & File | Key Test Cases |
|---|---|---|---|
| 1 | Track & Problem Statement Definition | `tier1_feature/test_presentation_artifacts.py` | `test_track3_alignment`, `test_problem_statement_clarity` |
| 2 | Quantitative Sustainable Impact Formulas | `tier1_feature/test_domain_models.py` | `test_fao56_penman_monteith_formula`, `test_ipcc_tier1_tier2_emissions_formula` |
| 3 | Preset Farm Scenarios & Telemetry Data | `tier4_scenarios/test_an_giang_rice_polder.py`, `tier4_scenarios/test_lam_dong_coffee_farm.py` | `test_an_giang_preset_telemetry_loading`, `test_lam_dong_preset_telemetry_loading` |
| 4 | Supervisor Orchestrator Node | `tier1_feature/test_supervisor_agent.py` | `test_supervisor_plan_generation`, `test_supervisor_worker_routing` |
| 5 | Sensing & Weather Worker Agent | `tier1_feature/test_tools.py`, `tier3_pairwise/test_sensing_dispatch_pipeline.py` | `test_weather_tool_execution`, `test_telemetry_tool_query` |
| 6 | Resource Eco-Dispatch Worker Agent | `tier3_pairwise/test_sensing_dispatch_pipeline.py`, `tier3_pairwise/test_peak_tariff_dispatch.py` | `test_irrigation_duration_calculation`, `test_evn_peak_hour_avoidance` |
| 7 | Carbon Footprint Auditor Worker Agent | `tier1_feature/test_domain_models.py`, `tier3_pairwise/test_dispatch_carbon_ledger.py` | `test_scope1_scope2_co2e_calculation`, `test_scope3_supply_chain_audit` |
| 8 | Safety Guardrails & Critic Agent | `tier2_boundary/test_tool_error_injection.py`, `tier3_pairwise/test_critic_self_correction_pipeline.py` | `test_critic_out_of_bounds_rejection`, `test_reflexion_retry_counter_limit` |
| 9 | Tool 1: `get_weather_forecast` | `tier1_feature/test_tools.py`, `tier2_boundary/test_network_failures.py` | `test_weather_tool_live_and_mock`, `test_weather_api_500_cache_fallback` |
| 10 | Tool 2: `query_sensor_telemetry` | `tier1_feature/test_tools.py`, `tier2_boundary/test_network_failures.py` | `test_telemetry_tool_fields`, `test_sensor_db_disconnect_synthetic_fallback` |
| 11 | Tool 3: `calculate_agricultural_emissions` | `tier1_feature/test_tools.py` | `test_emissions_tool_deterministic_output`, `test_emissions_tool_breakdown` |
| 12 | Tool 4: `record_esg_audit_entry` | `tier1_feature/test_tools.py`, `tier1_feature/test_domain_models.py` | `test_sha256_cryptographic_hash_chain`, `test_tamper_evident_verification` |
| 13 | Short-Term Context Memory Buffer | `tier1_feature/test_supervisor_agent.py` | `test_agent_state_thread_checkpointing`, `test_context_history_retention` |
| 14 | Long-Term Vector Store Memory | `tier1_feature/test_supervisor_agent.py` | `test_domain_guideline_retrieval_contract`, `test_rag_augmented_reasoning` |
| 15 | FastAPI Backend Service | `tier1_feature/test_backend_sse.py` | `test_healthcheck_endpoint`, `test_cors_middleware_headers`, `test_lifespan_startup` |
| 16 | SSE Thought Streaming Endpoint | `tier1_feature/test_backend_sse.py` | `test_sse_seven_event_types`, `test_sse_payload_json_structure` |
| 17 | Preset Demo Endpoints (<5s latency) | `tier1_feature/test_demo_latency.py` | `test_preset_response_latency_under_5s`, `test_preset_cache_warmup` |
| 18 | Health & System Status APIs | `tier1_feature/test_backend_sse.py` | `test_status_endpoint_tool_health`, `test_healthz_status_code` |
| 19 | Interactive Streamlit Web UI | `tier1_feature/test_demo_latency.py`, `tier1_feature/test_presentation_artifacts.py` | `test_thought_stream_component_contract`, `test_gauges_render_contract` |
| 20 | Bilingual ESG Certificate Export | `tier1_feature/test_presentation_artifacts.py`, `tier4_scenarios/test_lam_dong_coffee_farm.py` | `test_bilingual_vn_ja_fields_present`, `test_certificate_sha256_signature` |
| 21 | 10-Slide TiB Tokyo Pitch Deck | `tier1_feature/test_presentation_artifacts.py` | `test_pitch_deck_10_slides_structure`, `test_pitch_deck_content_rubrics` |
| 22 | TiB 60s Backup Demo Plan & Script | `tier1_feature/test_presentation_artifacts.py` | `test_backup_demo_60s_second_by_second`, `test_failsafe_three_tier_strategy` |
| 23 | TiB Judge Q&A Defense Playbook | `tier1_feature/test_presentation_artifacts.py` | `test_judge_qa_defense_hallucination_and_cost`, `test_judge_qa_ip_and_accuracy` |
| 24 | E2E Test Suite & Runner CLI | `tests/e2e_runner.py` | `test_runner_cli_flags`, `test_runner_exit_code_zero_on_pass` |
| 25 | 100% E2E Test Pass (Tiers 1-4) | `tests/e2e_runner.py` | `test_all_tiers_comprehensive_pass` |
| 26 | Adversarial Hardening (Tier 2 & 5) | `tier2_boundary/test_tool_error_injection.py`, `tier2_boundary/test_extreme_weather.py` | `test_adversarial_malformed_sensor_payload`, `test_adversarial_irrigation_overdose_blocked` |

---

## 5. Acceptance Criteria Verification Traceability

| Acceptance Criterion | Verification Method | Associated Tests |
|---|---|---|
| **AC 1**: Autonomous end-to-end multi-agent execution | Multi-agent state transition verification from user prompt to final dispatch & ESG ledger entry without human intervention. | `tier1_feature/test_supervisor_agent.py`, `tier3_pairwise/test_sensing_dispatch_pipeline.py` |
| **AC 2**: At least 3 automated tools called in context | Execution and context-driven parameterization of `get_weather_forecast`, `query_sensor_telemetry`, `calculate_agricultural_emissions`, and `record_esg_audit_entry`. | `tier1_feature/test_tools.py`, `tier3_pairwise/test_dispatch_carbon_ledger.py` |
| **AC 3**: Self-correction loop on tool errors | Fault injection into tool outputs; validation that Critic detects violation, increments retry count, and triggers re-planning within max 3 retries. | `tier2_boundary/test_tool_error_injection.py`, `tier3_pairwise/test_critic_self_correction_pipeline.py` |
| **AC 4**: Backend FastAPI starts with zero dependency errors | Lifespan, CORS, router mounting, and endpoint healthchecks validate zero runtime dependency failure. | `tier1_feature/test_backend_sse.py` |
| **AC 5**: Web UI / Preset response < 5.0 seconds | High-speed response latency benchmarks across An Giang and Lam Dong preset scenarios. | `tier1_feature/test_demo_latency.py` |
| **AC 6**: Quantitative sustainable impact verification | Mathematical validation of -38% water savings, -28.1% CO2e reduction, -30.5% fertilizer savings, and audit acceleration from 21 days to <3 minutes. | `tier1_feature/test_domain_models.py`, `tier4_scenarios/test_an_giang_rice_polder.py`, `tier4_scenarios/test_lam_dong_coffee_farm.py` |
