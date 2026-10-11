# Báo cáo Dogfood Hệ sinh thái Polaris - Aurora - Vega
**Chủ đề:** Machine Learning · Module 1 & Module 2.1 (Linear Regression)  
**Ngày thực hiện:** 2026-10-11  
**Mục tiêu:** Thử nghiệm toàn diện luồng phát triển khóa học dựa trên chứng cứ (Evidence-based Course Building) từ brief, nghiên cứu tài liệu, trích xuất dữ kiện, sinh lộ trình, xuất bài giảng Aurora và trích xuất thẻ nhớ Vega.

---

## 1. Tổng quan Sản phẩm và Đường dẫn Tài nguyên

Toàn bộ quy trình dogfood được thực thi khép kín trong không gian làm việc của môn học theo các nguyên tắc quản trị dữ liệu:

| Bước | Sản phẩm đầu ra | Đường dẫn tệp | Mô tả kỹ thuật |
|:---|:---|:---|:---|
| 1. Khởi tạo brief | `brief.json` | `polaris/brief.json` | Xác định mục tiêu M1 + M2.1, 3 chuẩn đầu ra có kiểm tra, 3 giờ/tuần, trỏ lộ trình ra `polaris/ROADMAP.polaris.md`. |
| 2. Nghiên cứu tài liệu | Shortlist nghiên cứu | `polaris/research/2026-10-11-machine-learning.md` | 48 tài liệu được tìm kiếm và xếp hạng tự động qua 4 nhà cung cấp không cần API key (OpenAlex, arXiv, Wikipedia, CrossRef). |
| 2. Đăng ký nguồn | `sources.json` & captures | `polaris/sources.json`<br>`polaris/captures/` | 10 nguồn tài liệu được xác thực và trích xuất nội dung sạch, bao gồm giáo trình nội bộ và bài giảng Stanford CS229. |
| 3. Trích xuất dữ kiện | `facts.json` | `polaris/facts.json` | 15 dữ kiện toán học và thực nghiệm có định vị chính xác (`lines`, `[p. N]`, `#anchor`), gắn nguồn đối chiếu chéo `crossCheck`. |
| 4. Sinh lộ trình | `roadmap.json`<br>`ROADMAP.polaris.md` | `polaris/roadmap.json`<br>`polaris/ROADMAP.polaris.md` | Lộ trình chuẩn 10 mục bằng tiếng Việt, tích hợp sơ đồ quan hệ Mermaid, bài tập 3 tầng có Definition of Done (DoD), câu hỏi ẩn đáp án. |
| 5. Xuất bài giảng | Cấu trúc khóa học<br>Đề cương bài học | `Slides/ml-polaris/course.json`<br>`polaris/lessons/*.outline.md` | Cấu hình Aurora Slides 2 bài học (midnight, ocean) và 2 tệp đề cương sư phạm đầy đủ theo khung Polaris. |
| 5. Dựng Slide bài học | Slide HTML hoàn chỉnh | `Slides/ml-polaris/02-m2-1-hoi-quy-tuyen-tinh-normal-equation-va-gradient-descent/` | 15 slide Apple-keynote hoàn chỉnh (HTML 1096 KB) với đầy đủ sơ đồ Mermaid, công thức LaTeX, Lâu đài ký ức, trang vở chép tay, predict slide và quiz. |
| 5. Ảnh kiểm tra slide | Ảnh contact sheet | `%TEMP%/aurora_contact_sheet.jpg` | Ảnh toàn bộ 15 slide được render qua headless browser để kiểm định bố cục trực quan. |
| 6. Ứng viên thẻ nhớ | Danh sách ứng viên Vega | Báo cáo chi tiết ở Mục 4 | 12 thẻ flashcard trích xuất tất định (5 palace, 5 notebook, 2 quiz), không ghi vào bộ sưu tập thật. |

---

## 2. Nhật ký Vượt qua các Cổng Kiểm định Chất lượng (Quality Gates)

Quá trình dogfood tuân thủ nghiêm ngặt các cổng kiểm soát chất lượng tự động:

### 2.1 Cổng Brief & Sources Gate
- **Brief Gate:** Đạt chuẩn. 3 mục tiêu đầu ra [O1], [O2], [O3] đều có tiêu chí kiểm tra định lượng rõ ràng; thời lượng 3 giờ/tuần khớp lịch học Tuần 1.
- **Sources Gate:** Đạt chuẩn. Tồn tại ít nhất 3 nguồn tài liệu gốc mang nhãn `course` (`math_primer.py`, `GIAO_TRINH_CHI_TIET_TOAN_BO_KHOA_HOC.md`, `regression.py`). Tất cả 10 nguồn đều có điểm đánh giá chất lượng (1-5) kèm lý do giải trình.

### 2.2 Cổng Facts Gate (Thử thách & Điều chỉnh)
- **Lần kiểm tra 1 (Thất bại - 4 lỗi):**
  - Hệ thống phát hiện các dữ kiện F3, F10, F13, F14 chứa ký tự số (`1e-5`, `0`, `1D`, `R^2`) nhưng thiếu mảng nguồn đối chiếu chéo `crossCheck` và không gắn nhãn `unverified`.
- **Hành động khắc phục:**
  - Bổ sung nguồn đối chiếu chéo từ tài liệu chính thống: F3 (`S7`), F10 (`S2`, `S7`), F13 (`S3`), F14 (`S6`).
- **Lần kiểm tra 2 (Thành công):**
  - Toàn bộ 15 dữ kiện đạt chuẩn kiểm định. Lệnh `polaris_check` xác nhận 0 lỗi, 0 cảnh báo.

### 2.3 Cổng Aurora Build & Audit Gate
- **Lần dựng 1 (Lỗi cú pháp schema):**
  - Slide dạng `statement` sử dụng thuộc tính `eyebrow` thay vì `kicker` theo quy định của schema `StatementSlide`. Hệ thống từ chối tạo file và thông báo lỗi chính xác.
- **Lần dựng 2 (Cảnh báo layout):**
  - Tiêu đề slide `title` có 9 từ, vượt ngưỡng khuyến nghị (<= 7 từ), khiến kích thước chữ tự động co lại 80%.
  - Slide `predict` dùng thuộc tính `code` thay vì liên kết `file` + `lines`.
- **Lần dựng 3 (Hoàn hảo):**
  - Rút gọn tiêu đề xuống 7 từ: `"Hồi quy: ++Normal Equation++ & ++Gradient Descent++"`.
  - Tạo tệp mã nguồn thực nghiệm `verify_ols.py` và liên kết qua `file: "verify_ols.py"`, trích dẫn dòng 1-8.
  - Kết quả kiểm định `aurora_audit`: **15 slides, 0 error(s), 0 warning(s)**.

---

## 3. Đánh giá Thực tế: Ưu điểm và Hạn chế Cần Cải tiến

### 3.1 Polaris MCP (Course Architect)
- **Điểm mạnh:**
  - Quy trình 4 bước (Brief -> Research -> Facts -> Roadmap) hoạt động logic và có tính cưỡng chế cao, ngăn chặn việc tạo ra các lộ trình chung chung thiếu căn cứ.
  - Cơ chế tự động bắt nội dung (`capture.ts`) xử lý tệp PDF trực tiếp rất mạnh: tải tệp bài giảng Stanford CS229 và phân tách từng trang có đánh dấu `[p. N]` tự động qua `pdftotext`/`pypdf`.
  - Khả năng xuất đề cương bài giảng Aurora (`export.ts`) cực kỳ chi tiết, chuyển hóa toàn bộ facts, misconceptions và bài tập thành dàn ý sư phạm trực quan.
- **Vấn đề phát hiện:**
  - *Độ nhạy số học quá mức (False Positives trong Facts Gate):* Biểu thức chính quy `/\b(\d+(?:[.,]\d+)?%?|\d{4}-\d{2}-\d{2})\b/` bắt cả những ký hiệu toán học hoặc thuật ngữ lập trình quen thuộc như `R^2` (bắt số 2), `1D`/`2D` (bắt số 1, 2), `O(d^3)` (bắt số 3). Điều này buộc người lập phải bổ sung `crossCheck` cho cả những khái niệm không phải là dữ liệu thống kê hay số đo thực nghiệm.
  - *Bị chặn bởi tường lửa nhà xuất bản khi nghiên cứu:* Khi truy vấn DOI bài báo qua Crossref, các đường dẫn tới ACM Digital Library hoặc IOP Publishing gặp mã lỗi `HTTP 403 Forbidden` hoặc bị Radware Bot Manager chặn bằng Captcha. Polaris chưa có cơ chế tự động chuyển hướng sang link Open Access tương ứng (thông qua Unpaywall hoặc OpenAlex).
  - *Tài liệu hướng dẫn chưa đầy đủ:* Thuộc tính `roadmapPath` trong `brief.json` hoạt động rất tốt để tránh ghi đè lên lộ trình chính của người học, nhưng chưa được ghi chép trong tài liệu hướng dẫn (`polaris_guide brief`).

### 3.2 Aurora Slides MCP (Lesson Engine)
- **Điểm mạnh:**
  - Bộ kiểm định tĩnh và kiểm tra bố cục tại thời điểm build (`aurora_create_deck`) hoạt động rất hiệu quả, phát hiện ngay các trường không hợp lệ và đo đạc tràn chữ chính xác.
  - Tích hợp sâu với Lâu đài ký ức (Memory Palace) hỗ trợ 2 chế độ `learn` và `recall`, kết hợp mượt mà với trang vở ghi chép (`notebook`) và slide dự đoán (`predict`).
  - Slide `diagram` kết xuất mã Mermaid thành SVG nội suy đồng bộ màu theo chủ đề (ocean), hiển thị sắc nét và tải nhanh không phụ thuộc mạng bên ngoài.
- **Vấn đề phát hiện:**
  - *Bất đồng nhất tên thuộc tính tiêu đề phụ:* Tất cả các slide (`title`, `section`, `bullets`, `diagram`, `formula`, `quiz`) đều dùng khóa `eyebrow`, riêng slide `statement` lại bắt buộc dùng khóa `kicker`. Sự không nhất quán này dễ gây lỗi gõ nhầm.
  - *Giới hạn độ dài phương án Quiz:* Bộ linter cảnh báo nếu phương án trắc nghiệm vượt quá 15-20 từ. Đối với các câu hỏi so sánh thuật toán Machine Learning hoặc giải thích sai lầm toán học, độ dài này đòi hỏi phải cắt gọt câu rất gắt gao.

### 3.3 Vega MCP (Card Generator)
- **Điểm mạnh:**
  - Trích xuất thẻ từ `deck.json` cực kỳ chuẩn xác và thông minh. Không bỏ sót bất kỳ trạm ghi nhớ nào từ Lâu đài ký ức, phân loại đúng thẻ công thức (`formula`), thẻ quy tắc (`rule`), thẻ mỏ neo (`anchor`) từ slide notebook, và lấy trọn vẹn câu hỏi kèm giải thích từ slide quiz.
  - Mỗi thẻ đều có định danh nguồn gốc rõ ràng (`origin: { kind, path, locator }`), giúp truy vết ngược lại chính xác vị trí bài học.
- **Vấn đề phát hiện:**
  - *Mặt trước thẻ công thức hơi khái quát:* Khi trích xuất từ notebook, mặt trước của thẻ công thức được đặt mặc định là `"Công thức (Trang vở M2.1: Hồi quy tuyến tính OLS)"`. Nếu một bài học có nhiều công thức, người học khi lật thẻ sẽ không biết hệ thống đang hỏi công thức nào (MSE hay Normal Equation). Nên đưa thêm nhãn hoặc tên biến vào mặt trước của thẻ.

---

## 4. Kết quả Trích xuất Thẻ nhớ Vega (Trích mẫu 5 thẻ)

Tổng số thẻ ứng viên trích xuất được từ `deck.json`: **12 thẻ** (5 thẻ Lâu đài ký ức, 5 thẻ Trang vở chép tay, 2 thẻ Trắc nghiệm).

Dưới đây là 5 ví dụ tiêu biểu trích xuất nguyên văn từ kết quả của `vega_candidates` (không ghi vào bộ sưu tập thực tế):

### Ví dụ 1: Thẻ Lâu đài ký ức (Palace Station)
- **Loại thẻ:** `palace`
- **Mặt trước (Front):** `Một vòng căn nhà nhớ quy trình hồi quy · Trạm: Cửa chính ra vào`
- **Mặt sau (Back):** `Đọc dữ liệu CSV`
- **Mỏ neo (Hook):** `Mở cửa thấy tệp StudentScore.xls rơi ra, bóc lớp vỏ thấy ruột là định dạng CSV`
- **Nguồn gốc (Origin):** `slide 8 (palace), station: Cửa chính ra vào`
- **Nhãn (Tags):** `["aurora", "palace"]`

### Ví dụ 2: Thẻ Lâu đài ký ức (Palace Station)
- **Loại thẻ:** `palace`
- **Mặt trước (Front):** `Một vòng căn nhà nhớ quy trình hồi quy · Trạm: Kệ để giày`
- **Mặt sau (Back):** `Chuẩn hóa thang đo`
- **Mỏ neo (Hook):** `Đặt chiếc cân StandardScaler cạnh kệ giày: gọt hai đặc trưng về cùng một cỡ`
- **Nguồn gốc (Origin):** `slide 8 (palace), station: Kệ để giày`
- **Nhãn (Tags):** `["aurora", "palace"]`

### Ví dụ 3: Thẻ Công thức từ Trang vở (Formula)
- **Loại thẻ:** `basic`
- **Mặt trước (Front):** `Công thức (Trang vở M2.1: Hồi quy tuyến tính OLS)`
- **Mặt sau (Back):** `\hat{\mathbf{y}} = X\mathbf{w} + b, \quad J(\mathbf{w}) = \frac{1}{n}\|X\mathbf{w} - \mathbf{y}\|^2`
- **Nguồn gốc (Origin):** `slide 9 (notebook)`
- **Nhãn (Tags):** `["aurora", "notebook", "formula"]`

### Ví dụ 4: Thẻ Quy tắc cốt lõi (Core Rule)
- **Loại thẻ:** `basic`
- **Mặt trước (Front):** `Quy tắc cốt lõi: Trang vở M2.1: Hồi quy tuyến tính OLS`
- **Mặt sau (Back):** `R^2 có thể âm trên test set nếu dự đoán tệ hơn trung bình`
- **Nguồn gốc (Origin):** `slide 9 (notebook)`
- **Nhãn (Tags):** `["aurora", "notebook", "rule"]`

### Ví dụ 5: Thẻ Trắc nghiệm Nhận thức sai lệch (Quiz)
- **Loại thẻ:** `basic`
- **Mặt trước (Front):** `Phát biểu nào sau đây là ĐÚNG về hệ số xác định R² trong hồi quy tuyến tính?`
- **Mặt sau (Back):** `Đáp án đúng: R² có thể nhận giá trị âm trên tập test nếu sai số dự đoán lớn hơn phương sai dữ liệu. (Chính xác! Theo định nghĩa R² = 1 - (SS_res / SS_tot), khi SS_res > SS_tot thì R² < 0.)`
- **Nguồn gốc (Origin):** `slide 12 (quiz)`
- **Nhãn (Tags):** `["aurora", "quiz"]`

---

## 5. Danh sách Hành động Cải tiến Ưu tiên (Prioritized Improvements)

| Mức ưu tiên | Thành phần | Hạng mục cải tiến đề xuất | Lý do kỹ thuật |
|:---:|:---|:---|:---|
| **P0** | Polaris MCP (`check.ts`) | Bỏ qua việc kiểm tra đối chiếu chéo số học (`crossCheck`) đối với các danh từ toán học/ký hiệu thứ nguyên thông dụng (`R^2`, `1D`, `2D`, `3D`, `L1`, `L2`, `O(d^3)`). | Giảm thiểu lỗi cảnh báo giả mạo (false positives) khiến người dùng phải thêm nguồn đối chiếu gượng ép cho các quy ước toán học thông thường. |
| **P1** | Polaris MCP (`capture.ts`) | Bổ sung cơ chế fallback tự động sang đường dẫn Open Access (qua OpenAlex / Unpaywall) khi fetch DOI bị chặn bởi `403 Forbidden` hoặc Bot Captcha. | Giúp quá trình capture tài liệu khoa học tự động không bị đứt gãy khi gặp các trang phân phối trả phí. |
| **P1** | Aurora Slides MCP (`schema.ts`) | Hỗ trợ thuộc tính `eyebrow` như một bí danh (alias) tương thích cho `kicker` trên slide dạng `statement`. | Đảm bảo trải nghiệm nhất quán trên mọi kiểu slide, tránh lỗi cú pháp không đáng có cho người soạn bài giảng. |
| **P2** | Vega MCP (`candidates.ts`) | Cải tiến tiêu đề mặt trước cho thẻ công thức trích xuất từ slide `notebook` bằng cách đọc từ khóa chú giải (ví dụ: gán tên công thức vào trường `term`). | Giúp thẻ flashcard hiển thị rõ ràng câu hỏi trên mặt trước thay vì chỉ ghi chung chung `"Công thức"`. |
| **P2** | Polaris MCP (`guide.ts`) | Bổ sung tài liệu giải thích rõ trường `roadmapPath` trong lệnh `polaris_start` và schema `BriefSchema`. | Giúp người dùng dễ dàng cấu hình đường dẫn lưu file lộ trình tùy biến mà không lo đè lên lộ trình chính. |
