# Original User Request

## 2026-09-22T11:25:22Z

Trích xuất toàn bộ thông tin bài giảng từ tệp video bài học AMD AI Academy: AI Agents 101, thực hiện bóc băng âm thanh (transcript có mốc thời gian), phân tích và tổng hợp thành một hệ thống khoá học chuyên sâu toàn diện bao gồm: tài liệu lý thuyết chi tiết, bộ bài tập thực hành code Python chạy được, và bộ đề kiểm tra trắc nghiệm đánh giá năng lực.

Working directory: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101
Integrity mode: development

Input video: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/01_Recordings/01_AI_Agents_101_Full.mov

## Requirements

### R1. Trích xuất âm thanh và Bóc băng (Audio Extraction & Transcript)
Trích xuất luồng âm thanh từ video bài học bằng `ffmpeg`, sau đó phiên âm (transcribe) toàn bộ bài giảng thành văn bản có mốc thời gian (timestamps) rõ ràng. Cung cấp cả bản tiếng Anh gốc và bản dịch tiếng Việt chuẩn xác theo thuật ngữ chuyên ngành AI.

### R2. Biên soạn Giáo trình & Bài giảng chuyên sâu (Curriculum & Lessons)
Dựa trên nội dung bài giảng và tài liệu của AMD, biên soạn hệ thống giáo trình chi tiết giải thích thấu đáo mọi chủ đề:
1. Bản chất và định nghĩa AI Agent so với Traditional LLMs.
2. 4 trụ cột kiến trúc cốt lõi: Perception, Planning & Reasoning, Tool Use & Action, Memory (Short-term & Long-term).
3. Các mô hình thiết kế tiêu biểu (ReAct loop, Reflection, Multi-Agent Collaboration).
4. Hệ sinh thái phần cứng và tối ưu suy luận của AMD (AMD ROCm, Ryzen AI NPU, Radeon/Instinct GPUs).
5. Trực quan hóa kiến trúc bằng các sơ đồ Mermaid chuẩn.

### R3. Bộ bài tập & Mã nguồn thực hành Python (Code Labs & Implementations)
Xây dựng các ví dụ mã nguồn thực hành hoàn chỉnh, có thể chạy kiểm thử độc lập trong thư mục `03_Materials_Code/`:
1. Vòng lặp Agent thuần (ReAct pattern từ đầu không dùng framework phụ thuộc).
2. Tác tử gọi công cụ (Tool Calling / Function Calling) xử lý tác vụ thực tế.
3. Tác tử ghi nhớ phiên làm việc (Conversation Memory & State Management).
4. Ví dụ ứng dụng với các framework hiện đại (LangGraph / CrewAI).
Kèm theo tệp `requirements.txt` và hướng dẫn chạy từng bài tập.

### R4. Hệ thống Đánh giá & Trắc nghiệm ôn tập (Quizzes & Self-Assessment)
Thiết kế bộ câu hỏi trắc nghiệm và tình huống thực tế (15 - 20 câu) phân loại theo các mức độ từ cơ bản đến nâng cao. Mỗi câu hỏi phải có đáp án chính xác kèm phần giải thích cặn kẽ tại sao đúng/sai để người học củng cố kiến thức.

## Acceptance Criteria

### Transcript & Nội dung bài học
- [ ] Tệp transcript bao phủ toàn bộ bài giảng (~19 phút 28 giây) với timestamps rõ ràng được lưu tại `02_Notes_Summaries/transcript.md`.
- [ ] Giáo trình bài học chi tiết được lưu thành các bài giảng có cấu trúc rõ ràng tại `02_Notes_Summaries/`, có tối thiểu 3 sơ đồ Mermaid minh họa kiến trúc.

### Mã nguồn & Kiểm thử
- [ ] Toàn bộ mã nguồn Python trong `03_Materials_Code/` vượt qua kiểm tra cú pháp (`python -m py_compile`) và chạy thử nghiệm thành công không có lỗi runtime.
- [ ] Có tệp `requirements.txt` liệt kê đầy đủ thư viện cần thiết.

### Đánh giá & Trắc nghiệm
- [ ] Tệp `02_Notes_Summaries/quiz_and_assessment.md` chứa tối thiểu 15 câu hỏi trắc nghiệm có đầy đủ đáp án và phân tích chi tiết.
- [ ] Tệp `README.md` tại thư mục gốc của khóa học được cập nhật chỉ mục liên kết đến tất cả các tài liệu, bài tập và video đã tạo.
