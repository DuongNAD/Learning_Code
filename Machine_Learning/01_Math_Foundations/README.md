# 📐 Nền Tảng Toán Học & Thuật Toán Cơ Sở Cho Machine Learning

Thư mục này cung cấp toàn bộ nền tảng toán học, giải thuật và bài tập code tay rèn luyện tư duy cho Kỹ sư Học Máy (Machine Learning Engineer).

---

## 📂 Cấu Trúc Thư Mục

1. **`math_primer.py`**:
   - File code mẫu trực quan hóa 4 trụ cột toán học của Machine Learning:
     - Đại số tuyến tính: Dot product, Chuẩn L1/L2, Cosine Similarity.
     - Giải tích: Đạo hàm riêng và Gradient Descent tối ưu hóa.
     - Hàm kích hoạt & kỹ thuật chống tràn số Overflow (Log-Sum-Exp / Max trick cho Softmax).
     - Hàm mất mát: Mean Squared Error (MSE) & Binary Cross-Entropy (BCE).
   - Chạy thử: `python3 math_primer.py`

2. **`Ex1_Python_Math_Algorithms/`**:
   - Bộ bài tập nền tảng từ Ex1 đến Ex8 kèm 16 bài tập mở rộng (`practice_exercises.py`).
   - **Giao diện Web Lab trực quan sinh động**: `interactive_hub.html` và `launch_hub.py` (Mô phỏng đồ thị SVG, ReLU, BFS Pathfinding, Cửa sổ trượt 1D Max Pooling, Cây quyết định).
   - **Hệ thống kiểm thử tự động**: `test_all.py` với 43 bài test passed 100% (`pytest test_all.py`).

3. **`Ex2_NLP_Text_Probability/`**:
   - `ex2.py` và tập ngữ liệu `story.txt`: Thao tác với mảng NumPy, kiểm tra phần tử, đảo ngược mảng, tìm cực trị theo trục, và phân tích tần suất từ vựng trong văn bản.
