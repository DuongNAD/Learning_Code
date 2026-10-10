"""
BÀI TẬP THỰC HÀNH GIAI ĐOẠN 7: TỰ CÀI ĐẶT CÔNG THỨC TOÁN DPO LOSS VÀ GRPO ADVANTAGE

Mục tiêu:
1. Cài đặt hàm mất mát DPO (Direct Preference Optimization).
2. Cài đặt chuẩn hóa lợi thế theo nhóm GRPO (Group Relative Policy Optimization).
"""
import torch
import torch.nn.functional as F

def compute_dpo_loss(
    pi_logps_chosen: torch.Tensor,
    pi_logps_rejected: torch.Tensor,
    ref_logps_chosen: torch.Tensor,
    ref_logps_rejected: torch.Tensor,
    beta: float = 0.1
) -> torch.Tensor:
    """
    Công thức:
    L_DPO = - E [ log sigmoid( beta * ( (log pi(y_w) - log ref(y_w)) - (log pi(y_l) - log ref(y_l)) ) ) ]
    
    Args:
        pi_logps_chosen: Log-probabilities của câu được chọn (chosen) dưới policy hiện tại. Tensor shape (B,)
        pi_logps_rejected: Log-probabilities của câu bị loại (rejected) dưới policy hiện tại. Tensor shape (B,)
        ref_logps_chosen: Log-probabilities của chosen dưới reference policy. Tensor shape (B,)
        ref_logps_rejected: Log-probabilities của rejected dưới reference policy. Tensor shape (B,)
        beta: Hệ số phạt KL (thường 0.1)
    """
    # TODO 1: Tính tỷ lệ log-ratio cho chosen: log(pi / ref) = log pi - log ref
    pi_logratios_chosen = pi_logps_chosen - ref_logps_chosen
    
    # TODO 2: Tính tỷ lệ log-ratio cho rejected: log(pi / ref) = log pi - log ref
    pi_logratios_rejected = pi_logps_rejected - ref_logps_rejected
    
    # TODO 3: Tính logits DPO: beta * (chosen_logratios - rejected_logratios)
    logits = beta * (pi_logratios_chosen - pi_logratios_rejected)
    
    # TODO 4: DPO Loss là trung bình âm của log sigmoid: -log(sigmoid(logits))
    # Trong PyTorch: -F.logsigmoid(logits) ổn định hơn về mặt số học
    losses = -F.logsigmoid(logits)
    
    return losses.mean()


def compute_grpo_advantages(rewards: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    """
    Chuẩn hóa điểm thưởng theo nhóm trong thuật toán GRPO (DeepSeek-R1):
    A_i = (r_i - mean(r)) / (std(r) + eps)
    
    Args:
        rewards: Tensor shape (B, G) trong đó B là batch size câu hỏi, G là số câu trả lời lấy mẫu trong mỗi nhóm.
    """
    # TODO 5: Tính mean theo chiều nhóm (dim=1, keepdim=True)
    mean = rewards.mean(dim=1, keepdim=True)
    
    # TODO 6: Tính độ lệch chuẩn std theo chiều nhóm
    std = rewards.std(dim=1, keepdim=True)
    
    # TODO 7: Tính advantage chuẩn hóa
    advantages = (rewards - mean) / (std + eps)
    
    return advantages


if __name__ == "__main__":
    # Test DPO Loss
    pi_w = torch.tensor([-1.2, -0.8])
    pi_l = torch.tensor([-2.5, -2.1])
    ref_w = torch.tensor([-1.2, -0.8])
    ref_l = torch.tensor([-2.5, -2.1])
    loss = compute_dpo_loss(pi_w, pi_l, ref_w, ref_l)
    print("Initial DPO Loss (khi pi == ref):", loss.item(), "(Mong doi: -log(0.5) ~ 0.6931)")
    
    # Test GRPO
    r = torch.tensor([[1.0, 0.0, 0.0, 1.0], [0.5, 0.5, 0.5, 0.5]])
    adv = compute_grpo_advantages(r)
    print("GRPO Advantages:\n", adv)
