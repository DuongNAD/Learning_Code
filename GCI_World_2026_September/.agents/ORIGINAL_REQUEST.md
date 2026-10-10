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

## 2026-09-24T11:26:41Z

# Teamwork Project Prompt — GCI World Knowledge Synthesis & Notebook-First Slide Syllabus

Xây dựng hệ thống học liệu và giáo trình ghi chép chi tiết, module hóa theo cấu trúc micro-learning cho khóa học GCI World 2026 September (Matsuo-Iwasawa Lab, ĐH Tokyo). Bộ tài liệu bao gồm hệ thống slide tối giản (Clean/Minimalist HTML/Markdown slides), tóm tắt lý thuyết để ghi chép vào vở viết tay, và lộ trình bài tập thực hành bám sát bài giảng từ Buổi 0 đến Buổi 1 và các tuần tiếp theo.

Working directory: /Volumes/KINGSTON/02_Learning_Knowledge/GCI_World_2026_September

## Requirements

### R1. Bộ slide bài giảng tối giản & trực quan (Minimalist Clean Slides)
Thiết kế hệ thống slide học tập chuẩn giao diện clean, font chữ hiện đại, bố cục rõ ràng, hỗ trợ mở rộng cho từng buổi học (Bắt đầu với Buổi 0 - Preparatory & Buổi 1 - Orientation). Mỗi slide tập trung vào 1 luận điểm duy nhất, có sơ đồ ASCII / Mermaid và công thức chuẩn KaTeX nếu có.

### R2. Đề cương ghi chép vở viết tay (Handwritten Notebook Syllabus)
Biên soạn cấu trúc ghi chép tối ưu cho vở viết tay theo phương pháp Cornell Note hoặc Mindmap 3 cột: (1) Khái niệm/Thuật ngữ cốt lõi, (2) Sơ đồ tư duy / Cơ chế vận hành, (3) Hành động thực tế & Mã code minh họa. Người học có thể mở tài liệu ra chép tay dễ dàng trước khi code.

### R3. Lộ trình thực hành vi mô (Micro-Practice Roadmap)
Chia nhỏ các bài thực hành, notebook và bài tập tuần (Homework & Competition) thành các nhiệm vụ nhỏ từ 15-30 phút, đi kèm tiêu chí nghiệm thu (DoD) rõ ràng và câu hỏi kiểm tra tư duy phản biện.

## Acceptance Criteria

### Tính đầy đủ & Tính chính xác học thuật
- [ ] Tổng hợp đầy đủ thông tin Buổi 0 (Preparatory Materials) kèm video chính thức từ Matsuo Lab (https://youtu.be/q2tRrzyQ27A) và trọn bộ 5 playlist.
- [ ] Phân rã toàn diện 34 slide và 1h09p bài giảng Buổi 1 thành các phân đoạn kiến thức độc lập (Data-driven mindset, AI Moat, 14-week curriculum).

### Tính thẩm mỹ & Khả năng ghi chép
- [ ] Cung cấp slide định dạng web (HTML/CSS độc lập, responsive, theme clean tối giản) hoặc Markdown presentation dễ xem trên mọi thiết bị.
- [ ] Bản đề cương ghi chú được định dạng sẵn bullet, highlight từ khóa, khung tóm tắt giúp việc chép vào vở mạch lạc, không bị ngợp.

## 2026-09-24T11:51:08Z

### User Requirement Clarification
Mỗi buổi học lớn (Session) cần được chia nhỏ thành 3 đến 5 buổi học nhỏ (Micro-sessions, 30–45 phút/buổi). Quy trình học của người học: (1) Mở đề cương ra chép tay vào vở trước (khái niệm + sơ đồ + công thức), (2) Thực hành bài tập nhỏ / trả lời câu hỏi phản xạ. Sau khi hoàn thành xong 3–5 buổi nhỏ của 1 Session, bắt buộc có 1 BUỔI ÔN TẬP TỔNG KẾT (Review / Synthesis Session) để củng cố và xâu chuỗi toàn bộ kiến thức trước khi chuyển sang học bài mới. Hãy đảm bảo lộ trình M3 (Micro-practice roadmap) và tài liệu tổng hợp thể hiện rõ ràng nhịp học 3–5 micro-sessions + 1 review session này!

## 2026-09-24T12:07:30Z

### User Preference Update — Interactive & Dynamic Slides
Người học đặc biệt thích slide động (interactive/dynamic slides), thiết kế đẹp, hiện đại, clean và có thể tương tác trực tiếp trên slide để hiểu sâu bản chất (interactive simulators, steppers, toggleable deep-dives). Hãy đảm bảo các slide HTML tích hợp các module động tương tác trực quan (như Food Truck simulator, Data Flywheel interactive loop, 7-Eleven stepper) và hướng dẫn ghi chép trực quan!

## 2026-09-24T18:39:57Z

# Teamwork Project Prompt — ThreeUI Explorable Interactive Learning System & Slide Engine

Nghiên cứu kiến trúc thẩm mỹ từ MengTo/threeui (Three.js 3D UI, WebGL Shaders, Glassmorphism) kết hợp với triết lý tài liệu tương tác phản ứng (Explorable Explanations / Idyll / Marimo). Xây dựng hệ thống học liệu và slide cuộn tương tác động cao cấp: người học cuộn trang mượt mà, kéo thanh trượt biến đổi công thức toán học và biểu đồ thời gian thực, có khung tóm tắt để chép vào vở viết tay trước khi thực hành, hỗ trợ mở rộng toàn diện cho khóa học GCI World.

Working directory: /Volumes/KINGSTON/02_Learning_Knowledge/GCI_World_2026_September
Integrity mode: development

## Requirements

### R1. Báo cáo nghiên cứu & Kiến trúc thiết kế (Open-Source Research & Design System)
Tổng hợp phân tích mã nguồn MengTo/threeui, Slidev, Motion Canvas, Idyll và Marimo. Thiết lập bộ quy chuẩn thiết kế (Design System Spec): bảng màu Dark/Light chuẩn mực, font Inter & JetBrains Mono, hiệu ứng đổ bóng vi tế, canvas nền nhẹ, cấu trúc trạng thái phản ứng (Reactive State Flow: Slider Input -> Reactive Variable -> KaTeX Formula Update -> Live Chart/Vector Re-render).

### R2. Động cơ học liệu tương tác Explorable Engine (Interactive Explorable Document & Slides)
Xây dựng một bộ khung engine tài liệu tương tác độc lập (Zero-dependency hoặc web-native Canvas/SVG/KaTeX) hỗ trợ 2 chế độ xem:
- Chế độ 1: Cuộn trang mượt mà (Explorable Document) với các thanh trượt điều chỉnh biến số, biểu đồ phản ứng tức thì và công thức toán học biến thiên theo thao tác kéo thả.
- Chế độ 2: Trình chiếu theo từng slide (Presentation Slide Deck) cho các buổi học.
Tích hợp sẵn các mô hình tương tác mẫu cho Buổi 1 (Food Truck censored demand, Compound Data Flywheel, 7-Eleven Tanpin Kanri) và Buổi 2 (NumPy multi-dimensional array broadcasting, vectorization speed benchmark).

### R3. Khung ghi chép vở viết tay vi mô & Bộ mẫu mở rộng (Notebook-First Templates)
Mỗi phần giải thích tương tác đều đi kèm một khung tóm tắt [Chép vào vở] (Cornell 3 cột) hiển thị ngắn gọn các hằng số, công thức bất biến và kết luận nghiệp vụ. Cung cấp bộ template mẫu (Boilerplate) để dễ dàng tạo học liệu tương tác mới cho các tuần tiếp theo (Pandas, Machine Learning, Deep Learning).

## Acceptance Criteria

### Tính trực quan & Tính tương tác phản ứng (Explorable Reactive Depth)
- [ ] Mọi thanh trượt (Slider) đều lập tức cập nhật giá trị số, công thức KaTeX và đồ thị minh họa trong thời gian thực với độ trễ < 16ms (chuẩn 60fps mượt mà).
- [ ] Tích hợp mô phỏng trực quan tương tác đa chiều cho dữ liệu thực tế (Dark Data, Data Flywheel, NumPy Array Slicing/Broadcasting).

### Tính thẩm mỹ & Trải nghiệm người dùng (ThreeUI Aesthetics)
- [ ] Giao diện tối giản, sang trọng theo phong cách ThreeUI (Glassmorphism, viền mảnh tinh tế, phối màu tương phản cao, chuyển đổi Dark/Light mode).
- [ ] Chạy mượt mà 100% trên các trình duyệt hiện đại (Chrome, Safari, Edge) không đòi hỏi cấu hình máy nặng.

### Chuẩn mực học thuật & Chính sách DeepTutor
- [ ] Tuân thủ tuyệt đối quy định không sử dụng biểu tượng cảm xúc (emoji_policy: none).
- [ ] Mã nguồn sạch, có chú thích giải thích rõ ràng và có bộ kiểm thử tự động xác nhận tính toàn vẹn của engine.

