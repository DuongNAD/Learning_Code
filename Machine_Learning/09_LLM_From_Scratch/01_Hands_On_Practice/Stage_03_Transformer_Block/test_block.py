"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO GIAI ĐOẠN 3 (TRANSFORMER BLOCK & RESIDUAL GRADIENTS)
Chạy bằng lệnh: python test_block.py
"""
import torch
from exercise_block import MLP, TransformerBlock

def test_mlp_expansion():
    C = 16
    mlp = MLP(C)
    x = torch.randn(2, 4, C)
    out = mlp(x)
    assert out.shape == (2, 4, C), f"MLP output shape sai! {out.shape}"
    print("[PASS] Test MLP: Mo rong 4x va chieu nguoc thanh cong!")

def test_block_gradients():
    B, T, C = 2, 5, 32
    block = TransformerBlock(n_head=4, n_embed=C, context_length=8)
    x = torch.randn(B, T, C, requires_grad=True)
    out = block(x)
    
    assert out.shape == (B, T, C), f"Block output shape sai! {out.shape}"
    
    # Kiem tra dong gradient chay qua Residual connections
    loss = out.sum()
    loss.backward()
    
    assert x.grad is not None, "Gradient khong truyen nguoc ve duoc x!"
    assert not torch.isnan(x.grad).any(), "Gradient chua gia tri NaN!"
    assert x.grad.abs().sum().item() > 0, "Gradient bi triet tieu hoan toan (Zero gradient)!"
    print("[PASS] Test Block: Gradient lan truyen nguoc qua Residual Highway hoan hao!")

if __name__ == "__main__":
    print("=" * 50)
    print("BAT DAU KIEM TRA GIAI DOAN 3...")
    test_mlp_expansion()
    test_block_gradients()
    print("CHUC MUNG! BAN DA HOAN THANH GIAI DOAN 3.")
    print("=" * 50)
