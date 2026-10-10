# ĐỀ CƯƠNG VỞ GHI CHÉP TAY (HANDWRITTEN NOTEBOOK SYLLABUS)
## Khóa Học: GCI World 2026 September · Matsuo-Iwasawa Lab (Đại Học Tokyo)
## Buổi: Buổi 0 — Preparatory Materials (Khóa Học Dự Bị & Nền Tảng Khoa Học Dữ Liệu)

> **Thông tin giáo trình:**
> - **Khái niệm cốt lõi:** Tư duy Nhà Khoa học Dữ liệu (Data Scientist Mindset), Quy trình 4 bước chuẩn, Thống kê mô tả, OOP Python, và Thuật toán Học máy cơ bản.
> - **Thời gian chép tay ước tính:** 20–25 phút (Chép tay và vẽ sơ đồ vào vở trước khi mở máy tính thực hành code).
> - **Quy ước bố cục trang vở Cornell 3 cột:**
>   - **Cột 1 — Lề trái (20% độ rộng):** Từ khóa cốt lõi, Câu hỏi truy hồi (Active Recall Cues), Mẹo ghi nhớ. Dùng để che tay tự kiểm tra kiến thức khi ôn tập.
>   - **Cột 2 — Thân giữa (50% độ rộng):** Sơ đồ tư duy dạng khối-mũi tên (ASCII Mindmaps), Cơ chế vận hành, Công thức toán học đóng khung chuẩn KaTeX.
>   - **Cột 3 — Lề phải (30% độ rộng):** Hành động thực tế, Mẫu code Python 3–5 dòng (không chép code dài), Cạm bẫy kỹ thuật thường gặp.

---

### PHẦN 1: TỔNG QUAN KHÓA HỌC & TƯ DUY NHÀ KHOA HỌC DỮ LIỆU

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **GCI Basic**<br>*(Khóa học Dự bị: Chương trình đào tạo nền tảng Khoa học Dữ liệu 6 giờ video & thực hành)*<br><br>*Gợi nhớ (Active Recall Cue):* Mục tiêu tối thượng của Buổi 0 là gì? | ```text<br>┌────────────────────────────────────────────────────────┐<br>│              GCI BASIC CURRICULUM (6 Giờ)              │<br>├──────────────────────────┬─────────────────────────────┤<br>│  Phần 1-5: Nền Tảng Lý   │  Phần 6-7: Xưởng Thực Hành  │<br>│  Thuyết (Video < 5 phút) │  Mô Hình Dự Báo Thực Tế     │<br>│  • DS Concept & Workflow │  • Regression: Car Price    │<br>│  • Python & OOP          │  • Classification: Mushroom │<br>│  • Thống kê & Math       │                             │<br>│  • ML Taxonomy & LLMs    │                             │<br>└──────────────────────────┴─────────────────────────────┘<br>```<br>**Thông điệp GS. Yutaka Matsuo:** Xây dựng tư duy khoa học dữ liệu kiểm chứng giả thuyết bằng số liệu thực nghiệm. | **Nguồn tài liệu:**<br>• Video mở đầu: `https://youtu.be/q2tRrzyQ27A`<br>• Trọn bộ 5 Playlists: 60 clip vi mô.<br><br>**Hành động:** Sử dụng 2 màn hình (1 màn hình xem video bài giảng, 1 màn hình thao tác Colab). |
| **The 3 Pillars**<br>*(3 Trụ cột Khoa học Dữ liệu: Giao thoa giữa Kiến thức nghiệp vụ 60-70%, Khoa học máy tính 20% và Toán thống kê 10-20%)*<br><br>*Gợi nhớ (Active Recall Cue):* Năng lực nào chiếm tỷ trọng thành bại lớn nhất? | ```text<br>          [1. Domain Knowledge] (60-70%)<br>                   ▲<br>                  ╱ ╲<br>                 ╱   ╲<br>                ╱     ╲<br>               ▼       ▼<br>[2. Computer Science] ◄──► [3. Math & Statistics]<br>      (20% Code)                 (10-20% Đo lường)<br>```<br>**Giao điểm:** Kỹ thuật lập trình và mô hình hóa chỉ có giá trị khi giải quyết đúng bài toán kinh doanh cụ thể. | **Nguyên tắc vàng:** Không bao giờ áp dụng thuật toán phức tạp nếu chưa hiểu rõ bản chất nghiệp vụ.<br><br>**Cạm bẫy:** Mất nhiều tuần tinh chỉnh tham số mô hình nhưng giải sai nhu cầu khách hàng. |
| **4-Step Workflow**<br>*(Quy trình 4 bước chuẩn: Chu trình khép kín gồm Hiểu dữ liệu $\to$ Tiền xử lý $\to$ Xây dựng mô hình $\to$ Đánh giá)*<br><br>*Gợi nhớ (Active Recall Cue):* Thứ tự các bước và vòng lặp phản hồi? | ```text<br>[1. Understanding Data] ──> [2. Preprocessing Data]<br>          ▲                                │<br>          │ Hiệu chỉnh giả thuyết           ▼<br>[4. Model Evaluation]   <── [3. Model Building]<br>```<br>**Cơ chế vận hành:**<br>1. *Understanding:* Khám phá hình dạng, phân phối, kiểu dữ liệu.<br>2. *Preprocessing:* Xử lý NaN, mã hóa dummy, chuẩn hóa thang đo.<br>3. *Modeling:* Huấn luyện thuật toán (Hồi quy / Cây quyết định).<br>4. *Evaluation:* Đo lường sai số trên tập kiểm thử chưa thấy. | **Thói quen chép vào vở:**<br>Vẽ hình chữ nhật 4 góc này vào trang đầu tiên của mọi bài toán phân tích.<br><br>**Hành động:** Luôn kiểm tra kết quả đánh giá (bước 4) để quyết định quay lại bước 1 hay bước 2. |

---

### PHẦN 2: BẢN CHẤT DỮ LIỆU & THANG ĐO BIẾN SỐ

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **Data Taxonomy**<br>*(Phân loại Dữ liệu: Phân chia thành Dữ liệu có cấu trúc dạng bảng ~20% và Dữ liệu phi cấu trúc văn bản/hình ảnh >80%)*<br><br>*Gợi nhớ (Active Recall Cue):* Dữ liệu bảng và văn bản thuộc nhóm nào? | ```text<br>┌────────────────────────────────────────────────────────┐<br>│                   PHÂN LOẠI DỮ LIỆU                    │<br>├────────────────────────────┬───────────────────────────┤<br>│ Có Cấu Trúc (Structured)   │ Phi Cấu Trúc (Unstructured│<br>│ • Bảng số liệu: Dòng & Cột │ • Văn bản tự do, Markdown │<br>│ • RDBMS, CSV, Parquet      │ • Hình ảnh, Âm thanh, Vid │<br>│ • Chiếm ~20% dung lượng    │ • Chiếm >80% dung lượng   │<br>│ • Xử lý: Pandas, SQL, ML   │ • Xử lý: Deep Learning    │<br>└────────────────────────────┴───────────────────────────┘<br>``` | **Code kiểm tra hình dạng bảng:**<br>```python<br>import pandas as pd<br>df = pd.read_csv('Car_Price_Data.csv')<br>print(df.shape)  # (205, 4)<br>print(df.dtypes) # Kiểm tra kiểu cột<br>``` |
| **Variable Scales**<br>*(Thang đo Biến số: 4 mức đo lường gồm Định lượng liên tục/rời rạc và Định tính danh nghĩa/thứ bậc)*<br><br>*Gợi nhớ (Active Recall Cue):* Biến liên tục khác gì biến rời rạc và biến danh mục? | ```text<br>                       ┌── Liên tục (Continuous): Giá xe, Trọng lượng<br>   ┌── 1. Định Lượng ──┤<br>   │      (Số học)     └── Rời rạc (Discrete): Số cửa xe, Số xi-lanh<br>Biến<br>   │      (Phân loại)  ┌── Danh nghĩa (Nominal): Màu sắc, Mùi hương<br>   └── 2. Định Tính ───┤<br>                       └── Thứ bậc (Ordinal): Xếp hạng sao, Học vấn<br>``` | **Cảnh báo lỗi nghiêm trọng:**<br>Tuyệt đối không tính phép toán trung bình ($\bar{x}$) trên biến Danh nghĩa (Nominal).<br><br>**Hành động:** Biến định tính bắt buộc phải mã hóa thành biến giả (Dummy) trước khi đưa vào mô hình. |

---

### PHẦN 3: TIỀN XỬ LÝ DỮ LIỆU (PREPROCESSING)

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **Missing Values**<br>*(Giá trị khuyết: Dữ liệu bị thiếu NaN/None cần kiểm toán bằng isnull() và xử lý bằng dropna() hoặc fillna())*<br><br>*Gợi nhớ (Active Recall Cue):* Khi nào xóa (`dropna`) và khi nào điền (`fillna`)? | ```text<br>                    Kiểm toán NaN: df.isnull().sum()<br>                                   │<br>                  ┌────────────────┴────────────────┐<br>                  ▼                                 ▼<br>       Tỷ lệ khuyết rất nhỏ (<1%)        Tỷ lệ khuyết đáng kể (>5%)<br>                  │                                 │<br>        Xóa dòng: df.dropna()              Điền khuyết (Imputation)<br>                                            ├─ Định lượng: Mean / Median<br>                                            └─ Định tính: Mode (Yếu vị)<br>``` | **Cú pháp Python:**<br>```python<br># Kiểm toán giá trị thiếu:<br>null_counts = df.isnull().sum()<br><br># Điền Mode cho biến định tính:<br>top_val = df['cap_color'].mode()[0]<br>df['cap_color'].fillna(top_val, inplace=True)<br>```<br>**Cạm bẫy:** Điền mean mà không kiểm tra ngoại lai sẽ làm lệch tâm phân phối. |
| **Dummy Variable Trap**<br>*(Bẫy biến giả đa cộng tuyến: Hiện tượng ma trận suy biến khi mã hóa đủ K cột cho K nhóm, khắc phục bằng drop_first=True)*<br><br>*Gợi nhớ (Active Recall Cue):* Vì sao biến có $K$ nhóm chỉ tạo $K-1$ cột? | **Cơ chế toán học:**<br>Nếu giữ nguyên $K$ cột, cột cuối cùng suy diễn được từ các cột trước:<br>$$ x_K = 1 - \sum_{j=1}^{K-1} x_j $$<br>$\implies$ Gây hiện tượng đa cộng tuyến hoàn hảo (Perfect Multicollinearity), ma trận hiệp phương sai bị suy biến ($|X^T X| = 0$), thuật toán OLS báo lỗi sập. | **Code chuẩn Matsuo Lab:**<br>```python<br># Bắt buộc truyền drop_first=True<br>df_dummy = pd.get_dummies(<br>    df, <br>    columns=['odor', 'bruises'], <br>    drop_first=True, <br>    dtype=int<br>)<br>```<br>**Quy tắc:** $K$ phân nhóm $\to K-1$ cột nhị phân. |
| **Z-Score Standardization**<br>*(Chuẩn hóa Z-Score: Biến đổi đặc trưng về phân phối chuẩn hóa có trung bình $\mu=0$ và độ lệch chuẩn $\sigma=1$)*<br><br>*Gợi nhớ (Active Recall Cue):* Công thức và ý nghĩa của việc đưa về $\mu=0, \sigma=1$? | **Công thức KaTeX:**<br>$$ z = \frac{x - \mu}{\sigma} $$<br>• $\mu$: Giá trị trung bình của đặc trưng.<br>• $\sigma$: Độ lệch chuẩn của đặc trưng.<br><br>**Ý nghĩa:** Triệt tiêu sự chênh lệch đơn vị đo (ví dụ: Giá xe $\$30,000$ vs Thể tích $150\text{ cc}$). Giúp các thuật toán Gradient Descent và khoảng cách Euclidean hội tụ ổn định. | **Quy tắc ngăn rò rỉ (Data Leakage):**<br>```python<br>from sklearn.preprocessing import StandardScaler<br>scaler = StandardScaler()<br># Fit và transform trên tập Train:<br>X_tr_s = scaler.fit_transform(X_train)<br># CHỈ transform trên tập Test:<br>X_te_s = scaler.transform(X_test)<br>```<br>[CẤM] CẤM gọi `fit_transform` trên `X_test`! |

---

### PHẦN 4: ĐÁNH GIÁ KHÁI QUÁT HÓA & PHÂN CHIA DỮ LIỆU

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **Train/Test Split**<br>*(Phân chia tập huấn luyện và kiểm thử: Tách độc lập tập Train ~80% để học tham số và tập Test ~20% để đánh giá khách quan)*<br><br>*Gợi nhớ (Active Recall Cue):* Tỷ lệ chia phổ biến và mục đích của tập Test? | ```text<br>┌────────────────────────────────────────────────────────┐<br>│              TOÀN BỘ DỮ LIỆU BAN ĐẦU (100%)            │<br>├─────────────────────────────────────────┬──────────────┤<br>│  Tập Huấn Luyện - TRAIN SET (~80%)     │ TEST (~20%)  │<br>│  • Dùng để mô hình học w và b           │ • Bị khóa kín│<br>│  • Tối thiểu hóa hàm mất mát MSE        │ • Đánh giá 1 │<br>│  • Được quyền fit_transform scaler      │   lần duy nhấ│<br>└─────────────────────────────────────────┴──────────────┘<br>``` | **Cú pháp Python:**<br>```python<br>from sklearn.model_selection import train_test_split<br>X_tr, X_te, y_tr, y_te = train_test_split(<br>    X, y, <br>    test_size=0.2, <br>    random_state=42<br>)<br>``` |
| **Overfitting**<br>*(Quá khớp / Học vẹt dữ liệu: Mô hình học cả nhiễu ngẫu nhiên của tập Train, đạt điểm cao khi học nhưng sụp đổ trên Test)*<br><br>*Gợi nhớ (Active Recall Cue):* Dấu hiệu nhận biết quá khớp trên số liệu? | ```text<br>Mô hình Quá Khớp (Overfitting / High Variance):<br>┌────────────────────────────┬───────────────────────────┐<br>│ Hiệu năng trên Train       │ Hiệu năng trên Test       │<br>├────────────────────────────┼───────────────────────────┤<br>│ R² = 0.999 (Rất cao)       │ R² = 0.420 (Rất thấp)     │<br>│ Sai số MSE tiệm cận 0      │ Sai số MSE bùng nổ        │<br>└────────────────────────────┴───────────────────────────┘<br>Nguyên nhân: Mô hình quá phức tạp, học vẹt cả nhiễu.<br>Khắc phục: Giảm số đặc trưng, giới hạn độ sâu cây max_depth.<br>``` | **Phương châm DeepTutor:**<br>"Một mô hình đạt 100% trên tập học nhưng sụp đổ trên thực tế là một mô hình rác."<br><br>**Hành động:** Luôn so sánh song song điểm số Train và Test. |

---

### PHẦN 5: THỐNG KÊ MÔ TẢ & PHÂN TÍCH ĐỒ THỊ

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **Central Tendency**<br>*(Xu hướng tập trung: Các thước đo vị trí trung tâm của phân phối gồm Trung bình Mean, Trung vị Median và Yếu vị Mode)*<br><br>*Gợi nhớ (Active Recall Cue):* Khi nào dùng Mean, khi nào dùng Median? | **1. Trung bình cộng (Mean):**<br>$$ \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i $$<br>Nhạy cảm với ngoại lai cực đoan.<br><br>**2. Trung vị (Median):** Điểm chia đôi mẫu dữ liệu đã xếp thứ tự. Bất biến (Robust) trước ngoại lai.<br><br>**3. Yếu vị (Mode):** Giá trị xuất hiện nhiều nhất (dùng cho biến danh mục). | **Code NumPy:**<br>```python<br>import numpy as np<br>mean_v = np.mean(df['engine-size'])<br>med_v  = np.median(df['engine-size'])<br>```<br>**Quy tắc thực tế:** Nếu dữ liệu bị lệch đuôi (thu nhập, giá nhà), dùng Median thay vì Mean. |
| **Dispersion**<br>*(Độ phân tán / Độ biến thiên: Các thước đo mức độ lan tỏa của dữ liệu gồm Phương sai Variance và Độ lệch chuẩn Standard Deviation)*<br><br>*Gợi nhớ (Active Recall Cue):* Vì sao cần độ lệch chuẩn bên cạnh phương sai? | **1. Phương sai (Variance $\sigma^2$):**<br>$$ \sigma^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2 $$<br>Đơn vị bị bình phương (e.g. $\text{USD}^2$).<br><br>**2. Độ lệch chuẩn (Standard Deviation $\sigma$):**<br>$$ \sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2} $$<br>Cùng đơn vị với dữ liệu gốc (e.g. $\text{USD}$).<br><br>**Quy tắc Gaussian:** $68.3\%$ trong $\pm 1\sigma$, $95.5\%$ trong $\pm 2\sigma$. | **Code NumPy:**<br>```python<br>var_v = np.var(df['engine-size'])<br>std_v = np.std(df['engine-size'])<br>```<br>**Ý nghĩa:** Độ lệch chuẩn càng nhỏ $\implies$ dữ liệu càng tập trung quanh mức trung bình. |
| **Box Plot & IQR**<br>*(Biểu đồ hộp & Khoảng tứ phân vị: Công cụ trực quan hóa phân phối 5 số và phát hiện ngoại lai theo hàng rào Tukey 1.5*IQR)*<br><br>*Gợi nhớ (Active Recall Cue):* Công thức tính hàng rào phát hiện ngoại lai? | ```text<br>                 Khoảng tứ phân vị: IQR = Q3 - Q1<br>    Lower Fence                           Upper Fence<br>  Q1 - 1.5*IQR     Q1      Median     Q3   Q3 + 1.5*IQR<br>───────[X]──────────|─────────[ | ]────────|──────────[X]───────<br>   (Outlier)       Min       (Q2)         Max      (Outlier)<br>```<br>**Ngưỡng Tukey:** Bất kỳ giá trị nào $x < Q_1 - 1.5\text{IQR}$ hoặc $x > Q_3 + 1.5\text{IQR}$ đều bị coi là ngoại lai. | **Lọc ngoại lai bài tập Car Price:**<br>```python<br># Lọc chiếc xe giá > 30000 nhưng nhẹ <= 3000 lbs:<br>mask = ~((df['curb-weight'] <= 3000) & (df['price'] >= 30000))<br>df_clean = df[mask]<br>```<br>[LƯU Ý] Chú ý: Dấu ngoặc đơn bắt buộc do toán tử `&` có độ ưu tiên cao hơn `<=`. |
| **Pearson Correlation**<br>*(Hệ số tương quan Pearson: Thước đo mức độ liên hệ tuyến tính chuẩn hóa giữa hai biến số liên tục trong đoạn [-1, 1])*<br><br>*Gợi nhớ (Active Recall Cue):* Miền giá trị và ý nghĩa của $r$? | **Công thức KaTeX:**<br>$$ r_{xy} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \in [-1, 1] $$<br>• $r \approx +1$: Tương quan dương mạnh ($\uparrow \uparrow$).<br>• $r \approx -1$: Tương quan âm mạnh ($\uparrow \downarrow$).<br>• $r \approx 0$: Không tương quan tuyến tính.<br><br>[LƯU Ý] **Correlation $\neq$ Causation (Tương quan $\neq$ Nhân quả):** Ăn kem và đuối nước cùng tăng vào mùa hè không có nghĩa ăn kem gây đuối nước! | **Code NumPy:**<br>```python<br>r = np.corrcoef(df['engine-size'], df['price'])[0, 1]<br>print(f"Pearson r: {r:.3f}") # r ≈ 0.87 (Tương quan mạnh)<br>```<br>**Hành động:** Khi 2 đặc trưng đầu vào có $r > 0.9$, cân nhắc bỏ 1 biến để tránh đa cộng tuyến. |

---

### PHẦN 6: KỸ THUẬT LẬP TRÌNH PYTHON HƯỚNG ĐỐI TƯỢNG & BẢNG QUAN HỆ

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **Python OOP**<br>*(Lập trình hướng đối tượng: Mô hình đóng gói trạng thái thuộc tính và hành vi phương thức vào Class để đúc các đối tượng instance)*<br><br>*Gợi nhớ (Active Recall Cue):* Class khác gì Object? Vai trò của `self`? | ```text<br>┌────────────────────────────────────────────────────────┐<br>│              CLASS (Bản Thiết Kế Khuôn Mẫu)            │<br>│  • Thuộc tính (State / Attributes): name, hp, attack    │<br>│  • Phương thức (Behavior / Methods): take_damage()     │<br>└───────────────────────────┬────────────────────────────┘<br>                            │  Khởi tạo instance (Đúc đối tượng)<br>            ┌───────────────┴───────────────┐<br>            ▼                               ▼<br>[pikachu = Pokemon(...)]       [charmander = Pokemon(...)]<br>``` | **Mẫu code chuẩn:**<br>```python<br>class Pokemon:<br>    def __init__(self, name: str, hp: int):<br>        self.name = name<br>        self.hp = hp<br>    def take_damage(self, dmg: int):<br>        self.hp -= dmg<br><br>p1 = Pokemon("Pikachu", 100)<br>p1.take_damage(20)<br>```<br>API của Scikit-learn thiết kế hoàn toàn theo mô hình Class này. |
| **Relational Merging**<br>*(Ghép bảng quan hệ: Phép kết hợp dữ liệu bảng dựa trên khóa chung bằng pd.merge theo các phương thức left, right, inner)*<br><br>*Gợi nhớ (Active Recall Cue):* Khi nào dùng `how='left'` trong phân tích dữ liệu? | ```text<br>Bảng Trái (Appearence)             Bảng Phải (Odor)<br>┌──────┬──────────┬────────┐       ┌──────┬────────┐<br>│  ID  │ cap_color│ poison │   +   │  ID  │  odor  │<br>├──────┼──────────┼────────┤       ├──────┼────────┤<br>│ 001  │   red    │   1    │       │ 001  │  foul  │<br>│ 002  │  yellow  │   0    │       │ 002  │  none  │<br>│ 003  │  white   │   0    │       │ ...  │  ...   │<br>└──────┴──────────┴────────┘       └──────┴────────┘<br>                 │                        │<br>                 └───────► pd.merge ◄─────┘<br>                       (how='left', on='ID')<br>``` | **Cú pháp Pandas:**<br>```python<br>df_all = pd.merge(<br>    df_app, <br>    df_odor, <br>    on='ID', <br>    how='left'<br>)<br># Kiểm toán dòng khuyết sau khi ghép:<br>print(df_all['odor'].isnull().sum()) # 4 dòng<br>```<br>**Cạm bẫy:** `how='inner'` sẽ làm biến mất âm thầm 4 mẫu nấm không khớp ID! |

---

### PHẦN 7: BỨC TRANH HỌC MÁY & MÔ HÌNH CÓ GIÁM SÁT

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **ML Taxonomy**<br>*(Phân loại các nhánh Học máy: Ba trụ cột chính gồm Học có giám sát, Học không giám sát và Học tăng cường)*<br><br>*Gợi nhớ (Active Recall Cue):* Khác biệt giữa Supervised, Unsupervised và RL? | ```text<br>                       ┌── Hồi quy (Regression): Mục tiêu liên tục<br>   ┌── 1. Có Giám Sát ──┤<br>   │      (Có nhãn X->y)└── Phân loại (Classification): Nhãn rời rạc<br>ML ┼── 2. Không Giám Sát ┌── Phân cụm (Clustering): K-Means gom nhóm<br>   │      (Không nhãn X) └── Giảm chiều (Dimensionality): PCA nén ma trận<br>   └── 3. Học Tăng Cường (RL): Agent hành động theo Thưởng/Phạt<br>``` | **Quy tắc phân loại:**<br>• Dự đoán Giá xe $\to$ Hồi quy.<br>• Dự đoán Nấm độc $\to$ Phân loại.<br>• Phân khúc khách hàng $\to$ Phân cụm K-Means.<br>• Nén ảnh / Giảm chiều $\to$ PCA. |
| **Linear Regression**<br>*(Hồi quy tuyến tính: Mô hình xấp xỉ siêu phẳng cực tiểu hóa hàm mất mát sai số toàn phương trung bình MSE bằng OLS)*<br><br>*Gợi nhớ (Active Recall Cue):* Ý nghĩa hình học của siêu phẳng và hàm MSE? | **1. Phương trình siêu phẳng:**<br>$$ \hat{y} = \mathbf{w}^T \mathbf{x} + b = w_1 x_1 + \dots + w_m x_m + b $$<br>Trọng số $w_i$: Mức độ tác động biên của đặc trưng $x_i$.<br><br>**2. Hàm mất mát Mean Squared Error (MSE):**<br>$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2 $$<br>OLS tìm nghiệm giải tích đóng để cực tiểu hóa MSE. | **Code Scikit-learn:**<br>```python<br>from sklearn.linear_model import LinearRegression<br>from sklearn.metrics import mean_squared_error<br>model = LinearRegression().fit(X_tr, y_tr)<br>y_pred = model.predict(X_te)<br>mse = mean_squared_error(y_te, y_pred)<br>r2  = model.score(X_te, y_te)<br>``` |
| **Decision Tree**<br>*(Phân loại Cây quyết định: Mô hình phân lớp đệ quy bằng các nhát cắt nhị phân tối ưu độ tinh khiết Gini hoặc Entropy)*<br><br>*Gợi nhớ (Active Recall Cue):* Cách cây phân chia và kiểm soát độ sâu? | ```text<br>                 [Gốc: Mùi odor == none?]<br>                        ╱        ╲<br>                 True  ╱          ╲ False<br>                      ▼            ▼<br>               [Ăn được: 99%]   [Kích thước lá?]<br>                                  ╱         ╲<br>                                 ▼           ▼<br>                            [Nấm độc]    [Ăn được]<br>```<br>**Cơ chế:** Tách nhị phân đệ quy theo ngưỡng làm giảm độ vẩn đục (Gini / Entropy) lớn nhất. | **Kiểm soát Overfitting:**<br>```python<br>from sklearn.tree import DecisionTreeClassifier<br>clf = DecisionTreeClassifier(<br>    max_depth=3,     # Bắt buộc khống chế độ sâu!<br>    random_state=42<br>)<br>clf.fit(X_tr, y_tr)<br>acc = clf.score(X_te, y_te)<br>```<br>[CẢNH BÁO] Không giới hạn `max_depth` $\implies$ Cây học vẹt 100% dữ liệu Train! |
| **Metrics Comparison**<br>*(So sánh độ đo hiệu năng: Đánh giá mô hình bằng RMSE/R2 cho Hồi quy và Accuracy/Precision/Recall/F1 cho Phân loại)*<br><br>*Gợi nhớ (Active Recall Cue):* Vì sao Accuracy thất bại khi dữ liệu mất cân bằng? | **Hồi quy:**<br>• $\text{RMSE} = \sqrt{\text{MSE}}$ (Cùng đơn vị với $y$).<br>• $R^2 \in (-\infty, 1]$: Tỷ lệ phương sai được giải thích.<br><br>**Phân loại:**<br>• $\text{Accuracy} = \frac{TP + TN}{N}$<br>[CẢNH BÁO] **Bẫy lớp mất cân bằng:** Với $1\%$ nấm độc, đoán toàn bộ $100\%$ ăn được vẫn đạt Accuracy $99\%$ nhưng làm chết người! | **Quy tắc vàng:**<br>Khi dữ liệu mất cân bằng lớp (Imbalanced Data), KHÔNG dùng Accuracy làm tiêu chí duy nhất. Chuyển sang Precision, Recall, F1-Score hoặc AUC-ROC. |

---

### PHẦN 8: HỌC MÁY KHÔNG GIÁM SÁT & BIÊN GIỚI AI HIỆN ĐẠI

| Cột 1: Từ khóa & Gợi nhớ (20%) | Cột 2: Sơ đồ tư duy & Cơ chế vận hành (50%) | Cột 3: Hành động & Code minh họa (30%) |
| :--- | :--- | :--- |
| **K-Means Clustering**<br>*(Phân cụm K-Means: Phương pháp học không giám sát gom nhóm dữ liệu quanh K tâm cụm qua các vòng lặp khoảng cách Euclidean)*<br><br>*Gợi nhớ (Active Recall Cue):* Các bước lặp hội tụ của thuật toán K-Means? | ```text<br>Chu trình 4 bước K-Means:<br>1. Khởi tạo K tâm cụm ngẫu nhiên c_1, ..., c_K.<br>2. Gán điểm vào tâm cụm gần nhất (Khoảng cách Euclidean):<br>   d(x, c) = sqrt(sum (x_j - c_j)^2)<br>3. Cập nhật tâm cụm bằng trung bình tọa độ các điểm trong cụm.<br>4. Lặp lại bước 2 & 3 cho đến khi tâm cụm ngừng di chuyển.<br>``` | **Điều kiện bắt buộc:**<br>Bắt buộc chuẩn hóa Z-Score trước khi chạy K-Means.<br><br>**Code mẫu:**<br>```python<br>from sklearn.cluster import KMeans<br>kmeans = KMeans(n_clusters=3, random_state=42)<br>clusters = kmeans.fit_predict(X_scaled)<br>``` |
| **PCA (Principal Component Analysis)**<br>*(Phân tích thành phần chính: Phép chiếu dữ liệu sang hệ trục trực giao mới bảo toàn tối đa phương sai)*<br><br>*Gợi nhớ (Active Recall Cue):* Mục đích của PCA và tính chất của các trục PC? | **Cơ chế nén ma trận trực giao:**<br>• Chiếu dữ liệu từ không gian $m$ chiều xuống $k$ chiều ($k < m$).<br>• Trục $PC_1$ lưu giữ phương sai lớn nhất.<br>• Trục $PC_2$ vuông góc (trực giao) với $PC_1$ và lưu phương sai lớn thứ hai.<br>• Triệt tiêu hoàn toàn đa cộng tuyến giữa các biến. | **Code Scikit-learn:**<br>```python<br>from sklearn.decomposition import PCA<br>pca = PCA(n_components=2)<br>X_pca = pca.fit_transform(X_scaled)<br>print("Tỷ lệ phương sai:", pca.explained_variance_ratio_)<br>```<br>**Ứng dụng:** Trực quan hóa dữ liệu nhiều chiều lên mặt phẳng 2D. |
| **Self-Supervised & LLMs (Large Language Models)**<br>*(Mô hình Ngôn ngữ Lớn: Huấn luyện tự giám sát dự đoán token tiếp theo trên quy mô dữ liệu khổng lồ)*<br><br>*Gợi nhớ (Active Recall Cue):* Bản chất toán học của Next Token Prediction? | **Next Token Prediction:**<br>Mô hình tự sinh nhãn giám sát bằng cách che giấu từ tiếp theo:<br>$$ P(w_t \mid w_1, w_2, \dots, w_{t-1}) $$<br>**Lộ trình 2 giai đoạn:**<br>1. *Pre-training:* Tự giám sát trên hàng nghìn tỷ từ ngữ để học tri thức tổng quát.<br>2. *Post-training (SFT / RLHF):* Tinh chỉnh theo hướng dẫn con người để an toàn, chính xác. | **Bản chất của Ảo giác (Hallucination):**<br>LLM không có khái niệm chân lý khách quan; nó chỉ tối ưu hóa xác suất chọn từ tiếp theo mượt mà nhất.<br><br>**Hành động:** Luôn kiểm chứng mã code sinh ra bởi LLM bằng các kiểm thử tự động (Pytest / AST). |

---

### PHẦN 9: TỔNG KẾT ĐƯỜNG ỐNG THỰC HÀNH VI MÔ (WORKSHOPS)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        TỔNG HỢP 2 WORKSHOP THỰC HÀNH CỐT LÕI                           │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ WORKSHOP 1: HỒI QUY GIÁ XE (Car Price)    │ WORKSHOP 2: PHÂN LOẠI NẤM ĐỘC (Mushroom)   │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ • Level 0: Hồi quy đơn biến baseline      │ • Level 0: Mã hóa Dummy & Cây quyết định   │
│   engine-size -> price; tính MSE          │   pd.get_dummies(drop_first=True)          │
│ • Level 1: Khảo sát tương quan Pearson    │ • Level 1: Kiểm toán dữ liệu thiếu         │
│   Vẽ Scatter Plot; nhận diện tuyến tính   │   isnull().sum() -> thử nghiệm dropna()    │
│ • Level 2: Chia Train/Test 80/20          │ • Level 2: Điền khuyết nâng cao            │
│   Hồi quy đa biến; so sánh R² train/test  │   Điền Mode theo nhóm phân loại            │
│ • Level 3: Xử lý ngoại lai dị biệt        │ • Level 3: Hợp nhất bảng dữ liệu           │
│   Lọc xe nhẹ giá đắt; chứng kiến R² tăng  │   pd.merge(how='left') -> kiểm tra 4 NaN   │
│ • Level 4: Hoàn thiện đường ống Z-Score   │ • Tiêu chuẩn nghiệm thu (DoD):             │
│   StandardScaler + OLS -> Test R² >= 0.70 │   Accuracy >= 95%, hiểu rõ False Negative  │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

---

### KHUNG TÓM TẮT & PHẢN XẠ 2 PHÚT CUỐI TRANG (2-MINUTE SUMMARY BOX)

> #### [CỐT LÕI] 3 CHÂN LÝ CỐT LÕI CẦN KHẮC SÂU VÀO TÂM TRÍ
> 1. **Data Scientist Mindset:** 70% giá trị nằm ở việc hiểu đúng bài toán nghiệp vụ và bản chất dữ liệu; thuật toán chỉ là công cụ tính toán thừa hành.
> 2. **Quy tắc Vàng Không Rò Rỉ Dữ Liệu (No Leakage):** Mọi phép tính toán tham số ($\mu, \sigma$, Imputation Mode) CHỈ ĐƯỢC PHÉP học trên tập **Train**. Tập **Test** phải được xem như dữ liệu đến từ tương lai.
> 3. **Cạm Bẫy Đa Cộng Tuyến:** Luôn luôn thiết lập `drop_first=True` khi tạo biến giả (Dummy Variables) cho mô hình Hồi quy tuyến tính để tránh sụp đổ ma trận.

---

> #### [ACTIVE RECALL] 3 CÂU HỎI TRUY HỒI TỰ KIỂM TRA PHẢN XẠ
> *(Hãy lấy một tờ giấy trắng che Cột 2 & Cột 3 và tự trả lời thành tiếng trước khi xem gợi ý)*
>
> 1. **Câu hỏi 1:** Khi tính hệ số tương quan Pearson $r$ giữa hai cột dữ liệu, nếu một cột chỉ chứa toàn một giá trị hằng số duy nhất (ví dụ: toàn số 5), hàm `np.corrcoef` sẽ trả về kết quả gì và tại sao?  
>    *Gợi ý suy luận:* Xem lại mẫu số của công thức Pearson — độ lệch chuẩn $\sigma$ của một biến hằng số bằng bao nhiêu? Một số chia cho 0 sẽ ra gì?
>
> 2. **Câu hỏi 2:** Tại sao thuật toán Cây Quyết Định (Decision Tree) lại không quan tâm đến việc bạn có chuẩn hóa Z-Score đặc trưng hay không, trong khi thuật toán K-Means lại bắt buộc phải có?  
>    *Gợi ý suy luận:* Cây quyết định so sánh giá trị theo kiểu nào ($x_j \le \theta$ hay tính khoảng cách hình học $\sqrt{\sum (x_j - c_j)^2}$)?
>
> 3. **Câu hỏi 3:** Trong bài toán chẩn đoán nấm độc ăn được hay chết người, loại sai lầm nào (False Positive hay False Negative) gây hậu quả nghiêm trọng hơn? Tại sao chỉ số Accuracy có thể tạo ra cảm giác an toàn giả tạo?  
>    *Gợi ý suy luận:* Giả sử có 1 cây nấm kịch độc trong 100 cây nấm. Một đứa trẻ đoán tất cả đều ăn được thì Accuracy là bao nhiêu? Điều gì xảy ra khi ăn cây nấm đó?

---

## [CHECKLIST] BẢNG CHECKLIST HÀNH ĐỘNG BUỔI 0 TRƯỚC KHI GẬP VỞ

- [ ] Đã chép đầy đủ các sơ đồ khối và công thức vào vở viết tay theo 3 cột Cornell.
- [ ] Đã hoàn thành 2 bài thực hành Workshop 1 (Car Price) và Workshop 2 (Mushroom) trên Google Colab.
- [ ] Nắm vững quy tắc không rò rỉ dữ liệu (No Data Leakage) và bẫy biến giả (Dummy Variable Trap).
- [ ] Sẵn sàng bước vào Buổi 1 với tâm thế của một Nhà Khoa học Dữ liệu thực nghiệm!

