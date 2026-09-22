# Original User Request

## 2026-09-20T15:02:13Z

# Teamwork Project Prompt — Draft

> Status: Ready for launch — awaiting user approval
> Goal: Craft prompt → get user approval → delegate to teamwork_preview
> Requested team: [none — teamwork routes from the description]

Nghiên cứu và tổng hợp toàn bộ tài liệu khóa học GCI World 202609 (slides, notebooks) thành các bản tóm tắt ngắn gọn, đầy đủ, và hệ thống để người dùng ôn tập và học thuật hiệu quả.

Working directory: d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes
Integrity mode: benchmark

## Requirements

### R1. Tóm tắt lý thuyết theo chủ đề
Đọc và trích xuất lý thuyết cốt lõi từ các slide và tài liệu, tạo thành các ghi chú (Markdown notes) riêng biệt cho từng chủ đề (VD: Python cơ bản, Thống kê, Regression, Classification). Bỏ qua các tài liệu thủ tục không liên quan.

### R2. Trích xuất Code Python cốt lõi
Lọc ra các cú pháp và đoạn code Python quan trọng nhất từ các Jupyter Notebooks, đưa vào phần tóm tắt lý thuyết của chủ đề tương ứng.

### R3. Hệ thống Flashcards (Active Recall)
Tạo danh sách các câu hỏi Hỏi/Đáp (Flashcards) cuối mỗi bài tóm tắt để người dùng tự kiểm tra kiến thức theo phương pháp Active Recall.

### R4. Sơ đồ tư duy trực quan
Sử dụng Mermaid.js để vẽ sơ đồ tư duy (Mindmaps) hoặc sơ đồ luồng (Flowcharts) mô tả các khái niệm, quy trình phân tích dữ liệu hoặc thuật toán phức tạp.

## Acceptance Criteria

### Verification & Quality
- [ ] Từng tài liệu tóm tắt chủ đề (Markdown) phải có ít nhất một sơ đồ Mermaid.
- [ ] Từng tài liệu tóm tắt chủ đề phải kết thúc bằng ít nhất 5 câu hỏi Flashcard (Hỏi/Đáp).
- [ ] Các đoạn code Python được trích xuất phải có chú thích (comments) giải thích rõ chức năng.
- [ ] Một agent đánh giá độc lập (Reviewer) xác nhận rằng các đề mục chính trong tài liệu gốc đã được tóm lược đầy đủ vào bản note mà không bị sót ý quan trọng.
