"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO GIAI ĐOẠN 7 (DPO LOSS & GRPO ADVANTAGES)
Chạy bằng lệnh: python test_alignment.py
"""
import torch
import math
from exercise_alignment import compute_dpo_loss, compute_grpo_advantages

def test_dpo_loss_properties():
    # 1. Khi pi_theta giong het pi_ref (mo hinh chua hoc duoc gi):
    # chosen_ratio = 0, rejected_ratio = 0 -> logits = 0
    # sigmoid(0) = 0.5 -> loss = -ln(0.5) = ln(2) ~ 0.6931
    pi_w = torch.tensor([-1.5, -2.0])
    pi_l = torch.tensor([-3.0, -3.5])
    ref_w = pi_w.clone()
    ref_l = pi_l.clone()
    
    loss_baseline = compute_dpo_loss(pi_w, pi_l, ref_w, ref_l)
    assert abs(loss_baseline.item() - math.log(2.0)) < 1e-4, f"Loss baseline khong bang ln(2)! {loss_baseline.item()}"
    print(f"[PASS] Test DPO Baseline: Loss = {loss_baseline.item():.4f} (~ ln(2) = 0.6931) chinh xac!")

    # 2. Khi policy hoc tot hon: xac suat chosen tang len, rejected giam di -> Loss phai giam
    pi_w_better = pi_w + 0.5
    pi_l_better = pi_l - 0.5
    loss_better = compute_dpo_loss(pi_w_better, pi_l_better, ref_w, ref_l)
    assert loss_better < loss_baseline, f"Loss khong giam khi policy tot hon! {loss_better} vs {loss_baseline}"
    print(f"[PASS] Test DPO Optimization: Khi policy uu tien chosen hon rejected, Loss giam xuong {loss_better.item():.4f}!")

def test_grpo_normalization():
    # Batch=2, Group size G=4
    rewards = torch.tensor([
        [10.0, 20.0, 30.0, 40.0],
        [5.0, 5.0, 5.0, 5.0]
    ])
    adv = compute_grpo_advantages(rewards)
    assert adv.shape == rewards.shape, f"Shape advantages sai! {adv.shape}"
    
    # Hang 1: Mean phai bang 0
    assert abs(adv[0].mean().item()) < 1e-5, f"Mean cua advantages hang 1 khong bang 0! {adv[0].mean()}"
    # Hang 1: Std phai bang 1
    assert abs(adv[0].std().item() - 1.0) < 1e-3, f"Std cua advantages hang 1 khong bang 1! {adv[0].std()}"
    print("[PASS] Test GRPO: Advantages duoc chuan hoa Zero-Mean Unit-Variance chuan xac!")

if __name__ == "__main__":
    print("=" * 50)
    print("BAT DAU KIEM TRA GIAI DOAN 7...")
    test_dpo_loss_properties()
    test_grpo_normalization()
    print("CHUC MUNG! BAN DA HOAN THANH GIAI DOAN 7.")
    print("=" * 50)
