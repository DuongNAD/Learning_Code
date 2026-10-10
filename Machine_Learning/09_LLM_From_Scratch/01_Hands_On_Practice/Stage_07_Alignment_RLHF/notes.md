# ⚖️ Giai đoạn 7: Căn chỉnh Mô hình (Alignment: Reward Modeling, DPO & GRPO)

## 1. Tại sao SFT là chưa đủ?
SFT chỉ dạy mô hình bắt chước văn bản tốt. Nhưng trong thực tế:
- Có nhiều câu trả lời khác nhau cùng đúng nhưng độ hữu ích, an toàn khác nhau.
- Mô hình có thể sinh ra thông tin nguy hiểm (hướng dẫn tạo mã độc, phân biệt đối xử) hoặc bị ảo giác (hallucination).
- Cần một cơ chế để **thưởng** cho hành vi tốt và **phạt** hành vi xấu.

---

## 2. Toàn cảnh các phương pháp Căn chỉnh (Alignment Taxonomy)

### 1. RLHF cổ điển (Reinforcement Learning from Human Feedback - OpenAI InstructGPT):
1. Huấn luyện **Reward Model** trên các cặp dữ liệu con người đánh giá: $y_w$ (Chosen/Win) tốt hơn $y_l$ (Rejected/Lose).
   $$\mathcal{L}_{\text{RM}} = -\log \sigma(r(x, y_w) - r(x, y_l))$$
2. Dùng thuật toán **PPO (Proximal Policy Optimization)** để huấn luyện Policy, kèm hàm phạt KL Divergence để mô hình không đi quá xa khỏi mô hình gốc.
*Nhược điểm*: Rất phức tạp, cần duy trì 4 mô hình đồng thời trong VRAM (Actor, Critic/Value, Reference, Reward).

### 2. DPO (Direct Preference Optimization - Stanford, 2023):
Đột phá toán học chứng minh rằng bài toán tối ưu có thưởng có thể được giải trực tiếp trên chính Policy mà **không cần Reward Model độc lập và không cần vòng lặp RL**:
$$\mathcal{L}_{\text{DPO}}(\theta; \pi_{\text{ref}}) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]$$
- $\beta$: Siêu tham số kiểm soát mức độ ràng buộc với mô hình tham chiếu $\pi_{\text{ref}}$ (thường từ 0.1 đến 0.5).

### 3. GRPO (Group Relative Policy Optimization - DeepSeek-R1, 2025):
Phương pháp căn chỉnh suy luận tăng cường (Reasoning RL) mới nhất:
- Thay vì dùng mạng Critic đồ sộ để ước lượng Advantage, với mỗi câu hỏi $x$, ta lấy mẫu một nhóm $G$ câu trả lời: $\{y_1, y_2, \dots, y_G\}$.
- Chấm điểm từng câu (dựa trên bộ kiểm tra quy tắc: ví dụ kết quả toán học đúng/sai, format code).
- Chuẩn hóa điểm thưởng trong nhóm (Mean = 0, Std = 1) để làm **Advantage**:
  $$A_i = \frac{r_i - \text{mean}(r)}{\text{std}(r) + \epsilon}$$
- Cực kỳ tiết kiệm VRAM và mở đường cho các mô hình suy luận sâu như DeepSeek-R1!
