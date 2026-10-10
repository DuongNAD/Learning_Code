# 🤖 Giai đoạn 4: Kiến trúc LLM Hoàn Chỉnh (MiniGPT) & Sinh Văn Bản

## 1. Bản đồ Kiến trúc LLM Toàn Diện
Một mô hình ngôn ngữ hoàn chỉnh (như GPT-2 / MiniGPT) gồm 4 thành phần chính:
```
Token IDs: (B, T)
    │
    ├── Token Embedding (vocab_size -> n_embed)
    └── Position Embedding (context_length -> n_embed)
    │
    ▼ (Cộng Embeddings)
(B, T, n_embed)
    │
    ▼
[ Transformer Block 1 ]
    │
    ▼
[ Transformer Block 2 ]
    │
    ...
    ▼
[ Transformer Block N ]
    │
    ▼
LayerNorm (n_embed)
    │
    ▼
LM Head (Linear: n_embed -> vocab_size)
    │
    ▼
Logits: (B, T, vocab_size)
```

---

## 2. Hàm Mất Mát (Loss Function)
Để huấn luyện mô hình dự đoán token tiếp theo, ta dùng **Cross-Entropy Loss**:
$$\mathcal{L} = -\sum_{i} \log P(y_i \mid x_{\le i})$$
Trong PyTorch, ta làm phẳng (flatten) tensor:
- `logits`: `(B * T, vocab_size)`
- `targets`: `(B * T)`
- `loss = F.cross_entropy(logits, targets)`

---

## 3. Chiến lược Sinh Văn Bản (Autoregressive Generation)
Trong quá trình suy luận (Inference), mô hình sinh từng token một:
1. Đưa chuỗi prompt ban đầu `idx` (độ dài $T$) vào mô hình.
2. Lấy logits của token cuối cùng $t = -1$: `logits[:, -1, :]`.
3. Áp dụng kỹ thuật điều chỉnh:
   - **Temperature ($T$)**: `logits = logits / temperature`. (Nhiệt độ thấp $\rightarrow$ câu trả lời chắc chắn, lặp; nhiệt độ cao $\rightarrow$ sáng tạo, đa dạng).
   - **Top-K Filtering**: Giữ lại $K$ token có xác suất cao nhất, gán $-\infty$ cho các token còn lại.
4. Lấy mẫu từ phân phối xác suất: `probs = F.softmax(logits, dim=-1)`, sau đó dùng `torch.multinomial(probs, num_samples=1)`.
5. Ghép token mới vào chuỗi `idx = torch.cat((idx, next_token), dim=1)` và lặp lại.
