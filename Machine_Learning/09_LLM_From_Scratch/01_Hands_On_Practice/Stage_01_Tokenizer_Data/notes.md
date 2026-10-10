# 📚 Giai đoạn 1: Tokenizer & Chuẩn bị Dữ liệu Huấn luyện (Data Pipeline)

## 1. Bản chất cốt lõi của Tokenizer
Mô hình ngôn ngữ (LLM) không thể hiểu trực tiếp các ký tự hay văn bản dạng chuỗi (string). Chúng chỉ có thể tính toán trên các ma trận số.
Nhiệm vụ của **Tokenizer** là cầu nối:
$$\text{"Xin chào thế giới"} \xrightarrow{\text{Encode}} [1250, 489, 7820] \xrightarrow{\text{Decode}} \text{"Xin chào thế giới"}$$

### Các cấp độ Tokenizer:
1. **Character-level (Cấp độ ký tự)**: Mỗi ký tự là 1 token (Từ vựng nhỏ: 100-256 tokens). Nhược điểm: Chuỗi token rất dài, mô hình khó học ngữ nghĩa dài.
2. **Word-level (Cấp độ từ)**: Mỗi từ là 1 token. Nhược điểm: Từ vựng khổng lồ (>100,000 từ), gặp lỗi OOV (Out-of-Vocabulary) khi gặp từ mới.
3. **Subword-level (Cấp độ âm tiết - BPE/WordPiece/SentencePiece)**: Tiêu chuẩn của GPT-4, LLaMA, DeepSeek. Ghép các byte/ký tự thường gặp thành cụm từ. Vừa kiểm soát kích thước từ vựng (32k - 128k), vừa không bao giờ bị OOV.

---

## 2. Sliding Window & Cặp Dữ liệu Huấn luyện $(X, Y)$
Trong bài toán huấn luyện mô hình ngôn ngữ tự hồi quy (Autoregressive Language Modeling), mục tiêu duy nhất là:
> **Dự đoán token tiếp theo (Next-Token Prediction)** dựa trên toàn bộ các token đã xuất hiện phía trước.

Nếu chuỗi token là: `[T_0, T_1, T_2, T_3, T_4]`
Với độ dài ngữ cảnh (`context_length = 4`):
- Đầu vào $X$: `[T_0, T_1, T_2, T_3]`
- Nhãn mục tiêu $Y$: `[T_1, T_2, T_3, T_4]` (dịch chuyển sang phải 1 bước)

Trong 1 khối dữ liệu đơn lẻ $(X, Y)$, ta đồng thời huấn luyện mô hình 4 ví dụ học:
- Khi thấy `[T_0]` $\rightarrow$ dự đoán `T_1`
- Khi thấy `[T_0, T_1]` $\rightarrow$ dự đoán `T_2`
- Khi thấy `[T_0, T_1, T_2]` $\rightarrow$ dự đoán `T_3`
- Khi thấy `[T_0, T_1, T_2, T_3]` $\rightarrow$ dự đoán `T_4`

---

## 3. Cấu trúc Tensor đầu vào
- $X \in \mathbb{R}^{B \times T}$: Batch các chuỗi token đầu vào.
- $Y \in \mathbb{R}^{B \times T}$: Batch các token nhãn mục tiêu cần dự đoán.
Trong đó:
- $B$ (Batch Size): Số lượng câu/đoạn văn bản xử lý song song trong 1 lượt.
- $T$ (Context Length / Block Size): Số lượng token tối đa trong 1 đoạn ngữ cảnh.
