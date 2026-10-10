"""
BÀI TẬP THỰC HÀNH GIAI ĐOẠN 3: TỰ DỰNG MLP VÀ KHỐI TRANSFORMER BLOCK

Mục tiêu:
1. Xây dựng lớp MLP (Feed-Forward Network) với hệ số mở rộng 4x và hàm kích hoạt GELU.
2. Lắp ráp khối Transformer Block hoàn chỉnh với Pre-LayerNorm và Residual Connections.
"""
import torch
import torch.nn as nn
import sys
import os

# Import MultiHeadAttention tu Stage_02
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Stage_02_Attention")))
from exercise_attention import MultiHeadAttention

class MLP(nn.Module):
    """
    Feed-Forward Network gồm 2 lớp Linear: n_embed -> 4 * n_embed -> n_embed
    """
    def __init__(self, n_embed: int):
        super().__init__()
        # TODO 1: Xây dựng mạng tuần tự nn.Sequential gồm:
        # Linear(n_embed, 4 * n_embed) -> nn.GELU() -> Linear(4 * n_embed, n_embed)
        self.net = nn.Sequential(
            nn.Linear(n_embed, 4 * n_embed),
            nn.GELU(),
            nn.Linear(4 * n_embed, n_embed),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class TransformerBlock(nn.Module):
    """
    Một khối Transformer hoàn chỉnh chuẩn kiến trúc Pre-LayerNorm.
    """
    def __init__(self, n_head: int, n_embed: int, context_length: int):
        super().__init__()
        # TODO 2: Khởi tạo 2 lớp LayerNorm cho trước Attention và trước MLP
        self.ln1 = nn.LayerNorm(n_embed)
        self.ln2 = nn.LayerNorm(n_embed)
        
        # TODO 3: Khởi tạo MultiHeadAttention và MLP
        self.attn = MultiHeadAttention(n_head, n_embed, context_length)
        self.mlp = MLP(n_embed)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Pre-LayerNorm với Residual Skip Connection:
        x = x + Attention(LayerNorm1(x))
        x = x + MLP(LayerNorm2(x))
        """
        # TODO 4: Áp dụng cơ chế Attention với Pre-LN và Residual Connection
        x = x + self.attn(self.ln1(x))
        
        # TODO 5: Áp dụng MLP với Pre-LN và Residual Connection
        x = x + self.mlp(self.ln2(x))
        
        return x


if __name__ == "__main__":
    B, T, C = 2, 4, 32
    x = torch.randn(B, T, C)
    block = TransformerBlock(n_head=4, n_embed=C, context_length=8)
    out = block(x)
    print("Input shape :", x.shape)
    print("Output shape:", out.shape)
    assert out.shape == x.shape, "Shape output phai bang shape input!"
    print("Transformer Block hoat dong tot!")
