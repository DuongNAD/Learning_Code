"""
Toán Nền Tảng Cho Học Máy (Machine Learning Math Primer in Python)

Bao gồm 4 trụ cột toán học của Machine Learning:
1. Đại Số Tuyến Tính (Linear Algebra): Tích vô hướng, Chiếu vector, Chuẩn L1/L2.
2. Giải Tích Đa Biến (Multivariate Calculus): Đạo hàm riêng, Gradient Vector, Thuật toán Gradient Descent.
3. Hàm Kích Hoạt & Ổn Định Số Học (Numerical Stability): Sigmoid, Softmax (với kỹ thuật Max-Trick chống tràn số Overflow).
4. Hàm Mất Mát (Loss Functions): Mean Squared Error (MSE), Binary Cross-Entropy (BCE).
"""

import numpy as np

# ==========================================
# 1. ĐẠI SỐ TUYẾN TÍNH
# ==========================================
def linear_algebra_demo():
    print("--- 1. Đại Số Tuyến Tính: Vector & Phép Đo ---")
    v1 = np.array([3.0, 4.0])
    v2 = np.array([1.0, 2.0])

    # Tích vô hướng (Dot product)
    dot_product = np.dot(v1, v2)
    # Độ dài chuẩn L2 (Euclidean Norm)
    norm_v1 = np.linalg.norm(v1, ord=2)
    # Độ dài chuẩn L1 (Manhattan Norm - nền tảng của Lasso L1 Regularization)
    norm_l1 = np.linalg.norm(v1, ord=1)
    # Cosine Similarity: cos(theta) = (v1 . v2) / (||v1|| * ||v2||)
    cos_sim = dot_product / (np.linalg.norm(v1) * np.linalg.norm(v2))

    print(f"Vector v1: {v1}, Vector v2: {v2}")
    print(f"Tích vô hướng v1 . v2: {dot_product:.2f}")
    print(f"Chuẩn L2 ||v1||: {norm_v1:.2f} (Độ dài hình học)")
    print(f"Chuẩn L1 ||v1||: {norm_l1:.2f} (Khoảng cách Manhattan)")
    print(f"Cosine Similarity giữa v1 và v2: {cos_sim:.4f}\n")

# ==========================================
# 2. GIẢI TÍCH & GRADIENT DESCENT
# ==========================================
def gradient_descent_demo():
    print("--- 2. Giải Tích: Tối Ưu Hóa Bằng Gradient Descent ---")
    # Giả sử hàm mất mát f(w) = w^2 - 4w + 5
    # Đạo hàm: f'(w) = 2w - 4
    # Cực tiểu lý thuyết tại w = 2
    w = 10.0  # Khởi tạo xa cực tiểu
    learning_rate = 0.1
    epochs = 20

    print(f"Điểm xuất phát w = {w:.2f} | f(w) = {w**2 - 4*w + 5:.2f}")
    for epoch in range(epochs):
        grad = 2 * w - 4
        w -= learning_rate * grad
        if (epoch + 1) % 5 == 0:
            loss = w**2 - 4*w + 5
            print(f"Bước {epoch + 1:2d}: w = {w:.4f}, f'(w) = {grad:.4f}, Loss = {loss:.4f}")
    print(f"Hội tụ tại w ≈ {w:.4f} (Lý thuyết: 2.0000)\n")

# ==========================================
# 3. HÀM KÍCH HOẠT & CHỐNG TRÀN SỐ HỌC
# ==========================================
def activations_demo():
    print("--- 3. Hàm Kích Hoạt & Kỹ Thuật Chống Tràn Số ---")
    # Kỹ thuật Max-Trick cho Softmax
    logits = np.array([1000.0, 1001.0, 1002.0]) # Nếu tính trực tiếp exp(1000) sẽ bị Overflow (inf)
    
    # Cách đúng: Trừ đi max(logits) trước khi exp
    shifted_logits = logits - np.max(logits)
    exp_logits = np.exp(shifted_logits)
    softmax_probs = exp_logits / np.sum(exp_logits)
    
    print(f"Logits cực lớn: {logits}")
    print(f"Softmax xác suất ổn định số: {softmax_probs}")
    print(f"Tổng xác suất: {np.sum(softmax_probs):.4f}\n")

# ==========================================
# 4. HÀM MẤT MÁT (LOSS FUNCTIONS)
# ==========================================
def loss_functions_demo():
    print("--- 4. Hàm Mất Mát: MSE & Binary Cross-Entropy ---")
    y_true = np.array([1, 0, 1, 1])
    y_pred_prob = np.array([0.9, 0.1, 0.8, 0.4])

    # 1. Mean Squared Error: 1/N * sum((y_pred - y_true)^2)
    mse = np.mean((y_pred_prob - y_true) ** 2)

    # 2. Binary Cross-Entropy: -1/N * sum(y*log(p) + (1-y)*log(1-p))
    eps = 1e-15 # Tránh log(0)
    p_clipped = np.clip(y_pred_prob, eps, 1 - eps)
    bce = -np.mean(y_true * np.log(p_clipped) + (1 - y_true) * np.log(1 - p_clipped))

    print(f"Nhãn thực tế y: {y_true}")
    print(f"Dự đoán xác suất: {y_pred_prob}")
    print(f"MSE Loss: {mse:.4f}")
    print(f"Binary Cross-Entropy Loss: {bce:.4f}\n")

if __name__ == "__main__":
    linear_algebra_demo()
    gradient_descent_demo()
    activations_demo()
    loss_functions_demo()
