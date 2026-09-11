# 📝 Đề Thi Chẩn Đoán 05: Deep Learning & PyTorch Cơ Bản

> Thiết kế bởi **DeepTutor AI Mentor**. Đánh giá hiểu biết sâu về mạng nơ-ron, hàm kích hoạt, lan truyền ngược và PyTorch.

---

### Câu 1: Tại sao mạng nơ-ron cần Hàm Kích Hoạt Phi Tuyến (Non-linear Activation)?
Nếu tất cả các tầng trong một mạng nơ-ron 100 tầng đều chỉ sử dụng hàm kích hoạt tuyến tính $f(z) = z$, mạng đó tương đương với cái gì?
- [A] Tương đương với một mạng nơ-ron hồi quy RNN.
- [B] Tương đương với một mô hình hồi quy tuyến tính đơn tầng (Single Linear Transformation) vì tích của nhiều ma trận tuyến tính vẫn chỉ là một ma trận tuyến tính duy nhất: $W_3(W_2(W_1 x)) = W_{total} x$.
- [C] Tương đương với một Decision Tree vô hạn tầng.
- [D] Mạng sẽ bị phân kỳ vô tận khi tính Gradient Descent.

---

### Câu 2: Vấn Đề Triệt Tiêu Đạo Hàm (Vanishing Gradient)
Hàm kích hoạt Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$ có đạo hàm $\sigma'(z) = \sigma(z)(1 - \sigma(z))$ đạt giá trị cực đại là $0.25$ tại $z=0$. Khi xếp chồng nhiều tầng Sigmoid trong mạng sâu, điều gì sẽ xảy ra với gradient ở các tầng đầu tiên?
- [A] Gradient sẽ bùng nổ vượt ngưỡng số thực (Exploding Gradient).
- [B] Gradient bị suy giảm theo cấp số nhân qua quy tắc chuỗi $\prod_{l} \sigma' \le (0.25)^L \approx 0$, khiến các tầng đầu tiên hầu như không học được gì (Vanishing Gradient).
- [C] Gradient đổi dấu liên tục khiến mô hình không hội tụ.
- [D] Không có ảnh hưởng gì vì PyTorch tự động nhân đôi gradient.

---

### Câu 3: Hàm Kích Hoạt ReLU và Hiện Tượng "Dead Neurons"
Hàm $\text{ReLU}(z) = \max(0, z)$ giải quyết được triệt tiêu đạo hàm cho vùng dương (đạo hàm = 1), nhưng nhược điểm lớn nhất của nó là gì?
- [A] Thời gian tính toán quá chậm so với hàm $\tanh$.
- [B] Với các đầu vào âm ($z < 0$), đạo hàm bằng 0 hoàn toàn; nếu trọng số bị đẩy vào vùng khiến nơ-ron luôn âm với mọi mẫu dữ liệu, nơ-ron đó sẽ "chết" vĩnh viễn và không bao giờ cập nhật nữa (Dying ReLU).
- [C] Làm tràn số máy tính vì không bị chặn trên.
- [D] Không thể tính được trong PyTorch.

---

### Câu 4: Vòng Lặp Huấn Luyện PyTorch và `optimizer.zero_grad()`
Tại sao trong PyTorch, chúng ta **bắt buộc** phải gọi `optimizer.zero_grad()` ở đầu mỗi bước lặp huấn luyện trước khi gọi `loss.backward()`?
- [A] Để giải phóng bộ nhớ GPU / RAM.
- [B] Vì theo mặc định, PyTorch **tích lũy gradient** (`gradient accumulation` bằng phép cộng dồn `param.grad += ...`) ở mỗi lần gọi `.backward()`; nếu không xóa về 0, gradient của các batch trước sẽ bị cộng dồn sai lệch vào batch hiện tại.
- [C] Để chuyển tensor từ GPU về CPU.
- [D] Để tính toán lại kích thước ma trận trọng số.

---

### Câu 5: Regularization trong Deep Learning: Dropout
Trong quá trình huấn luyện với PyTorch, `nn.Dropout(p=0.2)` hoạt động như thế nào và tại sao cần gọi `model.eval()` khi suy luận?
- [A] Trong lúc Train, ngẫu nhiên tắt $20\%$ nơ-ron (đặt giá trị bằng 0) và khuếch đại các nơ-ron còn lại để ép mạng không dựa dẫm vào nơ-ron riêng lẻ; khi Test/Eval (`model.eval()`), toàn bộ nơ-ron được kích hoạt để sử dụng toàn bộ tri thức đã học.
- [B] Dropout xóa vĩnh viễn $20\%$ trọng số khỏi mô hình để nén dung lượng file `.pth`.
- [C] Dropout chỉ có tác dụng khi chạy trên CPU.
- [D] `model.eval()` làm tăng tốc độ GPU lên $20\%$.

---

<details>
<summary><b>🔍 BẢNG ĐÁP ÁN & PHÂN TÍCH BẪY NHẬN THỨC (COGNITIVE GAPS)</b></summary>

| Câu | Đáp án đúng | Lỗ hổng nhận thức thường gặp |
|:---:|:---:|:---|
| 1 | **B** | Bản chất đại số tuyến tính: Phép biến đổi tuyến tính liên tiếp chỉ là một phép biến đổi tuyến tính đơn. Tính phi tuyến (Non-linearity) mới là thứ đem lại sức mạnh xấp xỉ vạn năng (Universal Approximation Theorem). |
| 2 | **B** | Đây là lý do kiến trúc mạng nơ-ron từng bị đình trệ trong thập niên 1990 cho tới khi hàm ReLU và các kỹ thuật khởi tạo trọng số mới (He/Xavier) ra đời. |
| 3 | **B** | Để khắc phục Dying ReLU, các biến thể như Leaky ReLU ($f(x) = \max(\alpha x, x)$), Parametric ReLU (PReLU), ELU đã được phát minh. |
| 4 | **B** | Rất nhiều người mới lập trình PyTorch quên `zero_grad()`, dẫn đến gradient tăng mất kiểm soát và loss phân kỳ. |
| 5 | **A** | `model.eval()` và `model.train()` chuyển đổi trạng thái của cả `Dropout` và `BatchNorm`, đây là lỗi "silent bug" phổ biến nhất khi deploy model Deep Learning. |

</details>
