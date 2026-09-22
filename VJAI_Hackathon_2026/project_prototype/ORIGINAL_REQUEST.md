# Original User Request

## 2026-09-08T05:47:56Z

Phát triển trọn gói một giải pháp ứng dụng Agentic AI dự thi Vietnam Japan AI Hackathon 2026 (Chủ đề: Agentic AI for Sustainable Goals), bao gồm: Kiến trúc đa tác nhân (LangGraph/CrewAI), Backend API (FastAPI), Giao diện người dùng (Streamlit/React), và Bộ tài liệu Pitch Deck chuẩn thi đấu tại TiB Tokyo.

Working directory: d:\02_Learning_Knowledge\VJAI_Hackathon_2026\project_prototype

## Requirements

### R1. Lựa chọn Bài toán Thực tế & Track Dự thi
Xác định một bài toán nhức nhối cụ thể (Real Problem) thuộc 1 trong 6 Tracks của VJAI Hackathon 2026 (ví dụ: Track 2 - Tự động hóa kế toán SME, hoặc Track 3 - Nông nghiệp chính xác / Tối ưu phát thải CO2), có đối tượng thụ hưởng rõ ràng và chỉ số tác động bền vững đo lường được (Measurable Impact).

### R2. Phát triển Hạt nhân Agentic AI (Multi-Agent Engine)
Xây dựng hệ thống tác nhân tự chủ với đầy đủ:
- Mô hình Supervisor Orchestrator điều phối các Worker Agents chuyên môn.
- Vòng lặp ReAct, phân tách nhiệm vụ (Planning) và cơ chế tự phản ánh (Self-Reflection / Guardrails).
- Danh mục công cụ thực thi (Tool Calling) kết nối API bên ngoài hoặc cơ sở dữ liệu.
- Bộ nhớ ngắn hạn (Context Buffer) và bộ nhớ dài hạn (Vector Database).

### R3. Giao diện Người dùng & Kịch bản Demo Khả thi (Feasible Prototype)
Xây dựng giao diện web trực quan hiển thị luồng suy nghĩ của Agent theo thời gian thực (Streaming token), có dữ liệu mẫu đặt sẵn (Preset demo cases) và video dự phòng 60 giây đảm bảo khả năng chạy mượt mà trên sân khấu Tokyo Innovation Base.

### R4. Bộ Pitch Deck 10 Slide Chuẩn Quốc tế
Soạn thảo bộ slide thuyết trình 10 trang định dạng PDF/Markdown bao quát trọn vẹn: Problem, Existing Flaws, Agentic Solution, System Architecture, Live Demo flow, Measurable Sustainable Impact, Business Model, Roadmap và Team.

## Acceptance Criteria

### Tính Độc lập & Tự chủ của Agent
- [ ] Agent tự chủ giải quyết luồng công việc từ đầu đến cuối mà không cần can thiệp từng bước của con người.
- [ ] Có ít nhất 3 công cụ (Tools) được gọi tự động dựa trên phân tích ngữ cảnh.
- [ ] Có cơ chế bắt lỗi và tự sửa sai (Self-Correction loop) khi tool trả về kết quả không hợp lệ.

### Tính Khả thi Kỹ thuật & Đo lường
- [ ] Backend FastAPI khởi chạy thành công, không phát sinh lỗi phụ thuộc.
- [ ] Giao diện Web hiển thị kết quả xử lý của Agent dưới 5 giây.
- [ ] Có bảng số liệu định lượng chứng minh tác động bền vững (Ví dụ: Giảm X% thời gian, tiết kiệm Y% chi phí).
