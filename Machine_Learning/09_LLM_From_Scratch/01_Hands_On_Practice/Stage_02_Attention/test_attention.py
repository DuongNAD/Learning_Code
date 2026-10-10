"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO GIAI ĐOẠN 2 (SELF-ATTENTION & MULTI-HEAD ATTENTION)
Chạy bằng lệnh: python test_attention.py
"""
import torch
import math
from exercise_attention import Head, MultiHeadAttention

def test_head_shape_and_causality():
    B, T, C = 2, 6, 16
    head_size = 8
    context_len = 10
    head = Head(head_size, C, context_len)
    x = torch.randn(B, T, C)
    out = head(x)
    
    assert out.shape == (B, T, head_size), f"Shape sai! Mong doi {(B, T, head_size)}, nhan duoc {out.shape}"
    
    # Kiem tra causal mask: Token tai t=0 KHONG the phu thuoc vao thay doi cua token tai t=1
    x1 = x.clone()
    x2 = x.clone()
    x2[:, 1:, :] = torch.randn_like(x2[:, 1:, :]) # Thay doi tat ca token tu vi tri 1 tro di
    
    out1 = head(x1)
    out2 = head(x2)
    
    # Output tai vi tri t=0 phai GIONG NHAU HOAN TOAN giua out1 va out2 vi t=0 khong duoc phep nhin tuong lai
    diff_t0 = (out1[:, 0, :] - out2[:, 0, :]).abs().max().item()
    assert diff_t0 < 1e-6, f"Vi pham Causal Mask! Token tai t=0 da bi anh huong boi token tuong lai (diff: {diff_t0})"
    print("[PASS] Test Head: Shape dung va Causal Masking ngan chan ro ri tuong lai tuyet doi!")

def test_multi_head_attention():
    B, T, C = 3, 5, 32
    n_head = 4
    mha = MultiHeadAttention(n_head=n_head, n_embed=C, context_length=8)
    x = torch.randn(B, T, C)
    out = mha(x)
    assert out.shape == (B, T, C), f"MHA shape sai! Mong doi {(B, T, C)}, nhan duoc {out.shape}"
    print("[PASS] Test MHA: MultiHeadAttention xu ly gop cac heads va chieu tuyen tinh thanh cong!")

if __name__ == "__main__":
    print("=" * 50)
    print("BAT DAU KIEM TRA GIAI DOAN 2...")
    test_head_shape_and_causality()
    test_multi_head_attention()
    print("CHUC MUNG! BAN DA HOAN THANH GIAI DOAN 2.")
    print("=" * 50)
