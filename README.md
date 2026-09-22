# 📚 02_Learning_Knowledge — Kho Tài Liệu & Dự Án Học Tập

Thư mục lưu trữ toàn bộ mã nguồn, bài tập thực hành, tài liệu nghiên cứu và ghi chú lập trình qua các ngôn ngữ, công nghệ và chủ đề khác nhau.

Toàn bộ kho lưu trữ này được đồng bộ từ Git repository:
🔗 **GitHub**: [DuongNAD/Learning_Code](https://github.com/DuongNAD/Learning_Code.git)

> 🎯 **Active Learning Hub:** Tham khảo [`ACTIVE_LEARNING.md`](./ACTIVE_LEARNING.md) để theo dõi 4–5 dự án trọng tâm và vòng quay quyết định hàng ngày (Roulette).

---

## 🗂️ Mục Lục Chủ Đề

| Chủ đề / Ngôn ngữ | Thư mục | Nội dung chính |
| :--- | :--- | :--- |
| **API** | `API/` | Thiết kế REST API, tích hợp dịch vụ bên ngoài |
| **Assembly** | `Asembly/` | Kiến trúc x86 / ASM, thanh ghi, chỉ lệnh cơ bản |
| **C Language** | `C/` | Cấu trúc dữ liệu, thuật toán, con trỏ và quản lý bộ nhớ C |
| **C# (.NET)** | `C#/` | Lập trình hướng đối tượng, ứng dụng .NET |
| **Computer Vision** | `CV/` | Xử lý ảnh số, OpenCV, thị giác máy tính |
| **Web Frontend** | `Html-Css-Js/` | HTML5, CSS3, JavaScript ES6+ căn bản |
| **Java** | `Java/` | Java Core, OOP, đa luồng và bài tập thuật toán |
| **Machine Learning** | `Machine_Learning/`, `Learning_Machine/` | Scikit-learn, hồi quy, phân loại, mạng nơ-ron |
| **PHP** | `PHP/` | Backend web script, MVC, tương tác MySQL |
| **Python** | `PythonProject/` | Thuật toán, automation scripts, xử lý dữ liệu Python |
| **Python Master** | `Python_Master/` | Bộ luyện thi Python Master 2026 (Bảng B), đề thi & chứng chỉ COS Pro |
| **Quantum Computing** | `Quantum_Computing/` | Katas thuật toán lượng tử, Qiskit / Qsim, QFT, QEC |
| **React** | `React/` | Frontend ReactJS, component lifecycle, hooks, Single Page Apps |
| **Databases / SQL** | `SQL/` | Thiết kế cơ sở dữ liệu quan hệ, truy vấn tối ưu SQL |
| **Embedded / Robotics** | `TestArm/` | Điều khiển cánh tay robot DENSO, ArUco markers, Arduino |
| **UI / UX Design** | `UI-UX/` | Thiết kế giao diện người dùng, layout, design tokens |

---

## ⚙️ Lưu Ý Khi Sử Dụng Git Trên Ổ SSD exFAT

Định dạng exFAT không lưu trữ quyền sở hữu tệp (POSIX file ownership). Do đó, Git trên cả Windows và macOS có thể cảnh báo `dubious ownership in repository`.

Để làm việc mượt mà không gặp lỗi:
1. **Trên Windows**: Chạy `Setup_Win.bat` ở thư mục gốc (hoặc chạy lệnh `git config --global --add safe.directory "D:/02_Learning_Knowledge"`).
2. **Trên macOS**: Chạy `Setup_Mac.command` ở thư mục gốc (hoặc chạy lệnh `git config --global --add safe.directory "/Volumes/KINGSTON/02_Learning_Knowledge"`).
3. **Môi trường ảo & Dependencies**: Tránh commit thư mục nặng như `node_modules` hoặc `.venv` trực tiếp lên ổ SSD exFAT để giữ hiệu năng tối đa và tránh nghẽn I/O khi quét tệp nhỏ.
