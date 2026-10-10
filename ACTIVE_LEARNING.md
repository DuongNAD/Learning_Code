---
document_type: active_learning_hub
version: 2.1.0
last_updated: 2026-10-10
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
task_tracker: file:///D:/02_Learning_Knowledge/TASKS.md
wip_limit: 5
rfc2119_compliance: strict
emoji_policy: none
---

# Active Learning Hub & Focus Board

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
System Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md)

## WIP Directive & Operational Bounds
- 2-Tier Architecture: This board serves as the Macro-level router. Granular micro-tasks MUST be maintained inside each active project's dedicated `TASKS.md`. Cross-cutting infrastructure tasks MUST be maintained in central [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md).
- WIP Limit: AI agents and learners MUST enforce a strict ceiling of 5 active subjects. AI agents MUST NEVER exceed 5 active subjects concurrently.
- Promotion Rule: A dormant topic from the backlog MUST NOT be promoted to active status; promotion is permitted ONLY IF an existing active subject is completed or explicitly parked.
- Parsing Invariance: Downstream tools (`pick_today.py`) parse the exact markdown sections `Today's Dynamic Goal` and `Active Projects`. Any edits MUST preserve heading names and bullet key formats (`- Directory:`, `- Tasks:`, `- Milestone:`, `- Checkpoint:`, `- Next Action:`). Heading structure MUST NEVER be altered arbitrarily.
- Time & Deadline Schema: All task items across boards MUST conform to `- [ ] [Deadline: YYYY-MM-DD HH:mm] [Priority: P0/P1/P2] Description`.

## Today's Dynamic Goal
- Date: 2026-10-05
- Subject: GCI World 2026
- Target: Hoàn thiện hàm homework() thực hiện Phân tích Pareto (Decile Analysis) trên tập dữ liệu MyAnimeList tại main.py trong Homework_Session_4: sắp xếp giảm dần theo metric_column, chia n nhóm đều bằng pd.qcut trên rank, tính tỷ lệ phần trăm đóng góp của từng nhóm và trả về pd.Series nhãn 'Group 1' đến 'Group n'.
- Definition of Done (DoD): File main.py tại GCI_World_2026_September/04_Assignments/Homework_Session_4/ thực thi vượt qua 100% test cases cục bộ (Test Case 1, 2, 3) với exit code 0; nộp hàm homework() lên Omnicampus Autograder đạt 3.0/3.0 điểm tối đa.
- Status: In Progress
- Deadline: 2026-10-22 18:00
- Priority: P0

## Active Priority Watchlist & Deadlines
- [x] [Deadline: 2026-09-24 19:00] [Priority: P0] GCI World: Chuẩn bị nội dung Buổi 2 (2026-09-24): Xử lý dữ liệu hiệu năng cao với NumPy.
- [x] [Deadline: 2026-10-08 18:00] [Priority: P0] GCI World: Khảo sát điểm danh Buổi 1 (Attendance Survey Session 1) - Status OK.
- [x] [Deadline: 2026-10-08 18:00] [Priority: P0] GCI World: HW1 for Session 2 - Nộp bài tập tuần (Đã nộp 提出済 - Đạt 3/3 điểm tối đa).
- [ ] [Deadline: 2026-09-26 23:59] [Priority: P1] Machine Learning: Cài đặt thuật toán Ridge và Lasso Regularization, phân tích hiện tượng Co-efficient Shrinkage trong [01_Regression](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning/01_Regression).
- [ ] [Deadline: 2026-09-27 23:59] [Priority: P1] Python Master: Khởi chạy [launch_hub.py](file:///D:/02_Learning_Knowledge/Python_Master/launch_hub.py) và chọn giải bài tập theo từng chuyên đề Bảng B.
- [ ] [Deadline: 2026-09-28 23:59] [Priority: P1] Quantum Computing: Khởi chạy công cụ luyện tập katas qua CLI: python katas/qk.py list.
- [ ] [Deadline: 2026-09-30 23:59] [Priority: P1] AMD AI Academy: Chạy bộ kiểm thử xác thực labs [verify_labs.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/verify_labs.py) sau khi thiết lập môi trường Python 3.11+.
- [ ] [Deadline: 2026-10-15 18:00] [Priority: P0] GCI World: Nộp Attendance Survey Buổi 3 trên Omnicampus (đóng 11:00 UTC, không nhận nộp muộn; cần tối thiểu 7/14 phiếu).

## Active Projects

### 1. GCI World 2026
- Directory: [GCI_World_2026_September](file:///D:/02_Learning_Knowledge/GCI_World_2026_September)
- Tasks: [TASKS.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/TASKS.md)
- Roadmap: [ROADMAP.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/roadmap/ROADMAP.md)
- Milestone: Master exploratory data analysis, Pareto/Decile analysis, and Matplotlib data visualization.
- Checkpoint: HW1 Session 2 đạt 3.0/3.0 điểm; HW2 Session 3 đạt 3.0/3.0 điểm; Đã đồng bộ tài liệu Session 4 từ Google Drive shortcut G:\ vào 03_Materials/04_Visualization và khởi tạo xong không gian làm việc 04_Assignments/Homework_Session_4/ (README.md, main.py scaffold, PARETO_DECIL_CHEATSHEET.md).
- Next Action: Người học triển khai hàm homework() trong main.py và kiểm thử đạt chuẩn trước khi submit Omnicampus.
- Deadline: 2026-10-22 18:00
- Priority: P0

### 2. Machine Learning
- Directory: [Machine_Learning](file:///D:/02_Learning_Knowledge/Machine_Learning)
- Tasks: [TASKS.md](file:///D:/02_Learning_Knowledge/Machine_Learning/TASKS.md)
- Roadmap: [ROADMAP.md](file:///D:/02_Learning_Knowledge/Machine_Learning/Roadmaps/ROADMAP.md)
- Milestone: Master supervised learning algorithms, evaluation metrics, and cross-validation.
- Checkpoint: Lộ trình v2 (2026-10-10) thay lịch cũ; practice_exercises.py mới làm dở bài 1.1/16; chưa có code hồi quy tuyến tính tự cài trong 01_Regression (task cũ đã tick nhưng chưa có file).
- Next Action: M1 + M2.1 (tuần 1): tự cài hồi quy tuyến tính bằng normal equation và gradient descent trên StudentScore, khớp LinearRegression.
- Deadline: 2026-10-18 21:00
- Priority: P1

### 3. Python Master
- Directory: [Python_Master](file:///D:/02_Learning_Knowledge/Python_Master)
- Tasks: [TASKS.md](file:///D:/02_Learning_Knowledge/Python_Master/TASKS.md)
- Roadmap: [ROADMAP.md](file:///D:/02_Learning_Knowledge/Python_Master/Roadmaps/ROADMAP.md)
- Milestone: Complete mock tests and algorithm problem sets for Table B (COS Pro certification).
- Checkpoint: Chẩn đoán 2026-10-10: 30/90 bài luyện PASS (Nhóm 1: 15, Nhóm 2: 14, Nhóm 3: 1, Nhóm 4-6: 0); đề 1 vòng loại 220/1000 (mới làm Q1-Q2).
- Next Action: M0: chạy so_theo_doi.py all, làm tiếp đề 1 Q3-Q10 bấm giờ 40 phút, ghi Sổ lỗi.
- Deadline: 2026-10-13 22:00
- Priority: P1

### 4. Quantum Computing
- Directory: [Quantum_Computing](file:///D:/02_Learning_Knowledge/Quantum_Computing)
- Tasks: [TASKS.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/TASKS.md)
- Roadmap: [ROADMAP.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/Roadmaps/ROADMAP.md)
- Milestone: Execute quantum circuit simulations and foundational katas.
- Checkpoint: Lộ trình v2 (2026-10-10): 0/350 kata; qsim chưa bắt đầu (39 test); máy chưa cài qiskit; phase0 h_test, giao_thoa, bell_test đã chạy.
- Next Action: Tạo venv ngoài SSD, cài qiskit 2.5.1 và qiskit-aer 0.17.2 từ requirements.txt, chạy python katas/qk.py status, bắt đầu M1.
- Deadline: 2026-10-18 21:00
- Priority: P2

### 5. AMD AI Academy - AI Agents 101
- Directory: [AMD_AI_Academy_AI_Agents_101](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101)
- Tasks: [TASKS.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/TASKS.md)
- Roadmap: [ROADMAP.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/04_Roadmaps/ROADMAP.md)
- Milestone: Implement autonomous agent patterns, function calling, and tool-use workflows.
- Checkpoint: Lộ trình v2 (2026-10-10): ghi chú cũ do AI sinh, có nội dung ngoài bài giảng; 4 lab là code tham chiếu với LLM giả lập; verify_labs.py chỉ PASS khi đặt PYTHONUTF8=1.
- Next Action: M0: chạy verify_labs.py với PYTHONUTF8=1 đạt 4/4 PASS, tóm tắt 12 phần video, tạo Sổ lỗi.
- Deadline: 2026-10-17 23:59
- Priority: P2

## Decision Roulette Runner

- Windows Script: [roll_study.bat](file:///D:/02_Learning_Knowledge/roll_study.bat)
- macOS Script: [roll_study.command](file:///D:/02_Learning_Knowledge/roll_study.command)
- CLI Runner: `python D:/02_Learning_Knowledge/pick_today.py`

## Goal Mutation Protocol

| Event | Precondition | State Change | Post-Action |
| :--- | :--- | :--- | :--- |
| Set New Goal | User starts session or runs roulette | Status set to `In Progress` | Record Date, Subject, Target, and DoD. |
| DoD Achieved | Code runs, tests pass, DoD criteria met | Status set to `Completed` | Update subject `Checkpoint` and define `Next Action`. |
| Goal Blocked | Technical impediment or time exhaustion | Status set to `Paused` | Document blocker in subject `Checkpoint`. |

- Goal transitions to `Completed` MUST occur ONLY IF code runs, tests pass, and all DoD criteria are verified.
- Status MUST NEVER be marked `Completed` with failing tests or unverified criteria.

## Backlog

- [React](file:///D:/02_Learning_Knowledge/React): Frontend engineering, component state sync, and custom hooks.
- [NodeJS](file:///D:/02_Learning_Knowledge/NodeJS), [PHP](file:///D:/02_Learning_Knowledge/PHP), [SQL](file:///D:/02_Learning_Knowledge/SQL): Backend APIs, database design, and query optimization.
- [Asembly](file:///D:/02_Learning_Knowledge/Asembly), [TestArm](file:///D:/02_Learning_Knowledge/TestArm): Low-level architecture and robotic arm control.
- [VAIC2026](file:///D:/02_Learning_Knowledge/VAIC2026), [VJAI_Hackathon_2026](file:///D:/02_Learning_Knowledge/VJAI_Hackathon_2026): AI competition projects and pipeline development.
- [UI-UX](file:///D:/02_Learning_Knowledge/UI-UX): Wireframing, interface prototyping, and design system tokens.
- Complete Backlog Catalog: Refer to [INDEX.md - Backlog Catalog](file:///D:/02_Learning_Knowledge/INDEX.md#5-parked-backlog-catalog-dormant-topics) for the full 22-subject catalog.
