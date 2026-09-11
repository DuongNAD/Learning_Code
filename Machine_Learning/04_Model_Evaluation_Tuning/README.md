# ⚙️ Thẩm Định Mô Hình & Tinh Chỉnh Siêu Tham Số (Model Evaluation & Tuning)

Thư mục cung cấp bộ công cụ toàn diện chuẩn công nghiệp phục vụ việc đánh giá, thẩm định độ ổn định, so sánh benchmark và tinh chỉnh siêu tham số cho các mô hình Học Máy.

---

## 📂 Danh Mục Công Cụ Cốt Lõi

1. **`model_evaluation_metrics.py`**:
   - **Thẩm định Phân loại (Classification)**:
     - Tính toán ma trận nhầm lẫn (`confusion_matrix`), Accuracy, Balanced Accuracy, Precision/Recall (Macro & Weighted), F1-Score, ROC-AUC và PR-AUC.
   - **Tối ưu hóa ngưỡng xác suất quyết định (Threshold Optimization)**:
     - `find_optimal_threshold(y_true, y_prob, metric='f1'|'youden')`: Tự động quét và tìm ngưỡng xác suất tối ưu theo chỉ số F1 hoặc Youden's J-statistic ($J = \text{Recall} + \text{Specificity} - 1$). Rất hữu ích cho các bài toán dữ liệu mất cân bằng và y tế.
   - **Thẩm định Hồi quy (Regression)**:
     - Tính toán MAE, MSE, RMSE, R², Adjusted R² (hiệu chỉnh theo bậc tự do), MAPE và sai số cực đại Max Error.
   - **Phân tích độ ổn định Cross-Validation**:
     - `evaluate_cv_stability(estimator, X, y, cv=5)`: Phân tích kỳ vọng và phương sai điểm số qua các folds để phát hiện rủi ro Overfitting.

2. **`hyperparameter_tuning_suite.py`**:
   - **So sánh Hiệu quả Tìm kiếm (GridSearchCV vs RandomizedSearchCV)**:
     - Đo lường thời gian thực thi, số lượng phép thử và chất lượng tham số tìm được để lựa chọn chiến lược tối ưu ngân sách tính toán.
   - **Chẩn đoán Overfitting qua Đường cong Kiểm định (Validation Curve)**:
     - Phân tích sự biến thiên của train score và validation score khi thay đổi một siêu tham số cụ thể (ví dụ: `max_depth`, `alpha`).

3. **`model_benchmark_comparison.py`**:
   - Khung so sánh đa mô hình (Logistic Regression, Decision Tree, Random Forest, SVM, KNN) trên cùng một bài toán, xuất bảng tổng hợp: Độ chính xác, F1-Score, ROC-AUC, thời gian huấn luyện (ms) và độ trễ suy luận ($\mu$s/sample).

4. **`diabetes_tuning_case_study.py`**:
   - Case study thực chiến hoàn chỉnh trên tập dữ liệu y tế Diabetes:
     - Chuẩn hóa đặc trưng bằng `StandardScaler`.
     - Tìm kiếm siêu tham số tối ưu bằng 5-Fold Stratified Cross-Validation.
     - Quét và hiệu chuẩn ngưỡng xác suất tối ưu ($0.20 \to 0.40$), nâng cao độ nhạy (Recall) phát hiện bệnh lý.
     - Xuất các tệp trọng số artifacts: `model.pkl`, `scaler.pkl`, `threshold.pkl`.

5. **`test_evaluation_tuning.py`**:
   - Bộ kiểm thử tự động `pytest` đảm bảo 100% tính chính xác toán học của toàn bộ các hàm đo lường và tối ưu.

---

## 🚀 Cách Chạy & Kiểm Thử

```bash
# Chạy bộ kiểm thử tự động
pytest 04_Model_Evaluation_Tuning/test_evaluation_tuning.py

# Chạy case study tinh chỉnh ngưỡng
python3 04_Model_Evaluation_Tuning/diabetes_tuning_case_study.py

# Chạy benchmark so sánh các mô hình
python3 04_Model_Evaluation_Tuning/model_benchmark_comparison.py
```
