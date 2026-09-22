## 2026-09-08T06:11:45Z
You are Milestone 2 Worker for AgriCarbon Agent (Vietnam Japan AI Hackathon 2026).
Working Directory: d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\worker_m2
Parent: Project Orchestrator (Conversation ID: 9ed17e46-bddf-44f6-9b7f-776ff56dd363)

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

MANDATORY INSTRUCTIONS:
1. Read d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\ORIGINAL_REQUEST.md and d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\PROJECT.md.
2. Read the architectural survey report from d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\explorer_survey_2\survey_report.md.
3. Read the existing domain models in core/domain/*.py and presets in data/presets/*.json.
4. Implement the production-grade Multi-Agent Engine Core (R2):
   - core/agents/__init__.py, state.py, supervisor.py, sensing_agent.py, dispatch_agent.py, carbon_agent.py, critic_agent.py, graph.py
   - core/tools/__init__.py, weather_tool.py, 	elemetry_tool.py, carbon_tool.py, ledger_tool.py, mock_data.py
   - core/memory/__init__.py, short_term.py, ector_store.py
5. Ensure:
   - Supervisor orchestrates specialized worker agents with ReAct planning and thought streaming emission.
   - At least 3 automated tools called in context (4 tools provided).
   - Self-correction / Reflexion loop triggers and recovers cleanly when tools return errors.
   - Dual-tier memory stores thread checkpoints and domain knowledge embeddings.
6. Write tests in 	ests/test_agent_core_m2.py and run tests (py -m pytest tests/ or py tests/e2e_runner.py --all) to verify 100% pass.
7. Write handoff report to d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype\.agents\worker_m2\handoff.md.
8. Send completion message back to Parent (Conversation ID: 9ed17e46-bddf-44f6-9b7f-776ff56dd363).
