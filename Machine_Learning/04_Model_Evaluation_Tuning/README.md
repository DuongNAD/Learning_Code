# ⚙️ Đánh Giá Mô Hình & Tinh Chỉnh Siêu Tham Số (Model Evaluation & Tuning)

Thư mục tập trung vào các kỹ thuật thẩm định mô hình chuyên sâu, chống overfitting, xử lý dữ liệu lệch lớp và tối ưu hóa ngưỡng quyết định trong môi trường thực chiến.

---

## 📂 Các Tập Tin Cốt Lõi

1. **`b8_tune.py`**:
   - Tinh chỉnh siêu tham số bằng `GridSearchCV` với 5-fold cross-validation.
   - So sánh không gian tham số của Decision Tree (`max_depth`, `min_samples_split`, `min_samples_leaf`), Random Forest (`n_estimators`, `max_depth`) và KNN (`n_neighbors`, `weights`).

2. **`b9_evaluate.py`**:
   - Đánh giá toàn diện mô hình:
     - Báo cáo phân loại (`classification_report`): Precision, Recall, Macro/Weighted F1.
     - Ma trận nhầm lẫn (`confusion_matrix`).
     - Đường cong ROC và chỉ số ROC-AUC (`roc_auc_score`).
     - Phương pháp 1: Phạt lỗi bằng trọng số lớp `class_weight='balanced'`.
     - Phương pháp 2: Quét ngưỡng xác suất tối ưu từ $0.20$ đến $0.30$ (Threshold Tuning) giúp tăng độ nhạy (Recall) lên trên $90\%$ cho các bài toán y tế.

3. **`b10_save.py`**:
   - Đóng gói mô hình tối ưu đã huấn luyện, bộ chuẩn hóa scaler và ngưỡng phân loại tối ưu thành các file artifacts (`model.pkl`, `scaler.pkl`, `threshold.pkl`).

4. **`outlier_explained.html`**:
   - Giao diện trực quan hoá nguyên lý xác định và xử lý ngoại lai bằng phân vị tứ phân (IQR).
