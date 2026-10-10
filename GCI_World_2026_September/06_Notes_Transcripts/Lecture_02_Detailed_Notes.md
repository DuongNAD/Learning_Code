# GCI World 2026 September — Buoi 2: Xu Ly Du Lieu Hieu Nang Cao Voi NumPy (Master Notes)

> **Khoa hoc:** Global Consumer Intelligence (GCI World 2026 September)  
> **Don vi to chuc:** Matsuo-Iwasawa Laboratory, Truong Sau dai hoc Ky thuat, Dai hoc Tokyo (The University of Tokyo)  
> **Thoi luong video bai giang chinh thuc:**
> - Video 1 (Opening): 15 phut 28 giay (928 giay) — [YouTube Official Link](https://www.youtube.com/watch?v=y54NnSpD4tg)
> - Video 2 (During Lecture): 01 gio 02 phut 35 giay (3,755 giay) — [YouTube Official Link](https://www.youtube.com/watch?v=Xg4QkVg7PAQ)
> - Video 3 (Closing): 13 phut 31 giay (811 giay) — [YouTube Official Link](https://www.youtube.com/watch?v=YJolwzY9vDE)
> - Tong thoi luong: 01 gio 31 phut 34 giay (5,494 giay)
> 
> **Giang vien & Dien gia:**
> - **Aki:** Quan ly chuong trinh, Matsuo-Iwasawa Lab (Dinh huong chuong trinh, quy che & logistics)
> - **Shun Takazawa:** Tro giang nghien cuu tai Matsuo-Iwasawa Lab, Dai hoc Tokyo; cuu hoc vien xuat sac GCI 2024 (Giang vien chinh Buoi 2)

---

## 1. Muc Luc Theo Truc Thoi Gian (Video Timeline Index)

Duoi day la bang tra cuu chi tiet toan bo noi dung tu 3 video trong Playlist Buoi 2 (PLDNJctuETAt4):

| Moc thoi gian | Phan doan & Noi dung ky thuat | Dien gia | Lien ket video |
| :--- | :--- | :--- | :--- |
| **Opening 00:00 - 01:30** | Chao mung, kiem tra am thanh, phat nhac dao dau | Aki | [00:00](https://www.youtube.com/watch?v=y54NnSpD4tg&t=0s) |
| **Opening 01:30 - 03:07** | Tom luoc Buoi 1: Nghich ly Xe Ban Do An (Food Truck), Vong lap Khoa hoc thuc nghiem & Han nop Survey Buoi 1 | Aki | [01:30](https://www.youtube.com/watch?v=y54NnSpD4tg&t=90s) |
| **Opening 03:07 - 04:30** | Gioi thieu giang vien Shun Takazawa & Dong luc hoc NumPy: Xu ly hang trieu ban ghi giao dich | Aki | [03:07](https://www.youtube.com/watch?v=y54NnSpD4tg&t=187s) |
| **Opening 04:30 - 07:20** | Thong bao he thong: Canh bao lua dao nhom WhatsApp & Quy dinh trung khop Slack Display Name voi OmniCampus | Shun | [04:30](https://www.youtube.com/watch?v=y54NnSpD4tg&t=270s) |
| **Opening 07:20 - 11:30** | Lich Office Hours thu Sau hang tuan (08:00 UTC), gioi thieu doi ngu TA & Tom luoc lo trinh 14 tuan | Shun | [07:20](https://www.youtube.com/watch?v=y54NnSpD4tg&t=440s) |
| **Opening 11:30 - 15:28** | Tong quan noi dung Buoi 2 & Huong dan mo Colab `lec2_notebook.ipynb` tren thu muc Google Drive cua khoa hoc | Shun | [11:30](https://www.youtube.com/watch?v=y54NnSpD4tg&t=690s) |
| **Lecture 00:00 - 02:20** | Khung chuong trinh 3 tuan thu vien Data Science (NumPy -> Pandas -> Matplotlib) & Triet ly hoc tap | Shun | [00:00](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=0s) |
| **Lecture 02:20 - 04:00** | On tap cu phap Python co ban: Bien, toan tu so hoc, danh sach list, tu dien dict va vong lap for | Shun | [02:20](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=140s) |
| **Lecture 04:00 - 05:54** | Khung phuong phap luan CRISP-DM & Ban chat thu vien NumPy: Viet bang C, tang toc dot pha so voi Python | Shun | [04:00](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=240s) |
| **Lecture 05:54 - 08:20** | Cu phap quy uoc `import numpy as np`, khai niem mang `ndarray` & Triet ly hoc hieu ban chat thay vi hoc vet | Shun | [05:54](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=354s) |
| **Lecture 08:20 - 12:45** | So sanh chuyen sau Python List vs `numpy.ndarray`: Kieu du lieu dong nhat, vung nho C-contiguous va SIMD | Shun | [08:20](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=500s) |
| **Lecture 12:45 - 16:55** | Ham van nang (Ufuncs): Phep toan theo tung phan tu (element-wise), cac ham toan hoc exp, log, sin, cos | Shun | [12:45](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=765s) |
| **Lecture 16:55 - 20:44** | Bo du lieu thoi tiet thuc te NOAA (TMAX, TMIN, PRCP), chuyen doi thang do va xu ly phep chia cho 0 | Shun | [16:55](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=1015s) |
| **Lecture 20:44 - 26:35** | Thuc hanh Live 2.1: Tao mang Chan/Le, phep cong ufunc vs phep noi List, chuan hoa vec-to don vi | Shun | [20:44](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=1244s) |
| **Lecture 26:35 - 29:30** | So sanh dieu kien phan tu (Boolean arrays), Co che lan truyen (Broadcasting) co ban & Cac ham thong ke | Shun | [26:35](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=1595s) |
| **Lecture 29:30 - 34:04** | Chi muc (Indexing) & Cat mang (Slicing) 1D: Quy tac 0-indexed, so am, buoc nhay step va bien can tren | Shun | [29:30](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=1770s) |
| **Lecture 34:04 - 38:07** | Mang 2 Chieu & Ma tran: Ngu nghia truc `axis=0` (doc cot) vs `axis=1` (ngang hang), tham so `keepdims` | Shun | [34:04](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=2044s) |
| **Lecture 38:07 - 44:25** | Thuc hanh Live 2.2: Loc nhiet do cac ngay Thu Hai thang 1/2010 (`jan_tmax[3::7]`), tinh mean & std | Shun | [38:07](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=2287s) |
| **Lecture 44:25 - 47:00** | Ham `reshape()` va suy dien chieu tu dong thong qua tham so `-1` | Shun | [44:25](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=2665s) |
| **Lecture 47:00 - 53:00** | Chi muc 2D: Cat hang/cot, Advanced Indexing va 3 quy tac cot loi (Axis-wise, Shape, Omitting) | Shun | [47:00](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=2820s) |
| **Lecture 53:00 - 55:30** | Chi muc luoi ma tran con voi `np.ix_()` & Phan biet Ban chieu (View) vs Ban sao (Copy) | Shun | [53:00](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=3180s) |
| **Lecture 55:30 - 58:15** | Mat na Boolean (Boolean Indexing): Loc du lieu khuyet tat NOAA (Ma cam bien hong 999.9) | Shun | [55:30](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=3330s) |
| **Lecture 58:15 - 01:02:35** | Ung dung thuc chien Machine Learning: Chuan hoa Z-Score ($z = (x - \mu)/\sigma$) & Cam bay gia tri thieu | Shun | [58:15](https://www.youtube.com/watch?v=Xg4QkVg7PAQ&t=3495s) |
| **Closing 00:00 - 01:45** | Tom tat buoi hoc, co cau 2 nhiem vu: Khao sat diem danh & Bai tap lap trinh tuan HW1 | Shun | [00:00](https://www.youtube.com/watch?v=YJolwzY9vDE&t=0s) |
| **Closing 01:45 - 03:45** | Huong dan quy trinh nop ma nguon bai tap HW1 tren cong cham tu dong OmniCampus Autograder | Shun | [01:45](https://www.youtube.com/watch?v=YJolwzY9vDE&t=105s) |
| **Closing 03:45 - 06:40** | Gioi thieu tro ly ao AI "Quri" va huong dan dang nhap bang tai khoan OmniCampus | Shun | [03:45](https://www.youtube.com/watch?v=YJolwzY9vDE&t=225s) |
| **Closing 06:40 - 08:00** | Chinh sach su dung Tri tue Nhan tao tao sinh (Generative AI): Minh bach lich su chat cho Competition & Do an | Shun | [06:40](https://www.youtube.com/watch?v=YJolwzY9vDE&t=400s) |
| **Closing 08:00 - 12:30** | Phien hoi dap truc tiep (Live Q&A): NumPy trong Hoc may & Phan tich chuyen sau gia tri khuyet 999.9 | Shun | [08:00](https://www.youtube.com/watch?v=YJolwzY9vDE&t=480s) |
| **Closing 12:30 - 13:31** | Gioi thieu noi dung Buoi 3: Xu ly du lieu bang voi Pandas & Loi chao be mac | Shun | [12:30](https://www.youtube.com/watch?v=YJolwzY9vDE&t=750s) |

---

## 2. Phan 1: Khai Mac, Quy Dinh He Thong & Dong Luc Hoc NumPy

### 2.1. On Tap Buoi 1: Nghich Ly Xe Ban Do An & Vong Lap Khoa Hoc Thuc Nghiem
Trong phan mo dau Buoi 2, co Aki da nhac lai cau hoi cot loi cua Buoi 1: *"Tai sao chung ta can nghien cuu Khoa hoc Du lieu?"*
Cau tra loi nam o viec: **Nhieu du lieu hon khong dong nghia voi viec co nhieu tri thuc hon**.

Nghich ly Xe Ban Do An (Food Truck Paradox) minh hoa sau sac nguyen ly nay:
- Tinh huong: Mot xe ban banh mi kep ghi nhan ban duoc 40 chiec trong ngay.
- Kich ban A: Banh mi ban het veo tu luc 11:30 sang. Dieu nay dong nghia voi viec chung ta da bo lo rat nhieu khach hang tiem nang (Dark Data / Unmet Demand).
- Kich ban B: Chiec banh mi cuoi cung duoc ban ngay truoc gio dong cua 18:00 chieu. So luong 40 chiec la hoan toan toi uu.
- **Ket luan nghiep vu:** Cung mot con so 40 trong co so du lieu, nhung tuy vao boi canh thoi gian va du lieu an ma hanh dong kinh doanh dua ra hoan toan trai nguoc nhau.

Chu trinh Khoa hoc Thuc nghiem (The Scientific Loop) gom 4 buoc lien hoan:
```text
┌────────────────────────────────────────────────────────┐
│ (1) HYPOTHESIZE  ──> Thiet lap gia thuyet co the do    │
│         │                                              │
│         ▼                                              │
│ (2) EXPERIMENT   ──> Thu nghiem thuc dia hoac mo hinh  │
│         │                                              │
│         ▼                                              │
│ (3) ANALYZE      ──> Phan tich bang chung so hoc       │
│         │                                              │
│         ▼                                              │
│ (4) REVISE       ──> Hieu chinh mo hinh va hanh dong   │
└────────────────────────────────────────────────────────┘
```
Ba chia khoa vang giup chu trinh van hanh hieu qua:
1. **Hypothesis-driven:** Luon xuat phat tu cau hoi nghien cuu ro rang, khong thu thap du lieu vo dinh.
2. **Actionable insights:** Du lieu phan tich ra phai dan toi quyet dinh hanh dong can thiep.
3. **Methods comparison:** Luon so sanh ket qua thuc nghiem voi mo hinh co so (Baseline).

### 2.2. Buoc Chuyen Quy Mo: Tu 1 Xe Banh Mi Den Ham Doi Do Thi
- Khi phan tich 1 xe ban banh mi don le, du lieu chi co vai chuc giao dich, ngon ngu Python thuan voi vong lap `for` van co the xu ly de dang.
- Tuy nhien, hay tuong tuong mot tap doan ban le quan ly **1,000 xe ban do an** chay khap do thi, ghi nhan giao dich theo tung phut trong suot 365 ngay.
- Dung luong du lieu lap tuc tang vot len hang chuc trieu diem du lieu ($10^6 - 10^8$ ban ghi).
- O quy mo nay, viet vong lap `for` bang Python thuan se mat hang gio de chay xong mot thu nghiem. Khi toc do phan tich bi tri tre, hoc vien khong the quay vong lap Hypothesize -> Experiment -> Analyze -> Revise mot cach linh hoat.
- **NumPy (Numerical Python)** ra doi nhu mot co che dien toan cot loi: luu tru cac con so trong cac mang da chieu dong nhat (`ndarray`), toi uu hoa bo nho o tang ngon ngu C, cho phep tinh toan song song ma khong can vong lap. Tuan hoan thu nghiem tu do duoc rut ngan tu hang chuc phut xuong vai mili-giay.

### 2.3. Thong Bao He Thong, Quy Dinh Slack & Lich Trinh
Giang vien Shun Takazawa va co Aki dua ra cac thong bao mang tinh bat buoc (RFC 2119):
1. **Canh bao lua dao nhom WhatsApp:** Ban to chuc khang dinh **KHONG CO** bat ky nhom WhatsApp chinh thuc nao. Moi lien ket moi vao nhom WhatsApp xuat hien tren Slack deu la tu phat va tiem an nguy co lua dao. Ban to chuc khong chiu trach nhiem cho bat ky su co nao phat sinh ngoai kenh Slack chinh thuc.
2. **Quy dinh bat buoc ve Display Name tren Slack:**
   - Hoc vien **MUST** doi Slack Display Name trung khop 100% voi ten tai khoan OmniCampus (vi du: `Duongne2000`).
   - Neu Display Name khong trung khop, he thong tu dong khong the doi chieu danh tinh hoc vien, dan den nguy co **mat toan bo diem so chuyen can va bai tap**.
3. **Lich Gio Tiep Sinh Vien (Office Hours):** Dien ra dinh ky vao **08:00 UTC Thu Sau hang tuan**. Day la co hoi de hoc vien trao doi truc tiep voi giang vien Shun Takazawa va cac cuu hoc vien xuat sac.
4. **Moi truong hoc tap Google Colab:** File notebook thuc hanh cua buoi hoc duoc luu tai `Google Drive / 3. Lecture Materials / Session 2 / lec2_notebook.ipynb`. Hoc vien can vao `File -> Save a copy in Drive` de luu ban sao ca nhan truoc khi chay code.

---

## 3. Phan 2: Nen Tang Dien Toan Mang Da Chieu NumPy (Technical Core)

### 3.1. Kien Truc Bo Nho: Python List vs `numpy.ndarray`
De hieu vi sao NumPy dat duoc toc do vuot troi tu 50 den 120 lan so voi Python truyen thong, ta phai phan tich kien truc vat ly cua bo nho RAM:

```text
Python List (Tap hop con tro phan tan tren Heap):
┌──────────────┐     ┌──────────────┐ ──> PyObject (int 64-bit + 28 bytes metadata)
│ List Pointer │ ──> │ Heap Ptr 0   │ ──> PyObject (int 64-bit + 28 bytes metadata)
└──────────────┘     │ Heap Ptr 1   │ ──> PyObject (int 64-bit + 28 bytes metadata)
                     │ Heap Ptr 2   │
                     └──────────────┘

NumPy ndarray (Vung dem C-Contiguous lien tuc trong RAM):
┌───────────────────────────────┐
│ Header: shape, strides, dtype │
└──────────────┬────────────────┘
               │ (Tro truc tiep den dia chi bo nho vat ly)
               ▼
┌──────────────┬──────────────┬──────────────┬──────────────┐
│  8 Bytes raw │  8 Bytes raw │  8 Bytes raw │  8 Bytes raw │  ... (Packed tightly)
└──────────────┴──────────────┴──────────────┴──────────────┘
```

1. **Python List la mang con tro bat dong nhat (Heterogeneous Array of Pointers):**
   - Moi phan tu trong list la mot con tro 64-bit tro den mot `PyObject` rieng biet nam rai rac tren bo nho Heap.
   - Moi con so nguyen trong Python ton khoang 28 bytes (chua metadata ve kieu du lieu, so luong tham chieu reference count).
   - Khi duyet qua mot list bang vong lap `for`, CPU lien tuc phai giai tham chieu con tro (pointer dereferencing), gay hien tuong mat dau vet trong bo nho dem (CPU Cache Miss). Dong thoi, trinh thong dich Python phai lien tuc kiem tra kieu du lieu dong (dynamic type checking) va chiu su kiem toa cua Global Interpreter Lock (GIL).

2. **NumPy `ndarray` la vung nho dong nhat lien tuc (C-Contiguous Memory Buffer):**
   - Ep buoc tat ca cac phan tu phai co cung mot kieu du lieu co dinh (vi du: `np.int64`, `np.float64` ton dung 8 bytes).
   - Cac byte du lieu duoc xep lien tuc sat nhau trong bo nho vat ly theo quy uoc C-order (row-major).
   - **Tinh cuc bo khong gian (Spatial Locality):** Khi CPU nap mot phan tu vao bo nho dem L1/L2, phan cung se tu dong nap nguyen ca mot dong bo nho dem (Cache Line thuong la 64 bytes, tuong duong 8 so thuc 64-bit). Cac phep tinh tiep theo dien ra ngay trong thanh ghi CPU ma khong can truy xuat lai vao RAM.

3. **Toi uu hoa phan cung bang Chi thi SIMD (Single Instruction, Multiple Data):**
   - NumPy lien ket voi cac thu vien dai so tuyen tinh cap thap viet bang C va Fortran (BLAS/LAPACK, Intel MKL).
   - Cac chi thi SIMD tren CPU hien dai (AVX-2, AVX-512) cho phep thuc thi phep tinh tren nhieu gia tri so hoc dong thoi trong mot chu ky xung nhip duy nhat:
     $$\text{Thanh ghi 512-bit}: [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8] + [b_1, b_2, \dots, b_8] \xrightarrow{1\text{ cycle}} [a_1+b_1, a_2+b_2, \dots, a_8+b_8]$$

### 3.2. Ham Van Nang (Universal Functions - ufuncs) & Xu Ly So Hoc An Toan
Trong NumPy, cac phep toan so hoc giua cac mang thuc chat la loi goi toi cac ham van nang (ufuncs) duoc bien dich san o tang C:
- Phep cong `a + b` tuong duong `np.add(a, b)`
- Phep tru `a - b` tuong duong `np.subtract(a, b)`
- Phep nhan `a * b` tuong duong `np.multiply(a, b)` (Tich Hadamard theo tung phan tu, khong phai nhan ma tran!)
- Phep chia `a / b` tuong duong `np.divide(a, b)`
- Phep luy thua `a ** b` tuong duong `np.power(a, b)`

**So sanh hanh vi phep toan voi Python List:**
```python
list_a = [1, 2]
list_b = [3, 4]
print(list_a + list_b)  # Tra ve [1, 2, 3, 4] (Noi chuoi danh sach!)
# list_a - list_b       # Nem ngoai le TypeError: unsupported operand type(s)

arr_a = np.array([1, 2])
arr_b = np.array([3, 4])
print(arr_a + arr_b)    # Tra ve array([4, 6]) (Cong dai so theo phan tu)
print(arr_a * arr_b)    # Tra ve array([3, 8])
```

#### Quy Tac Xu Ly Phep Chia Cho Khong Theo Chuan IEEE 754:
Trong Python thuan, phep chia mot so cho 0 se ngay lap tuc nem ngoai le va lam sap toan bo ung dung:
```python
10 / 0  # ZeroDivisionError: division by zero
```
Trong NumPy, phep chia mot mang so thuc cho 0 tuan thu chat che tieu chuan dau phay dong IEEE 754:
- Phep chia so duong cho 0: Tra ve `np.inf` (duong vo cuc).
- Phep chia so am cho 0: Tra ve `-np.inf` (am vo cuc).
- Phep chia 0 cho 0: Tra ve `np.nan` (Not a Number - khong phai mot con so).
- He thong chi phat ra canh bao `RuntimeWarning: divide by zero encountered` hoac `RuntimeWarning: invalid value encountered`, chu **KHONG** dung chuong trinh.
- **Cam bay hoc may:** Cac gia tri `inf` hoac `nan` nay neu khong duoc xu ly se lan truyen qua cac phep toan dai so tiep theo va lam vo mo hinh Scikit-Learn hoac PyTorch (bao loi `ValueError: Input contains NaN, infinity or a value too large`).
- **Phuong thuc kiem toan:**
  ```python
  has_inf = np.isinf(arr).any()
  has_nan = np.isnan(arr).any()
  # Loc bo cac phan tu loi
  clean_arr = arr[~np.isinf(arr) & ~np.isnan(arr)]
  ```

#### Bien Doi Logarit An Toan Voi `np.log1p` & `np.expm1`:
Khi phan tich du lieu luong mua hoac doanh thu chua nhieu so 0, viec goi `np.log(0)` se tra ve `-np.inf`. De phong ngua loi nay mot cach triet de, hoc vien **MUST** su dung ham `np.log1p`:
$$\text{np.log1p}(x) = \ln(1 + x) \implies \ln(1 + 0) = 0$$
Khi can khoi phuc lai thang do du lieu ban dau, su dung ham nguoc:
$$\text{np.expm1}(y) = e^y - 1$$

#### Chuan Hoa Vec-to Don Vi (Unit Vector Normalization):
Chuan hoa mot vec-to $\mathbf{v}$ ve do dai bang 1 giu nguyen huong:
$$\mathbf{u} = \frac{\mathbf{v}}{\|\mathbf{v}\|_2} = \frac{\mathbf{v}}{\sqrt{\sum_{i=1}^n v_i^2}}$$
```python
v = np.array([3.0, 4.0])
norm_v = np.linalg.norm(v)  # 5.0
u = v / norm_v              # array([0.6, 0.8]), co norm bang 1.0
```

---

### 3.3. Chi Muc & Cat Mang (Indexing & Slicing) Tren 1D va 2D
NumPy ap dung he thong chi muc bat dau tu 0 (0-indexed).

#### Cat mang 1 Chieu: Cu phap `array[start:stop:step]`
- `start`: Chi muc bat dau (bao gom phan tu nay).
- `stop`: Chi muc ket thuc (loai tru phan tu nay - exclusive bound).
- `step`: Buoc nhay (khoang cach giua cac chi muc, mac dinh la 1).
- Chi muc am: `-1` dai dien cho phan tu cuoi cung cua mang, `-2` la phan tu ke cuoi.

**Thuc hanh Live 2.2 — Trich xuat nhiet do cac ngay Thu Hai thang 1/2010:**
- Gia su ngay 01/01/2010 la Thu Sau (tuong ung chi muc 0).
- Trinh tu cac ngay: Thu Sau (0), Thu Bay (1), Chu Nhat (2), Thu Hai (3).
- Ngay Thu Hai dau tien roi vao chi muc 3. Chu ky lap lai giua cac ngay Thu Hai la 7 ngay (`step = 7`).
- Cu phap trich xuat:
  ```python
  monday_tmax = jan_tmax[3::7]
  mean_monday = np.mean(monday_tmax)
  std_monday = np.std(monday_tmax)
  ```

#### Chi muc va Cat mang 2 Chieu:
NumPy su dung cu phap mot cap ngoac vuong duy nhat ngan cach boi dau phay: `a[row_idx, col_idx]`.
- Trich xuat 1 hang: `a[0, :]` hoac viet tat la `a[0]`.
- Trich xuat 1 cot: `a[:, 1]` (Dau hai cham dai dien cho toan bo hang, **MUST NOT** bo quen).
- Cat khoi ma tran con: `a[0:2, 1:4]` trich xuat cac hang tu 0 den 1 va cac cot tu 1 den 3.

#### Ham `reshape()` & Suy Dien Chieu Tu Dong Voi `-1`:
Khi thay doi kich thuoc mang da chieu, tong so luong phan tu truoc va sau phai duoc bao toan tuyet doi. NumPy cho phep truyen vao gia tri `-1` tai toi da mot chieu de he thong tu tinh toan:
```python
data = np.arange(12)  # Mang 1D co 12 phan tu
matrix = data.reshape(3, -1)  # He thong tu dong suy ra shape la (3, 4)
```

---

### 3.4. Kien Truc Bo Nho: Ban Chieu (View) vs Ban Sao (Copy)
Day la nguon goc gay ra rat nhieu loi logic ngam nghiem trong trong lap trinh khoa hoc:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              BASIC SLICING TẠO RA BẢN CHIẾU (VIEW)                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Khi ta viết: b = a[1:4]                                                              │
│ • Không có dữ liệu mới nào được cấp phát trong RAM!                                    │
│ • b chỉ là một đối tượng ndarray mới trỏ chung vùng nhớ đệm với a, mang metadata:       │
│   - data_offset = 1 * itemsize                                                         │
│   - shape = (3,)                                                                       │
│   - strides = a.strides                                                                │
│ • NGUY CƠ: Nếu ta thay đổi b[0] = 999, giá trị a[1] trong mảng gốc SẼ BỊ ĐỘT BIẾN!     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                           ADVANCED INDEXING TẠO RA BẢN SAO (COPY)                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Khi ta viết: c = a[[1, 2, 3]] hoặc d = a[a > 10]                                    │
│ • NumPy cấp phát một vùng nhớ mới hoàn toàn trên Heap và sao chép từng giá trị sang.   │
│ • Nếu thay đổi c[0] = 777, mảng gốc a hoàn toàn KHÔNG bị ảnh hưởng.                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Cong Thuc Anh Xa Tuyen Tinh Bo Nho (Affine Memory Address Formula):
Dia chi byte vat ly cua phan tu tai toa do da chieu $(i_0, i_1, \dots, i_{k-1})$ duoc tinh theo he thong buoc nhay (strides):
$$\text{Memory Address}(i_0, i_1, \dots, i_{k-1}) = \text{Base Address} + \sum_{j=0}^{k-1} i_j \times \text{stride}_j$$
- Voi ma tran 2D kieu `float64` (8 bytes) kich thuoc $(M, N)$ sap xep theo C-order:
  $$\text{stride}_0 = N \times 8\text{ bytes}, \quad \text{stride}_1 = 1 \times 8\text{ bytes} = 8\text{ bytes}$$
- Khi cat mang voi buoc nhay `step`: $\text{stride}_{\text{new}} = \text{stride}_{\text{old}} \times \text{step}$.

**Quy tac an toan du lieu:** Khi can cat mang con de bien doi ma khong muon anh huong toi mang goc, hoc vien **MUST** goi phuong thuc `.copy()`:
```python
sub_array = original_array[0:5].copy()
```

---

### 3.5. Advanced Indexing & Chi Muc Luoi Ma Tran Con Voi `np.ix_`
NumPy dinh nghia 3 quy tac bat bien cho Advanced Indexing (dung danh sach chi muc nguyen):
1. **Axis-wise indexing:** Moi mang chi muc se dai dien cho toa do tren truc tuong ung.
2. **Shape and position preservation:** Hinh dang cua ket qua phan anh hinh dang cua cac mang chi muc duoc dua vao.
3. **Omitting notation:** Neu bo qua mot chieu, he thong se mac dinh lay toan bo chieu do.

**Cam bay khi trich xuat ma tran con (Submatrix Trap):**
Neu ta co ma tran $4 \times 4$ va muon lay giao diem cua cac hang $[0, 2]$ voi cac cot $[1, 3]$:
- Viet `a[[0, 2], [1, 3]]`: NumPy se ghep cap toa do $(0, 1)$ va $(2, 3)$, tra ve mang 1D co 2 phan tu: `array([a[0, 1], a[2, 3]])`. Day KHONG PHAI la ma tran con $2 \times 2$!
- **Giai phap dung dan:** Su dung `np.ix_` de tao luoi tich Descartes:
  ```python
  submatrix = a[np.ix_([0, 2], [1, 3])]
  # Tra ve ma tran 2x2 chua:
  # [[a[0, 1], a[0, 3]],
  #  [a[2, 1], a[2, 3]]]
  ```

---

### 3.6. Ngu Nghia Truc Khong Gian (Spatial Axes) & Quy Tac Truc Tieu Bien
Su nham lan giua `axis=0` va `axis=1` la tro ngai tam ly lon nhat cua nguoi moi hoc NumPy.

```text
Ma trận 2D shape (M, N) — M hàng (học sinh), N cột (môn học):
┌──────────────────────────────────────────────┐
│ Hàng 0: [ x_00,   x_01,   ...,   x_0(N-1) ]  │
│ Hàng 1: [ x_10,   x_11,   ...,   x_1(N-1) ]  │
│ ...                                          │
│ Hàng M-1: [ x_(M-1)0, ...,       x_(M-1)(N-1)]│
└──────────────────────────────────────────────┘
         │                               │
         ▼ (Áp dụng axis=0)              ▼ (Áp dụng axis=1)
   Thao tác dọc hàng (↓)          Thao tác ngang cột (→)
   TIÊU BIẾN M HÀNG                TIÊU BIẾN N CỘT
   Shape kết quả: (N,)            Shape kết quả: (M,)
   ==> THỐNG KÊ TỪNG CỘT          ==> THỐNG KÊ TỪNG HÀNG
   (Điểm trung bình từng môn)     (Điểm trung bình từng học sinh)
```

#### Quy Tac Truc Tieu Bien (The Collapsing Axis Invariant):
Gia tri cua tham so `axis` chi dinh **chieu se bi nén lai (tieu bien/eliminated)** trong qua trinh tinh toan thong ke:
- `axis=0`: Duyet doc qua tat ca cac hang, triet tieu chieu hang, giu lai ket qua cho tung cot.
- `axis=1`: Duyet ngang qua tat ca cac cot, triet tieu chieu cot, giu lai ket qua cho tung hang.

#### Vai Tro Cot Loi Cua Tham So `keepdims=True`:
Khi ap dung mot ham thu gon (nhu `mean`, `sum`, `std`):
- `scores.mean(axis=1)` se lam tieu bien chieu va dua ma tran $(M, N)$ ve mang 1D co shape $(M,)$.
- Khi muon tru diem trung binh cua tung hoc sinh khoi ma tran goc, phep tinh `scores - scores.mean(axis=1)` se nem loi `ValueError: operands could not be broadcast together` vi shape $(M, N)$ khong tuong thich truc tiep voi $(M,)$ o chieu cuoi!
- **Giai phap:** Dung `keepdims=True`:
  $$\text{Shape: } (M, N) \xrightarrow{\text{axis=1, keepdims=True}} (M, 1)$$
  Mang $(M, 1)$ se tu dong lan truyen (broadcast) hoan hao qua tat ca $N$ cot cua ma tran $(M, N)$!

---

### 3.7. Hinh Hoc Lan Truyen Kich Thuoc (Broadcasting Geometry)
Broadcasting cho phep thuc thi cac phep tinh so hoc giua cac mang co kich thuoc khac nhau ma khong can sao chep du lieu thua trong RAM.

#### Quy Tac Can Chinh Tu Chieu Cuoi Cung (Trailing Dimension Alignment Rule):
Hai mang $A$ va $B$ tuong thich broadcasting khi va chi khi:
1. So sanh kich thuoc cac chieu theo thu tu tu phai sang trai (bat dau tu chieu cuoi cung - Trailing Dimension).
2. Neu mot mang co it chieu hon, he thong se tu dong them cac chieu co kich thuoc $1$ vao **ben trai**.
3. Tai moi chieu duoc so sanh, hai kich thuoc $d_i^{(A)}$ va $d_i^{(B)}$ phai thoa man:
   $$d_i^{(A)} == d_i^{(B)} \quad \text{HOAC} \quad d_i^{(A)} == 1 \quad \text{HOAC} \quad d_i^{(B)} == 1$$
4. Chi vi tri nao co kich thuoc bang $1$ moi duoc keo gian ao (bang cach dat stride tai chieu do bang 0). Neu xuat hien cap kich thuoc khong bang nhau va khac 1 (vi du: 5 va 2), he thong se bao loi `ValueError: operands could not be broadcast together`.

**Vi du dien hinh ve Broadcasting:**
```text
Mang A (3D):  4 x 1 x 5
Mang B (2D):      3 x 5
-----------------------
1. Đệm chiều: 4 x 1 x 5
              1 x 3 x 5
2. So sánh:
   - Chiều 2: 5 == 5 (Hợp lệ)
   - Chiều 1: 1 vs 3 (Chiều 1 của A giãn thành 3)
   - Chiều 0: 4 vs 1 (Chiều 0 của B giãn thành 4)
-----------------------
Shape kết quả: 4 x 3 x 5 (Broadcasting thành công!)
```

#### Ma Tran Khoang Cach Euclid Khong Dung Vong Lap (Loopless Pairwise Distance Matrix):
Ung dung dinh cao cua Broadcasting trong Machine Learning la tinh toan khoang cach Euclid giua $N$ diem cua tap $A \in \mathbb{R}^{N \times D}$ va $M$ diem cua tap $B \in \mathbb{R}^{M \times D}$:
$$\mathbf{D}_{ij} = \sqrt{\sum_{k=1}^D (A_{ik} - B_{jk})^2}$$
Thay vi dung 2 vong lap `for` long nhau chay cham chap, ta mo rong chieu bang `np.newaxis`:
- $A[:, \text{np.newaxis}, :]$ co shape $(N, 1, D)$
- $B[\text{np.newaxis}, :, :]$ co shape $(1, M, D)$
- Hieu so $(A[:, \text{np.newaxis}, :] - B[\text{np.newaxis}, :, :])$ tu dong broadcast thanh hinh hop 3D shape $(N, M, D)$.
- Binh phuong, lay tong theo truc dac trung cuoi cung (`axis=-1`), va lay can bac hai:
```python
def compute_pairwise_distances(A, B):
    diff = A[:, np.newaxis, :] - B[np.newaxis, :, :]  # Shape: (N, M, D)
    return np.sqrt(np.sum(diff ** 2, axis=-1))        # Shape: (N, M)
```

---

### 3.8. Nghien Cuu Dien Hinh: Bo Du Lieu Thoi Tiet NOAA & Cam Bay Du Lieu Thieu
Trong bai giang, giang vien Shun Takazawa su dung bo du lieu thoi tiet thuc te tu NOAA (National Oceanic and Atmospheric Administration) de lam noi dung thuc hanh cot loi.

#### Dac ta bo du lieu:
- Duoc doc vao bang `np.loadtxt()`.
- Cac thuoc tinh: Station ID, Elevation, Latitude, Longitude, Date (YYYYMMDD).
- 3 chi so khi hau then chot:
  - `TMAX`: Nhiet do cao nhat trong ngay (don vi: $1/10$ do C).
  - `TMIN`: Nhiet do thap nhat trong ngay (don vi: $1/10$ do C).
  - `PRCP`: Luong mua tich luy trong ngay (don vi: $1/10$ mm).
- **Chuyen doi don vi:** `tmax_celsius = tmax_raw / 10.0`. Do chenh lech nhiet do trong ngay: `tmax_celsius - tmin_celsius`.

#### Cam Bay Gia Tri Thieu Cua Cam Bien (The Sensor Sentinel Trap):
- Khi cam bien khi tuong bi hong hoac mat tin hieu do bao, tram quan trac khong the de o trong ma ma hoa gia tri do bang con so cam co dac biet (Sentinel Value): **`999.9`** (hoac `9999`).
- **Tham hoa thong ke neu khong lam sach:**
  - Neu tinh truc tiep trung binh luong mua: `np.mean(PRCP)`, ket qua tra ve xap xi **64.0 mm** (mot con so qua lon, tuong duong mua bao ngap lut quanh nam!).
  - Khi dung mat na Boolean loc bo gia tri `999.9`:
    ```python
    valid_prcp = prcp[prcp != 999.9]
    actual_mean = np.mean(valid_prcp)
    ```
    Ket qua thuc te chi dat **~0.5 mm** den **1.0 mm**! Con so 64 mm hoan toan la ao giac do gia tri ngoai lai 999.9 gay ra.

#### Quy Tac Uu Tien Toan Tu Bitwise Trong Mat Na Boolean:
Khi loc mang bang dieu kien kep, hoc vien **MUST** su dung cac toan tu bitwise `&` (AND), `|` (OR), `~` (NOT), va **BAT BUOC PHAI DUNG DAU NGOAC DON `()`**:
- Toan tu bitwise `&` co do uu tien cao hon toan tu so sanh `==`, `!=`, `<`, `>`!
- Neu viet: `a % 5 == 0 & a % 2 != 0`, Python se danh gia `(0 & a)` truoc, gay sai lech toan bo logic.
- **Cu phap dung quy chuan cho Bai tap HW1:**
  ```python
  def homework(a):
      # Loc cac so chia het cho 5 nhung khong chia het cho 2 (so le chia het cho 5)
      mask = (a % 5 == 0) & (a % 2 != 0)
      return a[mask]
  ```

#### Chuan Hoa Du Lieu Z-Score (Feature Standardization):
Trong cac mo hinh hoc may nhu Gradient Descent hoac KNN:
- Nhiet do dao dong tu 20 den 35 do C.
- Luong mua dao dong tu 0 den 50 mm.
- Su chenh lech ve thang do vat ly se khien mo hinh bi thien vi vao bien co pham vi gia tri lon hon.
- **Cong thuc chuan hoa Z-Score:**
  $$z = \frac{x - \mu}{\sigma}$$
  Voi $\mu = \text{mean}(x)$ va $\sigma = \text{std}(x)$. Bien moi sau chuan hoa luon co gia tri trung binh bang 0 va do lech chuan bang 1 ($\mu_z = 0, \sigma_z = 1$).

---

## 4. Phan 3: Be Mac, Bai Tap Tuan HW1, Tro Ly Quri & Chinh Sach GenAI

### 4.1. Co Cau 2 Loai Nhiem Vu Cua Buoi 2
Ket thuc buoi hoc, giang vien Shun Takazawa nhan manh 2 deadline quan trong:
1. **Khao sat diem danh Buoi 2 (Attendance Survey):**
   - Dong link vao **11:00 AM UTC ngay 08/10/2026**.
   - Tuan thu tuyet doi chinh sach **Zero Late Policy** (khong co ngoai le nop muon).
   - Dieu kien hoan thanh khoa hoc: Nop toi thieu $\ge 7 / 14$ bai khao sat diem danh toan khoa.
2. **Bai tap lap trinh tuan 1 (Homework 1 - HW1 for Session 2):**
   - Han chót: **11:00 AM UTC ngay 08/10/2026**.
   - Thang diem:
     - Nop dung han (trong 2 tuan): Nhan toi da **3.0 diem**.
     - Nop muon (sau 2 tuan nhung trong thoi gian khoa hoc mo): Bi ap muc tran toi da **2.0 diem**.
   - Cho phep nop lai nhieu lan (Resubmission allowed), he thong se giu lai diem so cao nhat cua lan nop cuoi cung.
   - Tong diem toan khoa: Yeu cau dat toi thieu $\ge 14.0 / 24.0$ diem tren tong 8 bai tap tuan de du dieu kien tot nghiep.

### 4.2. Huong Dan Nop Bai Tren OmniCampus Autograder
Quy trinh nop bai tap HW1:
1. Mo Google Colab `lec2_notebook.ipynb`, hoan thanh ham `homework(a)`.
2. Truy cap cong dao tao OmniCampus: `https://edu.omnicamp.us/`.
3. Vao khoa hoc GCI World, cuon xuong muc **"Homework for Session 2"**.
4. Dan truc tiep doan ma nguon Python chua dinh nghia ham vao khung text box nop bai.
5. Nhan **Submit**. He thong Autograder se tu dong chay cac bo test bi mat va tra ve ket qua diem so tuc thi.

### 4.3. Tro Ly Ao AI Quri Cua Matsuo Lab
- He thong gia su AI rieng biet duoc thiet ke danh rieng cho hoc vien GCI World: `https://quri.omnicamp.us/`.
- Dang nhap truc tiep bang tai khoan OmniCampus.
- Quri duoc dao tao chuyen sau tren toan bo tai lieu khoa hoc cua Lab Matsuo, co kha nang giai dap:
  - Cac thac mac ve quy che khoa hoc, han nop bai tap.
  - So sanh cu phap Python thuan va thu vien NumPy.
  - Ho tro go loi lap trinh (Debugging) theo phuong phap su pham Socratic ma khong gian tiep tiet lo ma nguon gian lan.

### 4.4. Chinh Sach Su Dung Tri Tue Nhan Tao Tao Sinh (GenAI Policy)
- Ban to chuc **CHO PHEP** hoc vien su dung cac cong cu GenAI (ChatGPT, Claude, Quri, Gemini) nhu mot tro ly hoc tap de giai thich khai niem va ho tro tu duy.
- Tuy nhien, GenAI co the tao ra cac thong tin sai lech tinh vi (Hallucinations). Hoc vien phai chiu **trach nhiem 100%** ve do chinh xac va tinh toan ven cua ma nguon nop len he thong.
- **Yeu cau bat buoc doi voi Cuoc thi (Competition) va Do an Cuoi khoa (Final Assignment):** Hoc vien **MUST** nop kem duong dan lien ket (URL) toan bo lich su hoi thoai chat voi AI de dam bao tinh minh bach hoc thuat.

### 4.5. Phien Giai Dap Thac Mac Truc Tiep (Live Q&A Synthesis)
1. **Cau hoi 1: "NumPy duoc ung dung cu the nhu the nao trong Machine Learning?"**
   - *Tra loi cua giang vien Shun:* Trong hoc may, moi du lieu (hinh anh, am thanh, van ban, bang so lieu) deu phai duoc so hoa thanh cac ma tran hoac tensor so thuc. NumPy la nen tang tinh toan cot loi de:
     - Thuc hien tien xu ly va chuan hoa bien dac trung ($X$).
     - Tinh toan ham mat mat (Loss Function) nhu Mean Squared Error hoac Cross-Entropy.
     - Tinh toan dao ham va cap nhat trong so thong qua phep nhan ma tran truoc khi chuyen giao vao cac framework nhu PyTorch hoac Scikit-Learn.
2. **Cau hoi 2: "Tai sao gia tri trung binh luong mua lai vot len 64 mm va cach phat hien?"**
   - *Tra loi cua giang vien Shun:* Do cam bien mat ket noi ma hoa thanh 999.9. Trong thuc te, hoc vien khong bao gio duoc tin tuong du lieu tho ngay lap tuc. Truoc khi tinh toan, phai luon dung `np.unique()`, ve bieu do phan phoi hoac kiem tra cac gia tri cuc dai bat thuong de phat hien ma cam bien.

### 4.6. Gioi Thieu Buoi 3: Xu Ly Du Lieu Bang Voi Pandas
- Buoi 3 se dua nguoi hoc tu mảng so hoc thuan tuy (`ndarray`) sang cau truc du lieu bang thuc te (Data Table) voi thu vien **Pandas**.
- Noi dung trong tam: Cau truc `Series` (1D kem nhan chi muc) va `DataFrame` (2D kem ten cot va ten hang), phuong thuc xu ly du lieu khuyet (`dropna`, `fillna`), tong hop du lieu theo nhom (`groupby`), va ket noi cac bang quan he (`merge`, `join`).

---

## 5. Tong Ket Tri Thuc & Huong Dan Chuyen Giao

1. **NumPy la nen tang dien toan cot loi:** Giup giai phong khoa hoc du lieu khoi su cham chap cua Python thuan nho bo nho C-contiguous va chi thi phan cung SIMD.
2. **Ba quy tac vang can khac cot ghi tam:**
   - Luon dung `axis=0` de thu gon hang (tinh theo cot) va `axis=1` de thu gon cot (tinh theo hang).
   - Su dung `keepdims=True` de giu nguyen so chieu giup broadcasting khong bi loi.
   - Luon goi `.copy()` khi muon tach mot lat cat slicing thanh ban sao doc lap.
3. **Kiem tra hoan thanh nhiem vu truoc ngay 08/10/2026 (11:00 AM UTC):**
   - [ ] Hoan thanh khao sat diem danh Buoi 2 tren OmniCampus.
   - [ ] Nop code bai tap HW1 (`homework(a)`) len OmniCampus Autograder de dat 3.0/3.0 diem.
