# HƯỚNG DẪN BẬC THẦY VỞ GHI CHÉP CORNELL 3 CỘT (MASTER CORNELL NOTEBOOK GUIDE)
## Phương Pháp Luận Ghi Chép Tay Khoa Học, Thần Kinh Học Nhận Thức & Kỷ Luật Học Tập Dành Cho Nhà Khoa Học Dữ Liệu
### Chương trình: Global Consumer Intelligence (GCI World 2026 September) · Matsuo-Iwasawa Lab · Đại học Tokyo

---

## 1. THẦN KINH HỌC NHẬN THỨC: VÌ SAO NHÀ KHOA HỌC DỮ LIỆU PHẢI CHÉP TAY?

### 1.1. Cạm Bẫy Ảo Tưởng Năng Lực (The Illusion of Competence)
Trong kỷ nguyên số, người học lập trình và trí tuệ nhân tạo thường mắc phải hội chứng "Ảo tưởng năng lực" (Illusion of Competence). Khi xem video bài giảng hoặc đọc code mẫu trên màn hình máy tính, vỏ não thị giác ghi nhận luồng thông tin một cách thụ động, tạo cảm giác sai lầm rằng bản thân đã hiểu sâu và làm chủ kiến thức. Tuy nhiên, hành động sao chép - dán (copy-paste) mã nguồn hoặc bấm chạy các ô lệnh có sẵn trong Jupyter Notebook / Google Colab bỏ qua hoàn toàn quá trình mã hóa nhận thức (cognitive encoding). Khi đối mặt với một màn hình soạn thảo trống hoặc một bài toán thực tế chưa có lời giải, người học lập tức rơi vào trạng thái bế tắc vì thông tin chưa bao giờ được nạp vào trí nhớ dài hạn (Long-term Memory).

### 1.2. Cơ Chế Thần Kinh Của Hành Động Viết Tay
Các nghiên cứu kinh điển về tâm lý học nhận thức, tiêu biểu là công trình của Pam A. Mueller (Đại học Princeton) và Daniel M. Oppenheimer (Đại học California, Los Angeles, 2014) mang tên *"The Pen Is Mightier Than the Keyboard: Advantages of Longhand Over Laptop Note Taking"*, đã chứng minh rằng:
1. **Quá trình nén và xử lý tạo sinh (Generative Note-Taking):** Tốc độ viết tay chậm hơn tốc độ gõ bàn phím khoảng 2–3 lần. Giới hạn vật lý này buộc não bộ không thể chép nguyên văn từng chữ như một máy ghi âm. Người học bắt buộc phải lắng nghe, thấu hiểu, chắt lọc từ khóa, tóm lược ý chính và cấu trúc lại thông tin theo sơ đồ tư duy của riêng mình trước khi hạ bút.
2. **Kích hoạt mạng lưới liên kết đa giác quan (Sensorimotor Integration):** Viết tay huy động đồng thời Vỏ não vận động (Motor Cortex), Vỏ não cảm giác soma (Somatosensory Cortex), Hồi góc (Angular Gyrus) và Vùng Broca. Cử động tinh tế của các đầu ngón tay khi uốn lượn từng nét chữ tạo ra dấu vết thần kinh vật lý (Engram) bền vững hơn rất nhiều so với hành vi gõ các phím nhựa đồng nhất trên bàn phím.
3. **Kích hoạt Hệ thống Lưới Kích hoạt Não bộ (Reticular Activating System - RAS):** Động tác viết tay gửi tín hiệu mạnh mẽ đến vùng cuống não RAS, đóng vai trò như một bộ lọc tập trung tối cao, triệt tiêu các tác nhân gây xao nhãng từ thông báo mạng xã hội và màn hình thiết bị.

### 1.3. Tính Cấp Thiết Đặc Thù Trong Học Máy & Khoa Học Dữ Liệu
Khoa học Dữ liệu và Học máy không thuần túy là việc gõ mã lệnh Python; bản chất cốt lõi của ngành là sự kết hợp giữa:
- **Tư duy hình học và không gian véc-tơ:** Các khái niệm như siêu phẳng phân tách trong Hồi quy tuyến tính, khoảng cách Euclidean trong phân cụm K-Means, phép chiếu trực giao bảo toàn phương sai trong PCA, hay luồng phân nhánh nhị phân trong Cây quyết định đều đòi hỏi tư duy hình học trực quan. Việc tự tay vẽ các trục tọa độ, các điểm dữ liệu và ranh giới quyết định giúp người học khắc sâu bản chất topo của không gian đặc trưng.
- **Biểu thức toán học đa chiều:** Các công thức toán tối ưu hóa (MSE, Gradients, Cross-Entropy Loss) chứa ma trận, chỉ số dưới, chỉ số trên và tổng sigma. Gõ bàn phím rất mất thời gian để soạn thảo toán, trong khi viết tay cho phép thể hiện các biểu thức KaTeX phức tạp chỉ trong vài giây.
- **Dòng chảy dữ liệu (Data Pipelines):** Quy trình chuyển hóa dữ liệu từ dạng thô sang dạng sẵn sàng nạp vào mô hình (Raw Data -> Cleaned Data -> Scaled Features -> Model -> Prediction) là một lưu đồ tuần tự. Vẽ tay các khối hộp và mũi tên giúp trực giác hóa toàn bộ đường ống, ngăn ngừa triệt để các sai lầm chết người như Rò rỉ Dữ liệu (Data Leakage).

---

## 2. KIẾN TRÚC VỞ GHI CHÉP CORNELL 3 CỘT (THE 3-COLUMN CORNELL ARCHITECTURE)

Hệ thống ghi chép Cornell truyền thống do Giáo sư Walter Pauk (Đại học Cornell) phát triển vào thập niên 1950 gồm 2 cột (Cues và Notes) cùng 1 khung Summary. Để tối ưu hóa đặc thù của ngành Khoa học Dữ liệu, Matsuo-Iwasawa Lab áp dụng biến thể **Cornell 3 Cột (Data Science 3-Column Cornell System)** với cấu trúc phân bổ diện tích trang giấy chuẩn xác:

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ METADATA HEADER: Tên Buổi Học | Ngày Tháng | Khái Niệm Cốt Lõi | Thời Lượng Dự Kiến (10%)   │
├─────────────────────────┬──────────────────────────────────────────┬────────────────────────┤
│ CỘT 1: TỪ KHÓA & GỢI NHỚ│ CỘT 2: SƠ ĐỒ TƯ DUY & CÔNG THỨC TOÁN     │ CỘT 3: HÀNH ĐỘNG & MÃ  │
│      (Cues / 20%)       │       (Core Mechanics / 50%)             │   (Actions / 30%)      │
│                         │                                          │                        │
│ • Thuật ngữ chuyên môn  │ • Sơ đồ khối tư duy (ASCII / Mindmaps)   │ • Quy tắc ra quyết định│
│ • Câu hỏi Active Recall │ • Công thức toán học đóng khung KaTeX    │ • Mẫu code 3-5 dòng    │
│ • Điểm đối lập then chốt│ • Lưu đồ luồng dữ liệu (Data Pipelines)  │ • Cạm bẫy kỹ thuật     │
│ • Ký hiệu ghi nhớ nhanh │ • Phân phối & Ranh giới quyết định hình học│ • Kiểm toán dữ liệu  │
│                         │                                          │                        │
│ (Dùng bàn tay hoặc bìa  │ (Không chép văn xuôi dài dòng; dùng ký   │ (Tập trung cú pháp API │
│  giấy che lại khi tự    │  hiệu khối, mũi tên nhân quả A -> B)     │  và tham số then chốt) │
│  kiểm tra phản xạ)      │                                          │                        │
├─────────────────────────┴──────────────────────────────────────────┴────────────────────────┤
│ KHUNG TÓM TẮT CUỐI TRANG: 3 Điểm Chốt Hạ (Bottom Line) + 1 Câu Hỏi Tự Phản Biện (15%)      │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.1. Chi Tiết Vai Trò Từng Phân Khu Trên Trang Vở

#### A. Metadata Header (Phần Đầu Trang - 10% Diện Tích)
Mỗi trang vở bắt buộc phải ghi rõ các trường định danh chuẩn:
- **Tên khóa học & Đơn vị:** GCI World 2026 September · Matsuo-Iwasawa Lab (UTokyo).
- **Mã phiên học:** Buổi 0 (Prep), Buổi 1 (Orientation), hoặc các tuần tiếp theo.
- **Ngày thực hiện & Thời gian ước tính:** Ghi ngày giờ chép tay (e.g., 2026-09-24, 25 phút).
- **Mục tiêu phiên học:** Một câu ngắn gọn xác định năng lực cần đạt sau phiên ghi chép.

#### B. Cột 1: Từ Khóa & Gợi Nhớ (Retrieval Cues - 20% Độ Rộng Lề Trái)
- **Mục đích:** Đóng vai trò như các mỏ neo tinh thần (Mental Anchors) và câu hỏi gợi mở cho các buổi ôn tập truy hồi chủ động (Active Recall).
- **Nội dung:**
  - Tên thuật ngữ bằng tiếng Anh chuẩn xác (e.g., *Selection Bias*, *Overfitting*, *Multicollinearity*).
  - Câu hỏi truy vấn bắt đầu bằng "Tại sao...?", "Khi nào...?", "Khác biệt giữa A và B là gì?".
  - Ký hiệu phân loại mức độ quan trọng (sao, chấm than, dấu mũi tên).
- **Quy tắc sử dụng:** Khi ôn bài, dùng một tấm thẻ hoặc bàn tay che toàn bộ Cột 2 và Cột 3. Chỉ nhìn vào Cột 1 và buộc não bộ phải diễn giải to thành tiếng nội dung của Cột 2 và Cột 3.

#### C. Cột 2: Sơ Đồ Tư Duy & Công Thức Toán (Core Mechanics & Mathematics - 50% Thân Giữa)
- **Mục đích:** Nắm bắt sâu sắc cơ chế vận hành, bản chất toán học và luồng quan hệ nhân quả.
- **Nội dung:**
  - Tuyệt đối KHÔNG chép văn xuôi liên tục dạng đoạn văn dài.
  - Sử dụng sơ đồ khối ASCII hoặc sơ đồ phân nhánh: `[Đầu vào X] -> [Hộp biến đổi] -> [Đầu ra y]`.
  - Công thức toán học được viết chuẩn xác theo cú pháp KaTeX, đóng khung viền vuông nổi bật. Ghi rõ ý nghĩa từng biến số bên dưới công thức.
  - Vẽ biểu đồ hình học (đường hồi quy OLS cùng khoảng dư sai số $e_i$, cây nhị phân rẽ nhánh, biểu đồ hộp Box Plot kèm hàng rào Tukey).

#### D. Cột 3: Hành Động Thực Tế & Code Minh Họa (Actions, Code Signatures & Pitfalls - 30% Lề Phải)
- **Mục đích:** Chuyển hóa lý thuyết ở Cột 2 thành năng lực thực thi mã nguồn và phòng tránh lỗi sai trong dự án thực tế.
- **Nội dung:**
  - Chỉ chép các khối code Python vi mô từ 3 đến 5 dòng (micro-code snippets). Tuyệt đối không chép cả file script dài vào vở.
  - Nêu rõ tên thư viện, tên lớp, tên hàm và các đối số quan trọng (e.g., `pd.get_dummies(..., drop_first=True)`).
  - Cảnh báo cạm bẫy kỹ thuật kinh điển (Common Pitfalls) bằng mực màu phân biệt (e.g., cấm dùng `fit_transform` trên tập Test; cấm `shuffle=True` trên dữ liệu chuỗi thời gian).
  - Tiêu chí kiểm toán dữ liệu nhanh (e.g., `df.isnull().sum()`, `df.shape`).

#### E. Khung Tóm Tắt & Phản Biện Cuối Trang (Summary Box - 15% Đáy Trang)
- **Mục đích:** Buộc não bộ phải thực hiện bước trừu tượng hóa bậc cao (High-level Abstraction), nén toàn bộ kiến thức của trang giấy thành bản chất cô đặc nhất.
- **Nội dung:**
  - **3 Điểm Chốt Hạ (The 3 Bottom Lines):** 3 gạch đầu dòng súc tích, mỗi dòng không quá 20 từ, nêu bật nguyên lý nền tảng.
  - **1 Câu Hỏi Tự Phản Biện (Active Recall Challenge):** Một câu hỏi hóc búa mang tính tình huống thực tế hoặc bẫy tư duy, đòi hỏi người học phải tự liên kết các mắt xích kiến thức trong trang để giải quyết.

---

## 3. TRANG BỊ & DỤNG CỤ VẬT LÝ KHUYẾN NGHỊ (STATIONERY SPECIFICATION)

Để trải nghiệm ghi chép tay đạt hiệu quả cao nhất và không gây mỏi cơ tay trong các phiên học tập kéo dài, học viên NÊN chuẩn bị các trang bị sau:

### 3.1. Sổ Tay Vật Lý (Notebook)
- **Khổ giấy:** Khổ **B5** ($176 \times 250\text{ mm}$) hoặc **A4** ($210 \times 297\text{ mm}$). Khổ A5 quá nhỏ, không đủ không gian chia 3 cột và vẽ sơ đồ dữ liệu; khổ A3 quá cồng kềnh.
- **Định dạng trang:** Sổ kẻ ô vuông (Grid Paper $5 \times 5\text{ mm}$) hoặc sổ chấm bi (Dot-Grid Paper). Dòng kẻ ô vuông hỗ trợ vẽ trục tọa độ, bảng ma trận và sơ đồ khối thẳng hàng mà không cần dùng thước quá nhiều lần.
- **Định lượng giấy:** Tối thiểu **$100\text{ gsm}$** (gam trên mỗi mét vuông). Tránh các loại giấy mỏng $70–80\text{ gsm}$ vì mực bút gel hoặc bút dạ sẽ bị thấm sang mặt sau (Bleed-through/Ghosting), làm hỏng tính thẩm mỹ và khả năng đọc lại.

### 3.2. Hệ Thống Mã Màu Bút (Color-Coding Protocol)
Để thị giác có thể phân tách thông tin tức thì trong 0.5 giây khi quét mắt qua trang vở, người học BẮT BUỘC tuân thủ hệ thống mã hóa 3 màu mực chuẩn mực:
- **Màu 1 — Mực Đen hoặc Xanh Đen (Cấu trúc nền tảng):** Chiếm 70% nội dung trang. Dùng cho tiêu đề, văn bản định nghĩa, sơ đồ khối ASCII và khung kẻ cột.
- **Màu 2 — Mực Đỏ hoặc Cam (Cảnh báo & Cạm bẫy):** Chiếm 15% nội dung. Dùng cho các cảnh báo lỗi nghiêm trọng, bẫy rò rỉ dữ liệu (Data Leakage), bẫy đa cộng tuyến, các lưu ý bị trừ điểm hoặc vi phạm quy chế.
- **Màu 3 — Mực Xanh Lá Cây hoặc Tím (Toán học & Mã lệnh):** Chiếm 15% nội dung. Dùng để đóng khung các công thức KaTeX, ký hiệu toán học ($w, b, \sigma, \mu, R^2$) và các hàm API quan trọng trong Python (`StandardScaler`, `DecisionTreeClassifier`, `Optuna`).

### 3.3. Dụng Cụ Phụ Trợ
- Thước kẻ nhựa trong suốt 20 cm để kẻ 3 đường phân chia cột trong vòng 15 giây đầu mỗi buổi học.
- Bút nhớ dòng (Highlighter) màu pastel (vàng nhạt hoặc xanh bạc hà nhạt) để làm nổi bật từ khóa trong Cột 1. Tránh màu quá đậm làm che khuất nét chữ.

---

## 4. GIAO THỨC KỶ LUẬT 3 GIAI ĐOẠN (THE 3-PHASE HABIT PROTOCOL)

Một buổi học lý thuyết hoặc thực hành chuẩn mực của GCI World bắt buộc phải tuân thủ quy trình 3 giai đoạn khép kín:

```text
[ Giai đoạn 1: 5 Phút ] ──> [ Giai đoạn 2: 30-40 Phút ] ──> [ Giai đoạn 3: 5 Phút ]
  Chuẩn bị trang vở           Ghi chép tay sâu (Pen-First)     Tóm tắt & Phản xạ cuối trang
  Kẻ 3 cột, ghi Header        Chép sơ đồ, công thức, code      Viết 3 Điểm chốt hạ, tự giải
```

### 4.1. Giai Đoạn 1: Chuẩn Bị Trang Vở (Pre-Lecture Setup — 5 Phút)
- Mở sổ tay, dùng thước kẻ vạch 2 đường thẳng dọc trang để chia thành 3 cột theo tỷ lệ $20\% - 50\% - 30\%$.
- Kẻ một đường ngang cách mép trên $3\text{ cm}$ để tạo Header; kẻ một đường ngang cách mép dưới $4\text{ cm}$ để tạo Summary Box.
- Điền đầy đủ thông tin vào Header: Tên bài học, Mã phân đoạn (Micro-Session ID), Ngày tháng.
- Lướt nhanh qua tài liệu đề cương (`buoi0_handwritten_notebook_syllabus.md` hoặc `buoi1_handwritten_notebook_syllabus.md`) để nắm danh sách từ khóa Cột 1, ghi sẵn các từ khóa vào Cột 1 để tạo bộ khung đón nhận thông tin.

### 4.2. Giai Đoạn 2: Ghi Chép Tay Sâu — Ưu Tiên Bút Mực Trước Khi Mở Máy (Pen-First Focus — 30–40 Phút)
- **Quy tắc Vàng:** TUYỆT ĐỐI KHÔNG mở trình duyệt web hoặc phần mềm gõ code (Jupyter/Colab/VS Code) trong giai đoạn này. Máy tính để ở trạng thái tắt màn hình hoặc chuyển sang chế độ tập trung (Do Not Disturb).
- Theo dõi bài giảng hoặc đọc kỹ nội dung lý thuyết.
- Tự tay phác thảo sơ đồ tư duy vào Cột 2. Vẽ các hộp trạng thái, mũi tên chuyển dịch dữ liệu.
- Chép từng bước các công thức toán KaTeX. Viết chậm rãi để hiểu rõ từng thành phần biến số (ví dụ: trong MSE, tại sao lại lấy hiệu số trước khi bình phương, tại sao chia cho $n$).
- Chép mã lệnh vi mô 3–5 dòng vào Cột 3. Chú thích rõ vai trò của từng đối số tham số.
- Đánh dấu màu đỏ các cạm bẫy kỹ thuật cần lưu ý.

### 4.3. Giai Đoạn 3: Tóm Tắt & Tự Phản Biện (Post-Session Summary — 5 Phút)
- Sau khi hoàn thành nội dung bài học, tạm dừng 1 phút để mắt và não bộ nghỉ ngơi.
- Nhìn lại toàn bộ trang vở, tự đặt câu hỏi: *"Nếu chỉ được giữ lại 3 điều quan trọng nhất từ trang này để đi thi hoặc phỏng vấn, đó là 3 điều gì?"*
- Viết 3 điều đó vào khung **3 Điểm Chốt Hạ (Bottom Line)** ở đáy trang.
- Đọc to câu hỏi **Active Recall Check** và nhẩm câu trả lời trong đầu mà không nhìn lại Cột 2 hay Cột 3. Nếu còn ngập ngừng, lật lại kiểm tra ngay.

---

## 5. GIAO THỨC ÔN TẬP LẶP LẠI NGẮT QUÃNG & TRUY HỒI CHỦ ĐỘNG (SPACED REPETITION & ACTIVE RECALL)

Ghi chép xong mà không ôn tập thì sau 7 ngày, đường cong lãng quên Ebbinghaus (Ebbinghaus Forgetting Curve) sẽ xóa sạch hơn $80\%$ lượng thông tin vừa nạp. Để biến tri thức thành phản xạ bản năng, người học BẮT BUỘC áp dụng giao thức ôn tập sau:

```text
[ T+0: Ngay sau buổi ] ──> [ T+1: Sau 24 Giờ ] ──> [ T+3: Sau 3 Ngày ] ──> [ T+7: Trước Tuần Mới ]
  Điền Summary Box          Ôn Cột 1 (Cover-Recite)    Giải nhanh bài tập      Tổng hợp toàn Session
  (5 phút)                  (10 phút)                  (15 phút)               (30 phút)
```

### 5.1. Kỹ Thuật "Che & Tự Diễn Giải" (Cover-and-Recite Technique)
1. Dùng một tấm bìa cứng hoặc bàn tay trái che kín toàn bộ Cột 2 (Sơ đồ/Công thức) và Cột 3 (Code/Hành động).
2. Mắt chỉ nhìn vào Cột 1 (Từ khóa & Gợi nhớ).
3. Với mỗi từ khóa hoặc câu hỏi trong Cột 1:
   - Buộc miệng phải phát âm thành tiếng câu trả lời giải thích bản chất khái niệm.
   - Dùng một tờ giấy nháp vẽ nhanh lại sơ đồ khối hoặc viết lại công thức toán học từ trí nhớ.
4. Mở tấm bìa ra đối chiếu với Cột 2 và Cột 3:
   - Nếu trả lời đúng hoàn toàn và vẽ chuẩn xác: Đánh dấu tích xanh vào cạnh từ khóa.
   - Nếu trả lời sai, quên công thức hoặc sót cạm bẫy: Đánh dấu tròn đỏ. Lặp lại việc đọc lại nội dung đó 2 lần.

### 5.2. Lịch Trình Lặp Lại Ngắt Quãng (Spaced Repetition Schedule)
- **Mốc $T+0$ (Ngay sau khi học xong):** Hoàn thành Summary Box và trả lời câu hỏi tự phản xạ (5 phút).
- **Mốc $T+1$ (Sau 24 giờ):** Mở vở thực hiện kỹ thuật Cover-and-Recite cho toàn bộ trang của buổi học hôm trước (10 phút).
- **Mốc $T+3$ (Sau 3 ngày):** Chỉ kiểm tra lại các mục có đánh dấu tròn đỏ. Thực hiện bài tập vi mô tương ứng trên máy tính (15 phút).
- **Mốc $T+7$ (Sau 7 ngày — trước khi bắt đầu bài học mới):** Dành 20–30 phút tham gia **Buổi Ôn Tập Tổng Kết (Review / Synthesis Session)** để xâu chuỗi toàn bộ các trang vở của Session lớn, vẽ bản đồ khái niệm tổng thể và kiểm toán mức độ sẵn sàng.

---

## 6. BẢN MẪU TRANG VỞ CORNELL ĐIỂN HÌNH (EXEMPLAR CORNELL PAGE)

Dưới đây là một ví dụ trực quan mẫu về trang vở Cornell hoàn chỉnh cho chủ đề **Hồi Quy Tuyến Tính & Hàm Mất Mát OLS** thuộc Buổi 0:

```text
═════════════════════════════════════════════════════════════════════════════════════════════════
KHÓA HỌC: GCI World 2026 September · Matsuo-Iwasawa Lab (ĐH Tokyo)
BUỔI HỌC: Buổi 0 (Prep) | MICRO-SESSION: 0.4 | NGÀY: 2026-09-24 | THỜI GIAN: 40 Phút
MỤC TIÊU: Hiểu bản chất hình học OLS, hàm mất mát MSE và đánh giá mô hình không rò rỉ dữ liệu.
─────────────────────────────────────────────────────────────────────────────────────────────────
CỘT 1: TỪ KHÓA & GỢI NHỚ │ CỘT 2: SƠ ĐỒ TƯ DUY & CÔNG THỨC TOÁN     │ CỘT 3: HÀNH ĐỘNG & CODE
─────────────────────────┼──────────────────────────────────────────┼────────────────────────────
* Linear Regression      │ 1. Phương trình siêu phẳng tuyến tính:   │ * Import Scikit-learn:
  (Hồi quy tuyến tính)   │    y_hat = w_1*x_1 + ... + w_m*x_m + b   │   from sklearn.linear_model
                         │    w: Trọng số (Weights / Slope)         │     import LinearRegression
* Hỏi: Ý nghĩa hình học  │    b: Điểm cắt trục tung (Intercept)     │   from sklearn.metrics
  của w và b?            │                                          │     import mean_squared_error
                         │ 2. Hình học OLS & Phần dư sai số (Residual)│
                         │    y                                     │ * Khởi tạo & Huấn luyện:
                         │    ▲        *(y_i)                       │   model = LinearRegression()
                         │    │       /|                            │   model.fit(X_tr, y_tr)
                         │    │      / | e_i = y_i - y_hat_i        │
                         │    │     /  v                            │ * Dự báo & Đánh giá:
                         │    │    /---(y_hat_i) Siêu phẳng         │   y_pred = model.predict(X_te)
                         │    │   /                                 │   mse = mean_squared_error(
                         │    └──/─────────────────────► x          │           y_te, y_pred)
                         │                                          │   r2 = model.score(X_te, y_te)
                         │ 3. Hàm mất mát Mean Squared Error (MSE): │
                         │    MSE = (1/n) * SUM_{i=1}^n (y_i - y_hat_i)^2│ * Cạm bẫy kỹ thuật:
                         │                                          │   Tuyệt đối KHÔNG tính R2
* OLS Loss Mechanism     │    • Bình phương sai số e_i để phạt      │   trên tập Train rồi kết
  (Cơ chế phạt sai số)   │      cực nặng các điểm ngoại lai lớn.    │   luận mô hình hoàn hảo.
                         │    • OLS cực tiểu hóa MSE bằng nghiệm    │   Train R2 = 0.99 nhưng
* Hỏi: Vì sao bình       │      giải tích đóng (Normal Equation):   │   Test R2 = 0.40 -> Bệnh
  phương sai số e_i?     │      w = (X^T * X)^(-1) * X^T * y        │   Quá Khớp (Overfitting)!
─────────────────────────┴──────────────────────────────────────────┴────────────────────────────
KHUNG TÓM TẮT & PHẢN XẠ CUỐI TRANG (SUMMARY BOX)
1. 3 Điểm Chốt Hạ (Bottom Line):
   - Hồi quy tuyến tính OLS tìm siêu phẳng tối ưu hóa bằng cách cực tiểu hóa tổng bình phương phần dư (MSE).
   - Hàm mất mát MSE phạt theo hàm bậc hai đối với sai số lớn, khiến mô hình cực kỳ nhạy cảm với dữ liệu ngoại lai.
   - Luôn luôn đánh giá hiệu năng tổng quát hóa trên tập Test độc lập chưa từng tham gia huấn luyện.
2. Active Recall Check:
   *Nếu một điểm dữ liệu ngoại lai có khoảng cách sai số e_i tăng gấp 3 lần, giá trị phạt đóng góp vào hàm
   mất mát MSE của điểm đó sẽ tăng lên gấp bao nhiêu lần?*
═════════════════════════════════════════════════════════════════════════════════════════════════
```

---

## 7. QUY ĐỊNH TUÂN THỦ KỶ LUẬT (DISCIPLINARY REQUIREMENTS - RFC 2119)

1. Học viên **BẮT BUỘC (MUST)** chuẩn bị sẵn vở viết tay và kẻ sẵn cấu trúc 3 cột trước mỗi phiên học lý thuyết.
2. Học viên **KHÔNG ĐƯỢC PHÉP (MUST NOT)** sao chép mã nguồn trực tiếp vào máy tính trước khi hoàn thành việc ghi chép từ khóa, vẽ sơ đồ và viết công thức vào vở.
3. Học viên **NÊN (SHOULD)** sử dụng hệ thống mã hóa 3 màu mực (Đen - Đỏ - Xanh lá/Tím) để tối đa hóa khả năng nhận diện trực quan của não bộ.
4. Học viên **PHẢI (REQUIRED)** hoàn thành khung Tóm tắt 3 Điểm Chốt Hạ và trả lời câu hỏi tự phản biện cuối trang trước khi gập vở.
5. Học viên **BẮT BUỘC (MUST)** thực hiện quy trình kiểm tra che-tự diễn giải (Cover-and-Recite) tại các mốc ôn tập lặp lại ngắt quãng $T+1, T+3, T+7$.
