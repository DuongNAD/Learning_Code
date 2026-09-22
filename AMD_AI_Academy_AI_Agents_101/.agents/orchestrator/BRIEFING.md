# BRIEFING — 2026-09-22T18:26:30+07:00

## Mission
Orchestrate end-to-end course extraction, transcription (EN+VI timestamps), in-depth lesson authoring with Mermaid diagrams, runnable zero-defect Python code labs, comprehensive quiz assessment, and README catalog for AMD AI Academy: AI Agents 101.

## 🔒 My Identity
- Archetype: teamwork_preview_orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/orchestrator
- Original parent: parent (sentinel)
- Original parent conversation ID: bc98f4c5-f36e-4dac-bbd7-bd7e123d6755

## 🔒 My Workflow
- **Pattern**: Project Pattern (Orchestrator hierarchy, Survey -> Decompose & Delegate / Iteration Loop)
- **Scope document**: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/orchestrator/PROJECT.md
1. **Decompose**:
   - M0: Survey & Audio Extraction / Spec Mining (Extract audio from video, inspect content, produce baseline metadata)
   - M1: Transcription & Translation (Whisper/ASR timestamps, EN transcript + VI translation at 02_Notes_Summaries/transcript.md)
   - M2: In-depth Curriculum & Architecture Notes (Comprehensive lessons, 4 pillars, ReAct/reflection/multi-agent, AMD ROCm/Ryzen AI NPU/Instinct hardware, >=3 Mermaid diagrams in 02_Notes_Summaries/)
   - M3: Runnable Python Code Labs (Pure ReAct loop, Tool calling, Memory/state management, LangGraph/CrewAI, requirements.txt, verified py_compile and execution)
   - M4: Quiz & Self-Assessment (15-20 questions with answers and detailed explanations in 02_Notes_Summaries/quiz_and_assessment.md)
   - M5: README Catalog & Final Verification / Audit (README index linking all materials, full verification check, forensic audit)
2. **Dispatch & Execute**:
   - Survey via 3 Explorers / Spec Miners
   - Dispatch Workers for each Milestone with strict write ownership
   - Reviewers, Challengers, and Forensic Auditors per milestone gate
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (last resort)
4. **Succession**: Threshold at 16 spawns, write handoff.md, cancel crons, invoke successor.
- **Work items**:
  1. M0: Survey & Audio Extraction [pending]
  2. M1: Transcription & Translation (EN+VI with timestamps) [pending]
  3. M2: Curriculum & Architecture Notes (>=3 Mermaid) [pending]
  4. M3: Runnable Python Code Labs [pending]
  5. M4: Quiz & Assessment [pending]
  6. M5: README Catalog & Global Audit [pending]
- **Current phase**: 0 (Survey)
- **Current focus**: Survey and media inspection

## 🔒 Key Constraints
- NEVER write, modify, or create source code or content files directly — dispatch workers.
- NEVER run build/test commands directly — workers must execute.
- Dispatch Explorers for investigation.
- Use file-editing tools ONLY for metadata/state files (.md) in .agents/ folder.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh.
- Zero tolerance for cheating or fake data — Forensic Auditor has strict binary veto.

## Current Parent
- Conversation ID: bc98f4c5-f36e-4dac-bbd7-bd7e123d6755
- Updated: 2026-09-22T18:26:30+07:00

## Key Decisions Made
- Adopted Project Pattern with dual-track quality gating.
- Appointed dedicated agent directories under `.agents/` for each worker/subagent.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| explorer_1 | teamwork_preview_spec_miner | Survey & Media Extraction (audio extraction & ASR probe) | completed | 89c8e34c-4cb7-43f6-9850-f9f848a49ffd |
| explorer_2 | teamwork_preview_explorer | Survey: Curriculum & Architecture Blueprint | completed | 925e8359-cf35-4133-85d5-9ebb5690318e |
| explorer_3 | teamwork_preview_explorer | Survey: Python Environment & Labs Design | completed | 5e58a0f4-2dcf-46e4-b650-625b57e96005 |
| worker_m1 | teamwork_preview_worker | Milestone 1: Speech-to-Text & Technical Translation | completed | d819718b-834e-45fb-86f5-8669fef5daf8 |
| worker_m3 | teamwork_preview_worker | Milestone 3: Python Code Labs & Execution Verification | completed | d98f2178-8252-418e-9dbe-e8a1ee20ceb1 |
| worker_m2 | teamwork_preview_worker | Milestone 2: Curriculum & In-depth Architecture Notes | completed | 2051c5e7-ece1-4968-9516-848dd2e56596 |
| worker_m4 | teamwork_preview_worker | Milestone 4: Quizzes & Assessment Authoring | completed | 1258623d-5fe9-47b5-afbb-6f7740e585ca |
| worker_m5 | teamwork_preview_worker | Milestone 5: Course README Index & Catalog Integration | completed | 39ee1652-6af8-4c65-8ec0-2404e0fb3e1d |
| reviewer_1 | teamwork_preview_reviewer | Gate Review: Curriculum, Transcript & Assessment | completed | ad7796b7-1e06-4fbe-b5de-1db110c21739 |
| reviewer_2 | teamwork_preview_reviewer | Gate Review: Python Code Labs & Quality Verification | completed | e7ed2676-4e30-4930-b021-277c62a74d5a |
| challenger_1 | teamwork_preview_challenger | Gate Challenge: Code Labs Stress & Edge Case Harness | completed | b36027d5-c66a-4e54-82c7-5abe7f962064 |
| challenger_2 | teamwork_preview_challenger | Gate Challenge: Integration & Link Integrity | completed | 719f4476-7bd3-4fe2-a7cc-fe348354d458 |
| auditor_1 | teamwork_preview_auditor | Gate Audit: Independent Forensic Integrity Verification | completed | 5ce9e247-b6bc-4b34-8c1c-d81e17f6b1e9 |
| worker_m3_patch | teamwork_preview_worker | Iteration 2: Code Labs Robustness Hardening | completed | e0ff9f35-a969-421c-9329-0144bd4604de |
| challenger_1_v2 | teamwork_preview_challenger | Gate Re-verification: Code Labs Stress Harness | completed | a8d78124-3c70-4c2d-b493-efd198cc7043 |

## Succession Status
- Succession required: no
- Spawn count: 15 / 16
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: ce54950b-c6ea-4120-9565-9cb30f34033f/task-12
- Safety timer: none
- On succession: kill all timers before spawning successor
- On context truncation: run `manage_task(Action="list")` — re-create if missing

## Artifact Index
- /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md — Authoritative User Request
- /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/orchestrator/DISPATCH.md — Orchestrator Dispatch Log
- /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/orchestrator/BRIEFING.md — Persistent working memory
- /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/orchestrator/plan.md — Detailed orchestration plan
- /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/orchestrator/progress.md — Liveness & execution tracking
