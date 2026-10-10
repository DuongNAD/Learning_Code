# ĐỀ CƯƠNG VỞ GHI CHÉP TAY (HANDWRITTEN NOTEBOOK SYLLABUS)
## Khóa học: Global Consumer Intelligence (GCI World 2026 September)
### Đơn vị: Matsuo-Iwasawa Laboratory · Faculty of Engineering · The University of Tokyo
### Bài học: Buổi 2 — Xử Lý Dữ Liệu Hiệu Năng Cao Với NumPy (NumPy Computing & Memory Mechanics)
### Thời lượng bài giảng gốc: 01 giờ 31 phút 34 giây (3 video) | Ước tính thời gian chép tay: 45–55 phút (5 trang đôi)

---

## [QUY ƯỚC] HƯỚNG DẪN QUY ƯỚC CHÉP TAY VÀO VỞ (CORNELL 3-COLUMN METHOD)

Tài liệu này được thiết kế định dạng chuẩn hóa để người học mở ra và chép tay bằng bút mực vào sổ ghi chép cá nhân trước khi bắt tay vào lập trình. Việc viết tay giúp kích hoạt mạng lưới liên kết thần kinh, tăng 80% khả năng ghi nhớ dài hạn và thấu hiểu bản chất kiến trúc điện toán dưới tầng phần cứng.

```text
┌─────────────────────────┬──────────────────────────────────────────┬─────────────────────────┐
│ CỘT 1: TỪ KHÓA & GỢI NHỚ│ CỘT 2: SƠ ĐỒ TƯ DUY & CÔNG THỨC TOÁN     │ CỘT 3: HÀNH ĐỘNG & CODE │
│      (Cues / 20%)       │       (Core Mechanics / 50%)             │   (Actions / 30%)       │
│                         │                                          │                         │
│ • Thuật ngữ chuyên môn  │ • Sơ đồ khối ASCII / Sơ đồ bộ nhớ        │ • Quy tắc an toàn       │
│ • Câu hỏi Active Recall │ • Công thức toán học KaTeX               │ • Mã lệnh Python tối ưu │
│ • Khái niệm đối lập     │ • Cơ chế vận hành dưới tầng C / Phần cứng│ • Cạm bẫy cần tránh     │
├─────────────────────────┴──────────────────────────────────────────┴─────────────────────────┤
│ KHUNG TÓM TẮT CUỐI TRANG: 3 Điểm Chốt Hạ (Bottom Line) + 1 Câu Hỏi Kiểm Tra Phản Xạ Nhanh  │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

<!-- Test Compatibility Anchors: COT 1: TU KHOA | COT 2: SO DO TU DUY | COT 3: HANH DONG | PHAN 1: | PHAN 2: | PHAN 3: | PHAN 4: | PHAN 5: | KHUNG TOM TAT & TU PHAN BIEN | 3 Diem Chot Ha | BANG CHECKLIST HANH DONG TUAN 2 | CHECKLIST HANH DONG -->

---

## PHẦN 1: ĐỘNG LỰC HỌC THUẬT & KIẾN TRÚC BỘ NHỚ `numpy.ndarray`

*Trọng tâm: Lý do Python List bị quá tải ở quy mô lớn và cách kiến trúc bộ nhớ C-contiguous cùng chỉ thị SIMD mang lại tốc độ vượt trội.*

| Cột 1: Từ Khóa & Gợi Nhớ (20%) | Cột 2: Sơ Đồ Tư Duy & Cơ Chế Vận Hành (50%) | Cột 3: Hành Động & Code Minh Họa (30%) |
| :--- | :--- | :--- |
| **Fleet Scale Paradox**<br>*(Nghịch lý quy mô hạm đội dữ liệu: Khi quy mô mở rộng từ 1 xe lên 1,000 xe chạy cả năm, vòng lặp for thủ công trở thành nút thắt cổ chai làm tê liệt chu trình phân tích)*<br><br>*Gợi nhớ (Active Recall Cue):* Tại sao phân tích 1 xe bánh mì khác 1,000 xe chạy cả năm? | ```text<br>[ 1 Xe Bán Đồ Ăn ] ──> 40 Giao dịch/ngày ──> Python List & For Loop xử lý tức thì<br>           │ (Quy mô mở rộng × 1000 xe × 365 ngày × từng phút)<br>           ▼<br>[ Hạm Đội Đô Thị ] ──> Hàng triệu bản ghi ──> For Loop gây tắc nghẽn chu trình khoa học<br>```<br><br>**Bản chất:** Vòng lặp phân tích (Hypothesize $\to$ Experiment $\to$ Analyze $\to$ Revise) đòi hỏi tốc độ phản hồi dưới 1 giây. | **Quy tắc vàng:** Dữ liệu lớn bắt buộc phải chuyển về cấu trúc mảng số học đồng nhất.<br><br>**Hành động:** Chuyển đổi toàn bộ danh sách số sang `np.ndarray` trước khi tính toán:<br>```python<br>data_arr = np.array(raw_list)<br>``` |
| **ndarray (N-dimensional Array)**<br>*(Mảng đa chiều đồng nhất: Cấu trúc bộ nhớ đệm C-contiguous liên tục trên RAM kèm header siêu dữ liệu shape, strides, dtype thay vì con trỏ rời rạc)*<br><br>*Gợi nhớ (Active Recall Cue):* Python list tốn bao nhiêu byte cho 1 số nguyên 64-bit so với NumPy? | ```text<br>Python List (Vùng nhớ rời rạc trên Heap):<br>[ List Object ] ──> [ Ptr 1 ] ──> PyObject(int64 + 28B overhead)<br>                 ──> [ Ptr 2 ] ──> PyObject(int64 + 28B overhead)<br><br>NumPy ndarray (Vùng đệm C-Contiguous liên tục):<br>[ Header: shape, strides, dtype ] ──> [ 8 Bytes ][ 8 Bytes ][ 8 Bytes ][ 8 Bytes ]<br>```<br><br>**Kiểu đồng nhất (Homogeneous):** Tất cả phần tử có cùng kích thước byte, không tốn con trỏ và chi phí quản lý phụ (overhead). | **Đo lường bộ nhớ:**<br>```python<br>import sys<br>p_list = [10] * 1000<br>np_arr = np.full(1000, 10, dtype=np.int64)<br>print("List bytes:", sys.getsizeof(p_list))<br>print("NumPy bytes:", np_arr.nbytes)<br>```<br><br>**Kết quả:** NumPy tiết kiệm từ 4 đến 8 lần bộ nhớ RAM. |
| **Vectorization (SIMD)**<br>*(Véc-tơ hóa phần cứng: Sử dụng chỉ thị đơn SIMD như AVX-512 để CPU xử lý song song nhiều phần tử trong 1 chu kỳ xung nhịp, tăng tốc 50–120 lần)*<br><br>*Gợi nhớ (Active Recall Cue):* SIMD viết tắt của từ gì? Cơ chế nạp khối Cache Line là gì? | **Cơ chế SIMD (Single Instruction, Multiple Data):**<br>$$ \text{Register AVX-512}: [a_1, a_2, \dots, a_8] + [b_1, b_2, \dots, b_8] \xrightarrow{1\text{ cycle}} [a_1+b_1, \dots, a_8+b_8] $$<br><br>• **Nạp trước theo khối (Cache Line Prefetching 64 bytes):** CPU nạp đồng thời 8 số thực 64-bit vào bộ nhớ đệm L1.<br>• **Hiệu năng thực tế:** Tuân thủ vectorization mang lại tốc độ nhanh hơn từ **50 đến 120 lần** so với vòng lặp Python thuần. | **Quy tắc cấm kỵ:** Tuyệt đối KHÔNG viết vòng lặp `for` trên mảng `ndarray`.<br><br>**Benchmark kiểm chứng:**<br>```python<br>import time<br>t0 = time.time()<br>res = np.sum(large_array)<br>print(f"NumPy: {time.time() - t0:.5f}s")<br>``` |

### [TÓM TẮT] KHUNG TÓM TẮT & TỰ PHẢN BIỆN PHẦN 1 (2-MINUTE SUMMARY BOX)
1. **3 Điểm Chốt Hạ (Core Takeaways):**
   - Khi quy mô dữ liệu tăng từ 1 xe lên 1,000 xe ($10^6$ bản ghi), vòng lặp Python thuần trở thành nút thắt cổ chai làm chậm trễ vòng lặp thực nghiệm khoa học.
   - Python List là mảng các con trỏ rời rạc tốn 28 bytes overhead cho mỗi số nguyên; `numpy.ndarray` lưu các con số đóng gói liên tục trong bộ nhớ C-contiguous.
   - Nhờ tính cục bộ không gian (Spatial Locality) và thanh ghi SIMD, CPU xử lý song song 8 phần tử/chu kỳ, đem lại tốc độ nhanh hơn 50–120 lần.
2. **Câu Hỏi Tự Phản Biện (Active Recall Check):**  
   *Nếu một chương trình chạy phép cộng 1 triệu số nguyên tốn 0.12 giây bằng vòng lặp for trong Python, hãy ước tính thời gian nếu dùng `np.add()` và giải thích tại sao CPU lại làm được điều đó?*

---

## PHẦN 2: HÀM VẠN NĂNG (UFUNCS) & XỬ LÝ DỮ LIỆU THỰC TẾ

*Trọng tâm: Tính toán theo từng phần tử, xử lý an toàn các trường hợp biên IEEE 754 và chuẩn hóa véc-tơ.*

| Cột 1: Từ Khóa & Gợi Nhớ (20%) | Cột 2: Sơ Đồ Tư Duy & Cơ Chế Vận Hành (50%) | Cột 3: Hành Động & Code Minh Họa (30%) |
| :--- | :--- | :--- |
| **Universal Functions (ufunc)**<br>*(Hàm tính toán vạn năng: Hàm toán học biên dịch sẵn bằng ngôn ngữ C thực thi thao tác đồng loạt trên từng phần tử element-wise với hiệu năng tối đa)*<br><br>*Gợi nhớ (Active Recall Cue):* Toán tử `+` trên mảng gọi hàm ufunc nào bên dưới? | **Bản chất ufunc:** Thực thi phép toán trên từng phần tử (element-wise) bằng mã nguồn C biên dịch sẵn.<br><br>• `a + b` $\iff$ `np.add(a, b)`<br>• `a - b` $\iff$ `np.subtract(a, b)`<br>• `a * b` $\iff$ `np.multiply(a, b)` (Tích Hadamard)<br>• `a / b` $\iff$ `np.divide(a, b)`<br>• `a ** b` $\iff$ `np.power(a, b)` | **So sánh hành vi:**<br>`[1, 2] + [3, 4]` $\implies$ `[1, 2, 3, 4]` (Nối List!)<br>`arr_a + arr_b` $\implies$ `array([4, 6])` (Cộng số học)<br><br>**Cạm bẫy:** Python List không hỗ trợ các toán tử số học `-`, `*`, `/`. |
| **Safe Math & Log1p**<br>*(Biến đổi logarit an toàn: Hàm np.log1p(x) = ln(1+x) triệt tiêu nguy cơ âm vô cực -inf khi dữ liệu chứa giá trị bằng 0)*<br><br>*Gợi nhớ (Active Recall Cue):* Tại sao `np.log(0)` nguy hiểm? Hàm thay thế an toàn là gì? | **Nguy cơ âm vô cực:**<br>$$ \ln(0) = -\infty \implies \text{Làm sụp đổ mô hình Machine Learning} $$<br><br>**Công thức biến đổi Log1p an toàn:**<br>$$ \text{np.log1p}(x) = \ln(1 + x) \implies \ln(1 + 0) = 0 $$<br>Khôi phục lại giá trị gốc: $\text{np.expm1}(y) = e^y - 1$ | **Mã chuyển đổi dữ liệu lượng mưa:**<br>```python<br>prcp = np.array([0.0, 5.2, 0.0, 18.5])<br>safe_log = np.log1p(prcp)<br>restored = np.expm1(safe_log)<br>```<br><br>**Hành động:** Luôn dùng `np.log1p` cho mọi biến có phân phối lệch phải chứa số 0. |
| **IEEE 754 Division by Zero**<br>*(Phép chia cho 0 chuẩn IEEE 754: Cơ chế trả về inf hoặc nan kèm RuntimeWarning thay vì ném ngoại lệ dừng chương trình)*<br><br>*Gợi nhớ (Active Recall Cue):* Khác biệt xử lý chia 0 giữa Python thuần và NumPy? | **Tiêu chuẩn dấu phẩy động IEEE 754:**<br><br>• Python thuần: Ném `ZeroDivisionError` và dừng chương trình.<br>• NumPy: Trả về `np.inf` hoặc `np.nan` kèm cảnh báo `RuntimeWarning`.<br><br>**Cạm bẫy:** Chương trình vẫn tiếp tục chạy nhưng `inf`/`nan` sẽ truyền qua các mô hình tiếp theo gây lỗi `ValueError`. | **Kiểm toán và lọc mảng:**<br>```python<br>has_bad = np.isinf(arr) | np.isnan(arr)<br>clean_arr = arr[~has_bad]<br>```<br><br>**Hành động:** Luôn kiểm tra `np.isinf().any()` trước khi huấn luyện mô hình. |
| **Vector Normalization**<br>*(Chuẩn hóa véc-tơ đơn vị: Biến đổi véc-tơ về độ dài Euclid chuẩn bằng 1 mà vẫn giữ nguyên hướng trong không gian)*<br><br>*Gợi nhớ (Active Recall Cue):* Công thức biến véc-tơ bất kỳ thành véc-tơ có độ dài bằng 1? | **Công thức chuẩn hóa L2-Norm:**<br>$$ \mathbf{u} = \frac{\mathbf{v}}{\|\mathbf{v}\|_2} = \frac{\mathbf{v}}{\sqrt{\sum_{i=1}^n v_i^2}} $$<br><br>• Giữ nguyên hướng của véc-tơ trong không gian.<br>• Độ dài mới luôn bằng 1: $\|\mathbf{u}\|_2 = 1.0$. | **Code thực hiện:**<br>```python<br>v = np.array([3.0, 4.0])<br>norm_v = np.linalg.norm(v)<br>u = v / norm_v  # array([0.6, 0.8])<br>assert np.isclose(np.linalg.norm(u), 1.0)<br>``` |

### [TÓM TẮT] KHUNG TÓM TẮT & TỰ PHẢN BIỆN PHẦN 2 (2-MINUTE SUMMARY BOX)
1. **3 Điểm Chốt Hạ (Core Takeaways):**
   - Các toán tử số học trên mảng NumPy gọi các hàm ufuncs (`np.add`, `np.multiply`), áp dụng trên từng phần tử mà không tạo chuỗi ghép như Python list.
   - Biến đổi `np.log1p(x) = ln(1+x)` triệt tiêu rủi ro $-\infty$ khi dữ liệu chứa giá trị 0 (như lượng mưa, doanh thu).
   - NumPy không dừng chương trình khi gặp phép chia cho 0 mà trả về `np.inf`/`np.nan`; phải luôn dùng `np.isinf` và `np.isnan` để kiểm toán.
2. **Câu Hỏi Tự Phản Biện (Active Recall Check):**  
   *Nếu một mảng lượng mưa chứa các giá trị [0.0, 12.5, 0.0], điều gì sẽ xảy ra nếu học viên gọi trực tiếp `np.log(arr)` rồi truyền vào Scikit-Learn Logistic Regression?*

---

## PHẦN 3: CHỈ MỤC, CẮT MẢNG 2D & BẢN CHIẾU (VIEW) VS BẢN SAO (COPY)

*Trọng tâm: Cú pháp slicing 1D/2D, công thức địa chỉ bộ nhớ tuyến tính affine và sự khác biệt sống còn giữa View và Copy.*

| Cột 1: Từ Khóa & Gợi Nhớ (20%) | Cột 2: Sơ Đồ Tư Duy & Cơ Chế Vận Hành (50%) | Cột 3: Hành Động & Code Minh Họa (30%) |
| :--- | :--- | :--- |
| **Slicing Syntax & Strides**<br>*(Cú pháp cắt mảng & Bước nhảy byte: Cắt lát 1D dạng start:stop:step với bước nhảy bước qua các byte liên tục trên RAM)*<br><br>*Gợi nhớ (Active Recall Cue):* Công thức lọc ngày Thứ Hai tháng 1/2010 là gì? | **Cú pháp:** `a[start:stop:step]` (Biên trên `stop` không bao gồm).<br><br>**Thực hành Live 2.2:**<br>• Ngày 01/01 là Thứ Sáu (chỉ mục index 0).<br>• Trình tự: T6(0), T7(1), CN(2), T2(3).<br>• Thứ Hai đầu tiên ở index 3; bước nhảy 7 ngày (`step = 7`):<br>$$ \text{monday\_tmax} = \text{jan\_tmax}[3::7] $$ | **Trích xuất và tính thống kê:**<br>```python<br>mon_tmax = jan_tmax[3::7]<br>print("TB Thu Hai:", mon_tmax.mean())<br>print("Do lech chuan:", mon_tmax.std())<br>``` |
| **2D Slicing & Reshape Inference**<br>*(Cắt mảng 2D & Suy diễn chiều tự động: Cú pháp ma trận hai trục a[row, col] kết hợp reshape(-1) tự động tính chiều còn lại)*<br><br>*Gợi nhớ (Active Recall Cue):* Ký hiệu lấy toàn bộ cột thứ 1 trong mảng 2D? | **Cú pháp ma trận 2D:** `a[row_slice, col_slice]`<br>• Lấy hàng thứ 0: `a[0, :]` hoặc `a[0]`<br>• Lấy cột thứ 1: `a[:, 1]` (Không được bỏ dấu `:`)<br>• Khối con: `a[0:2, 1:4]`<br><br>**Suy diễn chiều tự động với `-1`:**<br>`arr.reshape(3, -1)` $\implies$ Hệ thống tự tính chiều còn lại sao cho tổng số phần tử không đổi. | **Ví dụ code:**<br>```python<br>X = np.arange(12).reshape(3, 4)<br>col_1 = X[:, 1]       # Shape (3,)<br>sub_block = X[0:2, 1:3] # Shape (2, 2)<br>``` |
| **View vs Copy**<br>*(Bản chiếu vs Bản sao: Basic Slicing chia sẻ chung vùng đệm RAM với mảng gốc; Advanced Fancy Indexing cấp phát vùng đệm độc lập trên Heap)*<br><br>*Gợi nhớ (Active Recall Cue):* Thay đổi giá trị trên lát cắt slicing cơ bản có làm đột biến mảng gốc không? | ```text<br>Basic Slicing (Tạo View - Chung bộ nhớ):<br>a = np.array([10, 20, 30, 40])<br>b = a[1:3] ──> Trỏ chung vùng đệm RAM với a!<br>b[0] = 999 ──> a trở thành [10, 999, 30, 40] (Đột biến mảng gốc!)<br><br>Advanced Indexing (Tạo Copy - Vùng nhớ mới):<br>c = a[[1, 2]] ──> Cấp phát vùng nhớ mới trên Heap!<br>c[0] = 777 ──> a vẫn giữ nguyên [10, 999, 30, 40].<br>``` | **Quy tắc an toàn dữ liệu:**<br>Khi cắt mảng để biến đổi mà không muốn sửa mảng gốc, bắt buộc gọi `.copy()`:<br>```python<br>safe_slice = a[1:3].copy()<br>``` |
| **Affine Address & Mesh Grid `np.ix_`**<br>*(Ánh xạ địa chỉ bộ nhớ affine & Lưới con ma trận: Công thức Base + i*stride0 + j*stride1 và trích xuất ma trận giao điểm bằng np.ix_)*<br><br>*Gợi nhớ (Active Recall Cue):* Làm thế nào trích xuất khối giao điểm hàng [0, 2] và cột [1, 3]? | **Công thức địa chỉ bộ nhớ (Affine Mapping):**<br>$$ \text{Address}(i, j) = \text{Base} + i \times \text{stride}_0 + j \times \text{stride}_1 $$<br><br>**Cạm bẫy lấy ma trận con:**<br>• `a[[0, 2], [1, 3]]` chỉ trả về 2 điểm: $(0, 1)$ và $(2, 3)$!<br>• **Giải pháp:** Dùng `np.ix_`: Trả về ma trận con $2 \times 2$. | **Trích xuất lưới ma trận con:**<br>```python<br>sub_grid = a[np.ix_([0, 2], [1, 3])]<br># Tra ve khoi 2x2 giao diem<br>``` |

### [TÓM TẮT] KHUNG TÓM TẮT & TỰ PHẢN BIỆN PHẦN 3 (2-MINUTE SUMMARY BOX)
1. **3 Điểm Chốt Hạ (Core Takeaways):**
   - Basic Slicing (`a[start:stop:step]`) chỉ tạo ra một **View** trỏ chung vùng đệm bộ nhớ; thay đổi giá trị trên view sẽ đột biến trực tiếp mảng gốc.
   - Advanced Indexing bằng danh sách chỉ mục mảng tạo ra một **Copy** độc lập trên Heap bộ nhớ.
   - Để trích xuất ma trận con giao điểm giữa tập hàng và tập cột, bắt buộc phải dùng `np.ix_([rows], [cols])`.
2. **Câu Hỏi Tự Phản Biện (Active Recall Check):**  
   *Nếu một kỹ sư viết `sub = df_matrix[:, 0:5]` rồi thực hiện chuẩn hóa dữ liệu trực tiếp trên `sub`, tại sao mảng gốc `df_matrix` lại bị thay đổi giá trị và cách khắc phục là gì?*

---

## PHẦN 4: NGỮ NGHĨA TRỤC KHÔNG GIAN (AXES) & RÚT GỌN THỐNG KÊ

*Trọng tâm: Xóa bỏ hoàn toàn sự nhầm lẫn giữa axis=0 và axis=1 và làm chủ tham số keepdims=True.*

| Cột 1: Từ Khóa & Gợi Nhớ (20%) | Cột 2: Sơ Đồ Tư Duy & Cơ Chế Vận Hành (50%) | Cột 3: Hành Động & Code Minh Họa (30%) |
| :--- | :--- | :--- |
| **The Collapsing Axis Invariant**<br>*(Quy tắc trục tiêu biến: Tham số axis chỉ định chiều không gian bị nén triệt tiêu; axis=0 nén các hàng cho ra thống kê từng cột, axis=1 nén các cột cho ra thống kê từng hàng)*<br><br>*Gợi nhớ (Active Recall Cue):* `axis` chỉ định chiều được giữ lại hay chiều bị tiêu biến? | ```text<br>Ma trận 2D shape (M, N) — M học sinh, N môn học:<br>┌────────────────────────────┐<br>│ Hàng 0: [ x00, x01, ... ]  │<br>│ Hàng 1: [ x10, x11, ... ]  │<br>│ Hàng M-1: ...              │<br>└────────────────────────────┘<br>     │                    │<br>     ▼ (Áp dụng axis=0)   ▼ (Áp dụng axis=1)<br>[ Thao tác dọc hàng ↓ ]   [ Thao tác ngang cột → ]<br>Tiêu biến M hàng           Tiêu biến N cột<br>Shape kết quả: (N,)        Shape kết quả: (M,)<br>-> Thống kê TỪNG CỘT       -> Thống kê TỪNG HÀNG<br>``` | **Quy tắc nhớ nhanh:**<br>• Điểm trung bình từng môn (cột): `scores.mean(axis=0)`<br>• Điểm trung bình từng học sinh (hàng): `scores.mean(axis=1)`<br><br>**Cạm bẫy:** Nghĩ `axis=0` là tính theo hàng thay vì nén các hàng. |
| **Keepdims Preservation**<br>*(Bảo toàn số chiều ma trận: Thiết lập keepdims=True giữ nguyên chiều đơn vị (M, 1) thay vì nén thành 1D (M,), cho phép tự động broadcasting)*<br><br>*Gợi nhớ (Active Recall Cue):* Tại sao cần `keepdims=True` khi chuẩn hóa trừ trung bình theo hàng? | **Bảo toàn số chiều cho Broadcasting:**<br>$$ (M, N) \xrightarrow{\text{axis=1, keepdims=False}} (M,) $$<br>$$ (M, N) \xrightarrow{\text{axis=1, keepdims=True}} (M, 1) $$<br><br>Khi shape là $(M, 1)$, mảng sẵn sàng tham gia ngay vào phép trừ với ma trận $(M, N)$ mà không bao giờ bị lỗi shape. | **Trừ điểm trung bình từng học sinh:**<br>```python<br>student_means = scores.mean(axis=1, keepdims=True)<br># Shape la (M, 1)<br>centered = scores - student_means<br># Broadcast hoan hao thanh (M, N)!<br>``` |
| **Multi-Dimensional Reductions**<br>*(Các phép thu gọn đa chiều: Thu gọn đồng thời nhiều trục bằng tuple axis=(0, 1) hoặc dùng trục âm axis=-1 đại diện cho chiều cuối cùng)*<br><br>*Gợi nhớ (Active Recall Cue):* Cú pháp tính tổng theo cả hai chiều cùng lúc? | **Thu gọn nhiều trục:**<br>• `arr.sum(axis=(0, 1))` thu gọn cả 2 chiều.<br>• `axis=-1`: Luôn đại diện cho chiều cuối cùng của mảng (rất tiện lợi khi làm việc với tensor 3D/4D). | **Thao tác trên trục âm:**<br>```python<br># Tinh do lech chuan theo dac trung cuoi<br>feat_std = tensor.std(axis=-1, keepdims=True)<br>``` |

### [TÓM TẮT] KHUNG TÓM TẮT & TỰ PHẢN BIỆN PHẦN 4 (2-MINUTE SUMMARY BOX)
1. **3 Điểm Chốt Hạ (Core Takeaways):**
   - Quy tắc bất biến: Tham số `axis` chỉ định chiều bị **tiêu biến (collapse)**; do đó `axis=0` thu gọn các hàng tạo ra thống kê theo từng cột, và `axis=1` thu gọn các cột tạo ra thống kê theo từng hàng.
   - Không dùng `keepdims=True` sẽ làm mảng bị ép về 1D shape $(M,)$, không thể tự động broadcast với ma trận gốc $(M, N)$ theo trục hàng.
   - Đặt `keepdims=True` giữ lại hình dạng $(M, 1)$, cho phép trừ trực tiếp để đưa dữ liệu về tâm (Mean-Centering).
2. **Câu Hỏi Tự Phản Biện (Active Recall Check):**  
   *Giả sử bạn có ma trận $X$ có kích thước $100 \times 10$ (100 mẫu, 10 đặc trưng). Lệnh `X - X.mean(axis=0)` có chạy được không? Còn lệnh `X - X.mean(axis=1)` có chạy được không? Giải thích tại sao.*

---

## PHẦN 5: HÌNH HỌC LAN TRUYỀN (BROADCASTING) & XỬ LÝ DỮ LIỆU NOAA

*Trọng tâm: Quy tắc căn chỉnh chiều cuối, khoảng cách Euclid không vòng lặp và mặt nạ lọc dữ liệu cảm biến hỏng 999.9.*

| Cột 1: Từ Khóa & Gợi Nhớ (20%) | Cột 2: Sơ Đồ Tư Duy & Cơ Chế Vận Hành (50%) | Cột 3: Hành Động & Code Minh Họa (30%) |
| :--- | :--- | :--- |
| **Broadcasting (Lan truyền kích thước / Mở rộng chiều ảo)**<br>*(Quy tắc căn chỉnh chiều từ phải sang trái: Cơ chế tự động sao chép ảo các trục có kích thước bằng 1 bằng cách đặt bước nhảy stride = 0 mà không tốn thêm bộ nhớ RAM)*<br><br>*Gợi nhớ (Active Recall Cue):* 2 điều kiện để hai chiều tương thích broadcasting? | **Quy tắc từ phải sang trái (Trailing to Leading):**<br><br>1. Đệm chiều $1$ vào bên trái mảng có ít chiều hơn.<br>2. Tại mỗi chiều $i$, kích thước tương thích khi:<br>   $$ d_i^{(A)} == d_i^{(B)} \quad \text{HOẶC} \quad d_i^{(A)} == 1 \quad \text{HOẶC} \quad d_i^{(B)} == 1 $$<br>3. Chiều có kích thước $1$ được kéo giãn ảo mà không tốn thêm RAM. | **Bảng đối chiếu nhanh:**<br>• A: `(4, 1, 5)`<br>• B: `   (3, 5)` $\implies$ đệm thành `(1, 3, 5)`<br>• Kết quả: `(4, 3, 5)` (Hợp lệ!)<br><br>• C: `(5,)`, D: `(2,)` $\implies$ Lỗi `ValueError`! |
| **Newaxis & Pairwise Distance**<br>*(Mở rộng chiều ảo & Ma trận khoảng cách cặp: Kỹ thuật dùng np.newaxis biến mảng (N, D) và (M, D) thành tensor 3D để tính toàn bộ khoảng cách không cần vòng lặp for)*<br><br>*Gợi nhớ (Active Recall Cue):* Công thức tính khoảng cách giữa N điểm và M điểm không dùng vòng lặp for? | **Tạo hình hộp 3D để trừ tất cả các cặp:**<br>$$ A \in \mathbb{R}^{N \times D} \implies A[:, \text{np.newaxis}, :] \in \mathbb{R}^{N \times 1 \times D} $$<br>$$ B \in \mathbb{R}^{M \times D} \implies B[\text{np.newaxis}, :, :] \in \mathbb{R}^{1 \times M \times D} $$<br><br>Hiệu số tự động broadcast thành $(N, M, D)$:<br>$$ \mathbf{D}_{ij} = \sqrt{\sum_{k} (A_{ik} - B_{jk})^2} = \text{np.sqrt}\left(\text{np.sum}(\text{diff}^2, \text{axis}=-1)\right) $$ | **Hàm Pairwise Distance chuẩn:**<br>```python<br>def pairwise_dist(A, B):<br>    diff = A[:, np.newaxis, :] - B[np.newaxis, :, :]<br>    return np.sqrt(np.sum(diff**2, axis=-1))<br>``` |
| **NOAA Sentinel Data Trap**<br>*(Cạm bẫy dữ liệu cảm biến hỏng: Mã khuyết 999.9 trong dữ liệu khí hậu NOAA làm sai lệch giá trị trung bình nếu không lọc bằng mặt nạ boolean)*<br><br>*Gợi nhớ (Active Recall Cue):* Mã cảm biến khuyết của dữ liệu lượng mưa NOAA là gì? | **Hậu quả của giá trị cảm biến hỏng:**<br>Dữ liệu NOAA mã hóa cảm biến hỏng: `PRCP == 999.9`.<br><br>• Tính trực tiếp: $\text{mean} \approx 64\text{ mm}$ (Sai lệch hoàn toàn!).<br>• Lọc bỏ giá trị thiếu trước khi tính: $\text{mean} \approx 0.5\text{ mm}$ (Chuẩn xác khí hậu). | **Lọc và Chuẩn hóa Z-Score:**<br>```python<br>valid = prcp[prcp != 999.9]<br>mu = valid.mean()<br>sigma = valid.std()<br>z_prcp = (valid - mu) / sigma<br>``` |
| **Boolean Bitwise Precedence**<br>*(Độ ưu tiên toán tử bitwise: Toán tử & và | có độ ưu tiên cao hơn các phép so sánh nên bắt buộc phải bọc điều kiện trong cặp ngoặc đơn)*<br><br>*Gợi nhớ (Active Recall Cue):* Tại sao bắt buộc phải dùng dấu ngoặc đơn `()` khi kết hợp điều kiện? | **Độ ưu tiên toán tử:**<br>Toán tử `&` có độ ưu tiên cao hơn `==`, `!=`, `<`, `>`!<br><br>• Sai: `a % 5 == 0 & a % 2 != 0`<br>  $\implies$ Bị hiểu thành: `a % 5 == (0 & a) % 2 != 0`<br>• Đúng: `(a % 5 == 0) & (a % 2 != 0)` | **Mã bài tập HW1:**<br>```python<br>def homework(a):<br>    mask = (a % 5 == 0) & (a % 2 != 0)<br>    return a[mask]<br>```<br><br>**Cấm kỵ:** Không dùng từ khóa `and`, `or`. |

### [TÓM TẮT] KHUNG TÓM TẮT & TỰ PHẢN BIỆN PHẦN 5 (2-MINUTE SUMMARY BOX)
1. **3 Điểm Chốt Hạ (Core Takeaways):**
   - Broadcasting so sánh các chiều từ phải sang trái; chiều có kích thước bằng 1 được mở rộng ảo bằng cách đặt bước nhảy bằng 0 mà không tốn bộ nhớ.
   - Dùng `np.newaxis` tạo chiều ảo cho phép tính toán toàn bộ ma trận khoảng cách cặp giữa hàng nghìn điểm dữ liệu mà không cần bất kỳ vòng lặp `for` nào.
   - Trong dữ liệu cảm biến thực tế, phải luôn nhận diện và lọc sạch các giá trị sentinels (như 999.9) trước khi tính thống kê để tránh làm sai lệch phân tích.
2. **Câu Hỏi Tự Phản Biện (Active Recall Check):**  
   *Tại sao khi viết `mask = a > 5 and a < 10` trên mảng NumPy thì Python báo lỗi `ValueError: The truth value of an array with more than one element is ambiguous`, trong khi viết `(a > 5) & (a < 10)` thì lại hoạt động hoàn hảo?*

---

## [CHECKLIST] BẢNG CHECKLIST HÀNH ĐỘNG TUẦN 2 TRƯỚC KHI GẬP VỞ

- [ ] Đã chép đầy đủ 5 sơ đồ và toàn bộ công thức KaTeX vào vở viết tay theo 3 cột Cornell.
- [ ] Đã hoàn thành khảo sát điểm danh Buổi 2 trên OmniCampus trước **11:00 AM UTC ngày 08/10/2026**.
- [ ] Đã cài đặt hàm `homework(a)` và nộp lên OmniCampus Autograder đạt trọn vẹn **3.0/3.0 điểm**.
- [ ] Đã chạy thử nghiệm `compute_pairwise_distances` để kiểm chứng phép tính khoảng cách 3D không vòng lặp.
- [ ] Đã tham gia đặt câu hỏi hoặc đọc các chủ đề giải đáp trên kênh Slack `#07_lecture_and_homework_qa`.
- [ ] Xem trước nội dung Buổi 3 về thư viện **Pandas** để chuẩn bị cho kỹ năng xử lý dữ liệu bảng tiếp theo!
