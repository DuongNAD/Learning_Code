# 🗺️ Lộ Trình Học & Tự Làm: Xây Dựng LLM Từ Đầu Đến Đuôi (7 Chặng)

Lộ trình này được thiết kế theo tư duy **First Principles (Nguyên lý đầu tiên)**: Mỗi khái niệm toán học đều tương ứng với một khối mã nguồn Python/PyTorch cụ thể mà bạn sẽ tự tay gõ và kiểm thử.

---

## 📌 Chặng 1: Tokenizer & Đường ống Dữ liệu (Data Pipeline)
- [ ] **Lý thuyết**: Hiểu sự khác biệt giữa Character-level, Word-level và Subword BPE (Byte-Pair Encoding).
- [ ] **Toán học & Cấu trúc**: Khái niệm Context Length $T$, Batch Size $B$, và nguyên lý Next-Token Prediction ($Y$ dịch 1 vị trí so với $X$).
- [ ] **Thực hành**:
  - Hoàn thiện [exercise_data.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_01_Tokenizer_Data/exercise_data.py)
  - Chạy xác thực bằng [test_data.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_01_Tokenizer_Data/test_data.py)
- [ ] **Tiêu chí hoàn thành (DoD)**: `test_data.py` báo PASS 100%.

---

## 📌 Chặng 2: Trái Tim Của LLM - Cơ Chế Tự Chú Ý (Attention Mechanisms)
- [ ] **Lý thuyết**: Bản chất của Query $Q$, Key $K$, Value $V$. Tại sao phải chia tỷ lệ $\sqrt{d_k}$?
- [ ] **Toán học**:
  $$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right)V$$
- [ ] **Kỹ thuật Causal Mask**: Tại sao ma trận tam giác dưới `torch.tril` ngăn chặn việc nhìn trộm tương lai?
- [ ] **Thực hành**:
  - Tự dựng `Head` và `MultiHeadAttention` trong [exercise_attention.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_02_Attention/exercise_attention.py)
  - Chạy xác thực bằng [test_attention.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_02_Attention/test_attention.py)
- [ ] **Tiêu chí hoàn thành (DoD)**: Gradient kiểm tra tính nhân quả không bị rò rỉ.

---

## 📌 Chặng 3: Khối Transformer Block & Mạng MLP
- [ ] **Lý thuyết**:
  - Sự khác biệt sinh tử giữa Pre-LayerNorm và Post-LayerNorm.
  - Tại sao MLP mở rộng $4 \times d_{\text{model}}$ và dùng GELU/SwiGLU thay vì ReLU?
- [ ] **Toán học**:
  $$x = x + \text{Attention}(\text{LN}_1(x))$$
  $$x = x + \text{MLP}(\text{LN}_2(x))$$
- [ ] **Thực hành**:
  - Hoàn thiện [exercise_block.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_03_Transformer_Block/exercise_block.py)
  - Chạy xác thực bằng [test_block.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_03_Transformer_Block/test_block.py)
- [ ] **Tiêu chí hoàn thành (DoD)**: Gradient chảy thông suốt qua Residual Highway không bị NaN.

---

## 📌 Chặng 4: Ghép Toàn Bộ Mô Hình GPT & Thuật Toán Sinh Text
- [ ] **Lý thuyết**:
  - Token Embeddings kết hợp Positional Embeddings.
  - Chiếu LM Head từ $n_{\text{embed}} \rightarrow \text{vocab\_size}$.
  - Giải mã tự hồi quy: Temperature Scaling, Top-K Sampling, Greedy Decoding.
- [ ] **Thực hành**:
  - Hoàn thiện lớp `MiniGPT` trong [exercise_gpt.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_04_Full_Transformer/exercise_gpt.py)
  - Chạy xác thực bằng [test_gpt.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_04_Full_Transformer/test_gpt.py)
- [ ] **Tiêu chí hoàn thành (DoD)**: Mô hình sinh chuỗi token mới mà không làm hỏng prompt ban đầu.

---

## 📌 Chặng 5: Huấn Luyện Mô Hình Cơ Sở (Pre-training)
- [ ] **Lý thuyết**: Vòng lặp tối ưu hóa, AdamW, Cosine Learning Rate Schedule, Gradient Clipping.
- [ ] **Thực hành**:
  - Chạy [train_mini_llm.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_05_Pretraining_Loop/train_mini_llm.py) trên GPU RTX 5060 Ti.
  - Quan sát Loss giảm từ $\sim 4.0$ xuống $< 0.8$ và Perplexity giảm mạnh.
- [ ] **Tiêu chí hoàn thành (DoD)**: Lưu thành công file checkpoint mô hình `mini_llm_checkpoint.pt`.

---

## 📌 Chặng 6: Tinh chỉnh Có Giám Sát (Supervised Fine-Tuning - SFT)
- [ ] **Lý thuyết**: Chuyển đổi từ "máy nói leo" (Base Model) sang "trợ lý đàm thoại" (Instruction-following Assistant).
- [ ] **Kỹ thuật Cốt lõi**:
  - Chat Template phân vai (`<|im_start|>user`, `<|im_start|>assistant`).
  - Label Masking: Gán nhãn `-100` cho phần prompt người dùng để mô hình chỉ học câu trả lời của trợ lý.
- [ ] **Thực hành**:
  - Hoàn thiện [exercise_sft.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_06_Supervised_FineTuning/exercise_sft.py)
  - Chạy xác thực bằng [test_sft.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_06_Supervised_FineTuning/test_sft.py)
- [ ] **Tiêu chí hoàn thành (DoD)**: Gradient tại các token thuộc phần prompt bằng chính xác 0.0.

---

## 📌 Chặng 7: Căn Chỉnh Nâng Cao (Alignment: Reward Modeling, DPO & GRPO)
- [ ] **Lý thuyết**:
  - Mô hình thưởng Bradley-Terry ($y_{\text{chosen}} \succ y_{\text{rejected}}$).
  - Thuật toán DPO (Direct Preference Optimization): Giải bài toán tối ưu trực tiếp mà không cần vòng lặp RL.
  - Thuật toán GRPO (Group Relative Policy Optimization): Bí quyết căn chỉnh mô hình suy luận của DeepSeek-R1.
- [ ] **Thực hành**:
  - Hoàn thiện [exercise_alignment.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_07_Alignment_RLHF/exercise_alignment.py)
  - Chạy xác thực bằng [test_alignment.py](file:///D:/02_Learning_Knowledge/Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_07_Alignment_RLHF/test_alignment.py)
- [ ] **Tiêu chí hoàn thành (DoD)**: Baseline Loss bằng $\ln(2) \approx 0.6931$ và Advantages chuẩn hóa đúng Zero-Mean Unit-Variance.
