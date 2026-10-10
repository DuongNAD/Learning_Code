# LỘ TRÌNH THỰC HÀNH VI MÔ & PHẢN XẠ NHẬN THỨC (MASTER MICRO-PRACTICE ROADMAP)
## Phân Rã Kiến Thức Thành Các Phiên Học 30–45 Phút Theo Nhịp Học Chuẩn 2 Bước & Buổi Ôn Tập Tổng Kết
### Chương trình: Global Consumer Intelligence (GCI World 2026 September) · Matsuo-Iwasawa Lab · Đại học Tokyo

---

## 1. NGUYÊN TẮC SƯ PHẠM & NHỊP HỌC CHUẨN (PEDAGOGICAL FRAMEWORK)

Nhằm tối ưu hóa hiệu quả tiếp thu kiến thức và ngăn chặn hội chứng "ảo tưởng năng lực" do copy-paste mã nguồn, toàn bộ chương trình GCI World 2026 September áp dụng quy trình học tập vi mô (Micro-learning) chuẩn mực:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        QUY TRÌNH HỌC TẬP 2 BƯỚC (2-STEP PEDAGOGICAL RHYTHM)            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [BƯỚC 1: PEN-FIRST (CHÉP TAY VÀO VỞ TRƯỚC KHI MỞ MÁY — 15–20 PHÚT)]                   │
│ • Mở Đề cương Vở viết tay (Cornell Notebook Syllabus) tương ứng.                      │
│ • Sử dụng sổ tay B5/A4 kẻ sẵn 3 cột theo tỷ lệ 20% - 50% - 30%.                        │
│ • Chép tay từ khóa vào Cột 1; vẽ sơ đồ khối, lưu đồ, công thức KaTeX vào Cột 2;        │
│   ghi nhận cú pháp API và cạm bẫy vào Cột 3.                                           │
│ • Nghiêm cấm mở Colab/Jupyter trong Bước 1 để não bộ tập trung mã hóa nhận thức sâu.   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [BƯỚC 2: PRACTICE & REFLECTION (THỰC HÀNH VI MÔ & PHẢN XẠ PHẢN BIỆN — 15–25 PHÚT)]     │
│ • Mở máy tính, thao tác trên môi trường Google Colab / Python cá nhân.                 │
│ • Giải quyết nhiệm vụ lập trình vi mô theo phương pháp Socratic 5 cấp độ của DeepTutor: │
│   Không cấp sẵn toàn bộ code hoàn chỉnh; hướng dẫn người học tự tư duy từ triệu chứng, │
│   quan sát biến trạng thái, kiểm tra trường hợp biên (edge cases) và cấu trúc hàm.     │
│ • Nghiệm thu theo Tiêu chí Hoàn thành (Definition of Done - DoD) rõ ràng, độc lập.    │
│ • Kiểm tra phản xạ tức thì thông qua Câu hỏi Active Recall chốt hạ.                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Quy Định Nhịp Học 3–5 Micro-Sessions + 1 Review Session Bắt Buộc:
- Mỗi buổi học lớn (Session) **BẮT BUỘC (MUST)** được chia nhỏ thành 3 đến 5 buổi học nhỏ (Micro-sessions), thời lượng từ **30 đến 45 phút** mỗi buổi.
- Sau khi hoàn thành toàn bộ các micro-sessions của một buổi lớn, học viên **BẮT BUỘC (MUST)** tham gia **1 Buổi Ôn Tập Tổng Kết (Review / Synthesis Session)** để liên kết các mắt xích, vẽ bản đồ khái niệm tổng thể và kiểm toán mức độ sẵn sàng trước khi chuyển sang buổi học tiếp theo.

---

## 2. LỘ TRÌNH BUỔI 0: PREPARATORY MATERIALS (KHÓA HỌC DỰ BỊ)

Buổi 0 bao gồm 4 Micro-Sessions (Micro-0.1 đến Micro-0.4) và 1 Buổi Ôn Tập Tổng Kết (Session 0.S).

```text
[ Micro-0.1: DS Mindset ] ──> [ Micro-0.2: Preprocessing ] ──> [ Micro-0.3: Stats & EDA ]
            │                                                               │
            └─────────────────────────┐   ┌─────────────────────────────────┘
                                      ▼   ▼
                           [ Micro-0.4: Basic ML & Validation ]
                                          │
                                          ▼
                           [ SESSION 0.S: SYNTHESIS & REVIEW ]
```

---

### MICRO-0.1: TƯ DUY KHOA HỌC DỮ LIỆU, QUY TRÌNH 4 BƯỚC & PHÂN LOẠI DỮ LIỆU
- **Mã phân đoạn:** `MISSION-0.1`
- **Thời lượng:** 35 Phút (15 phút chép tay + 20 phút thực hành vi mô)
- **Mục tiêu năng lực:** Hiểu rõ 3 trụ cột DS (Domain 60–70%), chu trình 4 bước chuẩn, phân biệt dữ liệu có cấu trúc vs phi cấu trúc, và biến định lượng vs định tính.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở tài liệu `syllabus/buoi0_handwritten_notebook_syllabus.md`, quan sát **PHẦN 1** và **PHẦN 2**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 0 | Micro-0.1 | Data Science Mindset & Taxonomy`.
3. Ghi vào Cột 1: `The 3 Pillars`, `4-Step Workflow`, `Data Taxonomy`, `Variable Scales`.
4. Vẽ vào Cột 2:
   - Sơ đồ tam giác 3 trụ cột: Domain Knowledge (60–70%) ở đỉnh, Computer Science (20%) và Math & Stats (10–20%) ở hai đáy.
   - Lưu đồ hình chữ nhật 4 bước: `[1. Understanding] -> [2. Preprocessing] -> [3. Modeling] -> [4. Evaluation]` với mũi tên phản hồi từ bước 4 quay lại bước 1.
   - Cây phân cấp phân loại biến số: Định lượng (Liên tục / Rời rạc) vs Định tính (Danh nghĩa / Thứ bậc).
5. Ghi vào Cột 3: Mã Python đọc dữ liệu và kiểm tra hình dạng `df.shape`, `df.dtypes`.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Khởi tạo một kịch bản kiểm toán dữ liệu cho tập dữ liệu ô tô (`Car_Price_Data.csv`) hoặc tạo DataFrame mẫu tương đương với 4 biến: `engine_size` (liên tục), `num_cylinders` (rời rạc), `body_style` (danh nghĩa), `safety_rating` (thứ bậc 1-5 sao).
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nhìn vào cột `safety_rating`, nếu tính `mean()` trên cột này thì kết quả có ý nghĩa toán học hay không? Còn nếu tính trên `body_style` ('sedan', 'hatchback') thì Python báo lỗi gì?
  - *Cấp độ 2 (Định hướng):* Làm thế nào để phân tách tự động các cột số và cột phân loại mà không cần nhập tay từng tên cột? Hãy tra cứu phương thức `df.select_dtypes()`.
- **Mã thực hành gợi ý:**
```python
import pandas as pd

# Khởi tạo dữ liệu mẫu mô phỏng Car Price Data
data = {
    "engine_size": [130.0, 152.0, 109.0, 136.0, 131.0],
    "num_cylinders": [4, 6, 4, 5, 5],
    "body_style": ["convertible", "hatchback", "sedan", "sedan", "hatchback"],
    "safety_rating": [3, 4, 2, 5, 4],
    "price": [13495, 16500, 13950, 17450, 15250],
}
df = pd.DataFrame(data)

# Kiểm toán cấu trúc
print("Kích thước bảng:", df.shape)
print("Các kiểu dữ liệu:\n", df.dtypes)

# Tách biến định lượng và định tính
num_cols = df.select_dtypes(include=["number"]).columns.tolist()
cat_cols = df.select_dtypes(exclude=["number"]).columns.tolist()
print("Biến định lượng:", num_cols)
print("Biến định tính:", cat_cols)
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Trang vở Cornell đã có sơ đồ 3 trụ cột và lưu đồ 4 bước được vẽ tay hoàn chỉnh.
- [ ] Đoạn mã Python thực thi không lỗi, phân tách chính xác danh sách các cột định lượng và định tính.
- [ ] Không sử dụng phép toán `mean()` trên các biến danh nghĩa.

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Tại sao trong thực tế, các dự án khoa học dữ liệu thất bại thường do thiếu Domain Knowledge chứ hiếm khi do thuật toán máy học chạy sai?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Thuật toán chỉ là công cụ tính toán thuần túy tối ưu hóa một hàm mất mát toán học. Nếu người làm dữ liệu không hiểu sâu nghiệp vụ (Domain Knowledge), họ sẽ định hình sai bài toán (Problem Formulation), chọn sai biến mục tiêu $y$, thu thập dữ liệu bị thiên lệch (Selection Bias) hoặc bỏ sót dữ liệu tối (Dark Data). Khi đó, mô hình dù có điểm số toán học rất cao trên tập kiểm thử vẫn hoàn toàn vô dụng hoặc gây thiệt hại kinh tế nặng nề cho doanh nghiệp khi triển khai thực tế.
</details>

---

### MICRO-0.2: TIỀN XỬ LÝ DỮ LIỆU, BẪY BIẾN GIẢ & CHUẨN HÓA Z-SCORE
- **Mã phân đoạn:** `MISSION-0.2`
- **Thời lượng:** 40 Phút (15 phút chép tay + 25 phút thực hành vi mô)
- **Mục tiêu năng lực:** Nắm vững quy tắc xử lý dữ liệu khuyết (`dropna` vs `fillna`), triệt tiêu bẫy biến giả đa cộng tuyến với `drop_first=True`, và chuẩn hóa Z-Score tuyệt đối không rò rỉ dữ liệu (No Data Leakage).

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi0_handwritten_notebook_syllabus.md`, quan sát **PHẦN 3**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 0 | Micro-0.2 | Data Preprocessing & Scaling`.
3. Ghi vào Cột 1: `Missing Values`, `Imputation Rules`, `Dummy Variable Trap`, `Multicollinearity`, `Z-Score Standardization`.
4. Vẽ vào Cột 2:
   - Sơ đồ rẽ nhánh xử lý NaN: Tỷ lệ khuyết $< 1\%$ $\to$ `dropna()`; Tỷ lệ khuyết $> 5\%$ $\to$ Imputation (Số học: Mean/Median; Danh mục: Mode).
   - Biểu thức bẫy biến giả: $x_K = 1 - \sum_{j=1}^{K-1} x_j \implies |X^T X| = 0$ (Ma trận suy biến).
   - Công thức Z-score KaTeX: $z = \frac{x - \mu}{\sigma}$.
5. Ghi vào Cột 3: Cú pháp `pd.get_dummies(..., drop_first=True)` và quy tắc chống rò rỉ dữ liệu của `StandardScaler`: `fit_transform` trên Train, chỉ `transform` trên Test.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Tạo một DataFrame có chứa giá trị NaN và cột phân loại; thực hiện điền Mode cho biến định tính; mã hóa One-Hot với `drop_first=True`; chia tập Train/Test và chuẩn hóa Z-Score đúng quy chuẩn Matsuo Lab.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nếu không truyền `drop_first=True`, một biến có 3 giá trị ('red', 'green', 'blue') sẽ sinh ra bao nhiêu cột nhị phân? Hãy tính tổng giá trị theo hàng ngang của 3 cột đó.
  - *Cấp độ 2 (Phản chứng):* Nếu bạn tính trung bình $\mu$ trên toàn bộ tập dữ liệu trước khi chia Train/Test, mô hình có thể đã "nhìn trộm" thông tin tương lai của tập Test như thế nào?
- **Mã thực hành gợi ý:**
```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Tạo dữ liệu kiểm thử
df_sample = pd.DataFrame({
    "engine_size": [130.0, np.nan, 109.0, 136.0, 131.0, 150.0],
    "fuel_type": ["gas", "gas", "diesel", np.nan, "gas", "diesel"],
    "price": [13495, 16500, 13950, 17450, 15250, 18000],
})

# 1. Kiểm toán NaN
print("Số lượng NaN ban đầu:\n", df_sample.isnull().sum())

# 2. Xử lý giá trị khuyết
df_sample["engine_size"] = df_sample["engine_size"].fillna(df_sample["engine_size"].median())
df_sample["fuel_type"] = df_sample["fuel_type"].fillna(df_sample["fuel_type"].mode()[0])

# 3. Tạo biến giả tránh đa cộng tuyến
df_encoded = pd.get_dummies(df_sample, columns=["fuel_type"], drop_first=True, dtype=int)

# 4. Phân chia dữ liệu
X = df_encoded.drop(columns=["price"])
y = df_encoded["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 5. Chuẩn hóa Z-Score không rò rỉ dữ liệu
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # CHỈ dùng transform

print("Trung bình Train sau chuẩn hóa (xấp xỉ 0):", np.round(X_train_scaled.mean(axis=0), 2))
print("Độ lệch chuẩn Train sau chuẩn hóa (xấp xỉ 1):", np.round(X_train_scaled.std(axis=0), 2))
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Công thức Z-score và phương trình giải thích bẫy biến giả được ghi chép vào Cột 2 vở viết tay.
- [ ] Mã hóa Dummy loại bỏ đúng 1 cột cơ sở (`drop_first=True`).
- [ ] `StandardScaler` được gọi phương thức `fit_transform` duy nhất 1 lần trên tập Train và `transform` trên tập Test; không có rò rỉ dữ liệu.

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Điều gì sẽ xảy ra về mặt đại số tuyến tính nếu ta đưa một tập biến One-Hot đầy đủ (không bỏ cột cơ sở) vào mô hình Hồi quy tuyến tính giải bằng phương trình Normal Equation $\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Khi giữ nguyên toàn bộ $K$ cột phân loại cùng với cột hệ số chặn bias ($x_0 = 1$), tổng của $K$ cột này luôn bằng chính xác cột hệ số chặn: $\sum_{j=1}^K x_{ij} = 1 = x_{i0}$ với mọi mẫu $i$. Điều này tạo ra sự phụ thuộc tuyến tính hoàn hảo giữa các cột trong ma trận thiết kế $\mathbf{X}$. Kết quả là ma trận $\mathbf{X}^T \mathbf{X}$ bị suy biến (Determinant $|\mathbf{X}^T \mathbf{X}| = 0$), không tồn tại ma trận nghịch đảo $(\mathbf{X}^T \mathbf{X})^{-1}$, và thuật toán OLS sẽ báo lỗi toán học sụp đổ ma trận (Singular Matrix Error).
</details>

---

### MICRO-0.3: PHÂN PHỐI THỐNG KÊ, TƯƠNG QUAN PEARSON & LỌC NGOẠI LAI TUKEY
- **Mã phân đoạn:** `MISSION-0.3`
- **Thời lượng:** 40 Phút (15 phút chép tay + 25 phút thực hành vi mô)
- **Mục tiêu năng lực:** Làm chủ các đại lượng đo lường xu hướng tập trung (Mean, Median), độ phân tán (Variance, Std Dev), tính toán tương quan Pearson $r$, và áp dụng hàng rào Tukey Boxplot ($1.5 \times \text{IQR}$) để phát hiện ngoại lai.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi0_handwritten_notebook_syllabus.md`, quan sát **PHẦN 5**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 0 | Micro-0.3 | Descriptive Statistics & Outliers`.
3. Ghi vào Cột 1: `Central Tendency`, `Dispersion`, `Boxplot & IQR`, `Tukey Fence`, `Pearson Correlation`, `Spurious Correlation`.
4. Vẽ vào Cột 2:
   - Công thức Mean $\bar{x} = \frac{1}{n}\sum x_i$ và Median (điểm chia 50%).
   - Công thức Phương sai $\sigma^2$ và Độ lệch chuẩn $\sigma = \sqrt{\sigma^2}$.
   - Sơ đồ giải phẫu Boxplot: Vạch Min, $Q_1$, Median ($Q_2$), $Q_3$, Max, cùng hai hàng rào ngoại lai: $Q_1 - 1.5\text{IQR}$ và $Q_3 + 1.5\text{IQR}$.
   - Công thức Pearson $r_{xy} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \in [-1, 1]$.
5. Ghi vào Cột 3: Code NumPy tính `np.mean()`, `np.median()`, `np.std()`, `np.corrcoef()`, và cú pháp lọc ngoại lai bằng Pandas `df[(condition1) & (condition2)]`.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Viết một đoạn script Python tính toán thống kê mô tả cho một chuỗi số liệu; tính hệ số tương quan Pearson giữa biến đặc trưng và biến mục tiêu; triển khai hàm phát hiện ngoại lai tự động theo quy tắc Tukey $1.5 \times \text{IQR}$.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nếu trong dãy số có 1 điểm cực đoan (ví dụ lương của 9 nhân viên là 10 triệu, riêng giám đốc là 500 triệu), chỉ số nào phản ánh trung thực mức thu nhập của đa số người lao động: Mean hay Median?
  - *Cấp độ 2 (Phản biện):* Nếu hệ số tương quan $r = 0$, có thể kết luận chắc chắn rằng hai biến số độc lập hoàn toàn với nhau không? (Gợi ý: Hãy nghĩ về quan hệ hàm phi tuyến $y = x^2$ trên đoạn $[-1, 1]$).
- **Mã thực hành gợi ý:**
```python
import numpy as np
import pandas as pd

# Tạo tập dữ liệu mô phỏng có ngoại lai
np.random.seed(42)
engine_sizes = np.array([100, 110, 120, 125, 130, 135, 140, 145, 150, 300]) # 300 là ngoại lai
prices = engine_sizes * 100 + np.random.normal(0, 500, len(engine_sizes))

# 1. Thống kê mô tả
mean_val = np.mean(engine_sizes)
median_val = np.median(engine_sizes)
std_val = np.std(engine_sizes)
print(f"Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std: {std_val:.2f}")

# 2. Tính hệ số tương quan Pearson
r = np.corrcoef(engine_sizes, prices)[0, 1]
print(f"Pearson r: {r:.4f}")

# 3. Phát hiện ngoại lai theo Tukey Boxplot
q1 = np.percentile(engine_sizes, 25)
q3 = np.percentile(engine_sizes, 75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

outliers = engine_sizes[(engine_sizes < lower_fence) | (engine_sizes > upper_fence)]
print(f"Hàng rào: [{lower_fence:.2f}, {upper_fence:.2f}]")
print(f"Các điểm ngoại lai phát hiện:", outliers)
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Đã vẽ hoàn chỉnh sơ đồ Boxplot và chú thích đầy đủ hai hàng rào Tukey vào Cột 2 vở viết tay.
- [ ] Đoạn mã tính toán ra đúng giá trị Pearson $r$, phân biệt rõ sự sai lệch giữa Mean và Median khi có điểm ngoại lai $300$.
- [ ] Hàm lọc ngoại lai phát hiện chính xác điểm $300$ nằm ngoài hàng rào trên $Q_3 + 1.5\text{IQR}$.

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Nếu một cột dữ liệu chỉ chứa toàn giá trị hằng số duy nhất (ví dụ toàn số 5 cho mọi dòng), hàm `np.corrcoef` sẽ trả về kết quả gì khi tính tương quan với một cột khác? Giải thích nguyên nhân dựa vào công thức toán học.*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Hàm `np.corrcoef` sẽ trả về giá trị `NaN` (Not a Number) và đưa ra cảnh báo chia cho số không (RuntimeWarning: invalid value encountered). Theo công thức Pearson $r_{xy} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$, mẫu số là tích của hai độ lệch chuẩn. Nếu một biến $X$ là hằng số, phương sai $\sigma_X^2 = \frac{1}{n}\sum(x_i - \bar{x})^2 = 0 \implies \sigma_X = 0$. Mẫu số bằng 0 dẫn tới phép chia không xác định trong toán học.
</details>

---

### MICRO-0.4: HỌC MÁY CƠ BẢN, KIẾN TRÚC OOP & ĐÁNH GIÁ MÔ HÌNH
- **Mã phân đoạn:** `MISSION-0.4`
- **Thời lượng:** 45 Phút (20 phút chép tay + 25 phút thực hành vi mô)
- **Mục tiêu năng lực:** Nắm vững cấu trúc Class OOP trong Python; phân biệt Học có giám sát (Hồi quy OLS, Cây quyết định) vs Không giám sát (K-Means, PCA); kiểm soát độ sâu `max_depth` chống quá khớp; hiểu cạm bẫy của chỉ số Accuracy.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi0_handwritten_notebook_syllabus.md`, quan sát **PHẦN 4, 6, 7, 8**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 0 | Micro-0.4 | Supervised ML & Evaluation`.
3. Ghi vào Cột 1: `Python OOP`, `Supervised vs Unsupervised`, `Linear Regression OLS`, `Decision Tree Splitting`, `Overfitting`, `MSE vs Accuracy`.
4. Vẽ vào Cột 2:
   - Sơ đồ Class Pokemon: Bản thiết kế (Attributes, Methods) $\to$ Đúc đối tượng instance.
   - Sơ đồ phân nhánh Cây quyết định và cơ chế tách nhị phân đệ quy.
   - Bảng so sánh rò rỉ dữ liệu: Train Set (80%) vs Test Set (20% bị khóa kín).
   - Công thức MSE KaTeX: $\text{MSE} = \frac{1}{n}\sum(y_i - \hat{y}_i)^2$ và chỉ số $R^2$.
5. Ghi vào Cột 3: Mẫu code khởi tạo mô hình Scikit-learn, thiết lập `max_depth=3`, tính toán MSE và $R^2$.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Xây dựng một đường ống huấn luyện hoàn chỉnh: phân chia Train/Test 80/20 (`random_state=42`), huấn luyện mô hình Linear Regression và mô hình Decision Tree Classifier với `max_depth=3`; đo lường và so sánh điểm số giữa tập Train và tập Test để đánh giá mức độ khái quát hóa.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nếu bạn để `max_depth=None` (không giới hạn độ sâu) cho Decision Tree, điểm Accuracy trên tập Train và tập Test thay đổi như thế nào? Dấu hiệu của Overfitting xuất hiện ở đâu?
  - *Cấp độ 2 (Phản biện):* Tại sao Decision Tree không bị ảnh hưởng bởi việc có chuẩn hóa Z-Score hay không, trong khi Linear Regression và K-Means lại bị ảnh hưởng trực tiếp?
- **Mã thực hành gợi ý:**
```python
from sklearn.datasets import make_regression, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

# 1. Thử nghiệm Hồi quy (Linear Regression)
X_reg, y_reg = make_regression(n_samples=200, n_features=3, noise=15.0, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

reg_model = LinearRegression().fit(X_tr, y_tr)
y_pred = reg_model.predict(X_te)
print("Linear Regression Test MSE:", round(mean_squared_error(y_te, y_pred), 2))
print("Linear Regression Test R2:", round(r2_score(y_te, y_pred), 4))

# 2. Thử nghiệm Cây quyết định kiểm soát độ sâu (Decision Tree)
X_clf, y_clf = make_classification(n_samples=200, n_features=4, random_state=42)
X_ctr, X_cte, y_ctr, y_cte = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

tree_controlled = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_ctr, y_ctr)
print("Tree Train Accuracy (max_depth=3):", round(tree_controlled.score(X_ctr, y_ctr), 4))
print("Tree Test Accuracy (max_depth=3):", round(tree_controlled.score(X_cte, y_cte), 4))
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Khái niệm OOP và công thức MSE được ghi chép chuẩn xác trong vở Cornell.
- [ ] Mô hình Hồi quy tuyến tính được huấn luyện và đánh giá trên tập Test độc lập, đạt $R^2 > 0.70$.
- [ ] Mô hình Cây quyết định được khống chế tham số `max_depth=3`, khoảng cách sai lệch giữa Train Accuracy và Test Accuracy nhỏ hơn 0.15 (không bị quá khớp nghiêm trọng).

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Tại sao trong bài toán chẩn đoán nấm độc ăn được hay gây chết người, chỉ số Accuracy lại nguy hiểm và gây ra cảm giác an toàn giả tạo? Chỉ số đo lường nào cần được ưu tiên tuyệt đối?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Trong bài toán nấm độc, tỷ lệ nấm kịch độc trong tự nhiên có thể rất thấp (ví dụ chỉ 1%). Một mô hình ngây ngô luôn dự đoán toàn bộ nấm là "ăn được" vẫn đạt chỉ số Accuracy lên tới 99%. Tuy nhiên, 1% nấm độc bị bỏ sót (False Negatives) sẽ gây chết người ngay lập tức. Trong bối cảnh này, chỉ số **Recall** (Độ nhạy: tỷ lệ nấm độc thực tế được phát hiện) phải được ưu tiên tối đa để đưa tỷ lệ bỏ sót ca nguy hiểm về tiệm cận 0.
</details>

---

### BUỔI ÔN TẬP TỔNG KẾT BUỔI 0 (SESSION 0.S: REVIEW & SYNTHESIS SESSION)
- **Mã phân đoạn:** `SYNTHESIS-0.S`
- **Thời lượng:** 45 Phút (20 phút tổng hợp bản đồ tri thức + 25 phút kiểm toán chuyển giao)
- **Mục tiêu:** Xâu chuỗi toàn bộ 4 micro-sessions của Buổi 0 thành một đường ống hoàn chỉnh (End-to-End Pipeline); đối chiếu bài học kinh nghiệm giữa hai Workshop kinh điển (Car Price vs Mushroom Classification); hoàn thành kiểm toán sẵn sàng bước sang Buổi 1.

#### 1. Bản Đồ Khái Niệm Tổng Thể Buổi 0 (Cross-Module Knowledge Graph)
Dưới đây là sơ đồ dòng chảy tổng hợp liên kết toàn bộ các mắt xích kiến thức từ Micro-0.1 đến Micro-0.4:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   DÒNG CHẢY ĐƯỜNG ỐNG DỮ LIỆU CHUẨN GCI (SESSION 0 PIPELINE)           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [BƯỚC 1: UNDERSTANDING (Micro-0.1 & Micro-0.3)]                                        │
│ • Kiểm toán kích thước bảng & kiểu biến (df.shape, df.dtypes).                         │
│ • Thống kê mô tả (Mean, Median, Std). Kiểm tra lệch phân phối.                         │
│ • Tính tương quan Pearson r; phát hiện ngoại lai bằng hàng rào Tukey 1.5*IQR.          │
│                                    │                                                   │
│                                    ▼                                                   │
│ [BƯỚC 2: PREPROCESSING (Micro-0.2)]                                                    │
│ • Kiểm toán NaN (df.isnull().sum()). Điền Median cho số, Mode cho phân loại.           │
│ • Mã hóa Dummy tránh bẫy đa cộng tuyến: pd.get_dummies(drop_first=True).               │
│ • Phân tách Train/Test 80/20 (random_state=42) TRƯỚC KHI thực hiện chuẩn hóa!          │
│ • Chuẩn hóa Z-Score: scaler.fit_transform(X_train), scaler.transform(X_test).         │
│                                    │                                                   │
│                                    ▼                                                   │
│ [BƯỚC 3: MODEL BUILDING (Micro-0.4)]                                                   │
│ • Lựa chọn thuật toán: Linear Regression (Hồi quy) hoặc Decision Tree (Phân loại).     │
│ • Kiểm soát siêu tham số: max_depth=3 để ngăn chặn học vẹt (Overfitting).              │
│ • Huấn luyện: model.fit(X_train_scaled, y_train).                                      │
│                                    │                                                   │
│                                    ▼                                                   │
│ [BƯỚC 4: EVALUATION & AUDIT (Micro-0.4)]                                               │
│ • Hồi quy: Đo lường MSE và R2 trên Test. So sánh sai lệch Train R2 vs Test R2.         │
│ • Phân loại: Lập ma trận nhầm lẫn, đo lường Accuracy, Precision, Recall.               │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 2. Bảng Đối Chiếu 2 Workshop Thực Hành Cốt Lõi Buổi 0
Học viên đối chiếu lại hai dự án thực hành vi mô trong đề cương:

| Đặc Điểm So Sánh | Workshop 1: Hồi Quy Giá Xe (Car Price) | Workshop 2: Phân Loại Nấm Độc (Mushroom) |
| :--- | :--- | :--- |
| **Loại bài toán** | Học có giám sát — Hồi quy (Regression) | Học có giám sát — Phân loại (Classification) |
| **Biến mục tiêu $y$** | Liên tục: Giá xe (`price` tính bằng USD) | Nhị phân: Ăn được (`e`) vs Độc hại (`p`) |
| **Thách thức dữ liệu** | Chênh lệch đơn vị đo; điểm ngoại lai đắt giá | Nhiều biến phân loại; dữ liệu bị khuyết |
| **Kỹ thuật xử lý** | Lọc ngoại lai Tukey + Chuẩn hóa Z-Score | `drop_first=True` + Điền Mode + Ghép bảng `how='left'` |
| **Thuật toán chính** | Hồi quy tuyến tính OLS (`LinearRegression`) | Cây quyết định (`DecisionTreeClassifier(max_depth=3)`) |
| **Thước đo cốt lõi** | Mean Squared Error (MSE) & Điểm số $R^2$ | Recall (Bắt trọn nấm độc) & Confusion Matrix |
| **Nguy cơ lớn nhất** | Bẫy đa cộng tuyến làm sập ma trận $X^T X$ | False Negative làm ngộ độc chết người |

#### 3. Bảng Kiểm Toán Mức Độ Sẵn Sàng (Milestone 0 Readiness Audit)
Học viên chỉ được phép chuyển sang Buổi 1 nếu thỏa mãn 100% các tiêu chí dưới đây:
- [ ] Vở viết tay cá nhân đã ghi chép đầy đủ 4 bài vi mô theo cấu trúc 3 cột Cornell.
- [ ] Không có bất kỳ công thức KaTeX hoặc sơ đồ nào bị bỏ trống.
- [ ] Đã trả lời chính xác cả 4 câu hỏi Active Recall trong các phân đoạn Micro-0.1 đến 0.4.
- [ ] Nắm vững quy tắc cấm gọi `fit_transform` trên tập kiểm thử (Test Set).
- [ ] Nắm vững lý do toán học vì sao biến phân loại $K$ nhóm chỉ tạo $K-1$ biến giả.

---

## 3. LỘ TRÌNH BUỔI 1: ORIENTATION, DATA MINDSET & AI MOATS (KHAI GIẢNG & HÀO LŨY AI)

Buổi 1 bao gồm 5 Micro-Sessions (Micro-1.1 đến Micro-1.5) và 1 Buổi Ôn Tập Tổng Kết (Session 1.S).

```text
[ Micro-1.1: Mindset & CRISP-DM ] ──> [ Micro-1.2: Dark Data & Translation ]
                 │                                        │
                 ▼                                        ▼
[ Micro-1.3: AI Moats & Tanpin Kanri ] ──> [ Micro-1.4: 14-Week & ML Ladder ]
                                                          │
                                                          ▼
                                           [ Micro-1.5: Ecosystem & Policies ]
                                                          │
                                                          ▼
                                           [ SESSION 1.S: SYNTHESIS & REVIEW ]
```

---

### MICRO-1.1: TƯ DUY ĐỊNH HƯỚNG DỮ LIỆU, BÙNG NỔ DỮ LIỆU & CHU TRÌNH CRISP-DM
- **Mã phân đoạn:** `MISSION-1.1`
- **Thời lượng:** 35 Phút (15 phút chép tay + 20 phút thực hành vi mô)
- **Mục tiêu năng lực:** Hiểu rõ quy mô bùng nổ dữ liệu (527 ZB năm 2029), nghịch lý lưu trữ vs tri thức, và 6 giai đoạn tuần hoàn của chu trình CRISP-DM.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi1_handwritten_notebook_syllabus.md`, quan sát **PHẦN 1**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 1 | Micro-1.1 | Data-Driven Mindset & CRISP-DM`.
3. Ghi vào Cột 1: `Evidence-Based Decision`, `Zettabyte Explosion (527 ZB)`, `CRISP-DM 6 Phases`, `Storage != Knowledge`.
4. Vẽ vào Cột 2:
   - Biểu thức quy đổi: $1\text{ ZB} = 10^{21}\text{ bytes} = 1\text{ Tỷ Terabytes}$.
   - Sơ đồ chu trình CRISP-DM 6 giai đoạn dạng vòng tròn khép kín:
     `(1) Business Understanding -> (2) Data Understanding -> (3) Data Preparation -> (4) Modeling -> (5) Evaluation -> (6) Deployment`.
   - Mũi tên hồi tiếp từ Giai đoạn 5 (Evaluation) quay lại Giai đoạn 1 nếu không đạt KPI.
5. Ghi vào Cột 3: Quy tắc phân bổ thời gian thực tế: 80% thời gian dự án nằm ở giai đoạn 2 & 3 (Data Understanding & Preparation).

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Viết script Python tính toán tốc độ tăng trưởng dữ liệu từ 64 ZB (2020) lên 527 ZB (2029); mô phỏng việc kiểm tra điều kiện đánh giá mô hình (Giai đoạn 5 CRISP-DM) để tự động quyết định có được phép đưa mô hình vào triển khai (Deployment) hay phải quay lại làm sạch dữ liệu.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nếu tỷ lệ dữ liệu lưu trữ tăng gấp 8 lần nhưng năng lực phân tích dữ liệu của con người không tăng tương ứng, điều gì sẽ xảy ra với chi phí hạ tầng và hiệu quả kinh doanh?
  - *Cấp độ 2 (Định hướng):* Tại sao giai đoạn 1 (Business Understanding) lại được đặt lên trước giai đoạn 2 (Data Understanding)? Nếu đảo ngược hai bước này thì rủi ro là gì?
- **Mã thực hành gợi ý:**
```python
# Mô phỏng tính toán bùng nổ Zettabyte
zb_2020 = 64
zb_2029 = 527
growth_factor = zb_2029 / zb_2020
print(f"Tốc độ tăng trưởng dữ liệu 2020-2029: {growth_factor:.2f} lần")
print(f"527 ZB tương đương: {527 * (10**9):,} Terabytes")

# Mô phỏng cổng kiểm soát CRISP-DM (Evaluation Gate)
def crisp_dm_decision_gate(test_r2: float, target_kpi: float = 0.75):
    print(f"Đánh giá mô hình: R2 = {test_r2:.3f} | KGI/KPI mục tiêu = {target_kpi:.3f}")
    if test_r2 >= target_kpi:
        return "PHÊ DUYỆT: Chuyển sang Giai đoạn 6 (Deployment & Expansion)"
    else:
        return "TỪ CHỐI: Quay lại Giai đoạn 1 (Business) hoặc Giai đoạn 3 (Data Prep)"

print(crisp_dm_decision_gate(test_r2=0.68))
print(crisp_dm_decision_gate(test_r2=0.82))
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay có sơ đồ 6 giai đoạn CRISP-DM kèm mũi tên phản hồi.
- [ ] Script Python tính đúng tốc độ tăng trưởng 8.23 lần và hiển thị đúng logic rẽ nhánh của cổng kiểm soát CRISP-DM.
- [ ] Trả lời mạch lạc lý do vì sao làm sạch dữ liệu chiếm 80% thời lượng dự án.

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Nếu một dự án khoa học dữ liệu đạt kết quả đánh giá mô hình rất cao ở Bước 5 (Evaluation) nhưng người dùng cuối từ chối sử dụng hệ thống ở Bước 6 (Deployment), sai lầm bắt nguồn từ giai đoạn nào của CRISP-DM?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Sai lầm bắt nguồn từ **Giai đoạn 1: Business Understanding (Thấu hiểu bài toán kinh doanh)**. Nhóm kỹ sư đã chỉ tập trung tối ưu hóa các chỉ số kỹ thuật trên dữ liệu mà không thấu hiểu sâu sắc quy trình tác nghiệp thực tế của người dùng, không xác định đúng rào cản chi phí chuyển đổi hoặc không tích hợp được mô hình vào luồng làm việc hàng ngày (Workflow Integration).
</details>

---

### MICRO-1.2: DỮ LIỆU TỐI, THIÊN LỆCH LỰA CHỌN & CHUYỂN NGỮ BÀI TOÁN KINH DOANH
- **Mã phân đoạn:** `MISSION-1.2`
- **Thời lượng:** 40 Phút (15 phút chép tay + 25 phút thực hành vi mô)
- **Mục tiêu năng lực:** Phân tích bản chất hiện tượng Dark Data qua nghịch lý xe bán đồ ăn (The Food Truck Paradox); nhận diện thiên lệch lựa chọn (Selection Bias); chuyển ngữ yêu cầu kinh doanh mơ hồ thành bộ ba toán học ($y, X, \text{Metric}$).

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi1_handwritten_notebook_syllabus.md`, quan sát **PHẦN 1**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 1 | Micro-1.2 | Dark Data & Problem Formulation`.
3. Ghi vào Cột 1: `Food Truck Paradox`, `Dark Data (Hand & Hosoya)`, `Selection Bias`, `Problem Formulation`, `Target y & Features X`.
4. Vẽ vào Cột 2:
   - Sơ đồ tảng băng trôi: Phần nổi 10% (Dữ liệu đã thu thập trong DB) vs Phần chìm 90% (Dữ liệu tối: khách bỏ đi, hết hàng sớm, yếu tố thời tiết).
   - Bảng chuyển ngữ 3 cột: Mong muốn kinh doanh $\to$ Biến mục tiêu $y \to$ Tập đặc trưng $X$.
   - Trích dẫn Demis Hassabis: *"Asking the right question is the hardest part of science."*
5. Ghi vào Cột 3: Danh mục câu hỏi kiểm toán thiên lệch: *"Dữ liệu này thiếu ai? Điều gì chưa được ghi nhận?"*.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Phân tích một kịch bản kinh doanh: Một ngân hàng muốn "dùng AI để giảm rủi ro tín dụng". Họ huấn luyện mô hình trên dữ liệu của các khách hàng đã từng được duyệt vay trong 5 năm qua. Hãy viết code minh họa sự sai lệch phân phối (Distribution Shift / Selection Bias) giữa tập khách hàng đã vay và toàn bộ tệp ứng viên nộp hồ sơ.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Triệu chứng):* Những người bị từ chối vay trong quá khứ có được lưu lịch sử trả nợ không? Mô hình có biết họ có thực sự vỡ nợ hay không?
  - *Cấp độ 2 (Phản biện):* Nếu chỉ huấn luyện trên những người được duyệt, mô hình đang học cách bắt chước chính sách xét duyệt cũ hay đang học rủi ro thực tế của thị trường?
- **Mã thực hành gợi ý:**
```python
import numpy as np
import pandas as pd

# Mô phỏng tập toàn bộ ứng viên nộp hồ sơ vay (Population)
np.random.seed(42)
n_applicants = 1000
credit_score = np.random.normal(600, 100, n_applicants)

# Chính sách xét duyệt cũ: Chỉ cho vay người có điểm tín dụng >= 650
approved_mask = credit_score >= 650
approved_data = credit_score[approved_mask]
rejected_dark_data = credit_score[~approved_mask]

print(f"Tổng số ứng viên: {n_applicants}")
print(f"Số lượng được duyệt (Visible Data): {len(approved_data)} ({len(approved_data)/n_applicants*100:.1f}%)")
print(f"Số lượng bị từ chối (Dark Data): {len(rejected_dark_data)} ({len(rejected_dark_data)/n_applicants*100:.1f}%)")
print(f"Điểm tín dụng trung bình nhìn thấy: {approved_data.mean():.2f}")
print(f"Điểm tín dụng trung bình thực tế toàn dân: {credit_score.mean():.2f}")
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở ghi chép có hình vẽ tảng băng chìm Dark Data và trích dẫn của Hand & Hosoya.
- [ ] Code Python minh chứng được sự chênh lệch lớn giữa phân phối dữ liệu nhìn thấy và phân phối thực tế của toàn thể dân số.
- [ ] Lập được bảng chuyển ngữ bài toán cụ thể cho 1 đề tài kinh doanh gồm đủ $y, X$ và Metric.

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Tại sao việc một nhà hàng đếm số lượng khách ăn hết sạch 100% đồ ăn trên đĩa lại không thể chứng minh khẳng định rằng món ăn đó ngon tuyệt đỉnh? Thành phần dữ liệu tối nào đang bị bỏ sót?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Số liệu đĩa ăn hết sạch chỉ phản ánh hành vi của những khách hàng **đã quyết định gọi món và đang đói**; nó không đo lường được những người vì đói hoặc tiếc tiền nên cố ăn hết dù vị rất tệ. Quan trọng hơn, thành phần **Dark Data khổng lồ** bị bỏ sót hoàn toàn bao gồm: những khách hàng nếm một miếng rồi bỏ dở đĩa nhưng bồi bàn dọn đi không ghi chép; những khách hàng cũ không bao giờ quay lại lần thứ hai; và những khách hàng đi ngang qua cửa nhìn vào thực đơn rồi bỏ đi nơi khác vì giá quá đắt hoặc món ăn nghèo nàn.
</details>

---

### MICRO-1.3: HÀO LŨY AI PHÒNG THỦ, BÁNH ĐÀ DỮ LIỆU & VÒNG LẶP SEVEN-ELEVEN JAPAN
- **Mã phân đoạn:** `MISSION-1.3`
- **Thời lượng:** 40 Phút (15 phút chép tay + 25 phút thực hành vi mô)
- **Mục tiêu năng lực:** Hiểu rõ tại sao database tĩnh không phải là hào lũy trong kỷ nguyên LLM; cơ chế Bánh đà Dữ liệu tích hợp quy trình (Workflow Integration); làm chủ 4 bước vòng lặp Tanpin Kanri tại Seven-Eleven Japan; áp dụng nguyên lý Falsification (chứng minh điều sai siêu tốc).

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi1_handwritten_notebook_syllabus.md`, quan sát **PHẦN 2**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 1 | Micro-1.3 | AI Moats & Tanpin Kanri`.
3. Ghi vào Cột 1: `Defensible AI Moat`, `Static SaaS Fall`, `Workflow Integration`, `Data Flywheel`, `Tanpin Kanri (7-Eleven)`, `Rapid Falsification`.
4. Vẽ vào Cột 2:
   - Trích dẫn giảng viên Shuda về sự suy tàn của database tĩnh.
   - Sơ đồ Bánh đà Dữ liệu tự cường hóa: `Tích Hợp Quy Trình -> Trải Nghiệm Người Dùng -> Dữ Liệu Tương Tác Mới -> Phản Hồi Độc Quyền -> Huấn Luyện Lại -> Mô Hình Vượt Trội`.
   - Vòng lặp Tanpin Kanri: `(1) Observe -> (2) Hypothesize -> (3) Order & Sell -> (4) Check & Revise`.
5. Ghi vào Cột 3: Mẫu hàm logic Python mô phỏng quyết định đặt hàng theo giờ và thời tiết; nguyên tắc phân công người - máy trong nghiên cứu khoa học.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Xây dựng một module Python mô phỏng logic ra quyết định đặt hàng tự động của cửa hàng Seven-Eleven dựa trên sự kết hợp giữa dữ liệu quá khứ, dự báo thời tiết và xu hướng giờ cao điểm; triển khai cơ chế kiểm tra phản nghiệm (Falsification check).
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nếu chỉ dựa vào số bán của tuần trước để đặt hàng cho hôm nay mà hôm nay trời đổ mưa bão bất ngờ, hậu quả tồn kho hoặc đứt hàng sẽ ra sao?
  - *Cấp độ 2 (Phản biện):* Thay vì cố gắng tìm một thuật toán dự báo hoàn hảo, việc dùng AI để chạy 100 kịch bản giả định khác nhau nhằm tìm ra những kịch bản chắc chắn gây thua lỗ lớn mang lại lợi thế gì?
- **Mã thực hành gợi ý:**
```python
def tanpin_kanri_order(
    base_demand: int,
    weather_rain: bool,
    temperature_drop: bool,
    pos_trend_ratio: float
) -> int:
    """
    Mô phỏng logic đặt hàng Tanpin Kanri cho mặt hàng Cơm nắm nóng / Lẩu Oden.
    """
    order_qty = float(base_demand)
    
    # 1. Quan sát & Điều chỉnh theo thời tiết
    if weather_rain and temperature_drop:
        order_qty *= 1.40  # Tăng 40% nhu cầu thức ăn nóng
    elif weather_rain and not temperature_drop:
        order_qty *= 0.85  # Giảm 15% do khách ngại ra đường
        
    # 2. Điều chỉnh theo xung lượng bán lẻ giờ gần nhất
    order_qty *= pos_trend_ratio
    
    return int(round(order_qty))

# Kiểm thử các kịch bản thực nghiệm
print("Kịch bản 1 (Trời nắng ráo, trend bình thường):", 
      tanpin_kanri_order(base_demand=100, weather_rain=False, temperature_drop=False, pos_trend_ratio=1.0))
print("Kịch bản 2 (Trời mưa rét, trend mua tăng cao):", 
      tanpin_kanri_order(base_demand=100, weather_rain=True, temperature_drop=True, pos_trend_ratio=1.25))
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay có sơ đồ vòng lặp Bánh đà Dữ liệu và 4 bước Tanpin Kanri.
- [ ] Đoạn mã hàm `tanpin_kanri_order` thực thi chính xác theo các điều kiện logic giả thuyết.
- [ ] Giải thích được tại sao Workflow Integration tạo ra hào lũy phòng thủ vững chắc hơn cơ sở dữ liệu tĩnh.

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Tại sao việc một công ty khởi nghiệp chỉ cào dữ liệu công khai trên mạng rồi đóng gói vào mô hình AI lại có nguy cơ bị phá sản cao khi các mô hình nền tảng như GPT-5 ra đời? Yếu tố nào tạo nên hào lũy bền vững duy nhất?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Khi một công ty chỉ sử dụng dữ liệu tĩnh cào từ Internet, các mô hình nền tảng thế hệ mới (như GPT-5 hay Claude 4) có năng lực khái quát hóa vượt trội và được nạp kho dữ liệu toàn cầu lớn hơn gấp vạn lần, dễ dàng thực hiện cùng tác vụ với chi phí rẻ hơn và độ chính xác cao hơn. Hào lũy phòng thủ bền vững duy nhất là **Tích hợp sâu vào quy trình nghiệp vụ (Workflow Integration)**. Khi sản phẩm được nhúng trực tiếp vào công việc hàng ngày của người dùng, nó liên tục tạo ra luồng dữ liệu tương tác độc quyền (Proprietary Interaction Data) mà các công ty AI bên ngoài không bao giờ có được, đồng thời tạo ra rào cản chi phí chuyển đổi cực cao cho khách hàng.
</details>

---

### MICRO-1.4: LỘ TRÌNH 14 TUẦN, NẤC THANG 5 BƯỚC ML & MA TRẬN ĐÁNH ĐỔI CHI PHÍ
- **Mã phân đoạn:** `MISSION-1.4`
- **Thời lượng:** 40 Phút (15 phút chép tay + 25 phút thực hành vi mô)
- **Mục tiêu năng lực:** Nắm vững cấu trúc 4 giai đoạn của lộ trình 14 tuần; làm chủ nấc thang 5 bước leo Leaderboard cuộc thi; phân tích sự đánh đổi giữa Accuracy và Recall dựa trên ma trận chi phí tài chính thực tế ($C_{\text{FN}}$ vs $C_{\text{FP}}$).

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi1_handwritten_notebook_syllabus.md`, quan sát **PHẦN 3**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 1 | Micro-1.4 | 14-Week Roadmap, ML Ladder & Cost Matrix`.
3. Ghi vào Cột 1: `14-Week Roadmap`, `5-Step ML Ladder`, `Cost Matrix Tradeoff`, `Precision vs Recall`, `Optuna Tuning`, `Temporal Leakage`.
4. Vẽ vào Cột 2:
   - Sơ đồ nấc thang 5 bước ML: `[1. Baseline] -> [2. New Features] -> [3. Change Model] -> [4. Tune Optuna] -> [5. Advanced Ensembling]`.
   - Công thức KaTeX của Recall $= \frac{\text{TP}}{\text{TP}+\text{FN}}$ và Precision $= \frac{\text{TP}}{\text{TP}+\text{FP}}$.
   - Phương trình ma trận chi phí: $\text{Total Cost} = C_{\text{FN}} \cdot \text{FN} + C_{\text{FP}} \cdot \text{FP}$.
   - Công thức chuỗi thời gian tự tương quan: $\rho_k = \frac{\sum (X_t - \bar{X})(X_{t-k} - \bar{X})}{\sum (X_t - \bar{X})^2}$.
5. Ghi vào Cột 3: Khung code Scikit-learn tính `confusion_matrix`, `classification_report`, và mẫu hàm mục tiêu Optuna `objective(trial)`.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Viết một chương trình Python mô phỏng bài toán phát hiện giao dịch gian lận hoặc chẩn đoán y tế có tỷ lệ dương tính thấp (10%); so sánh tổn thất tài chính giữa Model A (Accuracy 90%, Recall 50%) và Model B (Accuracy 90%, Recall 100%) khi chi phí bỏ sót gian lận $C_{\text{FN}} = 50,000\$$ và chi phí xác minh cảnh báo giả $C_{\text{FP}} = 200\$$.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nhìn vào điểm Accuracy, hai mô hình có điểm số giống hệt nhau không? Nhưng số ca gian lận lọt lưới ở Model A là bao nhiêu so với Model B?
  - *Cấp độ 2 (Phản biện):* Tại sao trong cuộc thi ML, việc đầu tư vào Feature Engineering (Bước 2) luôn mang lại lợi ích lớn hơn nhiều so với việc chỉ ngồi chạy Optuna dò siêu tham số (Bước 4)?
- **Mã thực hành gợi ý:**
```python
import numpy as np

# Giả lập 100 mẫu dữ liệu: 10 ca gian lận thực tế (Positive), 90 ca hợp pháp (Negative)
# Chi phí sai lầm kinh doanh:
C_FN = 50000  # Bỏ sót 1 ca gian lận mất 50,000 USD
C_FP = 200    # Khóa nhầm thẻ của khách hợp pháp mất 200 USD phí hỗ trợ

# Model A: Bắt được 5 ca, bỏ sót 5 ca (FN=5); Khóa nhầm 5 khách (FP=5)
# Accuracy = (5 + 85) / 100 = 90% | Recall = 5 / 10 = 50%
cost_model_a = (5 * C_FN) + (5 * C_FP)

# Model B: Bắt trọn 10 ca (FN=0); Khóa nhầm 10 khách (FP=10)
# Accuracy = (10 + 80) / 100 = 90% | Recall = 10 / 10 = 100%
cost_model_b = (0 * C_FN) + (10 * C_FP)

print(f"Tổng tổn thất tài chính Model A (Recall 50%): ${cost_model_a:,}")
print(f"Tổng tổn thất tài chính Model B (Recall 100%): ${cost_model_b:,}")
print(f"Model B tiết kiệm cho doanh nghiệp: ${cost_model_a - cost_model_b:,}")
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay có sơ đồ nấc thang 5 bước ML Ladder và công thức tính tổn thất ma trận chi phí.
- [ ] Script Python chứng minh định lượng rằng Model B tiết kiệm được hơn 240,000 USD so với Model A dù hai mô hình có cùng điểm Accuracy 90%.
- [ ] Nắm vững nguy cơ rò rỉ thời gian (Temporal Leakage) khi dùng `shuffle=True` trên chuỗi thời gian.

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Nếu một mô hình dự báo doanh số bán hàng trong tương lai đạt điểm $R^2 = 0.98$ khi kiểm thử bằng K-Fold Cross Validation ngẫu nhiên (`shuffle=True`), tại sao giảng viên Matsuo Lab sẽ lập tức đánh trượt bài làm này? Hiện tượng gì đã xảy ra?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Dữ liệu doanh số bán hàng là dữ liệu chuỗi thời gian (Time-Series) có tính phụ thuộc thời gian và tự tương quan $\rho_k$. Khi bật cờ `shuffle=True`, các mẫu dữ liệu của tương lai (ví dụ ngày 15/10) bị xáo trộn và đưa vào tập huấn luyện để dự báo doanh số của quá khứ (ví dụ ngày 10/10). Đây là hiện tượng **Rò rỉ dữ liệu xuyên thời gian (Temporal Data Leakage)**. Mô hình đã "học vẹt tương lai" nên đạt điểm $R^2$ cao giả tạo; khi đưa vào chạy thực tế trong tương lai chưa từng xảy ra, mô hình sẽ sụp đổ hoàn toàn. Quy chuẩn bắt buộc là phải cắt dữ liệu tuần tự theo trục thời gian (`TimeSeriesSplit` hoặc cắt theo mốc ngày cố định).
</details>

---

### MICRO-1.5: HỆ SINH THÁI CÔNG CỤ, QUY CHẾ KHÓA HỌC & TIÊU CHUẨN THAM QUAN ĐH TOKYO
- **Mã phân đoạn:** `MISSION-1.5`
- **Thời lượng:** 35 Phút (15 phút chép tay + 20 phút thực hành vi mô)
- **Mục tiêu năng lực:** Thiết lập toàn diện hệ sinh thái 4 công cụ (Omnicampus, Quri AI, Google Colab, Slack); nắm vững quy định điểm danh Zero Late Policy (14 bài khảo sát, tối thiểu $\ge 7$), quy chế tính điểm bài tập tuần (8 bài x 3đ = 24đ, tối thiểu $\ge 14$đ), và tiêu chuẩn xét duyệt chuyến đi Tokyo (Top 10% Final, Top 20% Competition).

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở `syllabus/buoi1_handwritten_notebook_syllabus.md`, quan sát **PHẦN 4**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 1 | Micro-1.5 | Ecosystem, Policies & Tokyo Tour`.
3. Ghi vào Cột 1: `Omnicampus LMS`, `Quri AI Tutor`, `Zero Late Policy (14 Surveys)`, `Homework Scoring (14/24)`, `3-Tier Graduation`, `Tokyo Study Tour Criteria`.
4. Vẽ vào Cột 2:
   - Sơ đồ 4 công cụ chính thức và URL tương ứng.
   - Sơ đồ hình tháp 3 cấp chứng chỉ tốt nghiệp: Completed ($\ge 7/14$ điểm danh, $\ge 14/24$ bài tập) $\to$ Honors (Top 10% Final + Top 20% Competition) $\to$ Outstanding (Tokyo Study Tour).
   - Hạn chót Khảo sát Buổi 1: **11:00 AM UTC ngày 08/10/2026**.
5. Ghi vào Cột 3: Hành động bắt buộc: Đổi Slack Display Name trùng khớp 100% với Username Omnicampus (`Duongne2000`); đặt toàn bộ repo bài tập ở chế độ Private.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Viết một script Python đóng vai trò "Trợ lý Giám sát Học tập Cá nhân" (Personal Academic Sentinel) kiểm tra điều kiện tốt nghiệp dựa trên số bài khảo sát đã làm, điểm số các bài tập tuần và xếp hạng cuộc thi; cảnh báo ngay lập tức nếu vi phạm bất kỳ điều kiện nào.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Nếu bạn được điểm tuyệt đối 24/24 bài tập tuần nhưng chỉ hoàn thành 6 bài khảo sát điểm danh, kết quả tốt nghiệp sẽ ra sao?
  - *Cấp độ 2 (Định hướng):* Tại sao chính sách của ĐH Tokyo quy định nộp muộn bài tập tuần vẫn được tối đa 2 điểm, nhưng khảo sát điểm danh thì tuyệt đối không mở lại sau hạn chót?
- **Mã thực hành gợi ý:**
```python
def check_graduation_status(
    attendance_count: int,
    homework_scores: list,
    final_submitted: bool,
    final_top_pct: float,
    comp_top_pct: float
) -> str:
    """
    Kiểm tra điều kiện phân tầng tốt nghiệp GCI World 2026.
    """
    total_hw = sum(homework_scores)
    
    # 1. Kiểm tra điều kiện tiên quyết Cấp 1 (Completed)
    if attendance_count < 7:
        return f"TRƯỢT: Không đủ điểm danh ({attendance_count}/14). Cần tối thiểu 7 buổi."
    if total_hw < 14.0:
        return f"TRƯỢT: Không đủ điểm bài tập ({total_hw:.1f}/24.0). Cần tối thiểu 14 điểm."
    if not final_submitted:
        return "TRƯỢT: Chưa nộp Đồ án Cuối khóa (Final Assignment)."
        
    # 2. Kiểm tra điều kiện Cấp 2 (Honors) & Cấp 3 (Outstanding)
    if final_top_pct <= 10.0 and comp_top_pct <= 20.0:
        return (f"XUẤT SẮC: Đạt chuẩn CẤP 2 (HONORS) & ỨNG VIÊN CẤP 3 (TOKYO STUDY TOUR)!\n"
                f"- Điểm danh: {attendance_count}/14\n"
                f"- Tổng điểm bài tập: {total_hw:.1f}/24.0\n"
                f"- Top Final: {final_top_pct}% (Đạt Top 10%)\n"
                f"- Top Competition: {comp_top_pct}% (Đạt Top 20%)")
    
    return f"ĐẠT: Tốt nghiệp CẤP 1 (COMPLETED STUDENT). Tổng điểm HW: {total_hw:.1f}, Điểm danh: {attendance_count}/14."

# Chạy thử nghiệm kịch bản
scores_sample = [3.0, 3.0, 2.0, 3.0, 3.0, 2.0, 3.0, 3.0] # 22 điểm
print(check_graduation_status(
    attendance_count=12,
    homework_scores=scores_sample,
    final_submitted=True,
    final_top_pct=8.5,
    comp_top_pct=15.0
))
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay ghi rõ hạn chót 08/10/2026 và tiêu chí 3 cấp độ tốt nghiệp.
- [ ] Hàm Python kiểm toán tốt nghiệp phản ánh chính xác 100% các ngưỡng điểm danh ($\ge 7$), điểm bài tập ($\ge 14$), và tiêu chuẩn Top 10% Final / Top 20% Competition.
- [ ] Slack Display Name đã được đồng bộ với tài khoản Omnicampus (`Duongne2000`).

#### Câu Hỏi Truy Hồi Tự Kiểm Tra (Diagnostic Active Recall)
*Nếu một học viên đạt điểm tuyệt đối 24/24 bài tập tuần và đứng Top 1 cuộc thi Machine Learning nhưng chỉ nộp 6 bài khảo sát điểm danh, học viên đó có được cấp chứng chỉ tốt nghiệp của Đại học Tokyo không? Tại sao?*

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:* Học viên đó **HOÀN TOÀN KHÔNG ĐƯỢC CẤP CHỨNG CHỈ TỐT NGHIỆP** (Fail). Theo quy chế chính thức của Ban Giảng huấn Matsuo-Iwasawa Lab (Đại học Tokyo), điều kiện hoàn thành khảo sát điểm danh tối thiểu $\ge 7 / 14$ buổi là **điều kiện tiên quyết bắt buộc (Hard Prerequisite)**. Do áp dụng chính sách Zero Late Policy tuyệt đối, việc thiếu dù chỉ 1 bài khảo sát điểm danh dưới ngưỡng 7 bài sẽ hủy bỏ tư cách công nhận tốt nghiệp của học viên, bất kể điểm số bài tập tuần hay thứ hạng cuộc thi có xuất sắc đến đâu.
</details>

---

### BUỔI ÔN TẬP TỔNG KẾT BUỔI 1 (SESSION 1.S: REVIEW & SYNTHESIS SESSION)
- **Mã phân đoạn:** `SYNTHESIS-1.S`
- **Thời lượng:** 45 Phút (20 phút tổng hợp chiến lược + 25 phút kiểm toán sẵn sàng)
- **Mục tiêu:** Xâu chuỗi toàn bộ 5 micro-sessions của Buổi 1 thành một bản đồ chiến lược học tập và hành động nhất quán; tích hợp tư duy định hướng dữ liệu, chiến lược hào lũy AI, nấc thang 5 bước ML và cam kết kỷ luật trước khi bước vào Tuần 2 (NumPy Foundations).

#### 1. Bản Đồ Khái Niệm Tổng Thể Buổi 1 (Cross-Module Knowledge Graph)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   BẢN ĐỒ CHIẾN LƯỢC TOÀN DIỆN BUỔI 1 (SESSION 1 STRATEGY)              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [TẦNG 1: TƯ DUY NỀN TẢNG (Micro-1.1 & Micro-1.2)]                                      │
│ • Thế giới bùng nổ 527 ZB -> Cần tư duy dựa trên bằng chứng (Evidence-Based).          │
│ • Áp dụng chu trình CRISP-DM 6 bước; 80% công sức tập trung vào Understanding/Prep.    │
│ • Cảnh giác với Dark Data & Thiên lệch lựa chọn (Selection Bias).                      │
│ • Chuyển ngữ mong muốn kinh doanh thành bộ ba kỹ thuật: Target y, Features X, Metric.  │
│                                    │                                                   │
│                                    ▼                                                   │
│ [TẦNG 2: CHIẾN LƯỢC CẠNH TRANH & VẬN HÀNH (Micro-1.3)]                                 │
│ • Database tĩnh không còn là hào lũy trước Foundation Models.                          │
│ • Hào lũy phòng thủ duy nhất là Tích Hợp Quy Trình (Workflow Integration).             │
│ • Vận hành bánh đà dữ liệu (Data Flywheel) tạo dữ liệu phản hồi độc quyền.             │
│ • Áp dụng vòng lặp Tanpin Kanri (Observe -> Hypothesize -> Action -> Revise).          │
│ • Dùng AI để bác bỏ nhanh các giả thuyết sai (Rapid Falsification).                    │
│                                    │                                                   │
│                                    ▼                                                   │
│ [TẦNG 3: NẤC THANG THỰC CHIẾN & TÀI CHÍNH (Micro-1.4)]                                 │
│ • Lộ trình 14 tuần: Nền tảng (W1-4) -> Học máy (W5-8) -> Big Data (W9-13) -> Final.   │
│ • Chinh phục Leaderboard bằng nấc thang 5 bước ML Ladder: Bắt đầu từ Baseline nộp sớm. │
│ • Phân tích ma trận chi phí: Tối ưu hóa tổn thất kinh tế (C_FN * FN + C_FP * FP).     │
│ • Tuyệt đối chống rò rỉ xuyên thời gian (Temporal Leakage) trên dữ liệu chuỗi.         │
│                                    │                                                   │
│                                    ▼                                                   │
│ [TẦNG 4: HỆ THỐNG VẬN HÀNH & KỶ LUẬT (Micro-1.5)]                                      │
│ • Làm chủ hệ sinh thái: Omnicampus LMS, Quri AI, Google Colab, Slack.                  │
│ • Tuân thủ kỷ luật Zero Late Policy điểm danh (>= 7/14 buổi, hạn Buổi 1: 08/10/2026).  │
│ • Bài tập tuần HW1-8: Đạt >= 14/24 điểm; nộp sớm bảo toàn 3đ, nộp muộn tối đa 2đ.      │
│ • Mục tiêu tối thượng: Top 10% Final + Top 20% Competition -> Chuyến đi Tokyo Tour!   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 2. Khung Kiểm Toán Chuyển Giao Buổi 1 Sang Tuần 2 (Milestone 1 Readiness Audit)
Học viên chỉ được phép bắt đầu Tuần 2 (NumPy Foundations) sau khi tích chọn đủ toàn bộ các mục:
- [ ] Vở viết tay cá nhân đã ghi chép đầy đủ 5 phân đoạn vi mô (Micro-1.1 đến 1.5) theo cấu trúc 3 cột Cornell.
- [ ] Hoàn thành khảo sát điểm danh Buổi 1 trên Omnicampus Questionnaire trước hạn chót.
- [ ] Đổi Slack Display Name thành đúng Username Omnicampus (`Duongne2000`).
- [ ] Tham gia các kênh trao đổi chuyên môn trên Slack (`#06_question_lecture`, `#07_question_assignment`).
- [ ] Đã trả lời và hiểu sâu toàn bộ 5 câu hỏi Active Recall của Buổi 1.
- [ ] Thiết lập lịch học cá nhân cố định 3–5 giờ/tuần để thực hiện các bài tập tuần và chuẩn bị cho Cuộc thi ML.

#### 3. Thử Thách Phản Xạ Đa Chiều Tổng Hợp (Cross-Topic Active Recall Challenge)
*(Hãy tự kiểm tra bản thân bằng 3 câu hỏi liên kết toàn diện trước khi khép lại Buổi 1)*

1. **Thử thách 1 (Liên kết Dark Data & Ma trận chi phí):** Trong bài toán phát hiện giao dịch lừa đảo trực tuyến, nếu hệ thống chỉ ghi nhận các giao dịch mà khách hàng chủ động khiếu nại báo mất tiền, thành phần Dark Data nào đang tồn tại? Nếu chi phí một vụ lừa đảo bị bỏ sót cao gấp 100 lần chi phí xác minh lại giao dịch nghi vấn, bạn sẽ điều chỉnh ngưỡng phân loại (Classification Threshold) theo hướng nào?

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*
1. **Thành phần Dark Data tồn tại:** Gồm hai nhóm lớn bị che giấu:
   - Các vụ lừa đảo tinh vi với số tiền nhỏ (Micro-fraud / Silent draining) mà nạn nhân không để ý hoặc không buồn khiếu nại.
   - Các nạn nhân đã phát hiện nhưng không tin tưởng ngân hàng, xấu hổ không khai báo, hoặc hủy thẻ rời bỏ dịch vụ trong im lặng. Dữ liệu chỉ ghi nhận "giao dịch bị khiếu nại" là mẫu bị thiên vị chọn lọc nghiêm trọng (Selection Bias).
2. **Điều chỉnh ngưỡng phân loại (Classification Threshold):**
   - Công thức ma trận chi phí: $\text{Total Cost} = C_{\text{FN}} \cdot \text{FN} + C_{\text{FP}} \cdot \text{FP}$, với $C_{\text{FN}} = 100 \cdot C_{\text{FP}}$.
   - Vì chi phí bỏ sót lừa đảo ($C_{\text{FN}}$) cực lớn, mục tiêu tối thượng là tối đa hóa **Recall** (giảm thiểu FN tiệm cận 0).
   - Do đó, ta **hạ thấp ngưỡng phân loại** (Classification Threshold) từ mặc định $0.5$ xuống mức rất thấp (ví dụ: $0.05$ hoặc $0.10$). Mô hình sẽ nhạy cảm hơn nhiều, chấp nhận tăng số lượng cảnh báo giả (FP) để con người kiểm tra lại, nhằm bắt trọn gần như $100\%$ các vụ lừa đảo thực tế.
</details>

2. **Thử thách 2 (Liên kết Tanpin Kanri & 5-Step ML Ladder):** Bước 2 trong nấc thang 5 bước ML Ladder (Domain-Driven Feature Engineering) tương ứng với mắt xích nào trong chu trình Tanpin Kanri của Seven-Eleven Japan? Tại sao cả hai đều nhấn mạnh việc quan sát thực tế hơn là chạy thuật toán phức tạp?

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*
1. **Mắt xích tương ứng:** Tương ứng với giai đoạn **Observe (Quan sát hiện trường & Tín hiệu ngoại cảnh)** và **Hypothesize (Thiết lập giả thuyết)** trong chu trình Tanpin Kanri:
   - Quan sát ngoại cảnh (thời tiết mưa lạnh lúc 17:00, học sinh tan trường) chuyển hóa trực tiếp thành đặc trưng miền (ví dụ: biến tương tác thời tiết × giờ cao điểm).
2. **Lý do nhấn mạnh quan sát thực tế hơn thuật toán phức tạp:**
   - Nguyên lý "Garbage In, Garbage Out": Nếu mô hình không được tiếp nhận các đặc trưng phản ánh đúng quy luật vận động thực tế, việc tinh chỉnh siêu tham số phức tạp (Optuna, Deep Neural Networks) chỉ dẫn đến việc quá khớp (Overfitting) trên nhiễu.
   - 60–70% thành bại của dự án Khoa học Dữ liệu đến từ Tri thức miền (Domain Knowledge). Đặc trưng tốt xuất phát từ thấu hiểu nghiệp vụ có thể giúp một thuật toán đơn giản (như Linear Regression hay Decision Tree) đánh bại các mô hình phức tạp nhưng thiếu đặc trưng cốt lõi.
</details>

3. **Thử thách 3 (Liên kết Kỷ luật khóa học & Lợi thế Tokyo):** Tại sao việc nộp một bản chạy được (Baseline) của Đồ án Cuối khóa ngay từ Tuần 3 lại giúp tăng cơ hội được xét tuyển học bổng tham quan Tokyo lên gấp nhiều lần so với việc chờ đến Tuần 13 mới bắt đầu làm?

<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*
1. **Kích hoạt Bánh đà Tự lặp (Iterative Feedback Loop):** Nộp bản Baseline chạy được ở Tuần 3 giúp học viên hoàn tất toàn bộ chu trình nộp bài tự động trên Omnicampus, kiểm chứng pipeline không lỗi cú pháp, và có điểm số khởi điểm trên bảng xếp hạng (Leaderboard).
2. **Thời gian chạy thử nghiệm & Falsification:** Thay vì phải chịu áp lực dồn vào 1 tuần cuối, học viên có trọn vẹn 10 tuần (Tuần 4 đến 13) để thử nghiệm hàng chục giả thuyết đặc trưng, áp dụng các kỹ thuật học được từ mỗi bài giảng vào mô hình, và liên tục cải thiện vị trí một cách bền bỉ qua từng tuần.
</details>

---

## 4. LỘ TRÌNH BUỔI 2: NUMPY COMPUTING & MEMORY MECHANICS (ĐIỆN TOÁN MA TRẬN)

Buổi 2 bao gồm 5 Micro-Sessions (Micro-2.1 đến Micro-2.5) và 1 Buổi Ôn Tập Tổng Kết (Session 2.S).

```text
[ Micro-2.1: Foundations & Architecture ] ──> [ Micro-2.2: Ufuncs & SIMD ] ──> [ Micro-2.3: Axes & Aggregations ]
                    │                                                                   │
                    └─────────────────────────┐       ┌─────────────────────────────────┘
                                              ▼       ▼
                                [ Micro-2.4: Broadcasting Geometry ]
                                              │
                                              ▼
                                [ Micro-2.5: Indexing, Views & Cleaning ]
                                              │
                                              ▼
                                [ SESSION 2.S: SYNTHESIS & BENCHMARK REVIEW ]
```

---

### MICRO-2.1: ĐỘNG LỰC HỌC THUẬT, KIẾN TRÚC BỘ NHỚ NDARRAY & VÙNG ĐỆM C-CONTIGUOUS
- **Mã phân đoạn:** `MISSION-2.1`
- **Thời lượng:** 30 Phút (15 phút chép tay + 15 phút thực hành vi mô)
- **Tiền đề:** Cú pháp biến số, danh sách `list` và vòng lặp `for` cơ bản trong Python.
- **Mục tiêu năng lực:** Hiểu rõ tại sao danh sách Python thất bại ở quy mô lớn; nắm vững cấu trúc bộ nhớ C-contiguous của `numpy.ndarray`, tính cục bộ không gian (Spatial Locality) và cơ chế tăng tốc 50x–120x thông qua chi thị SIMD.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở tài liệu `syllabus/buoi2_handwritten_notebook_syllabus.md`, quan sát **PHẦN 1**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 2 | Micro-2.1 | ndarray Architecture & C-Contiguous Memory`.
3. Ghi vào Cột 1: `Fleet Scale Paradox`, `Heterogeneous Pointer vs C-Contiguous`, `SIMD Hardware Vectorization`.
4. Vẽ vào Cột 2:
   - Sơ đồ phân nhánh so sánh bộ nhớ:
     * Python List: Vùng nhớ rời rạc trên Heap, danh sách các con trỏ trỏ tới từng `PyObject` (tốn 28 bytes overhead/số nguyên).
     * NumPy ndarray: Header (shape, strides, dtype) trỏ thẳng vào vùng đệm C-contiguous gồm các ô 8 bytes liên tiếp trong RAM.
   - Sơ đồ nạp dòng đệm phần cứng (Cache Line Prefetching 64 bytes): Nạp 8 số thực 64-bit cùng lúc vào L1 Cache.
   - Biểu diễn thanh ghi AVX-512 xử lý song song 8 phép cộng trong 1 xung nhịp.
5. Ghi vào Cột 3: Đo lường kích thước bộ nhớ `sys.getsizeof()` vs `arr.nbytes` và quy tắc cấm dùng vòng lặp `for`.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Khởi tạo một mảng gồm $1,000,000$ số nguyên ngẫu nhiên. So sánh dung lượng RAM tiêu thụ giữa Python `list` và `numpy.ndarray`. Sau đó đo thời gian tính tổng bằng hàm `sum()` của Python so với `np.sum()`.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Khi in dung lượng của `[10] * 1000` và `np.full(1000, 10, dtype=np.int64)`, con số chênh lệch nhau bao nhiêu lần?
  - *Cấp độ 2 (Định hướng):* Tại sao khi tính tổng trên mảng NumPy, nếu vô tình viết `sum(arr)` thay vì `np.sum(arr)` thì thời gian chạy lại chậm đi hàng chục lần?
  - *Cấp độ 3 (Phản ví dụ):* Thử chạy `np.sum(arr)` 100 lần và tính tốc độ trung bình; kiểm tra thanh ghi CPU có bị quá tải không.
  - *Cấp độ 4 (Mẫu cú pháp):* `start = time.time(); res = np.sum(arr); elapsed = time.time() - start`.
  - *Cấp độ 5 (Mã hoàn chỉnh):* Cung cấp đoạn mã đối chiếu benchmark chuẩn hóa dưới đây.
- **Mã thực hành gợi ý:**
```python
import sys
import time
import numpy as np

# 1. So sánh bộ nhớ
N = 1_000_000
py_list = list(range(N))
np_arr = np.arange(N, dtype=np.int64)

list_mem = sys.getsizeof(py_list) + sum(sys.getsizeof(i) for i in py_list[:100]) * (N // 100)
arr_mem = np_arr.nbytes

print(f"Ước tính RAM Python list: ~{list_mem / (1024**2):.2f} MB")
print(f"RAM NumPy ndarray:        {arr_mem / (1024**2):.2f} MB")

# 2. Benchmark tính tổng
t0 = time.time()
py_sum = sum(py_list)
t_py = time.time() - t0

t0 = time.time()
np_sum_val = np.sum(np_arr)
t_np = time.time() - t0

print(f"Thời gian Python sum: {t_py:.5f}s")
print(f"Thời gian NumPy sum:  {t_np:.5f}s")
print(f"Tốc độ tăng tốc:      {t_py / t_np:.1f}x")
assert py_sum == np_sum_val
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay cá nhân đã vẽ xong sơ đồ so sánh bộ nhớ Heap vs C-Contiguous.
- [ ] Script thực hành benchmark xác nhận `np.sum()` nhanh hơn Python thuan tối thiểu 20 lần.
- [ ] Trả lời chính xác 2 câu hỏi Active Recall bên dưới mà không nhìn tài liệu.

#### Câu Hỏi Kiểm Tra Phản Xạ Nhanh (Active Recall Reflex Questions)
1. **Câu hỏi 1:** Khi CPU nạp một mảng `numpy.ndarray` vào bộ nhớ đệm Cache L1, tại sao hiện tượng Cache Miss lại thấp hơn rất nhiều so với khi duyệt qua một Python list?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Vì các phần tử trong `numpy.ndarray` được xếp liên tiếp nhau trong một khối bộ nhớ C-contiguous (Spatial Locality). Khi CPU nạp một phần tử, cơ chế phần cứng tự động nạp nguyên một dòng Cache Line (thường là 64 bytes, tương đương 8 số thực 64-bit liền kề) vào L1. Trong khi đó, Python list chỉ chứa các con trỏ trỏ tới các đối tượng phân tán ngẫu nhiên khắp nơi trên Heap, buộc CPU phải giải tham chiếu liên tục và gây ra tình trạng Cache Miss triền miên.
</details>

2. **Câu hỏi 2:** Tại sao thư viện NumPy lại yêu cầu mảng phải có kiểu dữ liệu đồng nhất (Homogeneous type)? Điều này mang lại lợi ích gì cho các tập lệnh SIMD?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Kiểu dữ liệu đồng nhất giúp mỗi phần tử có kích thước byte hoàn toàn cố định (ví dụ chính xác 8 bytes cho `int64` hoặc `float64`). Nhờ đó, trình thông dịch không cần kiểm tra kiểu động ở từng bước lặp, và các thanh ghi SIMD (như AVX-512) có thể chia nhỏ thanh ghi thành các đoạn cố định để thực thi song song các phép toán cộng/nhân số học trên nhiều phần tử trong đúng 1 chu kỳ máy.
</details>

---

### MICRO-2.2: HÀM VẠN NĂNG (UFUNCS), TOÁN TỬ THEO PHẦN TỬ & CHUẨN IEEE 754
- **Mã phân đoạn:** `MISSION-2.2`
- **Thời lượng:** 30 Phút (15 phút chép tay + 15 phút thực hành vi mô)
- **Tiền đề:** Micro-2.1.
- **Mục tiêu năng lực:** Nắm vững bản chất ufuncs thực thi ở tầng C, hàm toán học an toàn `np.log1p`/`np.expm1`, cơ chế xử lý phép chia cho 0 theo chuẩn IEEE 754 (`np.inf`/`np.nan`), và kỹ thuật chuẩn hóa véc-tơ đơn vị L2.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở tài liệu `syllabus/buoi2_handwritten_notebook_syllabus.md`, quan sát **PHẦN 2**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 2 | Micro-2.2 | Universal Functions & IEEE 754 Safe Math`.
3. Ghi vào Cột 1: `Universal Functions (ufunc)`, `Safe Math & Log1p`, `IEEE 754 Division by Zero`, `Vector Normalization`.
4. Vẽ vào Cột 2:
   - Bảng chuyển đổi toán tử: `+` $\to$ `np.add`, `-` $\to$ `np.subtract`, `*` $\to$ `np.multiply` (Hadamard), `/` $\to$ `np.divide`.
   - Đồ thị biến đổi an toàn: Hàm $\ln(x)$ sụp đổ về $-\infty$ tại $x=0$, trong khi $\text{np.log1p}(x) = \ln(1 + x)$ đi qua gốc tọa độ $(0, 0)$.
   - Công thức chuẩn hóa véc-tơ L2: $\mathbf{u} = \mathbf{v} / \|\mathbf{v}\|_2$.
5. Ghi vào Cột 3: Mã lọc `np.isinf()`, `np.isnan()` và code chuẩn hóa véc-tơ.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Khởi tạo một mảng cảm biến lượng mưa chứa các giá trị đo thực tế gồm nhiều số 0 và phép chia tạo ra vô cực. Thực hiện biến đổi logarit an toàn bằng `np.log1p()`, khôi phục lại bằng `np.expm1()`, và viết hàm chuẩn hóa véc-tơ đơn vị kiểm tra assertion norm bằng 1.0.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Khi gọi `np.log(np.array([0.0, 5.0]))`, giá trị đầu tiên trả về là gì? Trình thông dịch có báo lỗi dừng chương trình không?
  - *Cấp độ 2 (Định hướng):* Nếu truyền mảng chứa `-np.inf` vào hàm tính `np.mean()`, kết quả là gì? Làm thế nào để loại bỏ triệt để các phần tử này?
  - *Cấp độ 3 (Phản ví dụ):* Thử lấy `np.array([0.0]) / 0.0` và kiểm tra `np.isnan()`.
  - *Cấp độ 4 (Mẫu cú pháp):* `clean = arr[~np.isinf(arr) & ~np.isnan(arr)]`.
- **Mã thực hành gợi ý:**
```python
import numpy as np

# 1. Đo lường rủi ro phép chia cho 0
sensor_readings = np.array([12.0, 0.0, -5.0, 0.0, 24.0])
div_result = 100.0 / sensor_readings
print("Kết quả chia cho 0:", div_result)
print("Có chứa inf không?", np.isinf(div_result).any())

# 2. Xử lý log1p an toàn trên lượng mưa
prcp = np.array([0.0, 0.2, 0.0, 15.4, 0.0, 32.1])
log_prcp = np.log1p(prcp)
restored_prcp = np.expm1(log_prcp)
assert np.allclose(prcp, restored_prcp)

# 3. Chuẩn hóa véc-tơ đơn vị
vec = np.array([3.0, 4.0])
unit_vec = vec / np.linalg.norm(vec)
print("Véc-tơ đơn vị:", unit_vec)
assert np.isclose(np.linalg.norm(unit_vec), 1.0)
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay đã ghi rõ công thức KaTeX của `np.log1p` và chuẩn hóa L2 norm.
- [ ] Thực thi kiểm tra thành công `np.allclose(prcp, np.expm1(np.log1p(prcp)))`.
- [ ] Viết bộ lọc loại bỏ toàn bộ `inf` và `nan` khỏi mảng số thực.

#### Câu Hỏi Kiểm Tra Phản Xạ Nhanh (Active Recall Reflex Questions)
1. **Câu hỏi 1:** Khi tính toán trên mảng NumPy, toán tử `*` giữa hai mảng `a * b` thực hiện phép nhân ma trận hay phép nhân từng phần tử? Nếu muốn nhân ma trận đại số tuyến tính thì dùng toán tử nào?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Toán tử `*` thực hiện phép nhân từng phần tử (Element-wise / Hadamard Product), gọi hàm `np.multiply(a, b)`. Nếu muốn nhân ma trận đại số tuyến tính (Matrix Multiplication / Dot Product), ta MUST sử dụng toán tử `@` hoặc hàm `np.matmul(a, b)` / `np.dot(a, b)`.
</details>

2. **Câu hỏi 2:** Tại sao trong bài toán dự báo chuỗi thời gian lượng mưa, việc sử dụng `np.log()` trực tiếp lại cực kỳ nguy hiểm, và tại sao `np.log1p()` khắc phục được triệt để vấn đề này?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Lượng mưa thường có rất nhiều ngày không mưa (giá trị bằng 0.0). Gọi `np.log(0)` sẽ sinh ra $-\infty$. Giá trị vô cực âm này sẽ phá hủy hoàn toàn hàm mất mát và thuật toán tối ưu Gradient Descent. Hàm `np.log1p(x) = \ln(1 + x)` đảm bảo khi $x = 0$, kết quả trả về là $\ln(1) = 0$, giúp dữ liệu được co kéo liên tục mà không sinh ra giá trị vô cực.
</details>

---

### MICRO-2.3: CHỈ MỤC, CẮT MẢNG ĐA CHIỀU & BẢN CHIẾU (VIEW) VS BẢN SAO (COPY)
- **Mã phân đoạn:** `MISSION-2.3`
- **Thời lượng:** 35 Phút (15 phút chép tay + 20 phút thực hành vi mô)
- **Tiền đề:** Micro-2.2.
- **Mục tiêu năng lực:** Làm chủ cú pháp cắt mảng 1D/2D `start:stop:step`, công thức ánh xạ địa chỉ bộ nhớ Affine Strides, phân biệt bản chiếu (View) vs bản sao (Copy) để chống đột biến dữ liệu, và trích xuất ma trận con bằng `np.ix_`.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở tài liệu `syllabus/buoi2_handwritten_notebook_syllabus.md`, quan sát **PHẦN 3**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 2 | Micro-2.3 | Multi-Dimensional Slicing & View vs Copy`.
3. Ghi vào Cột 1: `Slicing Syntax & Stride Steps`, `2D Slicing & Reshape Inference`, `Slicing View vs Advanced Copy`, `Affine Address & Mesh Grid np.ix_`.
4. Vẽ vào Cột 2:
   - Sơ đồ trục thời gian trích xuất ngày Thứ Hai: T6(0), T7(1), CN(2), T2(3) $\implies$ `jan_tmax[3::7]`.
   - Sơ đồ bộ nhớ phân biệt View vs Copy:
     * View: Trỏ chung vùng đệm byte gốc, chỉ thay đổi byte offset và strides. Sửa con là sửa mẹ!
     * Copy: Cấp phát mảng mới hoàn toàn trên Heap. Sửa con không ảnh hưởng mẹ.
   - Minh họa cạm bẫy cắt ma trận con: `a[[0, 2], [1, 3]]` (ra 2 điểm) vs `a[np.ix_([0, 2], [1, 3])]` (ra lưới 2x2).
5. Ghi vào Cột 3: Quy tắc bắt buộc gọi `.copy()` khi muốn cách ly dữ liệu.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Tái hiện bài tập trích xuất nhiệt độ các ngày Thứ Hai trong tháng 1/2010 từ mảng 31 ngày. Tạo một ma trận $4 \times 4$, thực hiện so sánh biến đổi trên lát cắt thường (View) và lát cắt có `.copy()`. Sử dụng `np.ix_` để trích xuất khối ma trận con giao điểm của hàng $[0, 2]$ và cột $[1, 3]$.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Khi thay đổi `b[0] = 999` trên `b = a[1:3]`, hãy in lại `a`. Giá trị `a[1]` đã bị biến đổi thành số mấy?
  - *Cấp độ 2 (Định hướng):* Làm thế nào để kiểm tra xem hai mảng có đang dùng chung một vùng nhớ đệm hay không? Hãy tra cứu thuộc tính `b.base`.
  - *Cấp độ 3 (Phản ví dụ):* Thử viết `c = a[[1, 2]]` rồi gán `c[0] = 777`. Kiểm tra `a[1]` xem có bị thay đổi không và giải thích tại sao.
  - *Cấp độ 4 (Mẫu cú pháp):* `sub = a[np.ix_([0, 2], [1, 3])]`.
- **Mã thực hành gợi ý:**
```python
import numpy as np

# 1. Trích xuất Thứ Hai tháng 1/2010 (31 ngày, 01/01 là Thứ Sáu)
np.random.seed(42)
jan_tmax = np.random.uniform(5.0, 18.0, size=31)
monday_tmax = jan_tmax[3::7]
print(f"Số ngày Thứ Hai: {len(monday_tmax)}, TB: {monday_tmax.mean():.2f}°C")

# 2. Thí nghiệm View vs Copy
orig = np.array([10, 20, 30, 40, 50])
view_slice = orig[1:4]
view_slice[0] = 999
print("Mảng gốc sau khi sửa View:", orig) # [10, 999, 30, 40, 50]
assert orig[1] == 999

copy_slice = orig[1:4].copy()
copy_slice[0] = -111
print("Mảng gốc sau khi sửa Copy:", orig) # Vẫn giữ nguyên 999!
assert orig[1] == 999

# 3. Lưới ma trận con với np.ix_
mat = np.arange(16).reshape(4, 4)
sub_trap = mat[[0, 2], [1, 3]]      # Ra array([1, 11])
sub_correct = mat[np.ix_([0, 2], [1, 3])] # Ra ma trận 2x2
print("Lưới ma trận con chuẩn:\n", sub_correct)
assert sub_correct.shape == (2, 2)
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay có sơ đồ minh họa cơ chế `b.base` trỏ về vùng đệm gốc của mảng.
- [ ] Chạy thành công đoạn mã thực nghiệm và xác nhận thuộc tính `view_slice.base is orig`.
- [ ] Nắm vững cú pháp `jan_tmax[3::7]` và hàm `np.ix_`.

#### Câu Hỏi Kiểm Tra Phản Xạ Nhanh (Active Recall Reflex Questions)
1. **Câu hỏi 1:** Trong NumPy, tại sao lệnh `b = a[0:5]` chỉ mất vài nano-giây dù mảng `a` có kích thước lên tới hàng trăm triệu phần tử?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Vì phép cắt mảng cơ bản (Basic Slicing) tạo ra một **View**, hoàn toàn không sao chép dữ liệu byte trong RAM. NumPy chỉ khởi tạo một đối tượng Header mới rất nhẹ chứa con trỏ trỏ tới vùng đệm cũ, cập nhật lại hình dạng `shape`, độ dời `offset` và bước nhảy `strides`. Do đó độ phức tạp thời gian luôn là $O(1)$ bất kể kích thước mảng lớn đến đâu.
</details>

2. **Câu hỏi 2:** Giả sử bạn có ma trận $A$ kích thước $10 \times 10$. Điều gì xảy ra nếu bạn cố lấy giao điểm các hàng $[1, 3, 5]$ và các cột $[0, 2]$ bằng lệnh `A[[1, 3, 5], [0, 2]]`?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
NumPy sẽ ném lỗi `IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (3,) (2,)` vì hai danh sách chỉ mục có chiều dài khác nhau (3 và 2) và không tương thích broadcasting. Để trích xuất đúng ma trận con $3 \times 2$, bắt buộc phải sử dụng `A[np.ix_([1, 3, 5], [0, 2])]`.
</details>

---

### MICRO-2.4: NGỮ NGHĨA TRỤC KHÔNG GIAN (AXES), RÚT GỌN THỐNG KÊ & KEEPDIMS
- **Mã phân đoạn:** `MISSION-2.4`
- **Thời lượng:** 35 Phút (15 phút chép tay + 20 phút thực hành vi mô)
- **Tiền đề:** Micro-2.3.
- **Mục tiêu năng lực:** Xóa bỏ hoàn toàn sự nhầm lẫn giữa `axis=0` và `axis=1` thông qua Quy tắc trục tiêu biến (Collapsing Invariant); bảo toàn số chiều với `keepdims=True` để phục vụ chuẩn hóa dữ liệu theo hàng và theo cột.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở tài liệu `syllabus/buoi2_handwritten_notebook_syllabus.md`, quan sát **PHẦN 4**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 2 | Micro-2.4 | Spatial Axes & Keepdims Preservation`.
3. Ghi vào Cột 1: `The Collapsing Axis Invariant`, `Keepdims Preservation`, `Multi-Dimensional Reductions`.
4. Vẽ vào Cột 2:
   - Sơ đồ ma trận $M \times N$ (Học sinh $\times$ Môn học):
     * Mũi tên dọc $\downarrow$ (`axis=0`): Nén $M$ hàng lại $\implies$ Kết quả còn $(N,)$ tương ứng điểm trung bình từng môn học.
     * Mũi tên ngang $\rightarrow$ (`axis=1`): Nén $N$ cột lại $\implies$ Kết quả còn $(M,)$ tương ứng điểm trung bình từng học sinh.
   - Sơ đồ biến đổi hình dạng với `keepdims`:
     * `axis=1, keepdims=False` $\to$ shape $(M,)$ (Không broadcast được với ma trận gốc).
     * `axis=1, keepdims=True` $\to$ shape $(M, 1)$ (Tự động broadcast hoàn hảo trừ theo từng hàng).
5. Ghi vào Cột 3: Bài tập thực hành trong `04_Assignments/numpy_axes_practice.py`.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Khởi tạo ma trận điểm thi của 4 học sinh qua 3 môn học. Tính điểm trung bình từng môn (`axis=0`) và điểm trung bình từng học sinh (`axis=1`). Sau đó thực hiện chuẩn hóa trừ điểm trung bình của mỗi học sinh khỏi điểm các môn của học sinh đó bằng cách dùng `keepdims=True`.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Khi gọi `scores.mean(axis=1)`, shape của kết quả là gì?
  - *Cấp độ 2 (Định hướng):* Thử gõ `scores - scores.mean(axis=1)`. Python báo lỗi gì? Tại sao chiều $(4, 3)$ không trừ được cho $(4,)$?
  - *Cấp độ 3 (Phản ví dụ):* Thêm `keepdims=True`. Shape mới là gì? Tại sao $(4, 3) - (4, 1)$ lại hợp lệ?
  - *Cấp độ 4 (Mẫu cú pháp):* `centered = scores - scores.mean(axis=1, keepdims=True)`.
- **Mã thực hành gợi ý:**
```python
import numpy as np

# Bảng điểm 4 học sinh x 3 môn (Toán, Lý, Hóa)
scores = np.array([
    [85.0, 90.0, 78.0],
    [70.0, 65.0, 80.0],
    [92.0, 88.0, 95.0],
    [60.0, 75.0, 70.0]
])

# 1. Thống kê theo môn (Rút gọn hàng -> axis=0)
subject_mean = scores.mean(axis=0)
print("Điểm TB từng môn (Toán, Lý, Hóa):", subject_mean) # Shape (3,)

# 2. Thống kê theo học sinh (Rút gọn cột -> axis=1)
student_mean_raw = scores.mean(axis=1) # Shape (4,)
print("Điểm TB từng học sinh (1D):", student_mean_raw)

# 3. Chuẩn hóa trừ điểm TB học sinh (Bắt buộc dùng keepdims=True)
student_mean_kd = scores.mean(axis=1, keepdims=True) # Shape (4, 1)
print("Điểm TB từng học sinh (keepdims=True):\n", student_mean_kd)

centered_scores = scores - student_mean_kd
print("Bảng điểm sau khi trừ TB học sinh:\n", centered_scores)
assert np.allclose(centered_scores.mean(axis=1), 0.0)
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay có sơ đồ hai mũi tên $\downarrow$ (`axis=0`) và $\rightarrow$ (`axis=1`).
- [ ] Chạy thành công toàn bộ file `04_Assignments/numpy_axes_practice.py` với tất cả các phép assert đều pass.
- [ ] Chứng minh được `centered_scores.mean(axis=1)` xấp xỉ bằng $0.0$.

#### Câu Hỏi Kiểm Tra Phản Xạ Nhanh (Active Recall Reflex Questions)
1. **Câu hỏi 1:** Khi tính giá trị lớn nhất theo từng cột trong một ma trận 2D, ta phải truyền vào tham số `axis=0` hay `axis=1`? Hãy giải thích bản chất cơ chế tiêu biến chiều.
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Phải truyền `axis=0`. Vì để tìm giá trị lớn nhất của từng cột, ta phải duyệt dọc qua toàn bộ các hàng của cột đó. Chiều bị nén lại và triệt tiêu (collapse) chính là chiều hàng (hàng biến mất, chỉ còn lại các cột). Theo quy tắc trục tiêu biến, chiều nào bị triệt tiêu thì tham số `axis` mang chỉ số của chiều đó (`axis=0` là chiều hàng).
</details>

2. **Câu hỏi 2:** Giả sử một mảng dữ liệu ảnh có kích thước $(B, H, W, C)$ tương ứng với (Batch size, Chiều cao, Chiều rộng, Số kênh màu). Nếu muốn tính độ lệch chuẩn trên từng kênh màu của toàn bộ ảnh trong batch, ta chọn tuple `axis` nào?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Ta chọn `axis=(0, 1, 2)`. Phép tính sẽ nén cả 3 chiều Batch ($B$), Chiều cao ($H$) và Chiều rộng ($W$), giữ lại duy nhất chiều Kênh màu ($C$), cho ra kết quả có kích thước $(C,)$ tương ứng với độ lệch chuẩn của từng kênh màu (ví dụ: R, G, B).
</details>

---

### MICRO-2.5: HÌNH HỌC LAN TRUYỀN (BROADCASTING), MẶT NẠ BOOLEAN & LỌC DỮ LIỆU NOAA
- **Mã phân đoạn:** `MISSION-2.5`
- **Thời lượng:** 40 Phút (15 phút chép tay + 25 phút thực hành vi mô)
- **Tiền đề:** Micro-2.4.
- **Mục tiêu năng lực:** Nắm vững quy tắc căn chỉnh chiều từ phải sang trái (Trailing Dimension Alignment), kỹ thuật mở rộng chiều ảo với `np.newaxis`, lọc dữ liệu thời tiết NOAA loại bỏ mã cảm biến hỏng 999.9, tuân thủ độ ưu tiên toán tử bitwise và làm chủ bài tập HW1.

#### Bước 1: Chép Tay Vào Vở Cornell (Pen-First Note Prompts)
1. Mở tài liệu `syllabus/buoi2_handwritten_notebook_syllabus.md`, quan sát **PHẦN 5**.
2. Kẻ trang vở Cornell mới với Header: `Buổi 2 | Micro-2.5 | Broadcasting Geometry & NOAA Cleaning`.
3. Ghi vào Cột 1: `Trailing Alignment Rule`, `Newaxis & Pairwise Distance`, `NOAA Sentinel Data Trap`, `Boolean Bitwise Precedence`.
4. Vẽ vào Cột 2:
   - Sơ đồ căn chỉnh chiều từ phải sang trái: Đệm 1 bên trái, kiểm tra $d_i = d_j$ hoặc $d = 1$.
   - Sơ đồ ma trận khoảng cách Euclid 3D không vòng lặp: $A(N, 1, D) - B(1, M, D) \to (N, M, D)$.
   - Minh họa cạm bẫy giá trị thiếu NOAA: Điểm đo 999.9 kéo lệch giá trị trung bình từ 0.5 mm lên 64 mm.
5. Ghi vào Cột 3: Mã hàm lọc `homework(a)` cho HW1 và công thức Z-Score: $z = (x - \mu)/\sigma$.

#### Bước 2: Thực Hành Vi Mô & Phản Xạ Phản Biện (Practice & Reflection)
- **Nhiệm vụ vi mô:** Xây dựng hàm làm sạch dữ liệu lượng mưa mô phỏng của NOAA, loại bỏ giá trị mã hóa thiếu 999.9 trước khi tính trung bình và độ lệch chuẩn. Cài đặt hàm `homework(a)` lọc các phần tử chia hết cho 5 nhưng không chia hết cho 2 để chuẩn bị nộp bài tập HW1 trên OmniCampus.
- **Hướng dẫn Socratic (DeepTutor):**
  - *Cấp độ 1 (Quan sát):* Khi chạy `a % 5 == 0 & a % 2 != 0`, tại sao Python lại báo lỗi hoặc trả về kết quả sai khác hoàn toàn so với khi có dấu ngoặc đơn `(a % 5 == 0) & (a % 2 != 0)`?
  - *Cấp độ 2 (Định hướng):* Hãy tra cứu bảng độ ưu tiên toán tử trong Python. Toán tử bitwise `&` được đánh giá trước hay sau toán tử so sánh `==`?
  - *Cấp độ 3 (Phản ví dụ):* Thử gõ `a > 5 and a < 10` trên mảng NumPy. Tại sao Python báo `ValueError: The truth value of an array with more than one element is ambiguous`?
  - *Cấp độ 4 (Mẫu cú pháp):* `mask = (a % 5 == 0) & (a % 2 != 0); return a[mask]`.
- **Mã thực hành gợi ý:**
```python
import numpy as np

# 1. Mô phỏng xử lý dữ liệu thời tiết NOAA
prcp_raw = np.array([0.0, 1.2, 0.0, 999.9, 0.5, 999.9, 2.8, 0.0])
print(f"Giá trị TB khi chưa lọc (Sai lệch): {prcp_raw.mean():.2f} mm")

# Lọc bỏ giá trị sentinel 999.9
valid_mask = (prcp_raw != 999.9) & (~np.isnan(prcp_raw))
prcp_clean = prcp_raw[valid_mask]
print(f"Giá trị TB sau khi làm sạch:        {prcp_clean.mean():.2f} mm")

# Chuẩn hóa Z-score
mu = prcp_clean.mean()
sigma = prcp_clean.std()
z_prcp = (prcp_clean - mu) / sigma
print("Dữ liệu Z-score:\n", z_prcp)

# 2. Cài đặt chuẩn hóa cho Homework 1 (HW1)
def homework(a):
    """
    Lọc các phần tử chia hết cho 5 nhưng không chia hết cho 2.
    """
    mask = (a % 5 == 0) & (a % 2 != 0)
    return a[mask]

test_arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])
res = homework(test_arr)
print("Kết quả HW1:", res)
assert np.array_equal(res, np.array([5, 15, 25, 35]))
```

#### Tiêu Chí Hoàn Thành (Definition of Done - DoD)
- [ ] Vở viết tay đã ghi rõ quy tắc ưu tiên toán tử bitwise và công thức Z-Score.
- [ ] Hàm `homework(a)` vượt qua 100% các assertion kiểm thử nội bộ.
- [ ] Hiểu rõ nguyên nhân và cách xử lý triệt để mã cảm biến 999.9.

#### Câu Hỏi Kiểm Tra Phản Xạ Nhanh (Active Recall Reflex Questions)
1. **Câu hỏi 1:** Cho hai mảng có kích thước lần lượt là $A: (8, 1, 6, 1)$ và $B: (7, 1, 5)$. Hai mảng này có thể thực hiện phép cộng broadcasting được không? Kích thước của mảng kết quả là bao nhiêu?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Có thể cộng được!  
Các bước căn chỉnh từ phải sang trái:
- Chiều 3 (cuối): $1$ vs $5 \implies$ mở rộng thành $5$.
- Chiều 2: $6$ vs $1 \implies$ mở rộng thành $6$.
- Chiều 1: $1$ vs $7 \implies$ mở rộng thành $7$.
- Chiều 0: $8$ vs đệm $1 \implies$ mở rộng thành $8$.  
Hình dạng mảng kết quả là: **$(8, 7, 6, 5)$**.
</details>

2. **Câu hỏi 2:** Tại sao ta không thể dùng từ khóa logic `and` của Python khi kết hợp nhiều điều kiện lọc trên mảng NumPy mà bắt buộc phải dùng toán tử bitwise `&`?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
Từ khóa `and` của Python cố gắng ép toàn bộ mảng đối tượng thành một giá trị chân lý đơn lẻ (`True` hoặc `False`), gây ra lỗi `ValueError: The truth value of an array with more than one element is ambiguous`. Ngược lại, toán tử bitwise `&` được nạp chồng (overloaded) bởi NumPy để thực thi phép tính AND luận lý trên từng cặp phần tử (Element-wise boolean operation), trả về một mảng mặt nạ boolean có cùng hình dạng.
</details>

---

### SESSION 2.S: TỔNG HỢP ĐIỆN TOÁN MA TRẬN, BENCHMARK SIMD & ĐÁNH GIÁ HW1
- **Mã phân đoạn:** `SYNTHESIS-2.S`
- **Thời lượng:** 45 Phút (Ôn tập tổng kết, kiểm toán toàn diện & nộp bài tập)
- **Tiền đề:** Hoàn thành toàn bộ 5 phân đoạn Micro-2.1 đến Micro-2.5.
- **Mục tiêu năng lực:** Xâu chuỗi toàn bộ kiến thức Buổi 2 thành một thể thống nhất; cài đặt ma trận khoảng cách Euclid không vòng lặp; kiểm toán tính sẵn sàng trước khi nộp bài tập HW1 và khảo sát điểm danh lên OmniCampus.

#### 1. Sơ Đồ Tích Hợp Tri Thức Toàn Diện Buổi 2
```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               BẢN ĐỒ TÍCH HỢP ĐIỆN TOÁN MA TRẬN NUMPY (SESSION 2 SYNTHESIS)             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [TẦNG 1: PHẦN CỨNG & BỘ NHỚ (Micro-2.1)]                                               │
│ • Vùng đệm C-Contiguous: Xếp khít các byte thô, không overhead con trỏ.                 │
│ • Tinh cục bộ không gian (Spatial Locality) nạp dòng đệm L1 Cache Line 64B.           │
│ • Khai thác triệt để thanh ghi SIMD AVX-512 tăng tốc độ tính toán từ 50–120 lần.        │
│                                    │                                                   │
│                                    ▼                                                   │
│ [TẦNG 2: HÀM VẠN NĂNG & AN TOÀN SỐ HỌC (Micro-2.2)]                                    │
│ • Toan tu goi ufuncs ở tầng C (np.add, np.multiply Hadamard).                          │
│ • Biến đổi log1p an toàn cho dữ liệu chứa số 0: ln(1 + x).                             │
│ • Xử lý phân nhánh IEEE 754: np.inf và np.nan không dừng chương trình.                 │
│                                    │                                                   │
│                                    ▼                                                   │
│ [TẦNG 3: CẮT MẢNG, KHÔNG GIAN TRỤC & TRUY XUẤT (Micro-2.3 & 2.4)]                       │
│ • Slicing tạo View (chung bộ nhớ); Advanced Indexing tạo Copy (cấp phát RAM mới).      │
│ • Cắt lưới ma trận con an toàn bằng np.ix_([rows], [cols]).                            │
│ • Quy tắc trục tiêu biến: axis=0 nén hàng (tính cột); axis=1 nén cột (tính hàng).      │
│ • Bảo toàn số chiều bằng keepdims=True để trừ trung bình hàng không lỗi shape.         │
│                                    │                                                   │
│                                    ▼                                                   │
│ [TẦNG 4: HÌNH HỌC LAN TRUYỀN & DỮ LIỆU THỰC TẾ (Micro-2.5)]                            │
│ • Quy tắc so khớp chiều từ phải sang trái (Trailing Dimension Alignment).              │
│ • Mở rộng chiều ảo np.newaxis tính khoảng cách cặp đa chiều D_ij không dùng for.       │
│ • Mặt nạ bitwise có ngoặc () lọc sạch mã cảm biến hỏng 999.9 trước khi tính Z-Score.    │
│ • Nộp bài tập HW1 trên OmniCampus Autograder đạt chuẩn 3.0/3.0 điểm.                   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 2. Khung Kiểm Toán Chuyển Giao Buổi 2 Sang Tuần 3 (Milestone 2 Readiness Audit)
Học viên chỉ được phép bắt đầu Tuần 3 (Pandas Data Wrangling) sau khi tích chọn đủ toàn bộ các mục:
- [ ] Vở viết tay cá nhân đã hoàn thiện trọn vẹn 5 phân đoạn vi mô (Micro-2.1 đến 2.5) theo cấu trúc 3 cột Cornell.
- [ ] Đã nộp Khảo sát điểm danh Buổi 2 trên OmniCampus trước **11:00 AM UTC ngày 08/10/2026**.
- [ ] Đã nộp code bài tập `homework(a)` của HW1 trên OmniCampus Autograder và đạt trọn vẹn **3.0 / 3.0 điểm**.
- [ ] Đã chạy file `04_Assignments/numpy_broadcasting_practice.py` và giải thành công bài toán khoảng cách cặp Euclid 3D.
- [ ] Trả lời trọn vẹn 3 thử thách phản xạ tổng hợp bên dưới mà không cần xem tài liệu.

#### 3. Thử Thách Phản Xạ Đa Chiều Tổng Hợp (Cross-Topic Active Recall Challenge)
*(Hãy tự kiểm tra bản thân bằng 3 câu hỏi liên kết toàn diện trước khi khép lại Buổi 2)*

1. **Thử thách 1 (Liên kết Bộ nhớ & Cắt mảng):** Giả sử bạn nhận được một ma trận dữ liệu khách hàng kích thước lớn $10,000 \times 500$ (kích thước ~40 MB). Bạn cần tạo một ma trận con gồm 1,000 khách hàng đầu tiên và 50 biến đặc trưng để huấn luyện thử nghiệm. Trong trường hợp nào bạn nên sử dụng lát cắt thường (`mat[:1000, :50]`), và trong trường hợp nào bạn BẮT BUỘC phải thêm `.copy()`?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
1. **Dùng lát cắt thường (View):** Khi bạn chỉ muốn đọc dữ liệu để tính toán thống kê (như tính trung bình, độ lệch chuẩn, kiểm tra phân phối) mà không làm biến đổi bất kỳ giá trị nào trên mảng con đó, hoặc khi bộ nhớ RAM đang cực kỳ khan hiếm và bạn muốn tiết kiệm bộ nhớ tối đa.
2. **Bắt buộc dùng `.copy()`:** Khi bạn dự định thực hiện các thao tác tiền xử lý làm biến đổi trực tiếp dữ liệu trên mảng con (ví dụ: gán nhãn, chuẩn hóa Z-Score tại chỗ, điền giá trị khuyết). Nếu không dùng `.copy()`, mọi thao tác ghi đè trên mảng con sẽ làm đột biến và phá hủy dữ liệu gốc của ma trận $10,000 \times 500$. Ngoài ra, việc giữ một View nhỏ của một mảng mẹ khổng lồ sẽ khiến trình gom rác (Garbage Collector) không thể giải phóng toàn bộ 40 MB bộ nhớ của mảng mẹ.
</details>

2. **Thử thách 2 (Liên kết Trục không gian & Lan truyền kích thước):** Cho ma trận $X$ có kích thước $(N, D)$ đại diện cho $N$ mẫu dữ liệu và $D$ đặc trưng. Để chuẩn hóa Min-Max từng đặc trưng về đoạn $[0, 1]$ theo công thức:
$$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$
Bạn cần tính $X_{\min}$ và $X_{\max}$ theo `axis` nào? Có cần thiết phải đặt `keepdims=True` không? Tại sao?
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
1. **Chọn trục:** Cần tính giá trị nhỏ nhất và lớn nhất của **từng đặc trưng (từng cột)**, do đó ta phải nén toàn bộ $N$ hàng lại. Theo quy tắc trục tiêu biến, ta MUST chọn `axis=0` (`X_min = X.min(axis=0)`).
2. **Vai trò của keepdims:**
   - Nếu không dùng `keepdims`: `X_min` có hình dạng là $(D,)$. Theo quy tắc broadcasting, khi so sánh $(N, D)$ với $(D,)$, chiều cuối cùng khớp nhau ($D == D$), hệ thống tự động đệm 1 vào bên trái thành $(1, D)$ và thực hiện phép trừ hoàn hảo. Vì vậy phép tính vẫn chạy đúng.
   - Tuy nhiên, việc đặt `keepdims=True` (`shape: (1, D)`) là một thực hành phòng thủ rất tốt (Defensive Programming), giúp mã nguồn tường minh tuyệt đối về mặt hình học ma trận và đồng bộ thói quen khi thao tác chuẩn hóa theo hàng (`axis=1`, nơi mà `keepdims=True` là **bắt buộc**).
</details>

3. **Thử thách 3 (Liên kết Bài toán Thực tế & Cạm bẫy Học máy):** Một nhà khoa học dữ liệu nạp dữ liệu trạm quan sát thời tiết gồm 3 biến: `TMAX` (Nhiệt độ cực đại, dao động $15 - 38^\circ\text{C}$), `PRCP` (Lượng mưa, dao động $0 - 45\text{ mm}$ chứa mã lỗi $999.9$), và `WIND` (Tốc độ gió, dao động $0 - 15\text{ m/s}$). Người này trực tiếp áp dụng thuật toán phân cụm $K$-Means mà không qua bước làm sạch. Hãy chỉ ra 2 thảm họa toán học chắc chắn sẽ xảy ra với các tâm cụm (Cluster Centroids).
<details>
<summary>Kiểm tra đáp án phản xạ</summary>

*Đáp án:*  
1. **Thảm họa 1: Mã lỗi $999.9$ thống trị hoàn toàn khoảng cách Euclid:** Thuật toán K-Means sử dụng khoảng cách Euclid $\sqrt{\sum (x_i - c_i)^2}$. Giá trị lỗi $999.9$ trong biến lượng mưa sẽ tạo ra khoảng chênh lệch bình phương xấp xỉ $(999.9 - 0)^2 \approx 1,000,000$, lấn át hoàn toàn mọi biến động tự nhiên của nhiệt độ ($15 - 38^\circ\text{C}$) và gió ($0 - 15\text{ m/s}$). Các tâm cụm sinh ra sẽ chỉ phân loại dữ liệu thành: "Nhóm cảm biến bị hỏng" vs "Nhóm cảm biến bình thường", hoàn toàn vô giá trị về mặt khí hậu học.
2. **Thảm họa 2: Mất cân bằng thang đo vật lý:** Ngay cả khi đã lọc bỏ $999.9$, nếu không thực hiện chuẩn hóa Z-Score ($z = (x - \mu)/\sigma$), biến lượng mưa ($0 - 45\text{ mm}$) có phương sai lớn hơn nhiều so với tốc độ gió ($0 - 15\text{ m/s}$). Khoảng cách không gian sẽ bị kéo dãn theo chiều lượng mưa, khiến thuật toán K-Means coi nhẹ tầm quan trọng của tốc độ gió và nhiệt độ.
</details>

