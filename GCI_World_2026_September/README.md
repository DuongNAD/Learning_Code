# GCI World 2026 September — Matsuo-Iwasawa Lab (The University of Tokyo)

> Thu muc tong hop tai lieu, video bai giang, loi tat va thong tin hoc tap khoa hoc **GCI World (Global Consumer Intelligence / Data Science & AI)** do **Phong nghien cuu Matsuo-Iwasawa, Truong Sau dai hoc Ky thuat, Dai hoc Tokyo** to chuc.

---

## 1. Thong Tin Tai Khoan Hoc Vien

* **Nen tang hoc tap:** Omnicampus
* **Ho va Ten (Full Name):** `Nguyen Anh Duong`
  * **Ho (Surname / 姓):** `NGUYEN`
  * **Ten (Given Name / 名):** `ANH DUONG`
* **Account Name (Omnicampus):** `Duongne2000`
* **Ten hien thi tren Slack (Display name):** `Duongne2000` *(bat buoc trung voi Account Name)*
* **Ten day du tren Slack (Full name):** `Nguyen Anh Duong`

---

## 2. Toan Bo Duong Link Quan Trong (Course Tools & Portals)

| Cong cu | Mo ta & Chuc nang | Duong link truc tiep |
| :--- | :--- | :--- |
| **Slide Portal Hub** | Cong slide tuong tac the he moi Reveal.js 5.1.0 CDN | [Mo Master Slide Hub](slides/index.html) |
| **Slide Buoi 0** | Slide 2D: Preparatory Knowledge & DS Foundations | [Mo Slide Buoi 0](slides/00_preparatory/index.html) |
| **Slide Buoi 1** | Slide 2D: Data-Driven Mindset, Dark Data & Flywheel | [Mo Slide Buoi 1](slides/01_orientation/index.html) |
| **Slide Buoi 2** | Slide 2D: NumPy High Performance & 3 Interactive Widgets | [Mo Slide Buoi 2](slides/02_numpy/index.html) |
| **Explorable ThreeUI** | He thong hoc lieu tuong tac phan ung cao cap ThreeUI | [Mo Explorable Portal](explorable/index.html) |
| **Omnicampus** | Nen tang hoc tap, xem bai hoc & nop bai tap hang tuan | [Mo Omnicampus Course](https://edu.omnicamp.us/courses/170/) |
| **Ho so Omnicampus** | Quan ly thong tin ca nhan hoc vien, xem Account Name & ID | [Trang Profile Omnicampus](https://edu.omnicamp.us/en/profile/) |
| **Student Guide** | So tay hoc vien tren Notion: Lich hoc, noi quy, tieu chuan | [Mo Student Guide](https://app.notion.com/p/GCI-World-2026-September-Student-Guide-971cfa7cece78245925781c15c64559b) |
| **Slack Workspace** | Cong dong thao luan, hoi dap voi Tro giang (TA) | [Huong dan vao Slack](https://curved-rambutan-a71.notion.site/GCI-World-2026-September-Register-for-Slack-3accfa7cece78245925781c15c64559b) |
| **Quri AI Tutor** | Tro ly hoc tap AI chuyen sau cua khoa hoc | [Mo Quri Omnicampus](https://quri.omnicampus.us/courses/gci-world-2026-september) |

*(Link Google Drive tai lieu, Zoom (kem ma vao phong) va Q&A Form/Sheet chi luu cuc bo trong thu muc `02_Shortcuts`, khong dua len repo vi repo nay cong khai. Lay link trong Student Guide hoac Slack.)*

---

## 3. Cau Truc Thu Muc Du An

```text
GCI_World_2026_September/
|-- 01_Recordings/               # Video bai giang chinh thuc & luu tru
|   |-- Lecture_01_Orientation_Official_Recording.mp4
|   `-- archive/
|-- 02_Shortcuts/                # Loi tat truy cap nhanh (.url va .webloc)
|   |-- 12_Slide_Buoi0_Preparatory (.url & .webloc)
|   |-- 13_Slide_Buoi1_Orientation (.url & .webloc)
|   |-- 14_Slide_Buoi2_NumPy_Interactive (.url & .webloc)
|   `-- 18_Slides_Master_Hub (.url & .webloc)
|-- 03_Materials/                # Tai lieu chinh thuc tu giang vien (PDF, Notebooks)
|   |-- 00_Preparatory/          # GCI Basic Learning Materials (PDF/DOCX), Pre-lecture slides & notebooks
|   |-- 01_Orientation/          # lec1_slides.pdf
|   `-- 02_NumPy/                # lec2_slides.pdf, lec2_notebook.ipynb, HW1 for Session2.ipynb
|-- 04_Assignments/              # Thuc hanh va bai tap hang tuan (HW1..HW8)
|-- 05_Competition/              # Du an tham gia cuoc thi Machine Learning
|-- 06_Notes_Transcripts/        # Ban boc bang YouTube Session 1 & 2 (JSON + full.md)
|-- explorable/                  # He thong hoc lieu tuong tac ThreeUI Explorable
|-- roadmap/                     # ROADMAP.md = lo trinh v2 (bat dau tu day); micro roadmap & matrix cu
|-- slides/                      # He sinh thai Slide Reveal.js 5.1.0 CDN hien dai
|   |-- index.html               # Cong Portal dieu huong Slide Hub
|   |-- css/                     # Glassmorphic Theme & Widget styling
|   |-- js/                      # Reveal.js bootstrap & 3 Interactive Widgets
|   |-- 00_preparatory/          # Slide Buoi 0: Preparatory Foundations
|   |-- 01_orientation/          # Slide Buoi 1: Orientation & Data-Driven Mindset
|   `-- 02_numpy/                # Slide Buoi 2: NumPy High Performance (tich hop 3 widget)
|-- study_notes/                 # 7 bo ghi chu hoc thuat chuyen sau
|-- syllabus/                    # So tay Cornell Note (3 cot: Cues, Notes, Actions + Summary)
|-- tests/                       # Bo kiem thu tu dong pytest (100% pass)
|-- PROJECT.md                   # Dac ta kien truc he thong va tinh nang
`-- README.md                    # File tong hop thong tin khoa hoc
```

---

## 4. He Sinh Thai Slide Tuong Tac Reveal.js 5.1.0 & 3 Visualizers

He thong slide moi duoc thiet ke theo triet ly **DeepTutor Micro-Learning** va **ThreeUI Glassmorphic Design**:
* **Dieu huong 2D Ma tran:** Truc ngang (phim Mui ten trai/phai) duyet qua cac Micro-Sessions; truc doc (phim Mui ten len/xuong) dao sau vao tung buoc ly thuyet, demo tuong tac, va khung tom tat Cornell [Chep vao vo].
* **Widget 1: NumPy Broadcasting Simulator:** Mo phong truc quan quy tac trailing dimensions, highlight o ao bo nho zero-stride (`stride=0`), tinh toan ty le RAM tiet kiem so voi copy thu cong.
* **Widget 2: ndarray Indexing & Memory Strides:** Thanh truot cat lat da chieu dynamic, cong thuc anh xa dia chi bo nho tuyen tinh affine `Addr(i, j) = Base + i*stride0 + j*stride1`, hien thi song song luoi 2D va dai RAM vat ly 1D, huy hieu phan biet View (0 bytes) vs Copy (heap allocation).
* **Widget 3: Vectorization vs Python Loop Benchmark:** Thanh truot kich thuoc mang $N$ tu $10^2$ den $10^7$, duong cong SVG hieu nang thoi gian thuc, duong gioi han tran SIMD AVX-512 (~297.6x), thanh tien do dua toc do truc quan giua C/SIMD va Python interpreter.
* **Phim tat ho tro (HUD):** Nhan `?` tren slide de bat bang tro giup phim tat (`Space`, `Arrows`, `O` xem overview grid, `F` toan man hinh, `S` ghi chu dien gia).

---

## 5. Dieu Kien Nhan Chung Chi (Certificate of Completion)

Khoa hoc do **Matsuo-Iwasawa Lab (The University of Tokyo)** cap chung chi uy tin. De hoan thanh khoa hoc:
1. **Nop day du bai tap tuan (Assignments):** Lam tren Jupyter Notebook / Omnicampus va nop truoc deadline.
2. **Tham gia cuoc thi Data Competition:** Co it nhat 1 lan submit mo hinh hop le.
3. **Nop bai tap lon cuoi khoa (Final Assignment):** Nop dung han.
4. **Loi khuyen tu giang vien:**
   * Danh rieng 10-20 tieng cho Competition va 10-20 tieng cho Final Assignment.
   * Hoan thanh ban nhap chay duoc (working draft) truoc deadline it nhat 1 tuan.
