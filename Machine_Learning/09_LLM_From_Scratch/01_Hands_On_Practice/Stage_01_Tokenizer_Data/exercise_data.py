"""
BÀI TẬP THỰC HÀNH GIAI ĐOẠN 1: TỰ VIẾT TOKENIZER VÀ DATALOADER CHO LLM

Mục tiêu:
1. Tự viết Character-level Tokenizer (encode, decode, vocab_size).
2. Tự viết hàm get_batch trích xuất tensor (x, y) phục vụ huấn luyện Next-token prediction.
"""
import torch

class SimpleCharTokenizer:
    """
    Tokenizer mức độ ký tự đơn giản nhưng cực kỳ mạnh mẽ để học nguyên lý.
    """
    def __init__(self, text: str):
        # TODO 1: Lấy danh sách các ký tự duy nhất trong văn bản text và sắp xếp theo thứ tự bảng chữ cái
        self.chars = sorted(list(set(text)))
        self.vocab_size = len(self.chars)

        # TODO 2: Tạo từ điển ánh xạ ký tự -> số nguyên (char to integer - stoi)
        # và số nguyên -> ký tự (integer to char - itos)
        self.stoi = {ch: i for i, ch in enumerate(self.chars)}
        self.itos = {i: ch for i, ch in enumerate(self.chars)}

    def encode(self, s: str) -> list[int]:
        """Chuyển chuỗi s thành danh sách số nguyên."""
        # TODO 3: Hoàn thành hàm encode
        return [self.stoi[c] for c in s if c in self.stoi]

    def decode(self, indices: list[int]) -> str:
        """Chuyển danh sách số nguyên trở lại chuỗi ký tự."""
        # TODO 4: Hoàn thành hàm decode
        return "".join([self.itos[i] for i in indices if i in self.itos])


def get_batch(data: torch.Tensor, batch_size: int, block_size: int, device: str = "cpu"):
    """
    Tạo ra một batch ngẫu nhiên gồm (x, y) để đưa vào mô hình Transformer.
    
    Args:
        data: 1D Tensor chứa toàn bộ token của tập dữ liệu
        batch_size: Số lượng chuỗi mẫu trong 1 batch (B)
        block_size: Độ dài ngữ cảnh của mỗi chuỗi (T / context_length)
        device: 'cpu' hoặc 'cuda'
        
    Returns:
        x: Tensor shape (batch_size, block_size)
        y: Tensor shape (batch_size, block_size) - dịch sang phải 1 token so với x
    """
    # TODO 5: Sinh ngẫu nhiên batch_size vị trí bắt đầu hợp lệ trong mảng data
    # Gợi ý: vị trí lớn nhất có thể bắt đầu là len(data) - block_size - 1
    max_idx = len(data) - block_size
    ix = torch.randint(0, max_idx, (batch_size,))
    
    # TODO 6: Lấy các đoạn x và y tương ứng từ ix
    x = torch.stack([data[i : i + block_size] for i in ix])
    y = torch.stack([data[i + 1 : i + block_size + 1] for i in ix])
    
    return x.to(device), y.to(device)


if __name__ == "__main__":
    sample_text = "Xin chao the gioi, toi dang hoc tu viet LLM tu so 0 bang PyTorch!"
    tokenizer = SimpleCharTokenizer(sample_text)
    print(f"Vocab size: {tokenizer.vocab_size}")
    encoded = tokenizer.encode("Xin chao")
    print(f"Encoded 'Xin chao': {encoded}")
    decoded = tokenizer.decode(encoded)
    print(f"Decoded: '{decoded}'")
    
    # Demo tensor batch
    tokens = torch.tensor(tokenizer.encode(sample_text), dtype=torch.long)
    x, y = get_batch(tokens, batch_size=2, block_size=8)
    print(f"\nx shape: {x.shape} (Batch, Time)")
    print(f"y shape: {y.shape}")
    print("x[0]:", x[0].tolist())
    print("y[0]:", y[0].tolist(), "(Token muc tieu dich 1 buoc)")
