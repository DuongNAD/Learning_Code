---
title: "Ban_do_hop_nhat_Machine_Learning"
topic: "Machine_Learning"
created_at: "2026-09-11T19:08:30.364525"
source: "DeepTutor Portable MCP Server"
tags:
  - roadmap
  - unified
  - zero_to_one
---

# 🗺️ BẢN ĐỒ HỢP NHẤT HỌC MÁY TỪ CON SỐ 0 (ZERO-TO-ONE UNIFIED BLUEPRINT)

> **Phương châm DeepTutor**: *"Lý thuyết soi đường — Trực quan thấu hiểu — Thực hành khắc sâu"*

---

## 🎯 1. Tại Sao Phải Gộp Hai Màn Hình Lại?

Trên bàn làm việc của bạn hiện đang có 2 công cụ bổ trợ nhau hoàn hảo:
* **Màn hình A (`00_Curriculum_and_Materials/AI_ML_Mastery_Slides.html`)**: **Tư duy Kiến trúc sư** — Cung cấp bức tranh toàn cảnh, bản chất bài toán, bẫy dữ liệu và quy trình chuẩn doanh nghiệp.
* **Màn hình B (`localhost:8081/interactive_hub.html`)**: **Kỹ năng Thợ rèn** — Mô phỏng thuật toán bằng hoạt ảnh trực quan và cung cấp 16 bài tập code nền tảng từ mộc mạc nhất đến phức tạp.

Nếu chỉ đọc Slide, bạn sẽ bị "chìm" trong lý thuyết trừu tượng. Nếu chỉ code bài tập nhỏ lẻ, bạn sẽ không hiểu bài tập đó dùng làm gì trong hệ thống AI lớn. **Bản đồ hợp nhất kết nối 2 nửa lại làm một.**

---

## 🧭 2. Ma Trận Ánh Xạ Hợp Nhất (Unified Learning Matrix)

| Giai đoạn | Nội dung trong Slide (`AI_ML_Mastery_Slides.html`) | Mô phỏng trong Lab (`interactive_hub.html`) | File Code thực hành | Lệnh kiểm thử tự động |
| :--- | :--- | :--- | :--- | :--- |
| **Chặng 1** *(Bắt đầu tại đây)* | **Phần 1 - Slide 1 đến 4**: Bức tranh AI/ML, Phân loại bài toán, Kiểu đặc trưng, Chia Train/Test | **Tab 1**: Phân loại số & Hàm ReLU<br>**Tab 7**: Số chẵn & Feature Hashing | `practice_exercises.py`<br>(Bài Ex1 & Ex7) | `pytest 01_Math_Foundations/Ex1_Python_Math_Algorithms/test_all.py -k "test_ex1 or test_ex7"` |
| **Chặng 2** | **Phần 3**: Tiền xử lý dữ liệu, Khử trùng, Xử lý ngoại lai, Chia K-Fold | **Tab 5**: Gộp & Khử trùng Set<br>**Tab 6**: Lọc chia hết & K-Fold Split | `practice_exercises.py`<br>(Bài Ex5 & Ex6) | `pytest 01_Math_Foundations/Ex1_Python_Math_Algorithms/test_all.py -k "test_ex5 or test_ex6"` |
| **Chặng 3** | **Phần 2 & Phần 6**: Đánh giá hiệu năng, Tối ưu siêu tham số, Cửa sổ trượt Time-Series | **Tab 3**: Cặp liền kề & 1D Pooling<br>**Tab 4**: Hoán vị & Grid Search | `practice_exercises.py`<br>(Bài Ex3 & Ex4) | `pytest 01_Math_Foundations/Ex1_Python_Math_Algorithms/test_all.py -k "test_ex3 or test_ex4"` |
| **Chặng 4** | **Phần 4, 5 & NLP**: Xử lý ngôn ngữ tự nhiên, Đồ thị gợi ý (Knowledge Graph / Recommender) | **Tab 2**: Đếm tần suất & Lọc NLP<br>**Tab 8**: Word Chain BFS Đồ thị | `practice_exercises.py`<br>(Bài Ex2 & Ex8) | `pytest 01_Math_Foundations/Ex1_Python_Math_Algorithms/test_all.py -k "test_ex2 or test_ex8"` |

---

## 🚀 3. Lộ Trình Hành Động Cho Buổi Học Hôm Nay (Day 1 Action Plan)

### 🔹 Bước 1: 15 Phút Định Hình Tư Duy (Tại Tab Slides)
Mở file `AI_ML_Mastery_Slides.html`:
1. **Slide 1**: Đọc kỹ phần *"Vì sao LLM không thể thay thế ML truyền thống?"*.
2. **Slide 2**: Phân biệt **Supervised (Có nhãn)** vs **Unsupervised (Không nhãn)**.
3. **Slide 3**: Biến **Numerical** (Số đo lường được) vs **Categorical** (Nhãn/Hạng mục).
4. **Slide 4**: Quy tắc chống **Data Leakage**: *Không bao giờ để dữ liệu tập Test "nhìn trộm" thông số tập Train*.

### 🔹 Bước 2: 10 Phút Trải Nghiệm Trực Quan (Tại Tab Interactive Hub)
Chuyển sang `http://localhost:8081/interactive_hub.html`:
1. Bấm vào tab **`1 Số Âm/Dương & ReLU`**: Thử kéo slider, quan sát cơ chế gạt phẳng số âm về 0 của hàm ReLU.
2. Bấm vào tab **`2 Tần Suất & Lọc Từ NLP`**: Xem biểu đồ tần suất từ và trực giác kỹ thuật Pruning lọc từ vựng.

### 🔹 Bước 3: 20 Phút Tự Tay Viết Code (Hands-on Coding)
Mở file `01_Math_Foundations/Ex1_Python_Math_Algorithms/practice_exercises.py`:
1. Cuộn đến bài **Ex1**.
2. Tự viết logic hàm phân loại số / ReLU, chú ý các trường hợp biên (`[]`, `0`, số âm lớn).

### 🔹 Bước 4: 5 Phút Kiểm Thử (PyTest Verification)
Chạy lệnh trong terminal:
```powershell
pytest 01_Math_Foundations/Ex1_Python_Math_Algorithms/test_all.py -k "test_ex1" -v
```
