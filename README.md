---
document_type: repository_overview
version: 2.0.0
last_updated: 2026-09-23
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
focus_board: file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md
rfc2119_compliance: strict
emoji_policy: none
---

# 02_Learning_Knowledge - Repository Hub & Learning Directory

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
Active Focus Board: [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md)
Task Tracker: [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md)
Remote Git Origin: [https://github.com/DuongNAD/Learning_Code.git](https://github.com/DuongNAD/Learning_Code.git)

This repository serves as the centralized workspace for programming source code, practical coursework, competitive research, and algorithmic problem sets across diverse technologies and domains.

---

## 1. Architectural Routing

AI agents and human engineers MUST refer to [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md) for the complete sitemap, condition-action navigation matrix, and dormant topic catalogs.

- Top 5 Active Projects: Detailed in [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md) and [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md). Backlog subjects MUST be promoted to active status ONLY IF an active slot is cleared. Active subjects MUST NEVER exceed the WIP limit of 5.
- Decision Roulette Runner: [roll_study.bat](file:///D:/02_Learning_Knowledge/roll_study.bat) (Windows) and [roll_study.command](file:///D:/02_Learning_Knowledge/roll_study.command) (macOS) wrapping [pick_today.py](file:///D:/02_Learning_Knowledge/pick_today.py).

---

## 2. Subject Directory Catalog

| Subject / Technology | Directory Link | Focus Domain |
| :--- | :--- | :--- |
| API | [API](file:///D:/02_Learning_Knowledge/API) | REST API design, external HTTP service integrations |
| Assembly | [Asembly](file:///D:/02_Learning_Knowledge/Asembly) | x86 architecture, registers, basic assembly instructions |
| C Language | [C](file:///D:/02_Learning_Knowledge/C) | Data structures, algorithms, pointers, dynamic memory |
| C# (.NET) | [C#](file:///D:/02_Learning_Knowledge/C#) | Object-oriented programming, .NET applications |
| Computer Vision | [CV](file:///D:/02_Learning_Knowledge/CV) | Digital image processing, OpenCV, computer vision |
| Web Frontend | [Html-Css-Js](file:///D:/02_Learning_Knowledge/Html-Css-Js) | HTML5, CSS3, modern ECMAScript / JavaScript |
| Java | [Java](file:///D:/02_Learning_Knowledge/Java) | Java Core, OOP, concurrency, algorithm sets |
| Machine Learning | [Machine_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning) | Scikit-learn, regression, classification, deep learning |
| PHP | [PHP](file:///D:/02_Learning_Knowledge/PHP) | Backend scripting, MVC architecture, MySQL persistence |
| Python | [PythonProject](file:///D:/02_Learning_Knowledge/PythonProject) | Algorithms, automation scripts, data wrangling |
| Python Master | [Python_Master](file:///D:/02_Learning_Knowledge/Python_Master) | Table B certification prep, mock tests, COS Pro |
| Quantum Computing | [Quantum_Computing](file:///D:/02_Learning_Knowledge/Quantum_Computing) | Quantum algorithms, katas, Qiskit/Qsim, QFT, QEC |
| React | [React](file:///D:/02_Learning_Knowledge/React) | ReactJS, component lifecycle, hooks, Single Page Apps |
| Databases / SQL | [SQL](file:///D:/02_Learning_Knowledge/SQL) | Relational schema design, query optimization |
| Embedded / Robotics | [TestArm](file:///D:/02_Learning_Knowledge/TestArm) | DENSO robotic arm control, ArUco markers, Arduino |
| UI / UX Design | [UI-UX](file:///D:/02_Learning_Knowledge/UI-UX) | Interface design, wireframes, layout, design tokens |
| GCI World 2026 | [GCI_World_2026_September](file:///D:/02_Learning_Knowledge/GCI_World_2026_September) | Global Competition Initiative curriculum & assignments |
| AMD AI Academy | [AMD_AI_Academy_AI_Agents_101](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101) | AI Agents 101 architectures and tool-use code |

---

## 3. exFAT Filesystem & Git Operational Rules

The workspace resides on an exFAT formatted SSD (Kingston XS2000). exFAT does not store POSIX file permissions.

To prevent Git `dubious ownership` warnings:
1. Windows: Execute `git config --global --add safe.directory "D:/02_Learning_Knowledge"`.
2. macOS: Execute `git config --global --add safe.directory "/Volumes/KINGSTON/02_Learning_Knowledge"`.
3. Dependency Isolation: Dependencies (`node_modules`, `.venv`, `vendor`) and build caches MUST NOT be committed to git to protect exFAT I/O throughput. Secrets, credentials, and API keys MUST NEVER be committed under any circumstances.
