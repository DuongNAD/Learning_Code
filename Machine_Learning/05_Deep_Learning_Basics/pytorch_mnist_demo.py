"""
PyTorch Handwritten Digits (MNIST) Classification Demo

Mục tiêu học tập:
1. Load dataset offline từ file `mnist.npz` bằng NumPy và chuyển sang `torch.Tensor` / `DataLoader`.
2. Xây dựng mạng nơ-ron đa tầng (MLP) với `torch.nn.Module`: Linear, ReLU, Dropout.
3. Vòng lặp huấn luyện chuẩn PyTorch: Optimizer zero_grad -> Forward -> Loss -> Backward -> Step.
4. Đánh giá độ chính xác trên tập kiểm thử độc lập (10,000 ảnh).
"""

import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MNIST_PATH = os.path.join(CURRENT_DIR, "mnist.npz")

class DigitClassifier(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_classes: int = 10):
        super().__init__()
        self.network = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        return self.network(x)

def load_data(batch_size: int = 64):
    if not os.path.exists(MNIST_PATH):
        raise FileNotFoundError(f"Không tìm thấy file dataset: {MNIST_PATH}")
    
    with np.load(MNIST_PATH) as data:
        x_train, y_train = data["x_train"], data["y_train"]
        x_test, y_test = data["x_test"], data["y_test"]

    # Chuẩn hóa ảnh [0, 255] về [0.0, 1.0] dạng float32
    x_train_t = torch.tensor(x_train, dtype=torch.float32) / 255.0
    y_train_t = torch.tensor(y_train, dtype=torch.long)
    x_test_t = torch.tensor(x_test, dtype=torch.float32) / 255.0
    y_test_t = torch.tensor(y_test, dtype=torch.long)

    train_loader = DataLoader(TensorDataset(x_train_t, y_train_t), batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(TensorDataset(x_test_t, y_test_t), batch_size=batch_size, shuffle=False)
    return train_loader, test_loader

def train_model(epochs: int = 2):
    train_loader, test_loader = load_data()
    device = torch.device("cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu"))
    print(f"Sử dụng thiết bị tính toán: {device}")

    model = DigitClassifier().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print(f"Bắt đầu huấn luyện trên 60,000 ảnh trong {epochs} epochs...")
    for epoch in range(epochs):
        model.train()
        total_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item() * len(labels)
            preds = outputs.argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += len(labels)

        train_acc = correct / total
        avg_loss = total_loss / total
        print(f"Epoch {epoch + 1}/{epochs} | Loss: {avg_loss:.4f} | Train Acc: {train_acc*100:.2f}%")

    # Đánh giá trên tập test
    model.eval()
    test_correct = 0
    test_total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            preds = outputs.argmax(dim=1)
            test_correct += (preds == labels).sum().item()
            test_total += len(labels)

    test_acc = test_correct / test_total
    print(f"\n==========================================")
    print(f"🎯 Độ chính xác kiểm thử (10,000 ảnh): {test_acc * 100:.2f}%")
    print(f"==========================================")

if __name__ == "__main__":
    train_model(epochs=2)
