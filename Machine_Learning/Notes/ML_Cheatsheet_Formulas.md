# 📐 Sổ Tay Công Thức Toán & Metrics Học Máy (ML Cheatsheet)

---

## 1. Đại Số Tuyến Tính & Phép Đo Khoảng Cách

- **Tích vô hướng (Dot Product)**:
  $$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta)$$

- **Chuẩn $L_1$ (Manhattan Norm)**:
  $$\|\mathbf{x}\|_1 = \sum_{i=1}^{n} |x_i|$$

- **Chuẩn $L_2$ (Euclidean Norm)**:
  $$\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2}$$

- **Cosine Similarity**:
  $$\text{CosineSim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$$

---

## 2. Hàm Kích Hoạt (Activation Functions)

| Tên hàm | Công thức | Đạo hàm | Miền giá trị | Đặc tính |
|:---|:---:|:---:|:---:|:---|
| **Sigmoid** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | $\sigma(z)(1 - \sigma(z))$ | $(0, 1)$ | Dễ triệt tiêu đạo hàm, dùng cho xác suất nhị phân. |
| **Tanh** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $1 - \tanh^2(z)$ | $(-1, 1)$ | Zero-centered, tốt hơn Sigmoid cho tầng ẩn. |
| **ReLU** | $\max(0, z)$ | $1 \text{ nếu } z > 0 \text{ else } 0$ | $[0, \infty)$ | Tính toán cực nhanh, tránh triệt tiêu đạo hàm nhưng bị Dead ReLU. |
| **Leaky ReLU** | $\max(\alpha z, z)$ | $1 \text{ nếu } z > 0 \text{ else } \alpha$ | $(-\infty, \infty)$ | Khắc phục Dead ReLU với hệ số $\alpha \approx 0.01$. |
| **Softmax** | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | Ma trận Jacobian | $(0, 1)$, $\sum = 1$ | Phân phối xác suất đa lớp (Multi-class). |

---

## 3. Hàm Mất Mát (Loss Functions)

- **Mean Squared Error (MSE)** - Dùng cho Hồi quy:
  $$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$

- **Mean Absolute Error (MAE)**:
  $$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$$

- **Binary Cross-Entropy (Log-Loss)** - Dùng cho Phân loại nhị phân:
  $$\mathcal{L}_{\text{BCE}} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \ln(\hat{p}_i) + (1 - y_i) \ln(1 - \hat{p}_i) \right]$$

- **Categorical Cross-Entropy** - Dùng cho Phân loại đa lớp:
  $$\mathcal{L}_{\text{CCE}} = -\frac{1}{N} \sum_{i=1}^{N} \sum_{c=1}^{C} y_{i, c} \ln(\hat{p}_{i, c})$$

---

## 4. Các Chỉ Số Đánh Giá Phân Loại (Classification Metrics)

Cho ma trận nhầm lẫn (Confusion Matrix):
- $TP$: True Positives (Dự đoán 1, Thực tế 1)
- $TN$: True Negatives (Dự đoán 0, Thực tế 0)
- $FP$: False Positives (Dự đoán 1, Thực tế 0 - Báo động giả / Type I Error)
- $FN$: False Negatives (Dự đoán 0, Thực tế 1 - Bỏ sót / Type II Error)

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP} \quad \text{(Trong số những ca mô hình báo bệnh, bao nhiêu ca thực sự có bệnh?)}$$

$$\text{Recall (Sensitivity)} = \frac{TP}{TP + FN} \quad \text{(Trong số tất cả những người thực sự bị bệnh, mô hình tóm được bao nhiêu %?)}$$

$$F_1\text{-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 TP}{2 TP + FP + FN}$$

$$F_{\beta}\text{-Score} = (1 + \beta^2) \frac{\text{Precision} \times \text{Recall}}{\beta^2 \text{Precision} + \text{Recall}} \quad (\beta = 2 \text{ khi ưu tiên Recall gấp đôi Precision})$$
