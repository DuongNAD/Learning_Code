# 📝 Đề Thi Chẩn Đoán 02: Supervised Learning (Regression & Classification)

> Thiết kế bởi **DeepTutor AI Mentor**. Hãy thử thách khả năng phân tích mô hình học máy có giám sát của bạn.

---

### Câu 1: Data Leakage trong Tiền Xử Lý
Nếu bạn áp dụng `StandardScaler.fit_transform(X)` trên **toàn bộ dataset** trước khi gọi `train_test_split()`, sai lầm nghiêm trọng nào đã xảy ra?
- [A] Overfitting nhẹ ở tập train nhưng không ảnh hưởng gì đến tập test.
- [B] Data Leakage (Rò rỉ thông tin): Mean và Standard Deviation của tập Test đã bị lộ cho tập Train học được, làm cho kết quả đánh giá mô hình lạc quan ảo.
- [C] Làm cho ma trận đặc trưng bị đa cộng tuyến hoàn hảo.
- [D] Làm cho mô hình không thể hội tụ khi dùng Gradient Descent.

---

### Câu 2: Bias-Variance Tradeoff trong Cây Quyết Định (Decision Tree)
Khi tăng tham số `max_depth` của Decision Tree lên vô hạn (None) mà không giới hạn `min_samples_split`, mô hình sẽ có đặc tính gì?
- [A] High Bias, Low Variance (Underfitting).
- [B] Low Bias, High Variance (Overfitting - học vẹt toàn bộ nhiễu của tập Train).
- [C] Cả Bias và Variance đều đạt mức tối thiểu lý tưởng.
- [D] Mô hình tự động chuyển thành Random Forest.

---

### Câu 3: Bản chất của Logistic Regression
Mặc dù có tên là "Regression", tại sao Logistic Regression lại là thuật toán Phân loại (Classification)?
- [A] Vì nó sử dụng hàm mất mát Mean Squared Error (MSE).
- [B] Vì nó dùng hàm kích hoạt Sigmoid để nén đầu ra tuyến tính $z = w^T x + b$ về khoảng xác suất $[0, 1]$, sau đó so sánh với ngưỡng (ngưỡng mặc định 0.5) để phân lớp nhị phân.
- [C] Vì nó chỉ áp dụng được cho bài toán nhiều lớp (Multi-class).
- [D] Vì các hệ số $w$ không thể tính đạo hàm được.

---

### Câu 4: Bagging vs Boosting
Sự khác biệt cốt lõi giữa **Random Forest** (Bagging) và **XGBoost/Gradient Boosting** (Boosting) là gì?
- [A] Random Forest xây dựng các cây độc lập, song song và lấy biểu quyết số đông để giảm Variance; Boosting xây dựng các cây tuần tự, mỗi cây sau cố gắng học và sửa sai sai số (Residuals) của các cây trước đó để giảm Bias.
- [B] Random Forest chỉ dùng cho hồi quy, còn XGBoost chỉ dùng cho phân loại.
- [C] Random Forest không sử dụng kỹ thuật Bootstrap sampling.
- [D] Random Forest có độ phức tạp thuật toán cao hơn XGBoost.

---

### Câu 5: Chuỗi Thời Gian & Cross-Validation
Tại sao KHÔNG ĐƯỢC dùng K-Fold Cross-Validation thông thường với dữ liệu chuỗi thời gian (Time Series)?
- [A] Vì chuỗi thời gian có quá ít mẫu dữ liệu.
- [B] Vì K-Fold xáo trộn ngẫu nhiên dữ liệu, dẫn đến việc dùng dữ liệu tương lai để dự đoán quá khứ (Look-ahead bias / Phá vỡ tính nhân quả thời gian).
- [C] Vì chuỗi thời gian không có nhãn mục tiêu.
- [D] Vì K-Fold chỉ hỗ trợ dữ liệu ảnh.

---

<details>
<summary><b>🔍 BẢNG ĐÁP ÁN & PHÂN TÍCH BẪY NHẬN THỨC (COGNITIVE GAPS)</b></summary>

| Câu | Đáp án đúng | Lỗ hổng nhận thức thường gặp |
|:---:|:---:|:---|
| 1 | **B** | Rất nhiều người mới mắc lỗi này. Nguyên tắc vàng: Chỉ `.fit()` trên tập Train, sau đó dùng scaler đó `.transform()` sang cả Train và Test! |
| 2 | **B** | Khi cây quá sâu, nó tạo ra các vùng quyết định siêu nhỏ bao quanh từng điểm nhiễu, khiến Test Error tăng vọt. |
| 3 | **B** | Bản chất là phân loại nhị phân dựa trên mô hình xác suất Log-Odds (Logit). |
| 4 | **A** | Hiểu đúng bản chất Bagging (Parallel, Giảm Variance) vs Boosting (Sequential, Giảm Bias) là chìa khóa phân biệt giữa Senior và Junior ML Engineer. |
| 5 | **B** | Với Time Series, bắt buộc phải dùng `TimeSeriesSplit` (Rolling Window / Expanding Window) để giữ nguyên trật tự thời gian. |

</details>
