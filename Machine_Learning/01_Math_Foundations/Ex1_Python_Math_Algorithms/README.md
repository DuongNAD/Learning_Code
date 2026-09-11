# 🚀 PYTHON & MACHINE LEARNING FOUNDATIONS LAB
## Hệ Thống Học Tập & Thực Hành Trực Quan Động (Interactive & Hands-on Learning)

Chào mừng bạn đến với không gian học tập và rèn luyện tư duy lập trình nền tảng cho **Machine Learning & Data Science**! Hệ thống này đã được nâng cấp toàn diện từ bộ bài tập `Ex1 -> Ex8` ban đầu thành một **Lab thực hành trực quan và tương tác chuyên sâu**.

---

## 🌟 1. CÁCH KHỞI ĐỘNG VÀ SỬ DỤNG GIAO DIỆN TRỰC QUAN (CLICK & INTERACT)

Bạn có thể tương tác trực quan (kéo slider, bấm nút xem hoạt ảnh, thử nghiệm dữ liệu tự nhập) bằng 1 trong 2 cách cực kỳ đơn giản:

### Cách 1: Khởi chạy bằng lệnh Python (Khuyên dùng)
Mở terminal PowerShell tại thư mục `Ex1` và chạy:
```powershell
py launch_hub.py
```
*Máy chủ cục bộ sẽ tự động khởi động và mở ngay giao diện Web trên trình duyệt mặc định của bạn.*

### Cách 2: Mở trực tiếp file HTML
Bạn chỉ cần click đúp chuột vào file:
📂 `interactive_hub.html`
*Giao diện chạy độc lập 100% offline, không cần cài đặt bất kỳ thư viện ngoài nào!*

---

## 🎮 2. CÁC TÍNH NĂNG TRỰC QUAN ĐỘNG CỦA TỪNG CHỦ ĐỀ

Mỗi chủ đề trên giao diện Web đều có bộ công cụ trực quan hóa động:

| Bài | Tên Chủ Đề | Công Cụ Trực Quan Động (Interactive Widgets) | Kết Nối Machine Learning |
| :--- | :--- | :--- | :--- |
| **Ex1** | **Phân Loại Số & ReLU** | Thùng chứa động (Buckets): Thả số vào nhóm Âm / 0 / Dương; Nút kích hoạt hàm **ReLU** ($f(x) = \max(0, x)$) triệt tiêu số âm về 0 và đo tỷ lệ *Dead Neurons*. | ReLU Activation & Chuẩn hóa Zero-Centering ($x - \mu$) |
| **Ex2** | **Tần Suất & Lọc Ngưỡng K** | Biểu đồ cột SVG động: Kéo thanh trượt điều chỉnh ngưỡng $K$, các cột có tần suất $> K$ phát sáng xanh lá; Click vào từng cột để xem vị trí xuất hiện. | Cắt tỉa từ vựng trong NLP (Vocabulary Pruning / Stop-words) |
| **Ex3** | **Cặp Liền Kề & Pooling** | Khung cửa sổ trượt (Sliding Window): Nút **Tự động chạy (Auto-play)**, Lùi/Tiến từng bước, hoạt ảnh so sánh đối kháng `max(a, b)` và đẩy giá trị cực đại xuống mảng kết quả. | Lớp **1D Max Pooling** trong mạng CNNs xử lý âm thanh/tín hiệu |
| **Ex4** | **Hoán Vị & Cây Quyết Định** | Cây lựa chọn phân nhánh 3 tầng: Bấm vào bất kỳ hoán vị nào để highlight đường đi từ gốc đến ngọn; Mô phỏng thuật toán quay lui (Backtracking). | **GridSearchCV** (Duyệt không gian siêu tham số mô hình) |
| **Ex5** | **Gộp & Khử Trùng Giữ Thứ Tự** | Băng chuyền lọc phần tử: Mô phỏng bộ nhớ Hash Set $O(1)$; Cảnh báo đỏ khi gặp phần tử trùng lặp và loại bỏ; Bảo toàn thứ tự ban đầu với `dict.fromkeys()`. | Làm sạch dữ liệu (Data Deduplication / Feature Store) |
| **Ex6** | **Ma Trận Lọc Chia Hết** | Lưới số màu sắc động: Nhập khoảng số và điều kiện chia hết (ví dụ: chia hết cho 7 và không chia hết cho 5); Các ô số tự đổi màu theo điều kiện. | Phân tầng mẫu & Kỹ thuật chia **K-Fold Cross Validation** |
| **Ex7** | **Khám Phá Số Chẵn & Parity** | Bộ phân tích số học theo thời gian thực: Nhập số bất kỳ để phân tích từng chữ số (All Even Digits) và tính biểu diễn nhị phân, số bit 1 (Hamming weight), Parity Bit. | Mã hóa đặc trưng nhị phân (Binary Feature Hashing Trick) |
| **Ex8** | **Word Chain Đồ Thị BFS** | Đồ thị mạng lưới (SVG Graph): Mô phỏng thuật toán duyệt theo chiều rộng (**Breadth-First Search - BFS**); Hiển thị hàng đợi Queue, tập Visited, và vạch đường đi ngắn nhất màu vàng rực rỡ! | Đồ thị tri thức (Knowledge Graphs) & Tìm đường AI |

---

## 💻 3. KHU VỰC TỰ LÀM: 16 BÀI TẬP THỰC HÀNH CHUYÊN SÂU

Trong file `practice_exercises.py`, chúng tôi đã chuẩn bị **16 bài tập thực hành** (mỗi chủ đề gồm 1 bài mở rộng nâng cao và 1 bài ứng dụng Machine Learning thực tế).

### Danh mục 16 bài tập:
1. **Bài 1.1:** Phân loại 3 nhóm: Âm, Không, Dương và tính đại lượng thống kê (Count, Sum, Mean).
2. **Bài 1.2:** Cài đặt hàm kích hoạt ReLU & Leaky ReLU, đo tỷ lệ nơ-ron chết (Dead Neurons Rate).
3. **Bài 2.1:** Tìm Top $K$ từ xuất hiện nhiều nhất trong chuỗi văn bản (Tokenization & Counting).
4. **Bài 2.2:** Cắt tỉa từ vựng NLP (Loại bỏ từ quá hiếm và từ quá phổ biến theo ngưỡng `[min_freq, max_freq]`).
5. **Bài 3.1:** Tính trung bình trượt 1D (Moving Average) làm mịn tín hiệu chuỗi thời gian.
6. **Bài 3.2:** Tự viết lớp 1D Max Pooling với tham số `pool_size` và `stride`.
7. **Bài 4.1:** Tự cài đặt thuật toán đệ quy quay lui (Backtracking) sinh hoán vị chập $r$ không dùng `itertools`.
8. **Bài 4.2:** Sinh tất cả cấu hình thử nghiệm siêu tham số GridSearchCV (Tích Descartes).
9. **Bài 5.1:** Khử trùng lặp danh sách giữ nguyên thứ tự với hàm `key_func` tùy chọn.
10. **Bài 5.2:** Hợp nhất hai bảng bản ghi dữ liệu Feature Store theo khóa định danh `id_key`.
11. **Bài 6.1:** Bộ lọc chia hết đa điều kiện: chia hết cho danh sách $A$ và không chia hết cho danh sách $B$.
12. **Bài 6.2:** Tự viết thuật toán chia tập dữ liệu thành $K$ nhóm kiểm định chéo (K-Fold Cross Validation).
13. **Bài 7.1:** Tìm các số có toàn bộ các chữ số đều là số chẵn (0, 2, 4, 6, 8).
14. **Bài 7.2:** Phân loại Parity bit nhị phân và tính trọng số Hamming (Hamming Weight).
15. **Bài 8.1:** Word Ladder kinh điển (LeetCode 127): Mỗi bước đổi đúng 1 chữ cái.
16. **Bài 8.2:** Bi-directional BFS Word Chain: Tìm kiếm 2 chiều tăng tốc độ gấp hàng trăm lần!

---

## 🧪 4. HƯỚNG DẪN TỰ CHẤM ĐIỂM & KIỂM THỬ CODE

### 1. Tự chấm điểm bài làm của bạn trong `practice_exercises.py`:
Mở file `practice_exercises.py`, viết code của bạn vào các hàm `practice_...`, sau đó chạy:
```powershell
# Chấm điểm toàn bộ 16 bài:
py practice_exercises.py

# Chỉ chấm điểm riêng Bài 1:
py practice_exercises.py 1

# Chỉ chấm điểm riêng Bài 8:
py practice_exercises.py 8
```

### 2. Chạy bộ kiểm thử tự động toàn diện (Comprehensive Pytest Suite):
Bộ kiểm thử bao phủ toàn bộ 43 test cases (cả Happy Paths lẫn Edge Cases như danh sách rỗng, số âm, phần tử trùng lặp, từ không tồn tại):
```powershell
py test_all.py
```
Hoặc dùng lệnh pytest:
```powershell
py -m pytest test_all.py -v
```

### 3. Tham khảo bộ lời giải mẫu chuẩn:
Nếu gặp khó khăn, bạn có thể tham khảo file:
📂 `solutions_practice.py`
Mỗi bài đều có lời giải kèm phân tích độ phức tạp thời gian $O(N)$ và không gian bộ nhớ.

---

## 📁 5. CẤU TRÚC THƯ MỤC DỰ ÁN

```text
Ex1/
├── Ex1.py                     # Đã nâng cấp: Hàm tách âm/dương, docstring, type hints
├── Ex2.py                     # Đã nâng cấp: Hàm tìm phần tử có tần suất > k
├── Ex3.py                     # Đã nâng cấp: Hàm lấy max cặp liền kề O(N)
├── Ex4.py                     # Đã nâng cấp: Hàm sinh hoán vị 3 phần tử
├── Ex5.py                     # Đã nâng cấp: Hàm gộp danh sách con khử trùng giữ thứ tự
├── Ex6.py                     # Đã nâng cấp: Hàm lọc số chia hết cho 7 và không cho 5
├── Ex7.py                     # Đã nâng cấp: Hàm lọc số chẵn & số có mọi chữ số chẵn
├── Ex8.py                     # Đã nâng cấp: Hàm BFS tìm chuỗi từ có bộ nhớ đệm cache
├── wordsEn.txt                # Từ điển tiếng Anh 109,000 từ
├── practice_exercises.py      # File thực hành 16 bài tập tự luyện kèm trình chấm điểm
├── solutions_practice.py      # Bộ lời giải chuẩn và phân tích thuật toán
├── test_all.py                # Bộ test tự động 43 test cases chạy với pytest
├── interactive_hub.html       # Web App trực quan động, click để tìm hiểu, có sandbox
├── launch_hub.py              # Script 1-click khởi chạy Web App trên trình duyệt
└── README.md                  # Tài liệu hướng dẫn chi tiết (bản này)
```

Chúc bạn học tập hứng khởi, nắm vững nền tảng tư duy lập trình và bứt phá trên con đường Machine Learning! 🚀
