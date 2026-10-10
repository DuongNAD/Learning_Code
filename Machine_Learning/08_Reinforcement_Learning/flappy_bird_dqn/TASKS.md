# Tasks: Flappy Bird Deep Q-Network (DQN)

## Milestone 1: Môi trường & Đặc tả bài toán RL (Environment Setup)
- [x] [Priority: P0] Cài đặt dependencies cơ bản (`torch`, `pygame`, `numpy`).
- [ ] [Priority: P0] Xây dựng hoặc tích hợp module Game Flappy Bird với API chuẩn RL (`reset()` và `step(action)`).
- [ ] [Priority: P0] Xác định State Representation: Trích xuất vector trạng thái (vị trí chim, khoảng cách tới ống trên/dưới, vận tốc).
- [ ] [Priority: P1] Thiết kế hàm thưởng (Reward Function): Thưởng sống sót, thưởng vượt qua ống, phạt nặng khi va chạm.

## Milestone 2: Kiến trúc mô hình DQN & Bộ nhớ đệm (Core Components)
- [ ] [Priority: P0] Xây dựng lớp mạng nơ-ron `DQN` bằng PyTorch (MLP dự đoán Q-values cho 2 actions).
- [ ] [Priority: P0] Cài đặt `ReplayBuffer` (lưu trữ transition `(s, a, r, s', done)` và lấy mẫu ngẫu nhiên theo mini-batch).
- [ ] [Priority: P1] Cài đặt chiến lược khám phá `Epsilon-Greedy` với cơ chế giảm dần epsilon (epsilon decay).

## Milestone 3: Vòng lặp huấn luyện (Training Loop)
- [ ] [Priority: P0] Khởi tạo Policy Network và Target Network (đồng bộ trọng số theo chu kỳ `target_update_freq`).
- [ ] [Priority: P0] Viết hàm tính toán DQN Loss dựa trên phương trình Bellman:
      `Loss = MSE(Q(s, a), r + gamma * max_a' Q_target(s', a'))`.
- [ ] [Priority: P1] Viết Training Loop chính: Thu thập kinh nghiệm vào Buffer, kích hoạt tối ưu hóa mô hình khi đủ dữ liệu.
- [ ] [Priority: P2] Ghi nhận log quá trình học (Loss, Score qua từng episode, Epsilon value).

## Milestone 4: Đánh giá, Lưu trữ & Demo (Evaluation & Deployment)
- [ ] [Priority: P1] Lưu checkpoint trọng số mô hình tốt nhất (`best_model.pth`).
- [ ] [Priority: P1] Viết script `demo.py` tải model đã train để agent tự chơi có giao diện đồ họa.
- [ ] [Priority: P2] Đo lường điểm số trung bình (Mean Score) qua 100 episodes kiểm thử độc lập.
