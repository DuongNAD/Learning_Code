"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO GIAI ĐOẠN 1 (TOKENIZER & DATALOADER)
Chạy bằng lệnh: python test_data.py
"""
import torch
import sys
from exercise_data import SimpleCharTokenizer, get_batch

def test_tokenizer():
    corpus = "abcdefghijklmnopqrstuvwxyz 0123456789"
    tok = SimpleCharTokenizer(corpus)
    assert tok.vocab_size == len(set(corpus)), "Vocab size khong khop voi so ky tu duy nhat!"
    
    test_phrase = "hello 2026"
    encoded = tok.encode(test_phrase)
    decoded = tok.decode(encoded)
    assert decoded == test_phrase, f"Decode khong khop! Goc: '{test_phrase}', Nhan duoc: '{decoded}'"
    print("[PASS] Test Tokenizer: Encode va Decode hoat dong chinh xac 100%!")

def test_dataloader_batch():
    dummy_data = torch.arange(100, dtype=torch.long)
    B, T = 4, 8
    x, y = get_batch(dummy_data, batch_size=B, block_size=T)
    
    assert x.shape == (B, T), f"Shape x sai! Mong doi: {(B, T)}, Nhan duoc: {x.shape}"
    assert y.shape == (B, T), f"Shape y sai! Mong doi: {(B, T)}, Nhan duoc: {y.shape}"
    
    # Kiem tra tinh chat Next-token prediction: y phai dich dung 1 buoc so voi x
    for b in range(B):
        for t in range(T):
            assert y[b, t].item() == x[b, t].item() + 1, (
                f"Vi tri b={b}, t={t} khong dich 1 token! x={x[b, t]}, y={y[b, t]}"
            )
    print("[PASS] Test DataLoader: Tensor x va nhan dich 1 token y chinh xac!")

if __name__ == "__main__":
    print("=" * 50)
    print("BAT DAU KIEM TRA GIAI DOAN 1...")
    test_tokenizer()
    test_dataloader_batch()
    print("CHUC MUNG! BAN DA HOAN THANH GIAI DOAN 1.")
    print("=" * 50)
