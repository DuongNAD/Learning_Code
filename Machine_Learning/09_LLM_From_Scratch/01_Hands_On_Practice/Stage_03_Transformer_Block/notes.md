# 🧱 Giai đoạn 3: Khối Transformer Block & Mạng Nơ-ron Lan truyền thẳng (MLP)

## 1. Mạng Lan truyền thẳng (Feed-Forward Network / MLP)
Sau khi cơ chế Attention giúp các token "trao đổi thông tin" với nhau qua ngữ cảnh, từng token cần một không gian để "suy ngẫm và xử lý độc lập":
$$\text{MLP}(x) = \text{GELU}(x W_1 + b_1) W_2 + b_2$$
- Kích thước mở rộng: Thông thường lớp ẩn ở giữa được mở rộng gấp **4 lần** số chiều embedding ($4 \times n_{\text{embed}}$), sau đó chiếu ngược lại về $n_{\text{embed}}$.
- Hàm kích hoạt: Thay vì ReLU (dễ gây chết nơ-ron), các LLM hiện đại dùng **GELU** (Gaussian Error Linear Unit) hoặc **SwiGLU**.

---

## 2. Kết nối Tắt (Residual / Skip Connections)
Được đề xuất bởi Kaiming He (ResNet), công thức:
$$\text{Output} = x + \text{SubLayer}(x)$$
### Ý nghĩa sinh tử đối với Deep Learning:
- Cho phép gradient chảy thẳng trực tiếp từ tầng cuối cùng về tầng đầu tiên mà không bị suy giảm theo cấp số nhân qua các ma trận trọng số.
- Cho phép xếp chồng hàng chục, hàng trăm khối Transformer Block mà không bị triệt tiêu đạo hàm (Vanishing Gradients).

---

## 3. Chuẩn hóa tầng: Pre-LayerNorm vs Post-LayerNorm
- **Post-LayerNorm** (Bài báo gốc "Attention is All You Need", 2017):
  $$x = \text{LayerNorm}(x + \text{SubLayer}(x))$$
  Rất khó hội tụ khi mô hình sâu, đòi hỏi learning rate warmup rất khắt khe.
- **Pre-LayerNorm** (Chuẩn mực của GPT-2, GPT-3, LLaMA):
  $$x = x + \text{SubLayer}(\text{LayerNorm}(x))$$
  Dòng chính (residual highway) luôn sạch sẽ, gradient chảy thông suốt, huấn luyện ổn định hơn rất nhiều.
