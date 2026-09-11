# 📝 Đề Thi Chẩn Đoán 01: Nền Tảng Toán & Thuật Toán Trong Machine Learning

> Thiết kế bởi **DeepTutor AI Mentor**. Hãy tự làm trước khi xem phần giải thích bẫy nhận thức ở cuối trang.

---

### Câu 1: Ý nghĩa hình học của Tích vô hướng (Dot Product)
Cho hai vector $\mathbf{u}$ và $\mathbf{v}$ trong không gian $\mathbb{R}^n$. Khi $\mathbf{u} \cdot \mathbf{v} = 0$, điều này chứng minh điều gì?
- [A] Hai vector cùng phương và cùng chiều.
- [B] Hai vector trực giao (vuông góc nhau góc 90 độ), không có thành phần nào chiếu lên nhau.
- [C] Một trong hai vector chắc chắn phải là vector 0.
- [D] Độ dài của hai vector bằng nhau.

---

### Câu 2: Regularization và Chuẩn L1 vs L2
Tại sao chuẩn L1 (Lasso) có xu hướng tạo ra mô hình thưa (Sparse Model - nhiều trọng số về chính xác bằng 0), trong khi L2 (Ridge) chỉ thu nhỏ trọng số về gần 0?
- [A] Vì đạo hàm của chuẩn L1 tại lân cận 0 là hằng số ($\pm 1$), lực kéo về 0 không bị giảm khi trọng số nhỏ dần; vùng ràng buộc của L1 có các đỉnh nhọn nằm ngay trên các trục toạ độ.
- [B] Vì L1 tính toán nhanh hơn L2 gấp 2 lần.
- [C] Vì L2 luôn làm cho ma trận nghịch đảo bị suy biến.
- [D] Vì chuẩn L1 không cho phép các biến tương quan cùng tồn tại.

---

### Câu 3: Kỹ thuật Số học Tránh Tràn Số (Numerical Overflow) trong Softmax
Khi tính hàm $\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$, nếu vector $z = [1000, 1001, 1002]$, máy tính sẽ báo lỗi Overflow do $e^{1000}$ vượt quá giới hạn biểu diễn số thực 64-bit (`inf`). Cách khắc phục chuẩn mực là gì?
- [A] Thay hàm mũ $e^z$ bằng logarit tự nhiên $\ln(z)$.
- [B] Chia toàn bộ vector $z$ cho 1000 trước khi tính.
- [C] Trừ giá trị cực đại $\max(z)$ khỏi từng phần tử: $z_i' = z_i - \max(z)$ trước khi tính $e^{z_i'}$.
- [D] Ép kiểu dữ liệu về số nguyên 32-bit.

---

### Câu 4: Cửa sổ trượt (Sliding Window) & Mạng Tích Chập 1D
Thuật toán lấy giá trị lớn nhất trong cửa sổ trượt (Sliding Window Maximum) tương đương với thao tác nào trong xử lý tín hiệu và Deep Learning?
- [A] 1D Average Pooling.
- [B] 1D Max Pooling.
- [C] Batch Normalization.
- [D] Dropout layer.

---

### Câu 5: Nghịch lý XOR và Giới hạn Tuyến tính
Tại sao một Perceptron đơn tầng với hàm kích hoạt Step function không thể học được bảng chân trị của cổng logic XOR?
- [A] Do cổng XOR có 4 mẫu dữ liệu, quá nhiều cho 1 nơ-ron.
- [B] Do không có đường thẳng đơn (hyperplane) nào trong mặt phẳng 2D có thể chia đôi 2 điểm có nhãn 1 và 2 điểm có nhãn 0 của cổng XOR (Non-linearly separable).
- [C] Do learning rate của Perceptron luôn bị phân kỳ trên các cổng logic.
- [D] Do cổng XOR yêu cầu hàm mất mát Cross-Entropy thay vì MSE.

---

<details>
<summary><b>🔍 BẢNG ĐÁP ÁN & PHÂN TÍCH BẪY NHẬN THỨC (COGNITIVE GAPS)</b></summary>

| Câu | Đáp án đúng | Lỗ hổng nhận thức thường gặp |
|:---:|:---:|:---|
| 1 | **B** | Người học hay nhầm với tích có hướng (Cross Product) hoặc nghĩ một trong hai vector phải bằng 0. |
| 2 | **A** | Hiểu sai rằng Lasso chọn lọc đặc trưng ngẫu nhiên. Thực chất là do hình học của khối cầu L1 ($L_1$-ball) tiếp xúc với đường đồng mức của hàm lỗi tại các góc nhọn trên trục. |
| 3 | **C** | Đây là kỹ thuật *Log-Sum-Exp Trick* kinh điển. Do $\frac{e^{z_i - C}}{\sum e^{z_j - C}} = \frac{e^{-C} e^{z_i}}{e^{-C} \sum e^{z_j}} = \text{Softmax}(z_i)$, kết quả toán học không đổi nhưng triệt tiêu hoàn toàn tràn số! |
| 4 | **B** | Max Pooling 1D dùng cửa sổ trượt để trích xuất tín hiệu nổi bật nhất và giảm chiều dữ liệu chuỗi thời gian hoặc âm thanh. |
| 5 | **B** | Phát hiện lịch sử của Minsky & Papert năm 1969 khiến giới nghiên cứu AI nhận ra tầm quan trọng của các tầng ẩn (Hidden Layers) phi tuyến. |

</details>
