# 🚀 Giai đoạn 5: Vòng lặp Huấn luyện Mô hình Cơ sở (Pre-training Loop)

## 1. Bản chất của Pre-training
Pre-training (Huấn luyện sơ bộ) là giai đoạn tốn kém và quan trọng nhất trong việc tạo ra một LLM:
- **Dữ liệu**: Hàng ngàn tỷ token văn bản thô không gán nhãn (Wikipedia, Sách báo, Mã nguồn Github, Web crawl).
- **Mục tiêu**: Nén toàn bộ tri thức của nhân loại vào các ma trận trọng số thông qua mục tiêu toán học duy nhất: **Dự đoán token tiếp theo**.
- **Kết quả**: Tạo ra một **Base Model** (Mô hình cơ sở). Base model chưa biết cách đóng vai trợ lý, nó chỉ biết tiếp tục hoàn thành câu một cách tự nhiên nhất theo xác suất thống kê.

---

## 2. Các kỹ thuật tối ưu hóa thiết yếu
1. **AdamW Optimizer**: Biến thể của Adam có tách biệt rõ ràng việc suy giảm trọng số (Weight Decay decoupling), giúp mô hình tổng quát hóa tốt hơn và không bị nổ trọng số.
2. **Gradient Clipping (`torch.nn.utils.clip_grad_norm_`)**: Cắt ngưỡng gradient (ví dụ: tối đa 1.0) để ngăn chặn hiện tượng Exploding Gradients khi loss đột biến.
3. **Learning Rate Scheduler**:
   - **Warmup**: Tăng dần learning rate từ 0 lên giá trị tối đa trong vài trăm bước đầu để ổn định thống kê ban đầu.
   - **Cosine Decay**: Giảm dần learning rate theo đường cong Cosine về 10% giá trị đỉnh để hội tụ mượt mà vào đáy hàm mất mát.
4. **Perplexity (Độ hỗn loạn)**:
   $$\text{PPL} = \exp(\text{Loss})$$
   Đo lường mức độ "bối rối" của mô hình khi chọn token tiếp theo. PPL càng thấp $\rightarrow$ mô hình càng tự tin và dự đoán chính xác.
