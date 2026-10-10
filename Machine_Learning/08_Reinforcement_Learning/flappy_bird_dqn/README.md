# Flappy Bird DQN (Deep Q-Network)

## 1. Giới thiệu
Mô tả mục tiêu dự án: Huấn luyện một tác tử (agent) tự động chơi Flappy Bird sử dụng thuật toán Học tăng cường sâu (Deep Q-Network - DQN).

## 2. Mô hình hóa bài toán Reinforcement Learning
- **Môi trường (Environment)**: Pygame / Flappy Bird emulator.
- **Không gian trạng thái (State Space)**: Ảnh màn hình (frame-based) hoặc vector tọa độ (khoảng cách tới ống tiếp theo, vận tốc, độ cao).
- **Không gian hành động (Action Space)**: 2 hành động: [0: Không làm gì, 1: Bay lên (Flap)].
- **Hàm thưởng (Reward Function)**: Cơ chế thưởng/phạt khi sống sót, vượt ống, hoặc va chạm.

## 3. Kiến trúc mô hình
- Mạng nơ-ron: DQN / CNN (nếu xử lý ảnh) hoặc MLP (nếu dùng vector tọa độ).
- Kỹ thuật bổ trợ: Experience Replay Buffer, Target Network, Epsilon-Greedy Policy.

## 4. Cài đặt & Chạy
- Yêu cầu môi trường (Python version, thư viện: PyTorch/TensorFlow, Pygame).
- Lệnh cài đặt dependencies.
- Lệnh chạy huấn luyện (train) và chạy đánh giá (test/demo).
