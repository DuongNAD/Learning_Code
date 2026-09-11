# 🎯 Học Có Giám Sát (Supervised Learning)

Chuyên mục toàn diện về các thuật toán và quy trình học có giám sát: từ các mô hình hồi quy (Regression), phân loại (Classification), dự báo chuỗi thời gian (Time Series Forecasting) đến quy trình phát triển mô hình chuẩn công nghiệp End-to-End.

---

## 📂 Các Tiểu Thư Mục Thực Hành

### 1. `01_Regression/`
- **Mục tiêu**: Dự đoán các biến liên tục.
- **Tập tin chính**:
  - `regression.py`: Huấn luyện hồi quy với Pipeline Scikit-learn (Imputer, StandardScaler, OneHotEncoder, OrdinalEncoder, ColumnTransformer, RandomForestRegressor).
  - `StudentScore.xls`: Bộ dữ liệu 1,000 học sinh dự đoán điểm thi Toán.

### 2. `02_Classification/`
- **Mục tiêu**: Phân loại nhị phân và đa lớp.
- **Tập tin chính**:
  - `classification.py`: Tinh chỉnh siêu tham số `RandomForestClassifier` với `GridSearchCV` trên bộ dữ liệu `diabetes.csv`.
  - `job_classification.py`: Xử lý ngôn ngữ tự nhiên (NLP) với TF-IDF Vectorizer và phân loại cấp bậc nghề nghiệp (`final_project.csv` & `final_project.ods`).
  - `car.csv`, `csgo.csv`: Dữ liệu phân loại thực hành mở rộng.

### 3. `03_Time_Series_Forecasting/`
- **Mục tiêu**: Dự báo tương lai dựa trên chuỗi thời gian quá khứ.
- **Tập tin chính**:
  - `time_series_forecasting.py`: Tạo lag features (cửa sổ trượt trễ) và dự báo nồng độ CO2.
  - `time_series_direct_forecasting.py`: Dự báo trực tiếp đa bước thời gian (Direct Multi-step Forecasting).
  - `co2.csv`: Dữ liệu phát thải khí CO2 theo thời gian.

### 4. `04_End_to_End_Diabetes_Pipeline/`
- **Mục tiêu**: Quy trình 10 bước chuẩn mực xây dựng sản phẩm ML:
  - `EDA.py`: Khám phá dữ liệu và phân tích thống kê.
  - `b2&3.py`: Xử lý missing values sinh học và lọc ngoại lai bằng IQR.
  - `b4_split.py`: Tách tập dữ liệu có phân tầng (`stratify=y`).
  - `b5_feature.py`: Chuẩn hóa đặc trưng với `StandardScaler`.
  - `traind.py`: So sánh đồng thời 5 mô hình cơ bản (Logistic, KNN, Decision Tree, Random Forest, SVM).
  - `b8_tune.py`: Tìm kiếm siêu tham số tối ưu bằng `GridSearchCV`.
  - `b9_evaluate.py`: Đánh giá ma trận nhầm lẫn, ROC-AUC và tối ưu ngưỡng xác suất.
  - `b10_save.py`: Đóng gói mô hình và bộ scale thành `model.pkl`, `scaler.pkl`, `threshold.pkl`.
  - `outlier_explained.html`: Minh họa trực quan tương tác về phân phối và Boxplot.
  - `huong_dan_cac_buoc.md`: Tài liệu hướng dẫn chi tiết từng bước bằng tiếng Việt.
