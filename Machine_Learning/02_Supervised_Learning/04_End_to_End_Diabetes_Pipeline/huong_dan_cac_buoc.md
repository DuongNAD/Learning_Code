# 🎯 Hướng Dẫn Từng Bước — ML Pipeline: Dự Đoán Bệnh Tiểu Đường

> **Dataset**: `diabetes.csv` — 768 mẫu, 8 features, 1 target (Outcome: 0/1)
> **Bài toán**: Binary Classification

---

## Bước 1: Khám Phá Dữ Liệu (EDA)

**Làm gì**: Nhìn tổng quan dữ liệu trước khi động tay vào bất cứ thứ gì.

- `df.shape` → xem có bao nhiêu dòng, bao nhiêu cột
- `df.describe()` → thống kê mô tả: mean, std, min, max, các phân vị (25%, 50%, 75%)
- `df.info()` → kiểu dữ liệu từng cột, có bao nhiêu non-null
- `df.isnull().sum()` → đếm số NaN mỗi cột
- `df['Outcome'].value_counts()` → xem tỷ lệ class 0 vs class 1 (có mất cân bằng không)
- Vẽ **histogram** từng feature → xem phân phối
- Vẽ **boxplot** → phát hiện outliers
- Vẽ **correlation heatmap** (`df.corr()`) → xem feature nào tương quan mạnh với Outcome

**Tại sao**: Nếu không hiểu dữ liệu mà nhảy thẳng vào train model thì rất dễ mắc sai lầm. EDA giúp phát hiện vấn đề sớm (missing values, outliers, class imbalance) để xử lý đúng cách.

---

## Bước 2: Xử Lý Missing Values

**Làm gì**: Dataset này KHÔNG có NaN chính thức, nhưng có **giá trị 0 bất hợp lệ**.

5 cột sau không thể bằng 0 ở người sống:

| Cột | Ý nghĩa | Số lượng 0 |
|-----|---------|-----------|
| Glucose | Đường huyết | 5 |
| BloodPressure | Huyết áp | 35 |
| SkinThickness | Độ dày da | 227 |
| Insulin | Insulin huyết thanh | 374 |
| BMI | Chỉ số khối cơ thể | 11 |

**Cách làm**:
1. Thay giá trị 0 ở 5 cột trên bằng `NaN`
2. Chọn cách điền (impute):
   - **Median**: Ổn định, không bị ảnh hưởng bởi outliers
   - **Mean**: Đơn giản nhưng bị kéo lệch bởi outliers
   - **KNN Imputer**: Dựa trên các dòng tương tự để điền — phức tạp hơn nhưng có thể chính xác hơn
3. Hoặc xoá dòng (sẽ mất nhiều data, đặc biệt Insulin mất gần 50%)

**Tại sao**: Giá trị 0 giả sẽ làm model học sai. Ví dụ model có thể nghĩ "BMI = 0 → không tiểu đường" — điều này vô nghĩa.

---

## Bước 3: Xử Lý Outliers

**Làm gì**: Xác định và quyết định xử lý các giá trị bất thường.

**Cách phát hiện**:
- **IQR (Interquartile Range)**: Giá trị nằm ngoài `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]` là outlier
- **Z-score**: Giá trị có |z| > 3 là outlier

**Cách xử lý** (tuỳ bạn quyết định):
- Cắt (clip) về giới hạn trên/dưới
- Xoá dòng
- Giữ nguyên (nếu outlier có ý nghĩa y khoa, ví dụ Insulin = 846 có thể là ca nặng thật)

**Tại sao**: Outliers có thể làm model bị "kéo lệch", đặc biệt các model nhạy cảm với scale như KNN, SVM, Logistic Regression. Tuy nhiên cần cẩn thận vì trong y tế, outlier có thể là ca bệnh thật.

---

## Bước 4: Chia Dữ Liệu Train/Test

**Làm gì**:
- Dùng `train_test_split()` chia thành train set và test set
- Dùng `stratify=y` để giữ tỷ lệ class 0/1 giống nhau ở cả train và test
- Set `random_state` cố định để kết quả reproducible

**Tại sao**: Test set dùng để đánh giá model công bằng — nó phải là dữ liệu model **chưa bao giờ thấy** trong quá trình training. Nếu không chia, bạn đang đánh giá model trên chính dữ liệu nó đã học → kết quả ảo.

> ⚠️ **QUAN TRỌNG**: Chia train/test **TRƯỚC** khi scaling/imputing. Mọi bước preprocessing phải fit trên train, rồi transform cả train lẫn test. Nếu fit trên toàn bộ data → thông tin từ test set rò rỉ vào train set → **data leakage**.

---

## Bước 5: Feature Scaling (Chuẩn Hoá)

**Làm gì**: Đưa tất cả features về cùng thang đo.

Các lựa chọn:
- **StandardScaler**: `(x - mean) / std` → mean=0, std=1. Phù hợp khi data gần phân phối chuẩn.
- **MinMaxScaler**: `(x - min) / (max - min)` → kéo về [0, 1]. Phù hợp khi cần giá trị dương.
- **RobustScaler**: `(x - median) / IQR` → dùng median và IQR thay vì mean và std. Phù hợp khi data có outliers.

**Quy tắc**:
1. `scaler.fit(X_train)` — chỉ fit trên train
2. `X_train_scaled = scaler.transform(X_train)`
3. `X_test_scaled = scaler.transform(X_test)` — dùng cùng scaler, chỉ transform

**Tại sao**: Các features có range khác nhau rất lớn (Pregnancies: 0-17 vs Insulin: 0-846). Nếu không scale, những features có giá trị lớn sẽ "áp đảo" model. Các model như KNN, SVM, Logistic Regression **bắt buộc** phải scale. Tree-based models (Random Forest, XGBoost) thì không cần nhưng scale cũng không hại.

---

## Bước 6: Feature Engineering (tuỳ chọn)

**Làm gì**: Tạo features mới hoặc chọn lọc features.

Một số ý tưởng:
- `Glucose * BMI` — tương tác giữa đường huyết và chỉ số cơ thể
- `Age` phân nhóm (trẻ / trung niên / già)
- `Insulin / Glucose` — tỷ lệ insulin so với glucose

Feature Selection:
- Xem correlation với Outcome → loại feature tương quan quá thấp
- Dùng `SelectKBest` hoặc `feature_importances_` từ Random Forest
- Loại features tương quan cao với nhau (multicollinearity)

**Tại sao**: Đôi khi tổ hợp features chứa thông tin mà từng feature đơn lẻ không thể hiện được. Feature selection giúp giảm noise và tăng tốc training.

---

## Bước 7: Huấn Luyện Mô Hình

**Làm gì**: Thử nhiều thuật toán, so sánh.

Gợi ý các model nên thử:
1. **Logistic Regression** — baseline đơn giản, dễ giải thích
2. **KNN** — dựa trên khoảng cách, cần scaling
3. **Decision Tree** — dễ hiểu, dễ overfit
4. **Random Forest** — ensemble nhiều trees, robust hơn
5. **SVM** — tốt với data ít chiều
6. **Gradient Boosting / XGBoost** — thường cho kết quả tốt nhất
7. **Neural Network (MLP)** — nếu muốn thử deep learning

Dùng **Cross-Validation** (5-fold hoặc 10-fold) thay vì chỉ nhìn score trên 1 lần split. CV cho kết quả đáng tin cậy hơn vì đánh giá trên nhiều fold.

**Tại sao**: Mỗi thuật toán có điểm mạnh/yếu khác nhau. Không có model nào "tốt nhất cho mọi bài toán" (No Free Lunch Theorem). Phải thử rồi so sánh.

---

## Bước 8: Tinh Chỉnh Hyperparameters

**Làm gì**: Tìm bộ tham số tốt nhất cho model.

- **GridSearchCV**: Thử tất cả tổ hợp tham số → chắc chắn tìm được best nhưng chậm
- **RandomizedSearchCV**: Thử ngẫu nhiên một số tổ hợp → nhanh hơn, phù hợp khi search space lớn

Ví dụ tham số cần tuning:
- Random Forest: `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`
- SVM: `C`, `gamma`, `kernel`
- KNN: `n_neighbors`, `weights`, `metric`
- XGBoost: `n_estimators`, `max_depth`, `learning_rate`, `subsample`

**Tại sao**: Tham số mặc định hiếm khi là tối ưu. Tuning có thể cải thiện performance đáng kể. Ví dụ Random Forest với `n_estimators=10` sẽ kém hơn nhiều so với `n_estimators=300`.

---

## Bước 9: Đánh Giá Mô Hình

**Làm gì**: Đánh giá model trên **test set** bằng nhiều metrics.

Các metric:
- **Accuracy** = (TP + TN) / Total — tỷ lệ đúng tổng thể
- **Precision** = TP / (TP + FP) — trong số dự đoán dương, bao nhiêu đúng
- **Recall** = TP / (TP + FN) — trong số thực sự dương, bao nhiêu được phát hiện
- **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall) — trung bình điều hoà
- **ROC-AUC** — khả năng phân biệt class, không phụ thuộc threshold
- **Confusion Matrix** — bảng chi tiết TP, TN, FP, FN

Bạn tự quyết định metric nào quan trọng nhất dựa trên bối cảnh bài toán.

**Tại sao**: Accuracy không đủ, đặc biệt khi data mất cân bằng. Ví dụ nếu 65% là class 0, model luôn đoán 0 sẽ có accuracy 65% nhưng hoàn toàn vô dụng. Cần nhìn nhiều metrics để đánh giá toàn diện.

---

## Bước 10: Lưu Mô Hình

**Làm gì**:
- Lưu model bằng `joblib` hoặc `pickle`
- Lưu cả scaler (vì data mới cũng cần transform giống train)
- Viết hàm predict nhận input → trả kết quả

**Tại sao**: Không thể train lại mỗi lần muốn dự đoán. Lưu model để dùng lại mà không cần retrain.

---

## Tóm Tắt Thứ Tự

```
1. EDA          → Hiểu data
2. Missing      → Thay 0 bất hợp lệ, impute
3. Outliers     → Phát hiện, xử lý
4. Split        → Chia train/test (TRƯỚC khi scale!)
5. Scale        → Fit trên train, transform cả 2
6. Features     → Tạo mới / chọn lọc (tuỳ chọn)
7. Train        → Thử nhiều model + cross-validation
8. Tune         → GridSearchCV / RandomizedSearchCV
9. Evaluate     → Nhiều metrics, confusion matrix, ROC
10. Save        → joblib.dump() model + scaler
```
