# Orchestration Plan: AMD AI Academy - AI Agents 101

## 1. Objective
Transform the raw video lecture `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/01_Recordings/01_AI_Agents_101_Full.mov` into a production-grade, highly structured, comprehensive educational knowledge base and course package satisfying all requirements in `ORIGINAL_REQUEST.md`:
- Audio extraction & complete transcript with timestamps (~19m28s), bilingual EN and technical VI.
- Deep curriculum & architectural notes in `02_Notes_Summaries/` with >=3 Mermaid diagrams covering AI Agent concepts, 4 pillars, design patterns, and AMD hardware ecosystems (ROCm, Ryzen AI NPU, Radeon, Instinct).
- Production-ready runnable Python labs in `03_Materials_Code/` (Pure ReAct loop, tool calling, memory/state, LangGraph/CrewAI) with `requirements.txt` and 100% verified execution.
- 15-20 question quiz with answer key and thorough explanations in `02_Notes_Summaries/quiz_and_assessment.md`.
- Comprehensive `README.md` catalog linking all materials.

## 2. Milestones & Phases

### Phase 0: Survey & Audio Extraction (Survey Phase)
- Dispatch Explorers / Spec Miners to:
  - Inspect the input video (duration, audio stream, resolution).
  - Extract audio via ffmpeg (e.g., wav/mp3 in appropriate temp/working location).
  - Mine specifications, tools available on the system (ffmpeg, whisper, python environment, installed libraries).
  - Deliver initial survey findings into `PROJECT.md`.

### Phase 1: Milestone 1 - Full Transcript & Translation (R1)
- Dispatch Worker to run speech recognition / transcription on the extracted audio.
- Format `02_Notes_Summaries/transcript.md` with:
  - Precise timestamps across the full ~19m28s lecture.
  - Original English text verbatim.
  - Accurate Vietnamese translation using standardized AI terminology.
- Verification: Reviewer & Challenger check timestamp continuity, coverage, terminology fidelity.

### Phase 2: Milestone 2 - In-depth Curriculum & Architecture Notes (R2)
- Dispatch Worker to author comprehensive Markdown lecture modules in `02_Notes_Summaries/`:
  - Definitional distinctions: Traditional LLMs vs AI Agents.
  - 4 Pillars: Perception, Planning & Reasoning, Tool Use & Action, Memory (Short & Long-term).
  - Architectural Design Patterns: ReAct loop, Self-Reflection, Multi-Agent Collaboration.
  - AMD Hardware Acceleration Ecosystem: AMD ROCm, Ryzen AI NPU (XDNA), Radeon & Instinct GPUs, ONNX Runtime / Vitis AI / local LLM inference.
  - At least 3 high-detail Mermaid diagrams.
- Verification: Reviewer & Challenger check depth, technical rigor, diagram validity.

### Phase 3: Milestone 3 - Python Code Labs & Execution Verification (R3)
- Dispatch Worker to implement zero-defect Python code in `03_Materials_Code/`:
  1. `01_pure_react_agent.py`: Pure ReAct agent loop from scratch without external frameworks.
  2. `02_tool_calling_agent.py`: Tool/function calling agent handling structured practical tasks.
  3. `03_memory_state_agent.py`: Working session memory, short-term buffer, and state management.
  4. `04_framework_agent_langgraph.py` / `04_framework_agent_crewai.py`: Multi-agent / graph workflow.
  5. `requirements.txt`: Clean dependency specification.
  6. `run_all_labs.sh` or comprehensive verification runner.
- Verification: Worker executes all scripts with syntax check (`python3 -m py_compile`) and runtime execution verification. Reviewer, Challenger, and Auditor verify integrity.

### Phase 4: Milestone 4 - Quizzes & Assessment (R4)
- Dispatch Worker to craft `02_Notes_Summaries/quiz_and_assessment.md`:
  - 15-20 rigorous conceptual and practical scenario questions.
  - Bloom's taxonomy spread (Fundamental -> Applied -> Architectural).
  - Complete answer key and thorough step-by-step rationales for correct and distractor choices.
- Verification: Reviewer verifies conceptual accuracy and explanation depth.

### Phase 5: Milestone 5 - Indexing, Integration & Forensic Audit
- Dispatch Worker to update `README.md` at the project root with comprehensive navigation, course overview, module links, lab instructions, and summary metrics.
- Dispatch Forensic Auditor for integrity verification.
- Synthesize all artifacts, verify gate conditions, and deliver completion report to Sentinel.
