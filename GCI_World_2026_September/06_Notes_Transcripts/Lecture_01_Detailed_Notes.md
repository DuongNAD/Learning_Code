# GCI World 2026 September — Buổi 1: Định Hướng & Tổng Quan Khóa Học (Master Notes)

> **Khóa học:** Global Consumer Intelligence (GCI World 2026 September)  
> **Đơn vị tổ chức:** Matsuo-Iwasawa Laboratory, Trường Kỹ thuật, Đại học Tokyo (The University of Tokyo)  
> **Thời lượng bài giảng:** 01 giờ 09 phút 23 giây  
> **Ngày diễn ra:** 17/09/2026  
> **Tài liệu nguồn:** Trích xuất từ Video gốc, Whisper Large-v3 Turbo Transcript, 69 Slide bài giảng và mã QR.

---

## 1. Mục Tiêu & Thông Điệp Cốt Lõi

1. **Tầm nhìn khóa học GCI World**:
   - Chuyển hóa tư duy từ người học lý thuyết AI đơn thuần thành người có **"Data-driven Mindset"** (tư duy dựa trên dữ liệu) có khả năng trực tiếp triển khai giải pháp giải quyết bài toán thực tế của xã hội và doanh nghiệp.
   - Khóa học dành cho tất cả mọi người (kể cả người mới bắt đầu, sinh viên mọi ngành nghề, phi kỹ thuật).
2. **Xu hướng AI & Lợi thế cạnh tranh (Defensible Moat)**:
   - Trong thời đại bùng nổ các mô hình nền tảng (Foundation Models), việc chỉ tích lũy dữ liệu thô dạng SaaS truyền thống không còn là hào lũy vững chắc.
   - Hào lũy thật sự nằm ở việc **nhúng sâu vào quy trình làm việc (Workflow integration)** để vừa thu thập vừa liên tục sinh ra dữ liệu mới (Data Flywheel), kết hợp với kỹ thuật đặc trưng chuyên ngành (Vertical Domain-specific Engineering).
3. **Định nghĩa về Chuyên gia Dữ liệu toàn diện (Well-rounded Data Scientist)**:
   - Viết code và sử dụng AI chỉ chiếm khoảng **30 - 40%** năng lực.
   - **60 - 70%** còn lại là năng lực phát hiện vấn đề cốt lõi, tư duy kinh doanh (Business & Domain Knowledge), và kỹ năng giao tiếp truyền đạt giải pháp cho con người.

---

## 2. Bốn Công Cụ Cốt Lõi & Toàn Bộ Đường Dẫn (Đã Giải Mã Mã QR)

| Công cụ | Mục đích chính | Đường dẫn trực tiếp |
| :--- | :--- | :--- |
| **Omnicampus** | Nền tảng LMS chính thức: Nộp khảo sát điểm danh, nộp bài tập tuần, nộp bài thi, xem bảng điểm. | [https://edu.omnicamp.us/courses/170/](https://edu.omnicamp.us/courses/170/) |
| **Quri AI Assistant** | Trợ lý AI hỏi đáp 24/7 về toàn bộ nội dung bài giảng và tài liệu khóa học. | [https://quri.omnicamp.us/courses/gci-world-2026-september](https://quri.omnicamp.us/courses/gci-world-2026-september) |
| **Student Guide (Notion)** | **Cẩm nang sinh viên quan trọng nhất**: Chứa toàn bộ lịch trình, thể lệ, quy định, link Drive, phòng Zoom. | [https://app.notion.com/p/GCI-World-2026-September-Student-Guide-971cfa7cece78245925781c15c64559b](https://app.notion.com/p/GCI-World-2026-September-Student-Guide-971cfa7cece78245925781c15c64559b) |
| **Google Drive** | Kho chứa slide bài giảng, file Google Colab Notebooks, bộ dữ liệu thực hành. | Link lưu trong thư mục `02_Shortcuts` & Student Guide |
| **Slack Workspace** | Cộng đồng thảo luận, thông báo chính thức từ ban tổ chức và đội ngũ trợ giảng (TAs). | Không gian Slack GCI World |

> [!WARNING]  
> **Cảnh báo từ Ban tổ chức**: Ban tổ chức **KHÔNG** tạo hay quản lý bất kỳ nhóm WhatsApp nào. Mọi nhóm WhatsApp học viên tự tạo bên ngoài đều là tự phát và BTC không chịu trách nhiệm về các vấn đề phát sinh tại đó.

---

## 3. Bản Đồ Kênh Slack (Quy Định Giao Tiếp)

- **Các kênh chỉ thông báo (Admin Only)**:
  - `00_guideline`: Bộ hướng dẫn cơ bản cho học viên.
  - `01_general_announcements`: Thông báo chung từ Admin & TAs.
  - `02_lecture_and_homework_notices`: Lịch học, tài liệu và hạn nộp bài tập.
  - `03_competition_notices`: Thông báo về cuộc thi Machine Learning.
  - `04_final_assignment_notices`: Thông báo về đồ án tốt nghiệp cuối khóa.
  - `05_office_hours_notices`: Lịch hẹn các buổi phụ đạo giải đáp trực tiếp.
- **Các kênh hỏi đáp (Q&A)**:
  - `06_admin_qa`: Hỏi đáp thủ tục hành chính.
  - `07_lecture_and_homework_qa`: Hỏi đáp nội dung bài học và code bài tập.
  - `08_competition_qa`: Hỏi đáp về cuộc thi.
  - `09_final_assignment_qa`: Hỏi đáp về đồ án cuối khóa.
- **Kênh giao lưu & Học thuật**:
  - `10_self_introduction`: Giới thiệu bản thân (học viên bắt buộc giới thiệu nếu chưa làm).
  - `11_casual_chat`: Trò chuyện tự do.
  - `12_research_discussion`: Thảo luận các đề tài nghiên cứu chuyên sâu.

> [!IMPORTANT]  
> **Quy tắc Tên hiển thị (Display Name)**: Học viên bắt buộc phải đổi **Display Name trên Slack** trùng khớp chính xác với **Account Name trên Omnicampus** (tài khoản của bạn là: `Duongne2000`).

---

## 4. Cơ Cấu Đánh Giá & Tiêu Chuẩn Cấp Bằng / Chuyến Đi Nhật Bản

Khóa học có **3 cấp độ hoàn thành**:

```
[Khởi đầu] ──> [Completed Student] ──> [Honors Student] ──> [Outstanding Student]
                     (Chứng chỉ)             (Bằng Danh Dự)        (Chuyến đi Nhật Bản)
```

| Cấp độ hoàn thành | Quyền lợi đạt được | Điều kiện chi tiết |
| :--- | :--- | :--- |
| **1. Completed Student (Tiêu chuẩn)** | Nhận **Certificate of Completion** từ Đại học Tokyo, tham gia mạng lưới cựu học viên (Alumni). | • Điểm danh (Attendance Survey): nộp tối thiểu **7 / 14 buổi**.<br>• Bài tập tuần (Homework): đạt tối thiểu **14 / 24 điểm**.<br>• Đồ án cuối khóa (Final Assignment): Nộp và vượt qua mức chuẩn tối thiểu.<br>• Cuộc thi (Competition): Không bắt buộc. |
| **2. Honors Student (Danh dự)** | Nhận chứng chỉ hoàn thành + **Chứng chỉ Danh dự đặc biệt**; quyền tham gia các chương trình đào tạo nâng cao độc quyền. | • Đạt toàn bộ điều kiện của Tiêu chuẩn.<br>• Final Assignment: Nằm trong **Top 10%** cao nhất.<br>• Competition: Nằm trong **Top 20%** bảng xếp hạng. |
| **3. Outstanding Student (Xuất sắc)** | Chứng chỉ Xuất sắc cao nhất + **Được tài trợ tham gia chuyến Study Tour tại Tokyo, Nhật Bản** (thăm Lab Matsuo, gặp trực tiếp GS Matsuo, tham quan doanh nghiệp công nghệ Nhật). | • Chọn lọc từ nhóm học viên top đầu của danh sách Honors.<br>• Thành tích xuất sắc toàn diện cả 4 hạng mục.<br>*(Lưu ý: Học viên học lại - Returning students không được xét chuyến đi Nhật).* |

---

## 5. Chi Tiết Các Hạng Mục Bài Tập & Điểm Số

### A. Khảo sát điểm danh (Attendance Survey)
- Tổng số: **14 bài** (1 bài sau mỗi buổi học).
- Yêu cầu: Hoàn thành ít nhất **7 bài**.
- Thời gian mở: 12:00 PM UTC ngày diễn ra bài giảng.
- Thời hạn làm bài: Mở trong vòng **2 tuần** (riêng Buổi 1 mở 3 tuần, hạn chót là **11:00 AM UTC ngày 08/10/2026**).
- **Tuyệt đối không có nộp muộn (No late submission)**.

### B. Bài tập tuần (Homework)
- Tổng số: **8 bài tập** (Bắt đầu từ Buổi 2).
- Điểm tối đa: **3 điểm / bài** $\rightarrow$ Tổng tối đa **24 điểm** (Cần đạt $\ge 14$ điểm để đỗ).
- Quy chế thời gian:
  - Mở trước buổi học 1 tuần (hoặc 1 ngày sau bài giảng trước).
  - Nộp đúng hạn trong vòng **2 tuần**: Điểm tối đa **3 điểm**.
  - Nộp muộn (Late submission): Vẫn được nộp nhưng bị trừ điểm, tối đa chỉ nhận **2 điểm**.
  - Cho phép nộp lại nhiều lần để tối ưu điểm số.

### C. Đồ án chiến lược kinh doanh (Final Assignment)
- Bắt đầu mở: Dự kiến từ **Tuần 3**.
- Nội dung: Đóng vai trò Data Scientist thực tế: Phân tích thị trường $\rightarrow$ Khám phá dữ liệu $\rightarrow$ Xây dựng mô hình Machine Learning $\rightarrow$ Đánh giá mô hình $\rightarrow$ Đề xuất chiến lược kinh doanh.
- Sản phẩm nộp: Slide thuyết trình, Jupyter Notebook hoàn chỉnh, Danh mục tài liệu tham khảo.

### D. Cuộc thi Machine Learning (In-class Competition)
- Bắt đầu mở: Dự kiến từ **Tuần 3**.
- Nội dung: Cạnh tranh xây dựng mô hình dự đoán đạt điểm số cao nhất trên Leaderboard của Omnicampus.
- Sản phẩm nộp: File kết quả dự đoán + Source code.

---

## 6. Chính Sách Sử Dụng Generative AI & Bản Quyền

- **Sử dụng AI**: Được phép sử dụng Generative AI (ChatGPT, Claude, Gemini, Antigravity,...) hỗ trợ làm bài tập. Tuy nhiên:
  - Học viên phải chịu trách nhiệm về tính chính xác của kết quả.
  - Một số bài tập có thể yêu cầu nộp kèm link lịch sử hội thoại với AI để đánh giá quy trình tư duy.
  - Khuyến khích tự suy nghĩ độc lập và thảo luận trước trên Slack cùng 40.000 học viên.
- **Bảo mật tài liệu**: Nghiêm cấm chia sẻ, phát tán video, slide, notebook ra ngoài. Vi phạm sẽ bị hủy tư cách hoàn thành và thu hồi chứng chỉ.

---

## 7. Ba Bí Quyết Vàng Để Hoàn Thành Khóa Học (Pro-Tips)

1. **Attend (Tham gia ngay)**: Học trực tiếp hoặc xem lại bản ghi hình ngay trong ngày/tuần, không trì hoãn.
2. **Schedule (Khóa lịch)**: Lên lịch cố định 2 - 3 giờ mỗi tuần trong Google Calendar để học và làm bài tập.
3. **Start Early (Bắt tay làm sớm)**: Dành từ **10 - 20 giờ** cho Final Assignment và Competition. Luôn hoàn thành bản nháp chạy được (working draft) **trước deadline ít nhất 1 tuần** để có thời gian trau chuốt và tối ưu.

---

## 8. Hành Động Cần Làm Ngay (Checklist Tuần 1)

- [ ] **Làm Khảo sát điểm danh Buổi 1**: Truy cập Omnicampus $\rightarrow$ Questionnaire $\rightarrow$ Session 1 (Hạn chót: 11:00 AM UTC ngày 08/10).
- [ ] **Kiểm tra tên Slack**: Đảm bảo Display Name là `Duongne2000` trùng với tên trên Omnicampus.
- [ ] **Đọc Cẩm nang Sinh viên**: Đọc kỹ trang Notion Student Guide.
- [ ] **Lưu Bookmark các công cụ**: Đã được lưu sẵn trong thư mục `02_Shortcuts` trên ổ SSD.
- [ ] **Chuẩn bị Buổi 2**: Thứ Năm ngày 24/09/2026 (Chủ đề: Xử lý dữ liệu hiệu năng cao với NumPy).
