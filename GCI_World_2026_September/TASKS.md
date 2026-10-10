---
document_type: project_task_board
project: GCI World 2026 September
version: 2.1.0
last_updated: 2026-10-01
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
focus_board: file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md
central_tasks: file:///D:/02_Learning_Knowledge/TASKS.md
rfc2119_compliance: strict
emoji_policy: none
---

# GCI World 2026 September - Task Board

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
Active Focus Board: [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md)
System Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md)
Project Overview: [README.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/README.md)

## Task Maintenance Rules (RFC 2119)
- Standardized Schema: All tasks MUST follow the tag format `- [ ] [Deadline: YYYY-MM-DD HH:mm] [Priority: P0/P1/P2] Description`.
- Task Preservation: AI agents MUST NEVER delete existing tasks.
- Status Transitions: Task status MUST ONLY be transitioned between `[ ]` and `[x]`, and status change to completed MUST occur ONLY IF verification criteria are met.
- Task Placement: Newly identified micro-tasks MUST be appended to the end of the appropriate section.
- Local Authority: Local operations within this project directory MUST update this file directly.
- Session Homework Onboarding Workflow: For each new session, AI agents MUST check Drive/local storage for new files, prepare a Vietnamese briefing in `04_Assignments/Homework_Session_X/README.md` with requirements, tools, and datasets, initialize the folder workspace, and leave implementation code for the learner to write independently.

## 1. Setup & Onboarding
- [ ] [Deadline: 2026-09-24 12:00] [Priority: P1] Kiểm tra tên Slack: Đảm bảo Display Name là Duongne2000 (trùng với tên trên Omnicampus).
- [ ] [Deadline: 2026-09-24 12:00] [Priority: P1] Đọc kỹ Cẩm nang Sinh viên (Notion Student Guide).
- [x] [Deadline: 2026-10-08 18:00] [Priority: P0] Làm Khảo sát điểm danh Buổi 1 (Attendance Survey) trên Omnicampus (Status: OK).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Thiết lập quy tắc giao tiếp và quản lý task tự động với DeepTutor.
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Lưu Bookmark các công cụ (đã lưu sẵn trong thư mục [02_Shortcuts](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/02_Shortcuts)).

## 2. Session 2 Preparation & Core Curriculum
- [x] [Deadline: 2026-09-24 19:00] [Priority: P0] Chuẩn bị nội dung Buổi 2 (2026-09-24): Xử lý dữ liệu hiệu năng cao với NumPy.
- [ ] [Deadline: 2026-09-24 19:00] [Priority: P1] Ôn tập và thực hành các thao tác mảng nhiều chiều (vectorized operations, broadcasting, indexing).
- [ ] [Deadline: 2026-09-25 23:59] [Priority: P2] Luyện tập Chủ động (Active Recall): Ôn tập 7 bài note tổng hợp trong thư mục [study_notes](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/study_notes).
- [x] [Deadline: 2026-09-25 23:59] [Priority: P2] Hỏi đáp và đối chiếu bài tập qua phương pháp Socratic với DeepTutor.
- [ ] [Deadline: 2026-10-15 17:00] [Priority: P1] Chuẩn bị Buổi 5: chạy Exercise_Regression_Level_0 và Exercise_Classification_Level_0 theo [roadmap/ROADMAP.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/roadmap/ROADMAP.md) Module 5.
- [ ] [Deadline: 2026-10-18 23:59] [Priority: P2] Ôn tổng hợp A (Module 2-4: NumPy, Pandas, Visualization) theo [roadmap/ROADMAP.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/roadmap/ROADMAP.md) mục 5.2.

## 3. Coursework & Practical Assignments
- [x] [Deadline: 2026-10-08 18:00] [Priority: P0] Homework: Giải quyết `HW1 for Session2.ipynb` trong thư mục [04_Assignments/Homework_Session_2](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/04_Assignments/Homework_Session_2) (Status: 提出済 - Đạt 3/3 điểm tối đa).
- [ ] [Deadline: 2026-10-15 18:00] [Priority: P1] Hoàn thành đầy đủ các bài tập tự luyện và notebook thực hành theo từng tuần.
- [ ] [Deadline: 2026-10-22 18:00] [Priority: P1] Data Competition: Phân tích dữ liệu, huấn luyện mô hình và submit ít nhất 1 lần lên nền tảng Omnicampus.
- [ ] [Deadline: 2026-11-05 18:00] [Priority: P0] Final Assignment: Hoàn thành bài tập lớn cuối khóa đúng hạn và đúng tiêu chí nghiệm thu.
- [x] [Deadline: 2026-09-24 19:00] [Priority: P1] Thực hành: Hoàn thiện template `numpy_benchmark_template.py` tại [04_Assignments/Homework_Session_2](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/04_Assignments/Homework_Session_2), đảm bảo NumPy khớp kết quả với vòng lặp và đạt zero errors.
- [x] [Deadline: 2026-10-15 18:00] [Priority: P0] Homework: Khởi tạo và giải quyết bài tập HW2 Session 3 (Pandas & Data Wrangling) tại [04_Assignments/Homework_Session_3](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/04_Assignments/Homework_Session_3) (Status: Hoàn thành - Đạt 3.0/3.0 điểm tối đa).
- [ ] [Deadline: 2026-10-22 18:00] [Priority: P0] Homework: Giải quyết bài tập HW3 Session 4 (Pareto Analysis & Decile Grouping) tại [04_Assignments/Homework_Session_4](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/04_Assignments/Homework_Session_4) (Status: Đã đồng bộ tài liệu, khởi tạo README.md, cheatsheet, dataset anime.csv và main.py scaffold).

## 4. Completed Milestones
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Giải nén dữ liệu: Đọc và phân tích cấu trúc file `GCI World_202609-20260920T135018Z-1-001.zip`.
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Xác định mục tiêu học tập (Bước 1-3): Elicit project idea, xác định format tài liệu (Markdown, Flashcards, Mindmap), và cấp quyền (Integrity mode).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Thiết lập Tiêu chí Nghiệm thu (Bước 4-9): Xây dựng `prompt_draft.md` hoàn chỉnh cho hệ thống Teamwork AI.
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Khởi chạy Hệ thống Đa Đặc vụ (Teamwork): Khởi chạy `teamwork_preview` và giám sát quá trình tổng hợp kiến thức.
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Nghiệm thu tài liệu (Victory): Hoàn thành 7 file Markdown tổng hợp lưu vào thư mục [study_notes](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/study_notes).
- [x] [Deadline: 2026-09-24 19:00] [Priority: P2] Hoàn thành Hệ thống Học liệu Vi mô & Slide Tương tác: Nghiệm thu Victory Confirmed (180/180 tests pass) gồm slide động HTML/Markdown, đề cương chép tay Cornell 3 cột, lộ trình phân mảnh 3–5 buổi nhỏ + 1 buổi ôn tập củng cố.
- [x] [Deadline: 2026-09-25 02:20] [Priority: P1] Hoàn thành Hệ thống Học liệu Explorable ThreeUI: Nghiệm thu Victory Confirmed (209/209 tests pass) gồm ThreeUIEngine phản ứng 60fps, WebGL ambient shader, Explorable Decks Buổi 1 & 2, Cornell Boilerplates và Master Hub Portal.

## 5. Sprint 3 Knowledge Synthesis & Documentation
- [x] [Deadline: 2026-10-01 21:00] [Priority: P0] Bóc băng toàn diện 3 video Session 2 (Opening, Lecture, Closing) lưu trữ tại 06_Notes_Transcripts/ (Status: OK).
- [x] [Deadline: 2026-10-02 18:00] [Priority: P0] Biên soạn tài liệu bài giảng tổng hợp Lecture_02_Detailed_Notes.md chuẩn học thuật trong 06_Notes_Transcripts/ (Status: Hoàn thành).
- [x] [Deadline: 2026-10-02 21:00] [Priority: P1] Biên soạn đề cương chép tay Cornell buoi2_handwritten_notebook_syllabus.md (3 cột, 5 module) trong syllabus/ (Status: Hoàn thành).
- [x] [Deadline: 2026-10-03 12:00] [Priority: P1] Tích hợp lộ trình thực hành vi mô Buổi 2 (Micro-2.1 đến Micro-2.5 + Session 2.S) vào roadmap/micro_practice_roadmap.md (Status: Hoàn thành).
- [x] [Deadline: 2026-10-03 18:00] [Priority: P1] Cập nhật ma trận đối soát chương trình đào tạo roadmap/curriculum_alignment_matrix.md bổ sung Buổi 2 (Status: Hoàn thành).

## 6. Sprint 3 Slide Modernization & Interactive Explorable Decks
- [ ] [Deadline: 2026-10-02 12:00] [Priority: P0] Dọn dẹp triệt để các file slide cũ không đạt chất lượng trong thư mục slides/ theo yêu cầu người dùng.
- [ ] [Deadline: 2026-10-03 23:59] [Priority: P0] Xây dựng hệ thống slide tương tác hiện đại Buổi 2 (NumPy Architecture, Axes, Broadcasting, Slicing) bằng Reveal.js/CDN trong slides/buoi2/.
- [ ] [Deadline: 2026-10-04 12:00] [Priority: P1] Tích hợp 3 widget tương tác trực quan (interactive components: bộ nhớ strides, mô phỏng broadcasting và speed benchmark) vào slide Buổi 2.
- [ ] [Deadline: 2026-10-04 18:00] [Priority: P1] Cập nhật lại slide Buổi 0 và Buổi 1 đồng bộ với giao diện slide tương tác thế hệ mới.

## 7. Coursework, Logistics & Autograder Deadlines
- [x] [Deadline: 2026-10-08 11:00] [Priority: P0] Khảo sát điểm danh Buổi 1 (Attendance Survey) trên OmniCampus (Status: Hoàn thành).
- [ ] [Deadline: 2026-10-08 11:00] [Priority: P0] Khảo sát điểm danh Buổi 2 (Attendance Survey) trên OmniCampus (Hạn chót 11:00 AM UTC, không nộp muộn).
- [x] [Deadline: 2026-10-08 11:00] [Priority: P0] Nộp bài tập tuần 1 (HW1 - HW1 for Session2.ipynb) trên OmniCampus Autograder (Status: Đạt 3/3 điểm tối đa).
- [ ] [Deadline: 2026-10-03 20:00] [Priority: P2] Kiểm tra hiển thị tài liệu và liên kết trên master portal README.md và INDEX.md.
- [ ] [Deadline: 2026-10-04 20:00] [Priority: P1] Chạy bộ kiểm thử tự động pytest (test_threeui_explorable_engine.py, test_syllabus_and_slides.py) đảm bảo 100% pass.
- [ ] [Deadline: 2026-10-11 23:59] [Priority: P0] Kiểm tra trạng thái Attendance Survey Buổi 2 (đã đóng 08/10 11:00 UTC) trên Omnicampus; nếu đã nộp thì tick task Buổi 2 ở trên.
- [ ] [Deadline: 2026-10-15 18:00] [Priority: P0] Nộp Attendance Survey Buổi 3 trên Omnicampus (đóng 11:00 UTC, không nhận nộp muộn; cần tối thiểu 7/14 phiếu).
- [ ] [Deadline: 2026-10-22 18:00] [Priority: P0] Nộp Attendance Survey Buổi 4 trên Omnicampus (đóng 11:00 UTC, không nhận nộp muộn).
- [ ] [Deadline: 2026-10-29 18:00] [Priority: P0] Nộp Attendance Survey Buổi 5 (hạn suy ra theo quy tắc 2 tuần; nộp ngay tối 15/10).
- [ ] [Deadline: 2026-10-29 18:00] [Priority: P0] Homework HW4 (Session 5 Supervised Learning) đạt 3/3 trên Omnicampus (hạn suy ra, xác nhận trong notebook HW4).
- [ ] [Deadline: 2026-10-30 23:59] [Priority: P0] Xác minh hạn chót thật của Competition và Final Assignment sau Buổi 7 (29/10); hạn 22/10 và 05/11 ở mục 3 chưa xác minh. Thêm task mới với hạn đúng và hạn bản nháp sớm hơn 7 ngày.
- [ ] [Deadline: 2026-11-01 23:59] [Priority: P0] Competition: nộp baseline đầu tiên trong 72 giờ sau Buổi 7 và tạo experiments.md (theo [roadmap/ROADMAP.md](file:///D:/02_Learning_Knowledge/GCI_World_2026_September/roadmap/ROADMAP.md) mục 6.1).
- [ ] [Deadline: 2026-11-05 18:00] [Priority: P0] Homework HW5 (Session 6 Model Evaluation) đạt 3/3 trên Omnicampus (hạn suy ra, xác nhận trong notebook HW5).

