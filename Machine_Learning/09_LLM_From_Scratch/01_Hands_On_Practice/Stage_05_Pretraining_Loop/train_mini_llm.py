"""
KỊCH BẢN THỰC CHIẾN HUẤN LUYỆN MINIGPT TỪ ĐẦU (END-TO-END PRE-TRAINING)

Tự động nhận diện GPU (NVIDIA RTX 5060 Ti) hoặc CPU.
Chạy huấn luyện một mô hình ngôn ngữ tí hon trên một ngữ liệu mẫu.
Quan sát trực quan:
- Loss giảm dần từ ~4.0 xuống < 1.0
- Sinh văn bản trước khi train (vô nghĩa ngẫu nhiên) và sau khi train (có cấu trúc từ ngữ).
"""
import torch
import torch.nn as nn
import sys
import os
import time

# Đường dẫn import các module thực hành từ các Stage trước
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "Stage_01_Tokenizer_Data"))
sys.path.append(os.path.join(BASE_DIR, "Stage_04_Full_Transformer"))

from exercise_data import SimpleCharTokenizer, get_batch
from exercise_gpt import MiniGPT

# 1. Dữ liệu ngữ liệu mẫu (Tin học & Trí tuệ nhân tạo)
CORPUS = """
Tri tue nhan tao la mot linh vuc khoa hoc may tinh nham tao ra cac he thong thong minh.
Mo hinh ngon ngu lon hay con goi la LLM duoc xay dung dua tren kien truc Transformer.
Kien truc Transformer gom co co che tu chu y self-attention va mang lan truyen thang feed-forward.
Cac khoi transformer block duoc xep chong len nhau voi ket noi tat residual connection.
Khi huan luyen mo hinh ngon ngu, chung ta su dung ham mat mat cross-entropy loss de du doan token tiep theo.
Sau khi pre-training xong tren van ban tho, mo hinh tro thanh mot base model co kha nang sinh van ban.
Sau do chung ta ap dung SFT de bien mo hinh thanh tro ly ao thong minh biet tra loi cau hoi.
Cuoi cung, chung ta can chinh mo hinh bang DPO, PPO hoac GRPO de mo hinh an toan va huu ich hon.
""" * 10  # Lặp lại để có đủ ngữ cảnh huấn luyện

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[*] Thiet bi huan luyen: {device.upper()}")
    if device == "cuda":
        print(f"[*] GPU Name: {torch.cuda.get_device_name(0)}")

    # 2. Tokenizer & Dữ liệu
    tokenizer = SimpleCharTokenizer(CORPUS)
    data = torch.tensor(tokenizer.encode(CORPUS), dtype=torch.long)
    print(f"[*] Kich thuoc tap du lieu: {len(data)} tokens")
    print(f"[*] Kich thuoc tu vung: {tokenizer.vocab_size} ky tu")

    # 3. Khoi tao mo hinh MiniGPT
    n_embed = 64
    context_length = 32
    n_head = 4
    n_layer = 4
    batch_size = 16
    max_iters = 300
    learning_rate = 1e-3

    model = MiniGPT(
        vocab_size=tokenizer.vocab_size,
        n_embed=n_embed,
        context_length=context_length,
        n_head=n_head,
        n_layer=n_layer
    ).to(device)

    total_params = sum(p.numel() for p in model.parameters())
    print(f"[*] Tong so tham so mo hinh: {total_params:,} parameters")

    # 4. Sinh van ban truoc khi train
    print("\n" + "=" * 60)
    print("--- VAN BAN SINH RA TRUOC KHI TRAIN (NGONG NGAU NHIEN) ---")
    prompt = "Tri tue"
    prompt_idx = torch.tensor([tokenizer.encode(prompt)], dtype=torch.long, device=device)
    raw_gen = model.generate(prompt_idx, max_new_tokens=40, temperature=0.8)
    print(tokenizer.decode(raw_gen[0].tolist()))
    print("=" * 60 + "\n")

    # 5. Vong lap huan luyen (Training Loop)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=1e-2)
    start_time = time.time()
    
    print("[*] Bat dau qua trinh huan luyen...")
    for iter_step in range(max_iters + 1):
        # Lay batch du lieu
        xb, yb = get_batch(data, batch_size=batch_size, block_size=context_length, device=device)

        # Forward pass
        logits, loss = model(xb, yb)

        # Backward pass & Optimizer step
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        # Gradient clipping ngan chan exploding gradients
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        if iter_step % 50 == 0:
            elapsed = time.time() - start_time
            print(f"Step {iter_step:3d}/{max_iters} | Loss: {loss.item():.4f} | Perplexity: {torch.exp(loss).item():.2f} | Time: {elapsed:.2f}s")

    # 6. Sinh van ban sau khi train
    print("\n" + "=" * 60)
    print("--- VAN BAN SINH RA SAU KHI TRAIN (DA HOC DUOC MAU CAU) ---")
    for test_prompt in ["Tri tue", "Kien truc", "Mo hinh"]:
        p_idx = torch.tensor([tokenizer.encode(test_prompt)], dtype=torch.long, device=device)
        trained_gen = model.generate(p_idx, max_new_tokens=50, temperature=0.7)
        print(f"Prompt: '{test_prompt}' -> Sinh ra:")
        print(tokenizer.decode(trained_gen[0].tolist()))
        print("-" * 40)
    print("=" * 60)

    # 7. Luu Checkpoint
    checkpoint_path = os.path.join(os.path.dirname(__file__), "mini_llm_checkpoint.pt")
    torch.save({
        'model_state_dict': model.state_dict(),
        'vocab_size': tokenizer.vocab_size,
        'chars': tokenizer.chars,
    }, checkpoint_path)
    print(f"\n[OK] Da luu checkpoint mo hinh tai: {checkpoint_path}")

if __name__ == "__main__":
    main()
