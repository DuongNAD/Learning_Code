# 💬 Giai đoạn 6: Tinh chỉnh có Giám sát (Supervised Fine-Tuning - SFT)

## 1. Từ Base Model thành Trợ lý AI (Assistant)
Sau khi Pre-training, mô hình chỉ đơn thuần là cỗ máy "nói leo" (tiếp tục sinh từ):
- Người dùng hỏi: *"Thủ đô của Việt Nam là gì?"*
- Base Model có thể tiếp tục: *"Thủ đô của Pháp là Paris. Thủ đô của Nhật là Tokyo..."* (vì trên internet thường có các danh sách liệt kê như vậy!).

Để biến nó thành một trợ lý ngoan ngoãn biết trả lời: *"Thủ đô của Việt Nam là Hà Nội."*, ta cần **Supervised Fine-Tuning (SFT)**.

---

## 2. Chat Template (Mẫu hội thoại)
Mỗi mô hình sử dụng các token đặc biệt (Special Tokens) để phân định vai trò:
```text
<|im_start|>system
Bạn là trợ lý AI hữu ích.<|im_end|>
<|im_start|>user
Thủ đô của Việt Nam là gì?<|im_end|>
<|im_start|>assistant
Thủ đô của Việt Nam là Hà Nội.<|im_end|>
```

---

## 3. Loss Masking (Mặt nạ Hàm mất mát)
Đây là bí quyết kỹ thuật cốt tử của SFT:
> **Chỉ tính đạo hàm trên các token do Trợ lý (Assistant) trả lời!**

- Trong hàm mất mát Cross-Entropy của PyTorch, giá trị nhãn `ignore_index = -100` sẽ bị bỏ qua hoàn toàn, không đóng góp vào hàm mất mát và không sinh gradient:
```python
targets[prompt_tokens] = -100  # Bỏ qua prompt của người dùng
targets[response_tokens] = tokens  # Chỉ phạt lỗi ở câu trả lời của trợ lý
loss = F.cross_entropy(logits, targets, ignore_index=-100)
```
Việc này ngăn mô hình lãng phí sức mạnh học cách bắt chước câu hỏi của người dùng, mà tập trung 100% vào việc sinh câu trả lời đúng chuẩn.
