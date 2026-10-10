"""
BÀI TẬP THỰC HÀNH GIAI ĐOẠN 6: CHAT TEMPLATE & SFT LOSS MASKING

Mục tiêu:
1. Xây dựng định dạng chuẩn hóa hội thoại (Chat Template).
2. Tạo mặt nạ nhãn (label masking với -100) để mô hình chỉ học từ câu trả lời của trợ lý.
"""
import torch
import torch.nn.functional as F

def format_chat_prompt(instruction: str, response: str) -> tuple[str, str]:
    """
    Tạo cấu trúc prompt theo chuẩn SFT:
    User Prompt: "User: {instruction}\nAssistant: "
    Full Sequence: "User: {instruction}\nAssistant: {response}<|endoftext|>"
    """
    user_prefix = f"User: {instruction}\nAssistant: "
    full_text = f"{user_prefix}{response}<|endoftext|>"
    return user_prefix, full_text

def create_sft_labels(input_ids: torch.Tensor, prompt_len: int) -> torch.Tensor:
    """
    Tạo nhãn targets cho SFT:
    - Các vị trí thuộc về prompt của User sẽ được gán giá trị -100 (bị bỏ qua trong loss).
    - Các vị trí thuộc về câu trả lời của Assistant được giữ nguyên nhãn token thực tế.
    
    Args:
        input_ids: Tensor 1D độ dài L
        prompt_len: Số lượng token thuộc về phần Prompt
    """
    # Khởi tạo targets là bản sao của input_ids
    targets = input_ids.clone()
    
    # TODO 1: Gán toàn bộ các token thuộc prompt (từ 0 đến prompt_len - 1) bằng -100
    targets[:prompt_len] = -100
    
    return targets

def compute_sft_loss(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """
    Tính Cross Entropy Loss với ignore_index=-100.
    
    Args:
        logits: Tensor (B, T, vocab_size)
        targets: Tensor (B, T)
    """
    # Shift logits và targets cho Next-token prediction
    # Token tại t dự đoán token tại t+1
    shift_logits = logits[..., :-1, :].contiguous()
    shift_targets = targets[..., 1:].contiguous()
    
    # TODO 2: Tính cross_entropy với ignore_index=-100
    loss = F.cross_entropy(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_targets.view(-1),
        ignore_index=-100
    )
    return loss


if __name__ == "__main__":
    prompt_pfx, full_txt = format_chat_prompt("1 + 1 bang may?", "1 + 1 bang 2.")
    print("User prefix :", repr(prompt_pfx))
    print("Full text   :", repr(full_txt))
