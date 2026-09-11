"""
Toán Nền Tảng Cho Học Máy (Machine Learning Math Primer in Python)
================================================================

Bao gồm 4 trụ cột toán học của Machine Learning:
1. Đại Số Tuyến Tính (Linear Algebra): Tích vô hướng, Chiếu vector, Chuẩn L1/L2, Cosine Similarity.
2. Giải Tích Đa Biến (Multivariate Calculus): Đạo hàm riêng, Gradient Vector, Thuật toán Gradient Descent.
3. Hàm Kích Hoạt & Ổn Định Số Học (Numerical Stability): Sigmoid, Softmax (kỹ thuật Max-Trick chống Overflow).
4. Hàm Mất Mát (Loss Functions): Mean Squared Error (MSE), Binary Cross-Entropy (BCE).
"""

import numpy as np


# ==========================================
# 1. ĐẠI SỐ TUYẾN TÍNH (LINEAR ALGEBRA)
# ==========================================
def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    """Tính tích vô hướng giữa 2 vector v1 . v2."""
    return float(np.dot(v1, v2))


def l2_norm(v: np.ndarray) -> float:
    """Độ dài chuẩn Euclid L2 ||v||_2."""
    return float(np.linalg.norm(v, ord=2))


def l1_norm(v: np.ndarray) -> float:
    """Độ dài chuẩn khoảng cách Manhattan L1 ||v||_1 (nền tảng Lasso)."""
    return float(np.linalg.norm(v, ord=1))


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """Cosine Similarity: cos(theta) = (v1 . v2) / (||v1|| * ||v2||)."""
    norm1 = l2_norm(v1)
    norm2 = l2_norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return float(np.dot(v1, v2) / (norm1 * norm2))


def linear_algebra_demo():
    print("--- 1. Đại Số Tuyến Tính: Vector & Phép Đo ---")
    v1 = np.array([3.0, 4.0])
    v2 = np.array([1.0, 2.0])

    dp = dot_product(v1, v2)
    norm_v1 = l2_norm(v1)
    norm_l1 = l1_norm(v1)
    cos_sim = cosine_similarity(v1, v2)

    print(f"Vector v1: {v1}, Vector v2: {v2}")
    print(f"Tích vô hướng v1 . v2: {dp:.2f}")
    print(f"Chuẩn L2 ||v1||: {norm_v1:.2f} (Độ dài hình học)")
    print(f"Chuẩn L1 ||v1||: {norm_l1:.2f} (Khoảng cách Manhattan)")
    print(f"Cosine Similarity giữa v1 và v2: {cos_sim:.4f}\n")


# ==========================================
# 2. GIẢI TÍCH & GRADIENT DESCENT
# ==========================================
def gradient_descent_step(w: float, learning_rate: float) -> tuple[float, float, float]:
    """
    Một bước tối ưu Gradient Descent cho hàm mục tiêu f(w) = w^2 - 4w + 5.
    Đạo hàm: f'(w) = 2w - 4.
    Cực tiểu lý thuyết tại w* = 2, f(2) = 1.
    """
    grad = 2 * w - 4
    w_new = w - learning_rate * grad
    loss = w_new**2 - 4 * w_new + 5
    return w_new, grad, loss


def gradient_descent_demo():
    print("--- 2. Giải Tích: Tối Ưu Hóa Bằng Gradient Descent ---")
    w = 10.0  # Khởi tạo xa cực tiểu
    learning_rate = 0.1
    epochs = 20

    print(f"Điểm xuất phát w = {w:.2f} | f(w) = {w**2 - 4*w + 5:.2f}")
    for epoch in range(epochs):
        w, grad, loss = gradient_descent_step(w, learning_rate)
        if (epoch + 1) % 5 == 0:
            print(f"Bước {epoch + 1:2d}: w = {w:.4f}, f'(w) = {grad:.4f}, Loss = {loss:.4f}")
    print(f"Hội tụ tại w ≈ {w:.4f} (Lý thuyết: 2.0000)\n")


# ==========================================
# 3. HÀM KÍCH HOẠT & CHỐNG TRÀN SỐ HỌC
# ==========================================
def stable_softmax(logits: np.ndarray) -> np.ndarray:
    """
    Kỹ thuật Max-Trick cho Softmax: trừ đi max(logits) trước khi exp
    để ngăn chặn triệt để lỗi Overflow (inf/nan) với giá trị số cực lớn.
    """
    shifted_logits = logits - np.max(logits)
    exp_logits = np.exp(shifted_logits)
    return exp_logits / np.sum(exp_logits)


def sigmoid(z: np.ndarray | float) -> np.ndarray | float:
    """Hàm kích hoạt Sigmoid mượt hóa xác suất [0, 1]."""
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))


def activations_demo():
    print("--- 3. Hàm Kích Hoạt & Kỹ Thuật Chống Tràn Số ---")
    logits = np.array([1000.0, 1001.0, 1002.0])
    softmax_probs = stable_softmax(logits)

    print(f"Logits cực lớn: {logits}")
    print(f"Softmax xác suất ổn định số: {softmax_probs}")
    print(f"Tổng xác suất: {np.sum(softmax_probs):.4f}\n")


# ==========================================
# 4. HÀM MẤT MÁT (LOSS FUNCTIONS)
# ==========================================
def mse_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean Squared Error: 1/N * sum((y_pred - y_true)^2)."""
    return float(np.mean((np.asarray(y_pred) - np.asarray(y_true)) ** 2))


def binary_cross_entropy(y_true: np.ndarray, y_pred_prob: np.ndarray, eps: float = 1e-15) -> float:
    """Binary Cross-Entropy Loss với kỹ thuật kẹp (clipping) tránh log(0)."""
    y_t = np.asarray(y_true, dtype=float)
    p = np.clip(np.asarray(y_pred_prob, dtype=float), eps, 1.0 - eps)
    return float(-np.mean(y_t * np.log(p) + (1.0 - y_t) * np.log(1.0 - p)))


def loss_functions_demo():
    print("--- 4. Hàm Mất Mát: MSE & Binary Cross-Entropy ---")
    y_true = np.array([1, 0, 1, 1])
    y_pred_prob = np.array([0.9, 0.1, 0.8, 0.4])

    mse = mse_loss(y_true, y_pred_prob)
    bce = binary_cross_entropy(y_true, y_pred_prob)

    print(f"Nhãn thực tế y: {y_true}")
    print(f"Dự đoán xác suất: {y_pred_prob}")
    print(f"MSE Loss: {mse:.4f}")
    print(f"Binary Cross-Entropy Loss: {bce:.4f}\n")


if __name__ == "__main__":
    linear_algebra_demo()
    gradient_descent_demo()
    activations_demo()
    loss_functions_demo()
