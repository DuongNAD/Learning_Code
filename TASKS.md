---
document_type: system_task_board
version: 2.1.0
last_updated: 2026-09-23
architecture: 2-Tier Task Architecture
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
focus_board: file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md
rfc2119_compliance: strict
emoji_policy: none
---

# Workspace System Task Board & Subproject Router

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
Active Focus Board: [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md)

This board manages workspace-level, cross-cutting infrastructure tasks and routes to project-specific task boards under the 2-Tier Task Architecture.

## 2-Tier Task Architecture Specification
- Macro-Tier (Workspace Focus): [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md) tracks the Top 5 active projects, milestones, checkpoints, deadlines, and today's dynamic mission.
- Micro-Tier (Project Execution): Each active project maintains its own dedicated `TASKS.md` for granular execution steps and sub-checklists.
- System Tier (This File): [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md) tracks cross-cutting workspace maintenance, link integrity, and routing pointers.

## Project Task Board Router (Active Projects)

| Active Subject | Project Directory | Local Task Board |
| :--- | :--- | :--- |
| 1. GCI World 2026 September | [GCI_World_2026_September](file:///D:/02_Learning_Knowledge/GCI_World_2026_September) | [TASKS.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/TASKS.md) |
| 2. Machine Learning | [Machine_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning) | [TASKS.md](file:///D:/02_Learning_Knowledge/Machine_Learning/TASKS.md) |
| 3. Python Master | [Python_Master](file:///D:/02_Learning_Knowledge/Python_Master) | [TASKS.md](file:///D:/02_Learning_Knowledge/Python_Master/TASKS.md) |
| 4. Quantum Computing | [Quantum_Computing](file:///D:/02_Learning_Knowledge/Quantum_Computing) | [TASKS.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/TASKS.md) |
| 5. AMD AI Academy - AI Agents 101 | [AMD_AI_Academy_AI_Agents_101](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101) | [TASKS.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/TASKS.md) |

*Note: Project-specific micro-tasks (Slack display name, Notion student guide, Session 2 NumPy prep, Session 1 attendance survey, HW1 submission) are managed in [GCI_World_2026_September/TASKS.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/TASKS.md).*

## Task Maintenance Rules (RFC 2119)
- Standardized Schema: All tasks MUST follow the tag format `- [ ] [Deadline: YYYY-MM-DD HH:mm] [Priority: P0/P1/P2] Description`.
- AI agents MUST NEVER delete existing tasks.
- Task status MUST ONLY be transitioned between `[ ]` and `[x]`, and status change to completed MUST occur ONLY IF verification criteria are met.
- System/workspace tasks MUST be managed in this file. Project-specific tasks MUST be recorded in the respective local `TASKS.md`.
- Newly identified workspace tasks MUST be appended to the end of the appropriate section.

## Workspace Infrastructure & Cross-Cutting Tasks

### In Progress
- [ ] [Deadline: 2026-09-25 18:00] [Priority: P1] Thiết lập kiểm tra tự động tính toàn vẹn liên kết nội bộ (file:/// link validator script).
- [ ] [Deadline: 2026-09-26 18:00] [Priority: P2] Rà soát định kỳ trạng thái đồng bộ git và dung lượng lưu trữ trên SSD Kingston XS2000.
- [ ] [Deadline: 2026-09-30 18:00] [Priority: P2] Đánh giá và luân chuyển chủ đề từ Backlog sang Active khi có dự án hoàn thành (tuân thủ WIP = 5).

### Completed
- [x] [Deadline: 2026-09-22 23:59] [Priority: P1] Thiết lập kiến trúc Master Knowledge Map tại [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P1] Thiết lập Active Learning Hub và trần WIP bound = 5 tại [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P1] Xây dựng công cụ ngẫu nhiên phần hardware Decision Roulette ([pick_today.py](file:///D:/02_Learning_Knowledge/pick_today.py), [roll_study.bat](file:///D:/02_Learning_Knowledge/roll_study.bat), [roll_study.command](file:///D:/02_Learning_Knowledge/roll_study.command)).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P1] Thiết lập quy tắc giao tiếp và quản lý task tự động với DeepTutor trong [GEMINI.md](file:///D:/02_Learning_Knowledge/GEMINI.md) và [AGENTS.md](file:///D:/02_Learning_Knowledge/AGENTS.md).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Lưu Bookmark các công cụ vào thư mục [02_Shortcuts](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/02_Shortcuts).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P1] Triển khai và chuẩn hóa kiến trúc quản lý task 2 cấp (2-Tier Task Architecture) trên toàn workspace `D:/02_Learning_Knowledge`.
- [x] [Deadline: 2026-09-23 01:00] [Priority: P0] Thiết lập và chuẩn hóa Time & Deadline Sentinel Protocol trên toàn bộ hệ thống tài liệu.
