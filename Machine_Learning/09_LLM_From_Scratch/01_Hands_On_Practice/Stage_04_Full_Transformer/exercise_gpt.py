"""
BÀI TẬP THỰC HÀNH GIAI ĐOẠN 4: LẮP RÁP TOÀN BỘ MÔ HÌNH MINIGPT VÀ THUẬT TOÁN SINH TỰ HỒI QUY

Mục tiêu:
1. Xây dựng lớp MiniGPT hoàn chỉnh (Embeddings + N Blocks + LayerNorm + LM Head).
2. Viết thuật toán forward tính toán Cross-Entropy Loss.
3. Viết hàm generate sinh văn bản tự hồi quy có điều chỉnh Temperature và Top-K.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import sys
import os

# Import TransformerBlock tu Stage_03
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Stage_03_Transformer_Block")))
from exercise_block import TransformerBlock

class MiniGPT(nn.Module):
    def __init__(self, vocab_size: int, n_embed: int, context_length: int, n_head: int, n_layer: int):
        super().__init__()
        self.context_length = context_length
        
        # TODO 1: Khởi tạo Token Embedding và Position Embedding
        self.tok_embed = nn.Embedding(vocab_size, n_embed)
        self.pos_embed = nn.Embedding(context_length, n_embed)
        
        # TODO 2: Khởi tạo n_layer khối TransformerBlock
        self.blocks = nn.ModuleList([
            TransformerBlock(n_head, n_embed, context_length) for _ in range(n_layer)
        ])
        
        # TODO 3: Lớp chuẩn hóa LayerNorm cuối cùng trước khi chiếu ra từ vựng
        self.ln_f = nn.LayerNorm(n_embed)
        
        # TODO 4: Lớp LM Head tuyến tính n_embed -> vocab_size (không dùng bias)
        self.lm_head = nn.Linear(n_embed, vocab_size, bias=False)

    def forward(self, idx: torch.Tensor, targets: torch.Tensor = None):
        """
        idx: Tensor (B, T)
        targets: Tensor (B, T) - nhãn token tiếp theo
        """
        B, T = idx.shape
        assert T <= self.context_length, f"Do dai chuoi {T} vuot qua context_length {self.context_length}!"
        
        # TODO 5: Tính tổng Token Embedding và Position Embedding
        pos = torch.arange(0, T, dtype=torch.long, device=idx.device) # (T)
        tok_emb = self.tok_embed(idx)     # (B, T, n_embed)
        pos_emb = self.pos_embed(pos)     # (T, n_embed)
        x = tok_emb + pos_emb             # (B, T, n_embed)
        
        # TODO 6: Truyền qua các TransformerBlock tuần tự
        for block in self.blocks:
            x = block(x)
            
        # Chuẩn hóa tầng cuối
        x = self.ln_f(x)
        
        # Chiếu ra logits từ vựng
        logits = self.lm_head(x) # (B, T, vocab_size)
        
        # TODO 7: Tính hàm mất mát Cross-Entropy nếu có targets
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
            
        return logits, loss

    @torch.no_grad()
    def generate(self, idx: torch.Tensor, max_new_tokens: int, temperature: float = 1.0, top_k: int = None):
        """
        Sinh token mới tự hồi quy.
        """
        for _ in range(max_new_tokens):
            # Cắt ngắn chuỗi nếu dài hơn context_length
            idx_cond = idx[:, -self.context_length:]
            
            # Forward lấy logits
            logits, _ = self(idx_cond)
            # Chỉ lấy logits tại token cuối cùng: (B, vocab_size)
            logits = logits[:, -1, :] / temperature
            
            # Áp dụng Top-K nếu được cấu hình
            if top_k is not None:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = float('-inf')
                
            # Tính xác suất bằng Softmax
            probs = F.softmax(logits, dim=-1)
            
            # Lấy mẫu token tiếp theo
            idx_next = torch.multinomial(probs, num_samples=1)
            
            # Nối vào chuỗi hiện tại
            idx = torch.cat((idx, idx_next), dim=1)
            
        return idx


if __name__ == "__main__":
    model = MiniGPT(vocab_size=100, n_embed=32, context_length=16, n_head=4, n_layer=2)
    dummy_x = torch.randint(0, 100, (2, 8))
    dummy_y = torch.randint(0, 100, (2, 8))
    
    logits, loss = model(dummy_x, dummy_y)
    print(f"Logits shape : {logits.shape}")
    print(f"Initial loss : {loss.item():.4f}")
    
    # Test generate
    generated = model.generate(dummy_x[:1, :2], max_new_tokens=5)
    print(f"Generated tokens sequence: {generated.tolist()}")
