# MA TRẬN ĐỐI SOÁT CHƯƠNG TRÌNH ĐÀO TẠO TOÀN DIỆN (COMPREHENSIVE CURRICULUM ALIGNMENT MATRIX)
## Khung Đối Soát Đa Chiều: Micro-Sessions, 14 Tuần Đào Tạo, 8 Bài Tập Omnicampus, Cuộc Thi Machine Learning & Đồ Án Cuối Khóa
### Chương trình: Global Consumer Intelligence (GCI World 2026 September) · Matsuo-Iwasawa Lab · Đại học Tokyo

---

## 1. TỔNG QUAN KIẾN TRÚC ĐÀO TẠO & KHUNG NĂNG LỰC TAM GIÁC

Chương trình đào tạo Global Consumer Intelligence (GCI World 2026 September) do Phòng thí nghiệm Matsuo-Iwasawa (Đại học Tokyo) thiết kế nhằm trang bị cho học viên năng lực giải quyết các bài toán kinh doanh phức tạp bằng phương pháp luận khoa học dữ liệu thực nghiệm. Chương trình được cấu trúc theo 4 giai đoạn tiến hóa nhận thức và bám sát khung năng lực tam giác (Competency Triad):

```text
               ┌────────────────────────────────────────────────────────┐
               │         1. DOMAIN & BUSINESS PROBLEM (60–70%)          │
               │  • Thấu hiểu bài toán nghiệp vụ, phát hiện Dark Data   │
               │  • Chuyển ngữ mong muốn kinh doanh thành KGI/KPI & y   │
               │  • Đánh đổi ma trận chi phí sai lầm (Cost Tradeoff)    │
               └───────────┬────────────────────────────────┬───────────┘
                           │                                │
            ┌──────────────┴──────────────┐  ┌──────────────┴──────────────┐
            ▼                             ▼  ▼                             ▼
┌───────────────────────────────┐              ┌───────────────────────────────┐
│  2. DATA SCIENCE (15%)        │              │  3. DATA ENGINEERING (15%)    │
│  • Thống kê thực nghiệm & EDA │ ◄──────────► │  • Python OOP, NumPy, Pandas  │
│  • Mô hình học máy OLS, Trees │              │  • Xử lý bảng SQL quy mô lớn  │
│  • Đánh giá không rò rỉ dữ liệu│              │  • Tự động hóa đường ống ETL  │
└───────────────────────────────┘              └───────────────────────────────┘
```

### 4 Giai Đoạn Tiến Hóa Nhận Thức 14 Tuần:
1. **Giai đoạn 1: Nền Tảng Dữ Liệu & Điện Toán Ma Trận (Tuần 1 đến Tuần 4):** Định hình tư duy định hướng dữ liệu (Data-driven Mindset) ở Tuần 1, làm chủ điện toán véc-tơ hiệu năng cao với NumPy ở Tuần 2, thao tác bảng dữ liệu phức tạp với Pandas ở Tuần 3, và trực quan hóa phân phối thống kê ở Tuần 4. Lĩnh vực trọng tâm: Data Science và Data Engineering.
2. **Giai đoạn 2: Học Máy Ứng Dụng, Đánh Đổi Sai Số & Tối Ưu Hóa (Tuần 5 đến Tuần 8):** Nắm vững các thuật toán học máy có giám sát kinh điển ở Tuần 5, phân tích ma trận chi phí thực tế ở Tuần 6, khởi động Cuộc thi Machine Learning trên Omnicampus ở Tuần 7 và làm chủ công cụ tự động dò tham số Optuna ở Tuần 8.
3. **Giai đoạn 3: Dữ Liệu Lớn, Tiếp Thị Định Lượng & Chuỗi Thời Gian (Tuần 9 đến Tuần 13):** Ứng dụng bài toán kinh doanh tiếp thị định lượng ở Tuần 9, khai thác cơ sở dữ liệu quan hệ quy mô lớn với SQL ở Tuần 10, học máy không giám sát (K-Means và PCA) ở Tuần 11, phân tích dự báo chuỗi thời gian ở Tuần 12, và bài giảng khách mời doanh nghiệp ở Tuần 13.
4. **Giai đoạn 4: Tốt Nghiệp & Chuyển Giao Giá Trị Doanh Nghiệp (Tuần 14):** Hoàn thiện và nộp Đồ án Kinh doanh Cuối khóa (Final Business Capstone Assignment) ở Tuần 14, thẩm định tính toàn vẹn và xét tuyển danh hiệu xuất sắc tham quan Tokyo Study Tour tại Đại học Tokyo.

---

## 2. MA TRẬN ĐỐI SOÁT CHI TIẾT TỪNG PHÂN ĐOẠN VI MÔ (MICRO-SESSION ALIGNMENT MATRIX)

Bảng dưới đây thiết lập mối liên kết hữu cơ giữa từng phân đoạn học vi mô (Micro-Sessions), phiên ôn tập tổng hợp (Synthesis Sessions) với toàn bộ 14 tuần đào tạo, 8 bài tập tuần, cuộc thi học máy và đồ án tốt nghiệp:

| Phân Đoạn Vi Mô | Tuần Đào Tạo | Trọng Tâm Kiến Thức (Features F01–F32) | Trụ Cột Năng Lực | Bài Tập Tuần (Homework) | Cuộc Thi ML (Competition) | Đồ Án Cuối Khóa (Capstone) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Micro-0.1**<br>DS Mindset & Workflow | Tuần 1<br>(Tuần 2–4 Prep) | F01: 4-Step Workflow<br>F02: Data Taxonomy<br>F18: Pandas Merging | Domain: 50%<br>DS: 30%<br>DE: 20% | Nền tảng cho HW1 (NumPy) & HW2 (Pandas) | Định hình tư duy kiểm chứng thực nghiệm | Xác định bài toán kinh doanh & dữ liệu thô |
| **Micro-0.2**<br>Preprocessing & Scaling | Tuần 3, 5, 8 | F03: Missing Values<br>F04: Dummy Trap<br>F05: Standardization | DS: 40%<br>DE: 60% | HW2 (Data Cleaning)<br>HW4 (Supervised ML) | Bước 2 trong 5 nấc thang: Làm sạch & Mã hóa biến | Tiền xử lý dữ liệu thực tế, chống rò rỉ Z-Score |
| **Micro-0.3**<br>Stats, Correlation & EDA | Tuần 3, 4, 11 | F12: Central Tendency<br>F13: Boxplot & IQR<br>F14: Pearson Correlation | DS: 70%<br>DE: 30% | HW3 (Data Visualization)<br>HW4 (Feature Selection) | Phát hiện quan hệ phi tuyến & loại bỏ ngoại lai | Khảo sát phân phối biến mục tiêu $y$ và các biến $X$ |
| **Micro-0.4**<br>Basic ML & Non-leakage | Tuần 5, 6 | F06: Train/Test Split<br>F07: Linear Regression<br>F08: Decision Tree<br>F15: MSE Metric | DS: 60%<br>Domain: 20%<br>DE: 20% | HW4 (Supervised Models)<br>HW5 (Metrics Evaluation) | Bước 1 & 3: Xây dựng Baseline & Chọn mô hình | Xây dựng mô hình cơ sở (Benchmark Baseline) |
| **Session 0.S**<br>Synthesis & Pipeline Prep | Mốc Chuyển Giao<br>(Prep -> Week 1) | Tổng hợp F01–F18<br>Khép kín Pipeline từ đầu đến cuối | Domain: 40%<br>DS: 40%<br>DE: 20% | Đạt chuẩn sẵn sàng làm trọn vẹn HW1 & HW2 | Nắm vững quy trình nộp thử nghiệm khép kín | Sẵn sàng cấu trúc thư mục và pipeline đồ án |
| **Micro-1.1**<br>Evidence & CRISP-DM | Tuần 1 | F19: Zettabyte Growth<br>F20: CRISP-DM Lifecycle<br>F23: Competency Triad | Domain: 70%<br>DS: 15%<br>DE: 15% | Khung phương pháp luận cho toàn bộ HW1–HW8 | Thiết lập chu trình thử nghiệm có kiểm soát | Khung 6 giai đoạn cấu trúc bài báo cáo đồ án |
| **Micro-1.2**<br>Dark Data & Translation | Tuần 1, 6, 9 | F21: Dark Data Hand/Hosoya<br>F22: Problem Translation<br>F32: Demis Hassabis Quote | Domain: 80%<br>DS: 20% | Đọc đề bài và xác định đúng nhãn cho HW4 & HW5 | Nhận diện mẫu dữ liệu thiếu trên Private Leaderboard | Định hình KGI/KPI kinh doanh thành Target $y$ cụ thể |
| **Micro-1.3**<br>AI Moats & Tanpin Kanri | Tuần 1, 7, 13 | F24: Seven-Eleven Loop<br>F25: Workflow AI Moat<br>F26: Data Flywheel | Domain: 70%<br>DE: 30% | Phương pháp luận kiểm định giả thuyết tự động | Bác bỏ siêu tốc các giả thuyết đặc trưng sai (Falsify) | Đề xuất giải pháp tích hợp quy trình cho doanh nghiệp |
| **Micro-1.4**<br>14-Week, ML Ladder & Cost | Tuần 1, 5, 6, 8 | F27: 14-Week Curriculum<br>F30: Course Policies<br>F31: 5-Step ML Ladder | Domain: 50%<br>DS: 50% | HW5: Tối ưu hóa ma trận chi phí sai lầm | Bước 1 đến 5: Leo hạng Top 20% Leaderboard | Phân tích giá trị kinh tế (ROI) và chi phí sai số |
| **Micro-1.5**<br>Ecosystem, Rules & Tokyo | Tuần 1 | F28: Omnicampus & Tools<br>F29: 3-Tier Completion<br>F30: Zero Late Policy | Kỷ luật học tập & Quản lý tiến độ | Hoàn thành Khảo sát Tuần 1 (Hạn chót 08/10/2026) | Chiến lược phân bổ thời gian thực chiến | Kế hoạch hoàn thành sớm trước deadline 1 tuần |
| **Session 1.S**<br>Synthesis & Master Strategy | Mốc Chuyển Giao<br>(Week 1 -> Week 2) | Tổng hợp F19–F32<br>Bản đồ hành động chiến lược | Domain: 50%<br>DS: 25%<br>DE: 25% | Khởi động chuỗi 8 bài tập tuần không bị phạt muộn | Định hướng tham gia cuộc thi ngay khi mở | Lựa chọn chủ đề đồ án kinh doanh thực tế |
| **Micro-2.1**<br>Foundations & ndarray | Tuần 2 | F56: Fleet Scale Motivation<br>F57: C-Contiguous Memory<br>F57: SIMD Hardware AVX-512 | DE: 60%<br>DS: 30%<br>Domain: 10% | Nền tảng cho HW1 (Cấu trúc mảng)<br>HW4 (Nạp dữ liệu mảng) | Tối ưu hóa tốc độ thử nghiệm trên tập dữ liệu lớn | Giảm thiểu bộ nhớ RAM cho ma trận đặc trưng lớn |
| **Micro-2.2**<br>Ufuncs & Safe Floats | Tuần 2 | F57: Element-wise Ufuncs<br>F57: Safe Log1p/Expm1<br>F57: IEEE 754 inf/nan | DS: 50%<br>DE: 40%<br>Domain: 10% | HW1 (Phép toán số học)<br>HW5 (Tính hàm mất mát) | Xử lý an toàn không để tràn số hay sập mô hình | Chuẩn hóa biến và biến đổi log hàm phân phối lệch |
| **Micro-2.3**<br>2D Slicing & Views | Tuần 2 | F57: Slicing Arithmetic<br>F57: View vs Copy Hazard<br>F57: Mesh Grid np.ix_ | DE: 70%<br>DS: 30% | HW1 (Trích xuất lát cắt mảng)<br>HW2 (Cắt bảng dữ liệu) | Tách tập dữ liệu con (Sub-sampling) không rò rỉ | Trích xuất khối biến độc lập và nhãn mục tiêu |
| **Micro-2.4**<br>Spatial Axes & Keepdims | Tuần 2 | F57: Collapsing Invariant<br>F57: axis=0 vs axis=1<br>F57: keepdims Preservation | DS: 60%<br>DE: 40% | HW1 (Rút gọn thống kê theo trục)<br>HW4 (Chuẩn hóa ma trận) | Giảm số chiều và tổng hợp vector đặc trưng | Trừ trung bình và chuẩn hóa dữ liệu theo hàng/cột |
| **Micro-2.5**<br>Broadcasting & NOAA | Tuần 2 | F57: Trailing Alignment<br>F57: Newaxis Expansion<br>F57: Boolean Mask & 999.9 | DS: 50%<br>DE: 40%<br>Domain: 10% | Nộp trọn vẹn HW1 (3.0/3.0 điểm)<br>HW2 (Lọc điều kiện bảng) | Tính toán ma trận khoảng cách siêu tốc không dùng for | Làm sạch triệt để giá trị cảm biến hỏng và Z-Score |
| **Session 2.S**<br>Synthesis & Review | Mốc Chuyển Giao<br>(Week 2 -> Week 3) | Tổng hợp F56–F57<br>Pairwise Distance & HW1 Audit | DS: 45%<br>DE: 45%<br>Domain: 10% | Đạt tối đa 3.0 điểm HW1<br>Hoàn thành Khảo sát Buổi 2 | Sẵn sàng cho đường ống tính toán ma trận thực chiến | Nắm vững kỹ thuật tính ma trận khoảng cách |

---

## 3. BẢN ĐỒ ĐƯỜNG GĂNG 8 BÀI TẬP TUẦN (HW1–HW8 ROAD TO GRADUATION)

Hệ thống bài tập lập trình tuần được quản lý và chấm điểm tự động thông qua nền tảng Omnicampus Autograder. Học viên BẮT BUỘC phải nắm vững thông số từng bài tập để đảm bảo đạt điều kiện tốt nghiệp:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        CHÍNH SÁCH ĐIỂM SỐ BÀI TẬP TUẦN (HOMEWORK)                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Tổng số: 8 Bài tập (HW1 đến HW8). Thang điểm tối đa: 3.0 Điểm / Bài (Tổng 24.0 Điểm) │
│ • Điều kiện tốt nghiệp tối thiểu: Đạt từ 14.0 / 24.0 Điểm trở lên (>= 58.3%)           │
│ • Nộp đúng hạn (Trong vòng 2 tuần kể từ ngày mở): Tối đa nhận trọn vẹn 3.0 Điểm       │
│ • Nộp muộn (Sau hạn chót 2 tuần): Bị áp dụng mức trần tối đa chỉ nhận 2.0 Điểm / Bài   │
│ • Cơ chế nộp lại (Resubmission): Cho phép nộp nhiều lần; hệ thống tự lưu điểm cao nhất│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Bảng Chi Tiết Kế Hoạch Thực Hiện 8 Bài Tập:

| Mã Bài Tập | Tuần Mở | Chủ Đề Trọng Tâm Kỹ Thuật | Tập Dữ Liệu Thực Hành | Điểm Chuẩn | Kỹ Năng Kế Thừa Từ Micro-Sessions | Lỗi Thường Gặp Bị Trừ Điểm |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **HW1** | Tuần 2 | Điện toán Mảng Đa Chiều NumPy, Broadcasting, Đại số Tuyến tính | Ma trận tín hiệu số & Ảnh | 3.0 / 3.0 | Micro-2.1 (Memory/SIMD)<br>Micro-2.4 (Axes & Keepdims)<br>Micro-2.5 (Broadcasting & Mask) | Lỗi sai trục chiều ma trận (`axis=0` vs `axis=1`), dùng vòng lặp `for` chậm |
| **HW2** | Tuần 3 | Thao tác Bảng Pandas, Xử lý NaN, Merge Bảng Khách Hàng CRM | Giao dịch bán lẻ & Khách hàng | 3.0 / 3.0 | Micro-0.2 (Missing/Dummy)<br>Micro-0.1 (Relational Merge) | Dùng `how='inner'` làm mất dữ liệu khuyết, quên `drop_first=True` |
| **HW3** | Tuần 4 | Trực Quan Hóa Dữ Liệu EDA, Phân Phối Thống Kê, Boxplot | Dữ liệu nhân khẩu học & Thu nhập | 3.0 / 3.0 | Micro-0.3 (Descriptive Stats)<br>Micro-1.1 (Data Understanding) | Bỏ sót giá trị ngoại lai Tukey, nhầm lẫn giữa tương quan và nhân quả |
| **HW4** | Tuần 5 | Mô Hình Hóa Học Máy Có Giám Sát (OLS & Cây Quyết Định) | Giá bán bất động sản / Xe hơi | 3.0 / 3.0 | Micro-0.4 (Linear Regression & Decision Trees) | Rò rỉ dữ liệu khi Z-Score: gọi `fit_transform` trên tập Test; không giới hạn `max_depth` |
| **HW5** | Tuần 6 | Đánh Giá Mô Hình, Tối Ưu Ma Trận Chi Phí Sai Lầm | Chẩn đoán y tế / Gian lận thẻ | 3.0 / 3.0 | Micro-1.4 (Cost Matrix)<br>Micro-0.4 (Accuracy Trap) | Tối ưu nhầm Accuracy trên dữ liệu mất cân bằng nặng thay vì tối ưu Recall/F1 |
| **HW6** | Tuần 8 | Kỹ Thuật Tạo Biến Nâng Cao & Tự Động Hóa Dò Tham Số Optuna | Dữ liệu hành vi người dùng | 3.0 / 3.0 | Micro-1.3 (Falsification)<br>Micro-1.4 (Optuna Tuning) | Quá khớp khi tìm tham số (Overfitting validation fold), tạo biến rò rỉ tương lai |
| **HW7** | Tuần 10 | Cơ Sở Dữ Liệu Lớn & Truy Vấn SQL Quan Hệ Phức Tạp | Cơ sở dữ liệu E-Commerce lớn | 3.0 / 3.0 | Micro-1.4 (SQL at Scale)<br>Micro-0.1 (Data Taxonomy) | Lọc sau khi `JOIN` thay vì lọc `WHERE` sớm, cú pháp `GROUP BY` thiếu trường |
| **HW8** | Tuần 12 | Phân Tích Chuỗi Thời Gian & Phân Cụm Khách Hàng K-Means | Doanh số chuỗi bán lẻ theo ngày | 3.0 / 3.0 | Micro-1.4 (Autocorrelation $\rho_k$)<br>Micro-0.4 (K-Means/PCA) | Xáo trộn ngẫu nhiên dữ liệu thời gian (`shuffle=True`), không chuẩn hóa trước K-Means |

---

## 4. CHIẾN LƯỢC CHINH PHỤC CUỘC THI MACHINE LEARNING (WEEKS 7–10)

Cuộc thi Machine Learning nội bộ được tổ chức trên nền tảng Omnicampus từ Tuần 7 đến Tuần 10. Để lọt vào **Top 20% Leaderboard** (điều kiện bắt buộc để đạt danh hiệu Honors Student), học viên BẮT BUỘC áp dụng phương pháp luận Nấc Thang 5 Bước (5-Step ML Ladder):

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               NẤC THANG 5 BƯỚC LEADERBOARD (5-STEP ML OPERATIONAL LADDER)              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [Bước 1: Submit Baseline Code (Tuần 7)]                                                │
│ • Mục tiêu: Đăng ký tên lên bảng xếp hạng ngay trong ngày đầu tiên cuộc thi mở.        │
│ • Hành động: Chạy code mẫu tối giản (Dummy/Median Baseline), nộp file CSV kết quả.     │
│ • Kiểm soát: Đảm bảo định dạng cột ID và Target khớp chính xác 100% với file mẫu.     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [Bước 2: Domain-Driven Feature Engineering (Tuần 7–8)]                                 │
│ • Mục tiêu: Tạo ra bước nhảy vọt điểm số lớn nhất (chiếm 70% thành bại của mô hình).  │
│ • Hành động: Đọc kỹ tài liệu mô tả dữ liệu (Data Dictionary). Tạo các biến tương tác, │
│   tính toán tỷ lệ (Ratios), biến tổng hợp hành vi khách hàng trong quá khứ.            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [Bước 3: Thử Nghiệm Kiến Trúc Mô Hình Hiện Đại (Tuần 8–9)]                             │
│ • Mục tiêu: Nâng cao năng lực học phi tuyến và xử lý biến bảng.                        │
│ • Hành động: Chuyển từ Decision Tree đơn giản sang LightGBM, XGBoost hoặc CatBoost.    │
│ • Kiểm soát: Thiết lập chiến lược kiểm định chéo K-Fold phân tầng (Stratified K-Fold).│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [Bước 4: Tự Động Dò Tham Số Bằng Optuna (Tuần 9)]                                      │
│ • Mục tiêu: Tối ưu hóa 5–10% hiệu năng còn lại mà không gây quá khớp.                  │
│ • Hành động: Dùng thuật toán Bayesian TPE trong thư viện Optuna để tìm kiếm tổ hợp:   │
│   `learning_rate`, `max_depth`, `num_leaves`, `subsample`, `reg_alpha`, `reg_lambda`.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [Bước 5: Ensembling & Post-Processing (Tuần 10)]                                       │
│ • Mục tiêu: Ổn định dự báo trên tập Private Test bí mật.                               │
│ • Hành động: Kết hợp trung bình trọng số (Weighted Blending) hoặc Stacking từ 3–5     │
│   mô hình có kiến trúc đa dạng (ví dụ: LightGBM + CatBoost + Logistic Regression).    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. CHIẾN LƯỢC ĐỒ ÁN KINH DOANH CUỐI KHÓA (FINAL BUSINESS CAPSTONE ASSIGNMENT)

Đồ án Cuối khóa (Final Assignment) kéo dài từ Tuần 3 đến Tuần 14, là tiêu chí số 1 để xét chọn danh hiệu **Honors Student (Top 10%)** và học bổng tham quan Đại học Tokyo (**Outstanding Student**).

### 5.1. Khung Tiêu Chuẩn Đánh Giá 5 Trọng Điểm Của Hội Đồng Matsuo Lab:
1. **Định hình bài toán kinh doanh (Business Understanding — Trọng số 30%):**
   - Khảo sát thực trạng, chỉ ra rõ bài toán kinh doanh cụ thể cần giải quyết.
   - Chuyển ngữ thành công mục tiêu định tính thành KGI/KPI định lượng và biến mục tiêu toán học $y$.
   - Phân tích cặn kẽ yếu tố Dark Data và các nguy cơ thiên lệch lựa chọn (Selection Bias).
2. **Khám phá và Tiền xử lý Dữ liệu (Data Preparation & EDA — Trọng số 20%):**
   - Kiểm toán toàn diện giá trị khuyết, ngoại lai và các phân phối dị biệt.
   - Thiết kế các đặc trưng mới (Feature Engineering) mang đậm hàm lượng tri thức nghiệp vụ.
   - Tuyệt đối không để xảy ra rò rỉ dữ liệu (No Data Leakage).
3. **Mô hình hóa và Kiểm chứng Thực nghiệm (Modeling & Validation — Trọng số 20%):**
   - Thiết lập mô hình cơ sở (Baseline Model) để đối chiếu hiệu quả tăng thêm.
   - Thử nghiệm có hệ thống các thuật toán học máy phù hợp.
   - Kiểm định chéo (Cross Validation) chặt chẽ, mô phỏng đúng bối cảnh thực tế.
4. **Phân tích Hiệu Quả Kinh Tế & Chi Phí Sai Lầm (Economic Value Analysis — Trọng số 20%):**
   - Xây dựng ma trận chi phí thực tế ($C_{\text{FN}}$ vs $C_{\text{FP}}$).
   - Lượng hóa tác động tài chính: Mô hình giúp doanh nghiệp tăng thêm bao nhiêu doanh thu hoặc tiết kiệm bao nhiêu chi phí vận hành.
5. **Khả năng Tích Hợp Quy Trình & Hào Lũy AI (Workflow Integration & AI Moat — Trọng số 10%):**
   - Đề xuất giải pháp nhúng mô hình vào quy trình tác nghiệp hàng ngày của nhân viên (giống vòng lặp Tanpin Kanri).
   - Thiết kế cơ chế Bánh đà Dữ liệu (Data Flywheel) để mô hình liên tục tự học và cải tiến sau khi triển khai.

---

## 6. KHUNG KIỂM TOÁN TỐT NGHIỆP 3 CẤP ĐỘ (3-TIER GRADUATION MILESTONE AUDIT)

Để đảm bảo quyền lợi tối cao và định hướng mục tiêu rõ ràng cho học viên ngay từ Tuần 1, hệ thống công nhận tốt nghiệp của GCI World được phân tầng thành 3 cấp độ danh dự:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      3 CẤP ĐỘ CÔNG NHẬN TỐT NGHIỆP GCI WORLD 2026                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [CẤP 1: COMPLETED STUDENT (Học Viên Tốt Nghiệp Tiêu Chuẩn)]                            │
│ • Hoàn thành Khảo sát Điểm danh: Đạt tối thiểu >= 7 / 14 Buổi (Tuyệt đối không trễ hạn)│
│ • Điểm Bài tập tuần (Homework): Đạt tối thiểu >= 14.0 / 24.0 Điểm                      │
│ • Đồ án Cuối khóa (Final Assignment): Nộp đúng hạn và đạt tiêu chuẩn đánh giá của Lab  │
│ • Cuộc thi Machine Learning: Tùy chọn (Optional)                                       │
│ • Quyền lợi: Chứng chỉ tốt nghiệp chính thức từ Matsuo-Iwasawa Lab, Đại học Tokyo.    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [CẤP 2: HONORS STUDENT (Học Viên Tốt Nghiệp Danh Dự)]                                  │
│ • Thỏa mãn toàn bộ điều kiện của Cấp 1 (Completed Student).                            │
│ • Xếp hạng Đồ án Cuối khóa: Nằm trong TOP 10% các bài xuất sắc nhất toàn khóa.        │
│ • Xếp hạng Cuộc thi Machine Learning: Nằm trong TOP 20% Private Leaderboard.          │
│ • Quyền lợi: Chứng chỉ Tốt nghiệp Danh dự (Honors Certificate); Được kết nối vào Mạng  │
│   lưới Tài năng Trí tuệ Nhân tạo Toàn cầu của Matsuo Lab.                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [CẤP 3: OUTSTANDING STUDENT (Đại Biểu Xuất Sắc — Học Bổng Chuyến Đi Tokyo)]            │
│ • Tuyển chọn gắt gao từ nhóm dẫn đầu danh sách Honors Student (Cấp 2).                 │
│ • Vượt qua vòng phỏng vấn chuyên sâu với Ban Giảng huấn Đại học Tokyo.                 │
│ • Áp dụng độc quyền cho học viên học lần đầu (First-time students only).               │
│ • Quyền lợi: HỌC BỔNG TOÀN PHẦN CHUYẾN THAM QUAN NGHIÊN CỨU TẠI TOKYO (TOKYO STUDY TOUR)│
│   Bao gồm vé máy bay khứ hồi, chi phí lưu trú, tham quan trụ sở Matsuo Lab tại        │
│   Khuôn viên Hongo (Đại học Tokyo) và giao lưu trực tiếp với các doanh nghiệp AI Nhật. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Checklist Hành Động Định Kỳ Đảm Bảo Tiến Độ Tốt Nghiệp:
- [ ] **Mỗi Tuần:** Hoàn thành ngay Khảo sát Điểm danh trong vòng 7 ngày đầu sau buổi giảng (Hạn cuối tuyệt đối không thể mở lại).
- [ ] **Mỗi 2 Tuần:** Nộp bản chạy được (Baseline) của Bài tập tuần trước hạn chót 14 ngày để bảo toàn thang điểm 3.0đ.
- [ ] **Tuần 3:** Khởi động Đồ án Cuối khóa; chọn đề tài và tiến hành thu thập làm sạch dữ liệu sơ bộ.
- [ ] **Tuần 7:** Nộp code Baseline lên Leaderboard Cuộc thi ML ngay trong tuần đầu tiên.
- [ ] **Tuần 13:** Hoàn thiện toàn bộ bài báo cáo Đồ án Cuối khóa trước deadline 1 tuần để kiểm thử tính toàn vẹn và chống rò rỉ dữ liệu.
