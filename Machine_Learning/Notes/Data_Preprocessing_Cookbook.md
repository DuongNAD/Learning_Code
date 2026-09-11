# 🍳 Cẩm Nang Tiền Xử Lý Dữ Liệu Thực Chiến (Data Preprocessing Cookbook)

---

## 1. Phòng Tránh Rò Rỉ Dữ Liệu (Preventing Data Leakage)
> **Quy tắc bất biến**: Mọi thông số thống kê (Mean, Median, Standard Deviation, Max, Min, Vocabulary của TF-IDF, Encoders) CHỈ ĐƯỢC PHÉP TÍNH TRÊN TẬP TRAIN!

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# BƯỚC 1: Tách Train / Test trước
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# BƯỚC 2: Fit CHỈ TRÊN TRAIN, sau đó transform cả hai
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Tuyệt đối KHÔNG fit_transform ở đây!
```

---

## 2. Chiến Lược Xử Lý Dữ Liệu Khuyết Thiếu (Missing Values)

| Loại dữ liệu | Tình huống | Giải pháp khuyến nghị | Code mẫu Scikit-Learn |
|:---|:---|:---|:---|
| **Số (Numerical)** | Phân phối chuẩn, ít ngoại lai | Thay bằng `Mean` | `SimpleImputer(strategy='mean')` |
| **Số (Numerical)** | Phân phối lệch (Skewed), nhiều Outliers | Thay bằng `Median` | `SimpleImputer(strategy='median')` |
| **Phân loại (Categorical)** | Dữ liệu dạng text / danh mục | Thay bằng `Most Frequent` (Mode) | `SimpleImputer(strategy='most_frequent')` |
| **Dữ liệu y sinh** | Giá trị 0 bất hợp lý (VD: Glucose=0, BP=0) | Chuyển 0 thành `np.nan` trước khi impute | `df[cols] = df[cols].replace(0, np.nan)` |

---

## 3. Lọc Ngoại Lai Bằng Khoảng Tứ Phân vị (IQR Method)

```python
def remove_outliers_iqr(df, columns, factor=1.5):
    cleaned_df = df.copy()
    for col in columns:
        Q1 = cleaned_df[col].quantile(0.25)
        Q3 = cleaned_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - factor * IQR
        upper_bound = Q3 + factor * IQR
        cleaned_df = cleaned_df[(cleaned_df[col] >= lower_bound) & (cleaned_df[col] <= upper_bound)]
    return cleaned_df
```

---

## 4. Lựa Chọn Bộ Chuẩn Hóa (Scalers)

1. **`StandardScaler`** ($z = \frac{x - \mu}{\sigma}$):
   - Đưa dữ liệu về phân phối có $\mu = 0, \sigma = 1$.
   - Nhạy cảm với Outliers.
   - Thích hợp cho: Logistic Regression, SVM, PCA, Neural Networks.

2. **`MinMaxScaler`** ($x' = \frac{x - \min}{\max - \min}$):
   - Đưa dữ liệu về đoạn chính xác $[0, 1]$.
   - Cần thiết cho: Xử lý ảnh pixel $[0, 255] \to [0.0, 1.0]$, thuật toán yêu cầu số dương.

3. **`RobustScaler`** ($x' = \frac{x - Q_2}{IQR}$):
   - Sử dụng Trung vị (Median) và IQR thay vì Mean và Std.
   - **Miễn nhiễm mạnh với Outliers**.
