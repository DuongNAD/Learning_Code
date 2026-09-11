# 🧠 Nhập Môn Học Sâu & PyTorch (Deep Learning Basics)

Khám phá quá trình tiến hóa từ nơ-ron sinh học đến Perceptron, mạng nơ-ron đa tầng (MLP), thuật toán lan truyền ngược (Backpropagation) và huấn luyện mô hình thị giác máy tính với PyTorch.

---

## 📂 Các Tập Tin Thực Hành

1. **`perceptron_from_scratch.py`**:
   - Tự viết thuật toán Perceptron học có giám sát từ đầu bằng NumPy.
   - Huấn luyện trên các cổng logic tuyến tính AND, OR.
   - Minh họa giới hạn không phân tách tuyến tính qua nghịch lý XOR của Minsky & Papert.
   - Chạy thử: `python3 perceptron_from_scratch.py`

2. **`mlp_backprop_numpy.py`**:
   - Xây dựng mạng nơ-ron đa tầng (Multi-Layer Perceptron - MLP) 2 tầng hoàn toàn bằng NumPy không dùng framework.
   - Triển khai Forward Pass, hàm kích hoạt phi tuyến Sigmoid và đạo hàm của nó.
   - Lan truyền ngược (Backpropagation) với quy tắc chuỗi (Chain Rule) để tính $dW_2, db_2, dW_1, db_1$.
   - Giải quyết triệt để bài toán XOR đạt độ chính xác 100%.
   - Chạy thử: `python3 mlp_backprop_numpy.py`

3. **`pytorch_mnist_demo.py`**:
   - Sử dụng PyTorch 2.x xây dựng mạng nơ-ron phân loại 10 chữ số viết tay trên bộ dữ liệu offline `mnist.npz`.
   - Vòng lặp huấn luyện chuẩn: `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`.
   - Tận dụng tăng tốc phần cứng Apple Silicon (GPU/MPS).
   - Đạt độ chính xác > 96% trên 10,000 ảnh kiểm thử.
   - Chạy thử: `python3 pytorch_mnist_demo.py`

4. **`mnist.npz`**:
   - Bộ dữ liệu 70,000 ảnh xám kích thước 28×28 chữ số viết tay từ 0 đến 9.
