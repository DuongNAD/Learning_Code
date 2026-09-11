# 📝 Đề Thi Chẩn Đoán 03: Đánh Giá Mô Hình, Tinh Chỉnh Siêu Tham Số & Metrics

> Thiết kế bởi **DeepTutor AI Mentor**. Kiểm tra khả năng chẩn đoán metrics và chiến lược thực chiến.

---

### Câu 1: Bẫy Accuracy trên Dữ Liệu Mất Cân Bằng (Class Imbalance)
Trong bài toán phát hiện bệnh ung thư, tập dữ liệu có 99% người khỏe mạnh (Class 0) và 1% người mắc bệnh (Class 1). Một mô hình "ngớ ngẩn" luôn dự đoán 0 cho mọi trường hợp sẽ có:
- [A] Accuracy = 50%, Recall = 50%.
- [B] Accuracy = 99%, nhưng Recall của Class 1 = 0% (Hoàn toàn vô dụng trong y khoa).
- [C] F1-Score = 0.99.
- [D] ROC-AUC = 1.0.

---

### Câu 2: Lựa chọn giữa Precision và Recall trong Y Tế
Trong bài toán sàng lọc bệnh tiểu đường hoặc ung thư (bỏ sót bệnh nhân nguy hiểm hơn là gọi đi xét nghiệm lại), bạn nên tối ưu metric nào?
- [A] Precision (Độ chính xác của cảnh báo dương tính).
- [B] Recall (Độ bao phủ / Độ nhạy - hạn chế tối đa False Negatives).
- [C] Specificity.
- [D] Chỉ cần nhìn MAE.

---

### Câu 3: Kỹ thuật Tối Ưu Ngưỡng Quyết Định (Threshold Tuning)
Khi mô hình có `class_weight='balanced'` nhưng Recall vẫn chưa đủ cao theo yêu cầu y khoa, ta có thể làm gì mà KHÔNG cần huấn luyện lại model?
- [A] Tăng learning rate của optimizer.
- [B] Hạ ngưỡng phân loại xác suất từ 0.5 xuống một mức thấp hơn (ví dụ 0.25 - 0.30) dựa trên phân tích đường cong Precision-Recall Tradeoff.
- [C] Xóa bớt đặc trưng trong bảng dữ liệu.
- [D] Chuyển đổi dữ liệu về dạng chuỗi văn bản.

---

### Câu 4: GridSearchCV vs RandomizedSearchCV
Khi không gian siêu tham số có 6 biến liên tục và tài nguyên tính toán có hạn, tại sao nên ưu tiên `RandomizedSearchCV` hơn `GridSearchCV`?
- [A] Vì GridSearchCV không hỗ trợ Cross-Validation.
- [B] Vì GridSearchCV phải duyệt tích Descartes của tất cả các giá trị (Bùng nổ tổ hợp), trong khi RandomizedSearchCV thăm dò đều khắp không gian và tìm ra nghiệm xấp xỉ tối ưu với số lần thử nghiệm ít hơn nhiều.
- [C] Vì RandomizedSearchCV luôn đảm bảo tìm được cực trị toàn cục 100%.
- [D] Vì GridSearchCV làm hỏng trọng số mô hình.

---

### Câu 5: Ý nghĩa của ROC-AUC
Điểm số ROC-AUC (Area Under ROC Curve) biểu thị xác suất nào?
- [A] Xác suất mô hình dự đoán đúng trên tập train.
- [B] Xác suất mà mô hình xếp hạng (đưa ra xác suất cao hơn) cho một mẫu dương ngẫu nhiên so với một mẫu âm ngẫu nhiên.
- [C] Tỷ lệ phần trăm các điểm dữ liệu nằm trong khoảng tin cậy 95%.
- [D] Tỷ lệ giữa True Positives và False Positives.

---

<details>
<summary><b>🔍 BẢNG ĐÁP ÁN & PHÂN TÍCH BẪY NHẬN THỨC (COGNITIVE GAPS)</b></summary>

| Câu | Đáp án đúng | Lỗ hổng nhận thức thường gặp |
|:---:|:---:|:---|
| 1 | **B** | Bẫy "Accuracy Paradox". Tuyệt đối không dùng Accuracy làm chỉ số duy nhất khi dữ liệu lệch lớp! |
| 2 | **B** | Trong y tế: False Negative (bỏ sót bệnh nhân) = chết người. Do đó Recall là ưu tiên số 1! Trong phát hiện spam email: False Positive (thư quan trọng bị vào spam) = tệ hơn, do đó ưu tiên Precision. |
| 3 | **B** | Đây chính là kỹ thuật được thực hiện trong file `b9_evaluate.py` (hạ ngưỡng từ 0.5 xuống 0.27 giúp Recall tăng vọt từ 55% lên 91%!). |
| 4 | **B** | Nghiên cứu của Bergstra & Bengio (2012) chứng minh Randomized Search hiệu quả vượt trội so với Grid Search trong không gian siêu tham số đa chiều. |
| 5 | **B** | ROC-AUC là thước đo năng lực phân biệt (Discriminative Power) độc lập với ngưỡng phân loại (Threshold-independent). |

</details>
