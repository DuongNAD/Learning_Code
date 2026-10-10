"""
SCRIPT TRUC QUAN HOA MA TRAN CHU Y (ATTENTION HEATMAP VISUALIZATION)
Ve do thi the hien trong so tu chu y giua cac token.
"""
import sys
import torch
import torch.nn.functional as F
import math

# Dam bao UTF-8 tren Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def plot_attention_demo():
    tokens = ["Toi", "dang", "hoc", "viet", "LLM", "tu", "dau"]
    T = len(tokens)
    head_size = 16
    
    # Tao ngau nhien Q va K
    torch.manual_seed(42)
    q = torch.randn(1, T, head_size)
    k = torch.randn(1, T, head_size)
    
    # Tinh Attention Weights
    scores = (q @ k.transpose(-2, -1)) / math.sqrt(head_size)
    tril = torch.tril(torch.ones(T, T))
    scores = scores.masked_fill(tril == 0, float('-inf'))
    weights = F.softmax(scores, dim=-1)[0].detach().numpy()
    
    print("\n" + "=" * 55)
    print("   MA TRAN TRONG SO TU CHU Y (CAUSAL ATTENTION MATRIX)   ")
    print("=" * 55)
    header = f"{'Token':<8}" + "".join([f"{t:>7}" for t in tokens])
    print(header)
    print("-" * 55)
    for i, t_row in enumerate(tokens):
        row_str = f"{t_row:<8}"
        for j in range(T):
            if j > i:
                row_str += f"{'0.000':>7}"
            else:
                row_str += f"{weights[i, j]:>7.3f}"
        print(row_str)
    print("=" * 55)
    print("[NHAN XET]:")
    print("1. Ma tran co dang tam giac duoi: Moi token chi duoc nhin ve qua khu va chinh no.")
    print("2. Tong cac gia tri tren moi hang luon bang dung 1.0 (nho ham Softmax).")
    print("=" * 55 + "\n")

if __name__ == "__main__":
    plot_attention_demo()
