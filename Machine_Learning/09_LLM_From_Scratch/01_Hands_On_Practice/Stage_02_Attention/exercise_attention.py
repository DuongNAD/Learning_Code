"""
BÀI TẬP THỰC HÀNH GIAI ĐOẠN 2: TỰ CÀI ĐẶT CƠ CHẾ SELF-ATTENTION & MULTI-HEAD ATTENTION

Mục tiêu:
1. Xây dựng 1 Attention Head độc lập (Key, Query, Value + Causal Mask).
2. Kết hợp nhiều Head thành MultiHeadAttention.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class Head(nn.Module):
    """
    Một Attention Head đơn lẻ.
    """
    def __init__(self, head_size: int, n_embed: int, context_length: int):
        super().__init__()
        # TODO 1: Khởi tạo 3 phép chiếu tuyến tính (linear projections) cho Key, Query, Value
        # Không dùng bias (bias=False)
        self.key = nn.Linear(n_embed, head_size, bias=False)
        self.query = nn.Linear(n_embed, head_size, bias=False)
        self.value = nn.Linear(n_embed, head_size, bias=False)
        
        # TODO 2: Đăng ký buffer ma trận tam giác dưới (tril) để làm causal mask
        self.register_buffer('tril', torch.tril(torch.ones(context_length, context_length)))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x shape: (B, T, C) trong đó C = n_embed
        output shape: (B, T, head_size)
        """
        B, T, C = x.shape
        head_size = self.key.out_features
        
        # TODO 3: Tính Key, Query và hệ số scale (1 / sqrt(head_size))
        k = self.key(x)     # (B, T, head_size)
        q = self.query(x)   # (B, T, head_size)
        scale = 1.0 / math.sqrt(head_size)
        
        # TODO 4: Tính tích vô hướng Attention Scores: q @ k.T
        # Shape: (B, T, head_size) @ (B, head_size, T) -> (B, T, T)
        scores = (q @ k.transpose(-2, -1)) * scale
        
        # TODO 5: Áp dụng Causal Masking: thay thế các vị trí tương lai bằng -inf
        scores = scores.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        
        # TODO 6: Áp dụng Softmax trên chiều cuối cùng để có phân phối xác suất
        weights = F.softmax(scores, dim=-1)
        
        # TODO 7: Nhân trọng số với Value matrix v
        v = self.value(x)   # (B, T, head_size)
        out = weights @ v   # (B, T, T) @ (B, T, head_size) -> (B, T, head_size)
        
        return out


class MultiHeadAttention(nn.Module):
    """
    Gộp nhiều Head chạy song song và chiếu qua 1 lớp tuyến tính đầu ra.
    """
    def __init__(self, n_head: int, n_embed: int, context_length: int):
        super().__init__()
        assert n_embed % n_head == 0, "n_embed phai chia het cho n_head!"
        head_size = n_embed // n_head
        
        # TODO 8: Tạo ModuleList chứa n_head Head
        self.heads = nn.ModuleList([Head(head_size, n_embed, context_length) for _ in range(n_head)])
        
        # TODO 9: Lớp Linear chiếu kết quả sau khi ghép (concatenation)
        self.proj = nn.Linear(n_embed, n_embed)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Nối kết quả của tất cả các đầu theo chiều kênh (dim=-1)
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        # Chiếu tuyến tính đầu ra
        out = self.proj(out)
        return out


if __name__ == "__main__":
    B, T, C = 2, 4, 32  # Batch=2, Context=4, Embedding=32
    x = torch.randn(B, T, C)
    
    # Test Head
    head = Head(head_size=16, n_embed=C, context_length=8)
    out_h = head(x)
    print("Head output shape:", out_h.shape, "(Mong doi: [2, 4, 16])")
    
    # Test MultiHeadAttention
    mha = MultiHeadAttention(n_head=4, n_embed=C, context_length=8)
    out_mha = mha(x)
    print("MHA output shape:", out_mha.shape, "(Mong doi: [2, 4, 32])")
