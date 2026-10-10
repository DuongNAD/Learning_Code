"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO GIAI ĐOẠN 6 (SFT LOSS MASKING)
Chạy bằng lệnh: python test_sft.py
"""
import torch
from exercise_sft import create_sft_labels, compute_sft_loss

def test_sft_loss_masking():
    seq_len = 10
    prompt_len = 4
    vocab_size = 20
    
    input_ids = torch.arange(seq_len)
    targets = create_sft_labels(input_ids, prompt_len)
    
    # 1. Kiem tra phan prompt phai bi gan -100
    assert (targets[:prompt_len] == -100).all(), "Prompt tokens chua duoc gan bang -100!"
    # 2. Kiem tra phan response phai giu nguyen
    assert (targets[prompt_len:] == input_ids[prompt_len:]).all(), "Response tokens bi thay doi sai lech!"
    
    # 3. Kiem tra gradient: Doi voi phan bi mask (-100), thay doi gia tri logits tai do KHONG duoc phep lam thay doi loss!
    B, T = 1, seq_len
    logits = torch.randn(B, T, vocab_size, requires_grad=True)
    batch_targets = targets.unsqueeze(0)
    
    loss = compute_sft_loss(logits, batch_targets)
    loss.backward()
    
    # Gradient tai cac buoc cua prompt phai bang 0
    # Chu y: shift_targets bat dau tu index 1, vi vay token 0 va cac token truoc prompt_len se co target=-100
    prompt_grad_sum = logits.grad[:, :prompt_len - 1, :].abs().sum().item()
    response_grad_sum = logits.grad[:, prompt_len:, :].abs().sum().item()
    
    assert prompt_grad_sum == 0.0, f"Prompt tokens van sinh gradient ({prompt_grad_sum})! Masking bi loi."
    assert response_grad_sum > 0.0, "Response tokens khong sinh gradient!"
    print("[PASS] Test SFT Masking: Cac token thuoc Prompt co gradient bang 0 tuyet doi, chi response sinh gradient!")

if __name__ == "__main__":
    print("=" * 50)
    print("BAT DAU KIEM TRA GIAI DOAN 6...")
    test_sft_loss_masking()
    print("CHUC MUNG! BAN DA HOAN THANH GIAI DOAN 6.")
    print("=" * 50)
