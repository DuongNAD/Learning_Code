# 🧠 Giai đoạn 2: Cơ chế Tự chú ý (Self-Attention & Multi-Head Attention)

## 1. Trực giác về Query (Q), Key (K), Value (V)
Cơ chế Attention trong Transformer giống như một hệ thống tra cứu cơ sở dữ liệu mềm (Soft Retrieval):
- **Query ($Q$)**: *"Tôi là token hiện tại, tôi đang tìm kiếm thông tin gì?"*
- **Key ($K$)**: *"Tôi là token trong ngữ cảnh, tôi có thông tin gì để chào mời?"*
- **Value ($V$)**: *"Nội dung thực sự của thông tin mà tôi mang theo là gì?"*

Khi $Q$ và $K$ khớp nhau (tích vô hướng $Q \cdot K^T$ cao), mô hình sẽ tập trung trọng số lớn để lấy thông tin từ $V$.

---

## 2. Công thức Scaled Dot-Product Attention
$$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}} + M\right) V$$

### Tại sao phải chia cho $\sqrt{d_k}$ (Scaling factor)?
Khi số chiều $d_k$ (head_size) lớn, tích vô hướng $Q \cdot K^T$ sẽ có phương sai tăng tỷ lệ thuận với $d_k$.
Nếu giá trị đầu vào của Softmax quá lớn, hàm Softmax sẽ bị bão hòa (vùng gradient cực nhỏ $\approx 0$), dẫn đến hiện tượng **Triệt tiêu đạo hàm (Vanishing Gradient)**. Việc chia cho $\sqrt{d_k}$ giữ cho phương sai luôn bằng 1.

---

## 3. Causal Masking (Mặt nạ nhân quả)
Trong mô hình sinh văn bản tự hồi quy (GPT), một token tại thời điểm $t$ **tuyệt đối không được phép nhìn thấy** các token tương lai $t+1, t+2, ...$.
Ta sử dụng một ma trận tam giác dưới (`torch.tril`):
$$M_{ij} = \begin{cases} 0 & \text{nếu } i \ge j \text{ (quá khứ và hiện tại)} \\ -\infty & \text{nếu } i < j \text{ (tương lai)} \end{cases}$$
Khi áp dụng $\text{Softmax}(-\infty)$, xác suất chú ý tới tương lai sẽ bằng $e^{-\infty} = 0$.

---

## 4. Multi-Head Attention (Đa đầu chú ý)
Thay vì chỉ có 1 góc nhìn chú ý duy nhất, Multi-Head Attention chia không gian biểu diễn thành $h$ đầu độc lập:
- Đầu 1 có thể học mối quan hệ ngữ pháp (chủ ngữ - vị ngữ).
- Đầu 2 có thể học mối quan hệ đại từ thay thế ("anh ấy" ám chỉ "Nam").
- Đầu 3 có thể học mối liên hệ thời gian hoặc không gian.
Sau đó nối ($Concat$) kết quả của $h$ đầu lại và chiếu qua 1 ma trận tuyến tính cuối cùng $W_O$.
