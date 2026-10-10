---
document_type: master_knowledge_map
version: 1.0.0
last_updated: 2026-10-10
architecture: AI-Native Markdown Knowledge Router
root_workspace: file:///D:/
learning_hub: file:///D:/02_Learning_Knowledge/
classification: Master Index
wip_limit: 5
rfc2119_compliance: strict
emoji_policy: none
---

# Master Knowledge Map & Navigation Router

Workspace Root: [D:/](file:///D:/)
Learning Hub: [D:/02_Learning_Knowledge/](file:///D:/02_Learning_Knowledge/)

This document defines the unified architectural index, navigation topology, and condition-action routing matrix for AI agents and human engineers operating in `D:/02_Learning_Knowledge`.

AI agents MUST read this document at the start of any session within this workspace to resolve paths, enforce governance, and maintain cognitive alignment.

---

## 1. Condition-Action Navigation Matrix

AI agents MUST evaluate this matrix to determine the correct execution protocol for incoming user requests.

| Agent Trigger / Intent | Precondition | Target Resource | Mandatory Protocol (RFC 2119) |
| :--- | :--- | :--- | :--- |
| Session Initialization | Agent enters workspace | [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md) | Agent MUST inspect INDEX.md first to load topology and operational bounds. |
| Pedagogical Interaction | User asks for coding help / tutorial | [GEMINI.md](file:///D:/02_Learning_Knowledge/GEMINI.md)<br>[AGENTS.md](file:///D:/02_Learning_Knowledge/AGENTS.md) | Agent MUST operate as DeepTutor. Agent MUST NOT write production solutions directly; full code solution is provided ONLY IF explicitly requested ("Show me the full code"). Agent MUST apply 5-level Socratic scaffolding. |
| Goal Setting / Daily Roulette | "Hôm nay học gì?", "Set mục tiêu", or daily startup | [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md)<br>[pick_today.py](file:///D:/02_Learning_Knowledge/pick_today.py) | Agent MUST execute or parse roulette output. Agent MUST set exactly 1 micro-mission with verifiable Definition of Done (DoD) in ACTIVE_LEARNING.md. |
| Active Project Study | Topic is within Top 5 Active Projects | Active Subject Directory (Section 4) | Agent MUST inspect subject README, checkpoint, and recent files before proposing exercises. |
| Backlog Topic Inquiry | Topic is parked (Section 5) | Backlog Subject Directory (Section 5) | Agent MUST clarify that topic is currently parked. Topic MUST NOT be activated; promotion into active status is permitted ONLY IF an existing active slot is cleared (WIP limit 5). Agent MUST NEVER exceed WIP limit 5. |
| Task Status Mutation | User begins, makes progress, or finishes task | Local [TASKS.md](file:///D:/02_Learning_Knowledge/) per project<br>[TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md)<br>[ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md) | Agent MUST update status between `[ ]` and `[x]` in the project's local TASKS.md (or central TASKS.md for workspace tasks). Tasks MUST be marked `[x]` ONLY IF verified. Agent MUST NEVER delete existing tasks. |
| SSD Sync / Health Check | User requests sync, or session concludes | [GEMINI.md](file:///D:/GEMINI.md)<br>`D:/sync_repos.ps1` | Agent MUST verify git status. Agent MUST NEVER commit secrets or dependencies (`.venv`, `node_modules`). |

---

## 2. Core Governance & Instruction Architecture

The workspace is governed by a hierarchical instruction model. AI agents MUST observe the precedence hierarchy: Root Workspace > Learning Workspace Hub > Subject Specific.

### 2.1 Root Workspace Directives
- File: [GEMINI.md](file:///D:/GEMINI.md)
- Scope: Kingston XS2000 external SSD (exFAT).
- Rules:
  - Cross-platform parity: Windows and macOS compatibility MUST be maintained.
  - Symlinks: Symlinks MUST NOT be created directly on the exFAT filesystem.
  - Character set: Invalid Windows characters (`\ / : * ? " < > |`) MUST NEVER be used in file names.
  - Secret & Dependency Quarantine: `.env`, API credentials, `.venv`, `node_modules`, and build caches MUST NOT be committed to git.

### 2.2 Learning Hub Directives (DeepTutor Protocol)
- Directives: [GEMINI.md](file:///D:/02_Learning_Knowledge/GEMINI.md) and [AGENTS.md](file:///D:/02_Learning_Knowledge/AGENTS.md)
- Role: DeepTutor (Pedagogical Mentor).
- Rules:
  - Agent MUST NOT output turnkey code solutions; complete code is provided ONLY IF explicitly requested by the learner ("Show me the full code"). Agent MUST NEVER bypass pedagogical scaffolding.
  - Agent MUST apply the 5-Level Socratic Scaffolding (Symptom observation -> Guiding questions -> Minimal counter-example -> Abstract syntax pattern -> Concrete solution).
  - Agent MUST assess Cognitive Gaps (Structural, Deviation, Application, Metacognitive).

---

## 3. Operational Hubs & Execution Tooling

| Component | File Path | Function & Execution Protocol |
| :--- | :--- | :--- |
| Master Knowledge Map | [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md) | Unified sitemap, directory router, and condition-action execution table. |
| Active Learning Focus Board | [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md) | Primary dashboard tracking Top 5 active projects, checkpoints, DoD, and WIP rule enforcement. |
| Master Roadmap (5 courses) | [Roadmaps/MASTER_ROADMAP.md](file:///D:/02_Learning_Knowledge/Roadmaps/MASTER_ROADMAP.md) | Cross-course plan: priorities, weekly time budget, weekly schedule, 10-week milestones, synergy map (learner-facing, Vietnamese). |
| Task Tracker & System Router | [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md) | Workspace-level infrastructure tracking and 2-tier subproject task board router. |
| Decision Roulette (Engine) | [pick_today.py](file:///D:/02_Learning_Knowledge/pick_today.py) | Cryptographically secure random selector using hardware entropy (`secrets` module). |
| Decision Roulette (Windows) | [roll_study.bat](file:///D:/02_Learning_Knowledge/roll_study.bat) | Windows batch execution wrapper for `pick_today.py`. |
| Decision Roulette (macOS) | [roll_study.command](file:///D:/02_Learning_Knowledge/roll_study.command) | macOS terminal execution wrapper for `pick_today.py`. |
| Repository Readme | [README.md](file:///D:/02_Learning_Knowledge/README.md) | High-level repository overview and exFAT compatibility instructions. |

---

## 4. Top 5 Active Focus Projects (WIP Bound = 5)
 
Work-in-Progress (WIP) limit is strictly set to 5. An active subject MUST be marked completed or explicitly parked to the backlog before any new subject is promoted.

### 4.1 GCI World 2026 September
- Path: [GCI_World_2026_September](file:///D:/02_Learning_Knowledge/GCI_World_2026_September)
- Navigation:
  - Overview: [README.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/README.md)
  - Slide Portal Hub: [slides/index.html](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/slides/index.html)
  - Roadmap (v2, 2026-10-10): [roadmap/ROADMAP.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/roadmap/ROADMAP.md)
  - Micro-Roadmap (old, sessions 0-2 only): [roadmap/micro_practice_roadmap.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/roadmap/micro_practice_roadmap.md)
  - Agent Config: [AGENTS.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/AGENTS.md)
  - Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/TASKS.md)
  - Materials: [03_Materials](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/03_Materials)
  - Assignments: [04_Assignments](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/04_Assignments)
  - Notes: [06_Notes_Transcripts](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/06_Notes_Transcripts)
- Focus: High-performance data processing with NumPy for Session 2 (2026-09-24).
- Checkpoint: Hoàn thành khảo sát Buổi 1; HW1 đạt 3/3 điểm; Hoàn thành thực hành NumPy Benchmark (numpy_benchmark_template.py), Boolean Masking (main.py), và thao tác trục Axis 0/1 (numpy_axes_practice.py).

### 4.2 Machine Learning
- Path: [Machine_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning)
- Navigation:
  - Overview: [README.md](file:///D:/02_Learning_Knowledge/Machine_Learning/README.md)
  - Roadmap (v2, 2026-10-10): [Roadmaps/ROADMAP.md](file:///D:/02_Learning_Knowledge/Machine_Learning/Roadmaps/ROADMAP.md)
  - Instructions: [GEMINI.md](file:///D:/02_Learning_Knowledge/Machine_Learning/GEMINI.md) | [AGENTS.md](file:///D:/02_Learning_Knowledge/Machine_Learning/AGENTS.md)
  - Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/Machine_Learning/TASKS.md)
  - Math Foundations: [01_Math_Foundations](file:///D:/02_Learning_Knowledge/Machine_Learning/01_Math_Foundations)
  - Supervised Learning: [02_Supervised_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning)
  - Unsupervised Learning: [03_Unsupervised_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning/03_Unsupervised_Learning)
  - Evaluation & Tuning: [04_Model_Evaluation_Tuning](file:///D:/02_Learning_Knowledge/Machine_Learning/04_Model_Evaluation_Tuning)
  - Deep Learning Basics: [05_Deep_Learning_Basics](file:///D:/02_Learning_Knowledge/Machine_Learning/05_Deep_Learning_Basics)
  - Deployment API: [07_Model_Deployment_API](file:///D:/02_Learning_Knowledge/Machine_Learning/07_Model_Deployment_API)
  - Reinforcement Learning: [08_Reinforcement_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning/08_Reinforcement_Learning)
  - LLM From Scratch: [09_LLM_From_Scratch](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch)
- Focus: Supervised learning algorithms, deep neural networks, RL, and building LLMs from scratch.
- Checkpoint: Math foundations, baseline notebooks, and LLM 7-stage practice workspace initialized.

### 4.3 Python Master
- Path: [Python_Master](file:///D:/02_Learning_Knowledge/Python_Master)
- Navigation:
  - Overview: [README.md](file:///D:/02_Learning_Knowledge/Python_Master/README.md)
  - Roadmap (v2, 2026-10-10): [Roadmaps/ROADMAP.md](file:///D:/02_Learning_Knowledge/Python_Master/Roadmaps/ROADMAP.md)
  - Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/Python_Master/TASKS.md)
  - Cheatsheet: [CHEATSHEET.md](file:///D:/02_Learning_Knowledge/Python_Master/CHEATSHEET.md)
  - Launch Hub: [launch_hub.py](file:///D:/02_Learning_Knowledge/Python_Master/launch_hub.py)
  - Practice Set: [python-master-bang-b](file:///D:/02_Learning_Knowledge/Python_Master/python-master-bang-b)
- Focus: Mock tests and algorithm problem sets for Table B (COS Pro certification).
- Checkpoint: Practice repository, cheatsheet, and launch hub initialized.

### 4.4 Quantum Computing
- Path: [Quantum_Computing](file:///D:/02_Learning_Knowledge/Quantum_Computing)
- Navigation:
  - Overview: [README.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/README.md)
  - Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/TASKS.md)
  - Roadmap (v2, 2026-10-10): [Roadmaps/ROADMAP.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/Roadmaps/ROADMAP.md)
  - Curriculum Roadmap (old): [lo-trinh-quantum-zero-to-hero.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/lo-trinh-quantum-zero-to-hero.md)
  - Phase 0 Basics: [phase0](file:///D:/02_Learning_Knowledge/Quantum_Computing/phase0)
  - Katas Suite: [katas](file:///D:/02_Learning_Knowledge/Quantum_Computing/katas)
  - Quantum Simulator: [qsim](file:///D:/02_Learning_Knowledge/Quantum_Computing/qsim)
- Focus: Quantum circuit simulations, foundational katas, Bell states, and QFT.
- Checkpoint: Zero-to-Hero curriculum defined; phase0 initialized.

### 4.5 AMD AI Academy - AI Agents 101
- Path: [AMD_AI_Academy_AI_Agents_101](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101)
- Navigation:
  - Overview: [README.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/README.md)
  - Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/TASKS.md)
  - Recordings: [01_Recordings](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/01_Recordings)
  - Notes & Summaries: [02_Notes_Summaries](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries)
  - Materials & Code: [03_Materials_Code](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code)
  - Roadmap (v2, 2026-10-10): [04_Roadmaps/ROADMAP.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/04_Roadmaps/ROADMAP.md)
- Focus: Autonomous agent architectures, tool-use protocols, and function calling workflows.
- Checkpoint: Lecture notes and curriculum structured in 02_Notes_Summaries.

---

## 5. Parked Backlog Catalog (Dormant Topics)
 
Backlog topics MUST remain dormant. Promotion to active status is permitted ONLY IF an active slot is cleared under the WIP limit rule. Agents MUST NEVER activate backlog topics concurrently exceeding WIP limits.
 
| Identifier | Subdirectory Link | Domain & Scope |
| :--- | :--- | :--- |
| API | [API](file:///D:/02_Learning_Knowledge/API) | REST API design, HTTP methods, headers, authentication, external integrations. |
| Assembly | [Asembly](file:///D:/02_Learning_Knowledge/Asembly) | Low-level x86 architecture, registers, instruction sets, stack frames. |
| C | [C](file:///D:/02_Learning_Knowledge/C) | C language systems programming, pointers, structs, dynamic memory allocation. |
| C# | [C#](file:///D:/02_Learning_Knowledge/C#) | .NET development, object-oriented design, LINQ, C# desktop/backend applications. |
| CV | [CV](file:///D:/02_Learning_Knowledge/CV) | Computer Vision, OpenCV filters, transformations, image detection pipelines. |
| Class FPT | [Class_FPT](file:///D:/02_Learning_Knowledge/Class_FPT) | FPT university class coursework, lab submissions, academic modules. |
| Data Analysis | [Data_Analysis](file:///D:/02_Learning_Knowledge/Data_Analysis) | Exploratory data analysis, Pandas, NumPy, statistical hypothesis testing. |
| FPT Courses | [FPT_Courses](file:///D:/02_Learning_Knowledge/FPT_Courses) | Institutional course materials, syllabi, study tracks. |
| FPT University | [FPT_University](file:///D:/02_Learning_Knowledge/FPT_University) | General university resources, thesis notes, administrative academic files. |
| HTML-CSS-JS | [Html-Css-Js](file:///D:/02_Learning_Knowledge/Html-Css-Js) | Semantic HTML5, modern CSS layouts (Flexbox/Grid), ECMAScript JavaScript. |
| IMLC 2026 | [IMLC_2026](file:///D:/02_Learning_Knowledge/IMLC_2026) | International Machine Learning Competition 2026 research papers, LaTeX docs, proofs. |
| Java | [Java](file:///D:/02_Learning_Knowledge/Java) | Java Core, OOP design patterns, multithreading, collections, algorithm practice. |
| NodeJS | [NodeJS](file:///D:/02_Learning_Knowledge/NodeJS) | Node.js asynchronous backend runtime, Express.js server, REST endpoints, npm. |
| PHP | [PHP](file:///D:/02_Learning_Knowledge/PHP) | Backend PHP scripting, MVC architecture, MySQL database connectivity. |
| Python Project | [PythonProject](file:///D:/02_Learning_Knowledge/PythonProject) | General Python scripting, utility scripts, automation prototypes. |
| React | [React](file:///D:/02_Learning_Knowledge/React) | React component architecture, JSX, hooks, state lifecycle, Single Page Apps. |
| SQL | [SQL](file:///D:/02_Learning_Knowledge/SQL) | Relational database schema design, indexing, joins, query performance tuning. |
| TestArm | [TestArm](file:///D:/02_Learning_Knowledge/TestArm) | DENSO robotic arm automation, ArUco visual markers, Arduino serial controls. |
| UI-UX | [UI-UX](file:///D:/02_Learning_Knowledge/UI-UX) | Wireframing, UX research, interface prototyping, design tokens, Figma handoff. |
| VAIC 2026 | [VAIC2026](file:///D:/02_Learning_Knowledge/VAIC2026) | Vietnam AI Contest 2026 dataset processing and model training pipelines. |
| VJAI Hackathon 2026 | [VJAI_Hackathon_2026](file:///D:/02_Learning_Knowledge/VJAI_Hackathon_2026) | Vietnam-Japan AI Hackathon 2026 prototype designs and hackathon submissions. |
| Aptech Learning | [aptech-learning](file:///D:/02_Learning_Knowledge/aptech-learning) | Aptech curriculum modules, legacy course assignments, diploma syllabus. |
 
---
 
## 6. Maintenance & Verification Rules
 
1. Link Integrity:
   - All links in documentation MUST use absolute `file:///` format with forward slashes for cross-platform validity.
   - Broken or relative links MUST NEVER be introduced in root-level or hub-level indexes.
   - New index links MUST be committed ONLY IF target paths exist on the live filesystem.
2. Icon & Emoji Prohibition:
   - Key documentation files MUST maintain zero icons or emojis to maximize parser predictability and signal-to-noise ratio.
   - Decorative emojis or glyphs MUST NEVER be added to scripts or operational documents.
3. Decision Engine Invariance:
   - `pick_today.py` MUST strictly parse `## Today's Dynamic Goal` and `## Active Projects` from [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md).
   - Any modification to `ACTIVE_LEARNING.md` MUST preserve markdown heading hierarchy to prevent parser failure.

