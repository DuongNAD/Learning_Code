# Original User Request

## 2026-09-18T12:15:21Z

# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Craft prompt → get user approval → delegate to teamwork_preview
> Requested team: Đội ngũ đầy đủ (Full team)

Nghiên cứu và phân tích tổng quan cấu trúc cuộc thi IMLC, cùng với nền tảng kiến thức (trực quan kết hợp toán học cơ bản) cho 5 bài toán trong đề Qualification Round 2026. Mục tiêu là xây dựng tài liệu ôn tập mà không giải trực tiếp bài tập. Nhóm làm việc với quy mô lớn (full team) để rà soát toàn diện.

Working directory: d:\02_Learning_Knowledge\IMLC_2026
Integrity mode: development

## Requirements

### R1. Phân tích tổng quan IMLC
Trình bày cấu trúc, định dạng và các chủ đề thường gặp của cuộc thi IMLC, liên hệ với các kỳ thi ML tương tự để học viên có cái nhìn toàn cảnh.

### R2. Tổng hợp kiến thức 5 bài toán (PDF)
Phân tích nền tảng lý thuyết cho các chủ đề: ML Lifecycle, Decision Trees, Polynomial Regression & Regularization, RLHF & KL Divergence, AI Ethics/Deployment. Nội dung phải kết hợp giải thích trực quan và công thức toán học ở mức độ vừa phải (ví dụ: loss function, đạo hàm cơ bản).

### R3. Không cung cấp lời giải
Tuyệt đối không giải trực tiếp hoặc cung cấp đáp án cho các câu hỏi cụ thể trong đề (A, B, C, D, E). Chỉ đóng vai trò hướng dẫn lý thuyết.

## Acceptance Criteria

### Đánh giá chất lượng (Agent-as-judge Rubric)
- [ ] Tài liệu có phần giới thiệu chi tiết về format cuộc thi IMLC.
- [ ] Chủ đề "Regularization" và "RLHF Drift" có ít nhất một đoạn giải thích bằng khái niệm và một đoạn minh họa bằng công thức toán học.
- [ ] Kiểm tra chéo toàn bộ tài liệu để đảm bảo KHÔNG có đáp án trực tiếp cho các số liệu/câu hỏi trong đề thi.
- [ ] Mỗi chủ đề có đính kèm một danh sách các từ khóa (keywords) để người học tự tra cứu thêm.
