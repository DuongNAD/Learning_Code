# 📝 Đề Thi Chẩn Đoán 04: Unsupervised Learning & Recommender Systems

> Thiết kế bởi **DeepTutor AI Mentor**. Kiểm tra tư duy về thuật toán phân cụm, giảm chiều và hệ gợi ý.

---

### Câu 1: Thuật toán K-Means và Khởi tạo Trọng tâm (K-Means++)
Tại sao thuật toán `K-Means++` lại được Scikit-Learn dùng làm mặc định thay vì chọn ngẫu nhiên đồng đều các trọng tâm ban đầu?
- [A] Vì K-Means++ tự động tìm ra số cụm K tốt nhất.
- [B] Vì K-Means++ phân tán các trọng tâm khởi tạo ban đầu càng xa nhau càng tốt theo phân phối xác suất tỉ lệ với bình phương khoảng cách, giúp tránh rơi vào cực tiểu địa phương nghèo nàn và tăng tốc hội tụ.
- [C] Vì K-Means++ không cần tính toán khoảng cách Euclid.
- [D] Vì K-Means++ loại bỏ hoàn toàn nhiễu Outlier trước khi phân cụm.

---

### Câu 2: Hệ số bóng đổ (Silhouette Score)
Hệ số Silhouette Score có giá trị nằm trong khoảng $[-1, +1]$. Khi Silhouette Score của một điểm dữ liệu xấp xỉ $+1$, điều đó có nghĩa là gì?
- [A] Điểm dữ liệu đó nằm rất sát ranh giới giữa hai cụm lân cận.
- [B] Điểm dữ liệu đó được phân cụm rất chuẩn: rất gần với các điểm trong cùng cụm của nó ($a(i)$ nhỏ) và cách rất xa các điểm thuộc cụm lân cận gần nhất ($b(i)$ lớn).
- [C] Điểm dữ liệu đó có thể đã bị gán nhầm vào cụm sai.
- [D] Dữ liệu bị đa cộng tuyến nghiêm trọng.

---

### Câu 3: PCA (Principal Component Analysis)
Mục tiêu toán học chính của PCA khi tìm các thành phần chính (Principal Components) là gì?
- [A] Tối đa hóa phương sai (Variance) của dữ liệu được chiếu lên trục mới và đồng thời giảm thiểu sai số tái tạo (Reconstruction Error).
- [B] Loại bỏ tất cả các dòng dữ liệu có chứa giá trị ngoại lai.
- [C] Làm cho tất cả các biến đầu vào tuân theo phân phối đều.
- [D] Giảm số lượng mẫu dữ liệu từ $N$ xuống $\sqrt{N}$.

---

### Câu 4: Content-Based Filtering vs Collaborative Filtering
Trong hệ gợi ý xem phim (MovieLens), phương pháp **Content-Based Filtering** (như triển khai trong `recommendation_system.py`) dựa vào yếu tố nào để gợi ý phim?
- [A] Dựa vào lịch sử chấm điểm và đánh giá của hàng triệu người dùng khác (User-Item Matrix).
- [B] Dựa vào các thuộc tính nội dung của chính bộ phim (Thể loại Genres, Đạo diễn, Tóm tắt nội dung TF-IDF) để so sánh độ tương đồng Cosine với những bộ phim người dùng đã thích trước đây.
- [C] Dựa vào vị trí địa lý của máy chủ mạng người dùng.
- [D] Dựa vào thuật toán sắp xếp nổi bọt (Bubble Sort).

---

### Câu 5: Vấn đề Cold-Start trong Hệ Gợi Ý
Khi một người dùng mới vừa tạo tài khoản và chưa từng xem hay chấm điểm bất kỳ bộ phim nào, phương pháp nào sau đây giúp giải quyết bài toán Cold-Start hiệu quả nhất?
- [A] Không thể gợi ý gì cả cho đến khi họ tự tìm kiếm ít nhất 10 bộ phim.
- [B] Kết hợp gợi ý các phim phổ biến nhất (Popularity-based / Trending) hoặc khảo sát nhanh sở thích ban đầu để chuyển sang Content-Based Filtering.
- [C] Chạy thuật toán K-Means trên cơ sở dữ liệu trống.
- [D] Ép buộc mô hình Matrix Factorization tạo vector nhúng ngẫu nhiên.

---

<details>
<summary><b>🔍 BẢNG ĐÁP ÁN & PHÂN TÍCH BẪY NHẬN THỨC (COGNITIVE GAPS)</b></summary>

| Câu | Đáp án đúng | Lỗ hổng nhận thức thường gặp |
|:---:|:---:|:---|
| 1 | **B** | Khởi tạo trọng tâm ban đầu có ảnh hưởng sống còn tới nghiệm hội tụ của K-Means. K-Means++ là giải pháp đột phá năm 2007 của Arthur & Vassilvitskii. |
| 2 | **B** | Công thức: $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$. Giá trị gần 1 = cụm đậm đặc và tách biệt tốt; gần 0 = nằm trên biên; âm = gán sai cụm. |
| 3 | **A** | PCA tìm kiếm các trục trực giao mà khi chiếu dữ liệu lên đó, lượng thông tin (đo bằng phương sai) được giữ lại là tối đa. |
| 4 | **B** | File `recommendation_system.py` tính Cosine Similarity trên ma trận TF-IDF của cột `genres` của phim, đây là điển hình của Content-Based Filtering. |
| 5 | **B** | Hybrid Recommender Systems (kết hợp Content-based + Collaborative + Heuristics) là kiến trúc chuẩn công nghiệp để khắc phục Cold Start. |

</details>
