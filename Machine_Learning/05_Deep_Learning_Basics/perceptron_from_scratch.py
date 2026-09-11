"""
Perceptron from Scratch (Học Thuật Toán Perceptron Từ Đầu Bằng NumPy)

Mục tiêu học tập:
1. Hiểu công thức toán: y_hat = step(w^T * x + b)
2. Quy tắc cập nhật trọng số Perceptron: w <- w + lr * (y - y_hat) * x
3. Khám phá giới hạn tuyến tính (Linear Separability) & nghịch lý XOR của Minsky & Papert (1969).
"""

import numpy as np

class Perceptron:
    def __init__(self, learning_rate: float = 0.1, max_epochs: int = 100):
        self.lr = learning_rate
        self.max_epochs = max_epochs
        self.weights = None
        self.bias = 0.0

    def step_function(self, z: np.ndarray) -> np.ndarray:
        return np.where(z >= 0, 1, 0)

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for epoch in range(self.max_epochs):
            errors = 0
            for xi, target in zip(X, y):
                linear_output = np.dot(xi, self.weights) + self.bias
                y_pred = self.step_function(linear_output)
                update = self.lr * (target - y_pred)
                
                if update != 0.0:
                    self.weights += update * xi
                    self.bias += update
                    errors += 1
            if errors == 0:
                print(f"[Perceptron] Hội tụ hoàn hảo tại epoch {epoch + 1}!")
                break

    def predict(self, X: np.ndarray) -> np.ndarray:
        linear_output = np.dot(X, self.weights) + self.bias
        return self.step_function(linear_output)

if __name__ == "__main__":
    # Dữ liệu cổng logic AND
    X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_and = np.array([0, 0, 0, 1])

    print("=== 1. Huấn luyện Perceptron trên cổng AND ===")
    p_and = Perceptron(learning_rate=0.2)
    p_and.fit(X_and, y_and)
    print(f"Trọng số w: {p_and.weights}, Bias b: {p_and.bias:.4f}")
    preds_and = p_and.predict(X_and)
    print(f"Dự đoán: {preds_and} | Thực tế: {y_and}\n")

    # Dữ liệu cổng logic OR
    y_or = np.array([0, 1, 1, 1])
    print("=== 2. Huấn luyện Perceptron trên cổng OR ===")
    p_or = Perceptron(learning_rate=0.2)
    p_or.fit(X_and, y_or)
    print(f"Trọng số w: {p_or.weights}, Bias b: {p_or.bias:.4f}")
    preds_or = p_or.predict(X_and)
    print(f"Dự đoán: {preds_or} | Thực tế: {y_or}\n")

    # Nghịch lý XOR (Không phân tách tuyến tính)
    y_xor = np.array([0, 1, 1, 0])
    print("=== 3. Cổng XOR (Giới hạn của Perceptron đơn tầng) ===")
    p_xor = Perceptron(learning_rate=0.2, max_epochs=20)
    p_xor.fit(X_and, y_xor)
    preds_xor = p_xor.predict(X_and)
    print(f"Dự đoán XOR: {preds_xor} | Thực tế: {y_xor}")
    print("-> Perceptron đơn tầng không thể giải quyết XOR! Cần Multi-Layer Perceptron (MLP) với phi tuyến tính.")
