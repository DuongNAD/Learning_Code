# Project: AMD AI Academy - AI Agents 101 Course Package

## Architecture
- Root: `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101`
- Audio/Video: `01_Recordings/01_AI_Agents_101_Full.mov`
- Knowledge Base & Curricula: `02_Notes_Summaries/`
  - `transcript.md`: Full timestamped transcript (EN + VI) covering ~19m28s.
  - `curriculum/` or module notes: In-depth lectures on 4 Pillars, ReAct/Reflection/Multi-Agent, AMD Ecosystem (ROCm, Ryzen AI NPU, Radeon, Instinct).
  - `>=3` Mermaid architecture diagrams.
  - `quiz_and_assessment.md`: 15-20 questions with answers and comprehensive rationales.
- Practical Code Labs: `03_Materials_Code/`
  - `01_pure_react_agent.py`: Pure ReAct implementation without external frameworks.
  - `02_tool_calling_agent.py`: Real-world tool / function calling.
  - `03_memory_state_agent.py`: Session & conversation memory, state management.
  - `04_framework_agent_langgraph.py`: LangGraph / CrewAI integration.
  - `requirements.txt`: Clean, complete dependencies.
  - `test_labs.py` or runner script: 100% automated syntax and execution verification.
- Top-level Course Index: `README.md`

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Media Extraction | Extract audio stream from 01_AI_Agents_101_Full.mov via ffmpeg | M0 | ORIGINAL_REQUEST §R1 |
| 2 | Full Transcription | Produce accurate EN transcript with timestamps for ~19m28s video | M1 | ORIGINAL_REQUEST §R1 |
| 3 | Specialized Translation | Translate transcript to Vietnamese with proper AI domain terminology | M1 | ORIGINAL_REQUEST §R1 |
| 4 | Core Conceptual Foundation | AI Agents vs Traditional LLMs conceptual distinctions | M2 | ORIGINAL_REQUEST §R2 |
| 5 | 4 Architectural Pillars | In-depth analysis of Perception, Planning, Action/Tools, Memory | M2 | ORIGINAL_REQUEST §R2 |
| 6 | Agent Design Patterns | ReAct, Self-Reflection, Multi-Agent Collaboration | M2 | ORIGINAL_REQUEST §R2 |
| 7 | AMD Hardware Acceleration | AMD ROCm, Ryzen AI NPU (XDNA), Radeon/Instinct GPUs, inference optimization | M2 | ORIGINAL_REQUEST §R2 |
| 8 | Architecture Visualizations | At least 3 standards-compliant Mermaid diagrams | M2 | ORIGINAL_REQUEST §R2 |
| 9 | Lab 1: Pure ReAct Loop | Zero-dependency implementation of Thought-Action-Observation loop | M3 | ORIGINAL_REQUEST §R3 |
| 10 | Lab 2: Tool Calling Agent | Function calling and external API integration | M3 | ORIGINAL_REQUEST §R3 |
| 11 | Lab 3: Memory & State | Short-term & long-term memory buffer management | M3 | ORIGINAL_REQUEST §R3 |
| 12 | Lab 4: Framework Agent | LangGraph / CrewAI workflow implementation | M3 | ORIGINAL_REQUEST §R3 |
| 13 | Lab Dependencies & Runner | requirements.txt and verification scripts | M3 | ORIGINAL_REQUEST §R3 |
| 14 | Knowledge Assessment | 15-20 questions across bloom levels in quiz_and_assessment.md | M4 | ORIGINAL_REQUEST §R4 |
| 15 | Course Catalog & Index | Unified README.md indexing all course materials, labs, notes | M5 | ORIGINAL_REQUEST §Acceptance |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M0 | Survey & Media Extraction | Inspect video, extract audio, probe tools | None | DONE |
| M1 | Full Transcript (EN+VI) | Produce transcript.md with timestamps | M0 | DONE |
| M2 | Comprehensive Curriculum & Notes | Author in-depth modules & >=3 Mermaid diagrams | M1 | DONE |
| M3 | Python Code Labs & Verification | Implement and test 4 runnable labs | M0 | DONE |
| M4 | Quiz & Assessment | Write 15-20 questions + comprehensive rationales | M2 | DONE |
| M5 | Course Catalog & Final Audit | README.md update, full audit, Sentinel handoff | M1, M2, M3, M4 | DONE |

## Code Layout
- `01_Recordings/01_AI_Agents_101_Full.mov`
- `02_Notes_Summaries/`
  - `transcript.md`
  - `01_foundations_and_agent_architecture.md`
  - `02_core_pillars_and_design_patterns.md`
  - `03_amd_hardware_and_rocm_ecosystem.md`
  - `quiz_and_assessment.md`
- `03_Materials_Code/`
  - `01_pure_react_agent.py`
  - `02_tool_calling_agent.py`
  - `03_memory_state_agent.py`
  - `04_framework_agent_langgraph.py`
  - `requirements.txt`
  - `verify_labs.py`
- `README.md`
