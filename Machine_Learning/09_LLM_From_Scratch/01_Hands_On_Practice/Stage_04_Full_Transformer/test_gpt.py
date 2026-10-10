"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO GIAI ĐOẠN 4 (FULL MINIGPT ARCHITECTURE & GENERATION)
Chạy bằng lệnh: python test_gpt.py
"""
import torch
import math
from exercise_gpt import MiniGPT

def test_model_forward_and_loss():
    vocab_size = 50
    n_embed = 32
    context_length = 16
    model = MiniGPT(vocab_size=vocab_size, n_embed=n_embed, context_length=context_length, n_head=4, n_layer=2)
    
    B, T = 2, 8
    x = torch.randint(0, vocab_size, (B, T))
    y = torch.randint(0, vocab_size, (B, T))
    
    logits, loss = model(x, y)
    assert logits.shape == (B, T, vocab_size), f"Logits shape sai! {logits.shape}"
    assert loss is not None, "Loss tra ve None khi co target y!"
    
    # Loss khoi tao ly thuyet gan bang -ln(1 / vocab_size)
    expected_initial_loss = math.log(vocab_size)
    print(f"[INFO] Khoi tao Loss: {loss.item():.4f} (Ly thuyet: ~{expected_initial_loss:.4f})")
    assert abs(loss.item() - expected_initial_loss) < 1.5, "Loss khoi tao bat thuong! Co the do loi khoi tao trong so."
    print("[PASS] Test Forward & Loss: Logits va Cross-Entropy Loss hoat dong hoan hao!")

def test_generation():
    vocab_size = 50
    model = MiniGPT(vocab_size=vocab_size, n_embed=32, context_length=16, n_head=4, n_layer=2)
    
    prompt = torch.tensor([[1, 2, 3]], dtype=torch.long)
    new_tokens = 5
    out = model.generate(prompt, max_new_tokens=new_tokens, temperature=0.8, top_k=10)
    
    assert out.shape == (1, 3 + new_tokens), f"Do dai chuoi sinh sai! {out.shape}"
    assert (out[:, :3] == prompt).all(), "Prompt ban dau bi thay doi trong qua trinh sinh!"
    print("[PASS] Test Generation: Sinh text tu hoi quy token-by-token thanh cong!")

if __name__ == "__main__":
    print("=" * 50)
    print("BAT DAU KIEM TRA GIAI DOAN 4...")
    test_model_forward_and_loss()
    test_generation()
    print("CHUC MUNG! BAN DA HOAN THANH GIAI DOAN 4.")
    print("=" * 50)
