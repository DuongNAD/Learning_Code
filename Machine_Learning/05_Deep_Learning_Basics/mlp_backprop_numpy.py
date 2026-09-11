"""
Multi-Layer Perceptron (MLP) & Backpropagation From Scratch (NumPy)

Mục tiêu học tập:
1. Kiến trúc mạng nơ-ron 2 tầng: Input (2) -> Hidden (4) -> Output (1)
2. Lan truyền tiến (Forward Pass): z1 = X @ W1 + b1, a1 = sigmoid(z1), z2 = a1 @ W2 + b2, y_hat = sigmoid(z2)
3. Lan truyền ngược (Backpropagation): Quy tắc chuỗi (Chain Rule) để tính đạo hàm dL/dW2, dL/db2, dL/dW1, dL/db1
4. Giải quyết triệt để bài toán phi tuyến XOR!
"""

import numpy as np

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))

def sigmoid_derivative(a):
    # a là giá trị sau khi đã qua sigmoid: a = sigmoid(z)
    return a * (1.0 - a)

class TwoLayerMLP:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, lr: float = 0.5):
        self.lr = lr
        np.random.seed(42)
        # Khởi tạo trọng số Xavier / He
        self.W1 = np.random.randn(input_dim, hidden_dim) * np.sqrt(2.0 / input_dim)
        self.b1 = np.zeros((1, hidden_dim))
        self.W2 = np.random.randn(hidden_dim, output_dim) * np.sqrt(2.0 / hidden_dim)
        self.b2 = np.zeros((1, output_dim))

    def forward(self, X: np.ndarray):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, X: np.ndarray, y: np.ndarray):
        m = X.shape[0] # số mẫu (batch size)

        # 1. Đạo hàm của MSE Loss theo a2: L = 1/2m * sum((a2 - y)^2) -> dL/da2 = (a2 - y) / m
        # 2. Delta tầng ra: dL/dz2 = dL/da2 * da2/dz2 = (a2 - y) * sigmoid_derivative(a2)
        delta2 = (self.a2 - y) * sigmoid_derivative(self.a2)
        
        # 3. Đạo hàm theo trọng số tầng ra
        dW2 = np.dot(self.a1.T, delta2) / m
        db2 = np.sum(delta2, axis=0, keepdims=True) / m

        # 4. Delta tầng ẩn: delta1 = (delta2 @ W2.T) * sigmoid_derivative(a1)
        delta1 = np.dot(delta2, self.W2.T) * sigmoid_derivative(self.a1)
        
        # 5. Đạo hàm theo trọng số tầng ẩn
        dW1 = np.dot(X.T, delta1) / m
        db1 = np.sum(delta1, axis=0, keepdims=True) / m

        # 6. Cập nhật Gradient Descent
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

    def fit(self, X: np.ndarray, y: np.ndarray, epochs: int = 5000):
        for epoch in range(epochs):
            preds = self.forward(X)
            loss = np.mean((preds - y) ** 2)
            self.backward(X, y)

            if (epoch + 1) % 1000 == 0:
                print(f"Epoch {epoch + 1:4d} | MSE Loss: {loss:.6f}")

    def predict(self, X: np.ndarray) -> np.ndarray:
        return (self.forward(X) >= 0.5).astype(int)

if __name__ == "__main__":
    # Huấn luyện MLP trên cổng phi tuyến XOR
    X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_xor = np.array([[0], [1], [1], [0]])

    print("=== Huấn luyện Multi-Layer Perceptron (MLP) giải quyết XOR ===")
    mlp = TwoLayerMLP(input_dim=2, hidden_dim=4, output_dim=1, lr=3.0)
    mlp.fit(X_xor, y_xor, epochs=3000)

    predictions = mlp.predict(X_xor)
    raw_probs = mlp.forward(X_xor)

    print("\n=== KẾT QUẢ CUỐI CÙNG ===")
    for xi, prob, pred, actual in zip(X_xor, raw_probs, predictions, y_xor):
        print(f"Input: {xi} -> Prob: {prob[0]:.4f} -> Pred: {pred[0]} (Thực tế: {actual[0]})")

    accuracy = np.mean(predictions == y_xor)
    print(f"\nĐộ chính xác trên XOR: {accuracy * 100:.1f}%")
