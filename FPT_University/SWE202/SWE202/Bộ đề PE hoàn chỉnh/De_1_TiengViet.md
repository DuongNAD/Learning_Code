# ĐỀ THI THỰC HÀNH – NHẬP MÔN CÔNG NGHỆ PHẦN MỀM (SWE202c – Đề Mẫu 2026)

**Chủ đề:** Hệ thống Quản lý Phòng khám Thông minh (SHCMS)  
**Thời gian:** 120 phút  
**Công cụ:** MS Word, Draw.io, MS Visio, Astah, Visual Paradigm, StarUML  
**Lưu ý:** Được mở tài liệu. KHÔNG được dùng Internet.

---

## I. TÌNH HUỐNG (CASE STUDY)

MediCare Plus là một phòng khám đa khoa hiện đại với 15 khoa và hơn 100 bác sĩ. Hiện tại, việc đặt lịch hẹn và quản lý hồ sơ bệnh nhân được xử lý thủ công qua điện thoại và hồ sơ giấy, dẫn đến thời gian chờ lâu, mất dữ liệu và khó theo dõi tiền sử bệnh dài hạn. Ban giám đốc đã quyết định đặt hàng xây dựng **Hệ thống Quản lý Phòng khám Thông minh (SHCMS)**, hoạt động trên cả nền tảng Web và Mobile.

SHCMS dự kiến phục vụ bốn nhóm người dùng chính:

- **Bệnh nhân (Patients)** cần đăng ký tài khoản, tìm bác sĩ theo chuyên khoa, đặt lịch hẹn trong các khung giờ trống, nhận email nhắc nhở, và xem kết quả xét nghiệm/đơn thuốc trực tuyến. Nếu khung giờ đã đầy, bệnh nhân có thể tham gia "Danh sách chờ ưu tiên" (Priority Waitlist); nếu có người hủy lịch, hệ thống tự động đẩy người đầu tiên trong danh sách lên.

- **Bác sĩ (Doctors)** cần xem lịch hẹn hàng ngày, cập nhật hồ sơ bệnh án điện tử (chẩn đoán, triệu chứng), kê đơn thuốc điện tử (e-prescription), và yêu cầu xét nghiệm.

- **Nhân viên y tế / Lễ tân (Medical Staff / Receptionists)** chịu trách nhiệm xác nhận lịch hẹn, thực hiện check-in bệnh nhân, quản lý lịch trực bác sĩ, và tạo hóa đơn.

- **Quản trị viên hệ thống (System Administrator)** quản lý tài khoản người dùng, cấu hình tham số hệ thống, và đảm bảo sao lưu dữ liệu an toàn.

Về mặt kỹ thuật, phòng khám đặt ra các ràng buộc sau:
- Hệ thống phải xử lý ít nhất **500 yêu cầu đặt lịch đồng thời** với thời gian phản hồi dưới **2 giây**.
- Dữ liệu y tế rất nhạy cảm → tất cả dữ liệu lưu trữ phải mã hóa **AES-256**, truyền tải phải dùng **TLS 1.3**.
- Hệ thống phải có **Xác thực đa yếu tố (MFA)** cho bác sĩ và admin.
- Nền tảng phải đạt **99.9% thời gian hoạt động** (High Availability).
- Kiến trúc nên dùng **Microservices** để mở rộng theo chiều ngang và dễ tích hợp module mới trong tương lai (ví dụ: xử lý yêu cầu bảo hiểm).

---

## II. CÂU HỎI

> Trả lời TẤT CẢ các câu dựa trên case study SHCMS. Dùng ký hiệu UML chuẩn khi cần.

---

### Câu 1: Mô hình Phát triển Phần mềm (2.0 điểm)

- Xác định và **giải thích** mô hình phát triển phần mềm (SDLC) phù hợp nhất cho dự án SHCMS. Đề cập đến: **(1.0 điểm)**
  - Sự ổn định của yêu cầu y tế và quy định chăm sóc sức khỏe.
  - Nhu cầu phản hồi liên tục từ bác sĩ và nhân viên lâm sàng.
  - Các yếu tố rủi ro cụ thể (ví dụ: bảo mật dữ liệu y tế, tính khả dụng hệ thống).
- Chọn MỘT mô hình SDLC thay thế và **so sánh** với mô hình đã chọn. Nêu ít nhất hai ưu điểm và hai nhược điểm cho mỗi mô hình trong bối cảnh hệ thống phòng khám này. **(1.0 điểm)**

---

### Câu 2: Mô hình Use Case (1.5 điểm)

- Xác định TẤT CẢ các actor trong SHCMS. Với mỗi actor, nêu mục tiêu chính và là actor chính (primary) hay phụ (secondary). **(0.3 điểm)**
- Liệt kê ít nhất **TÁM** use case cho SHCMS. Nêu actor khởi tạo và mục tiêu một câu cho mỗi use case. **(0.4 điểm)**
- Vẽ sơ đồ Use Case UML đầy đủ cho SHCMS, bao gồm: **(0.8 điểm)**
  - Ranh giới hệ thống (system boundary), tất cả actor và use case chính.
  - Ít nhất MỘT quan hệ `<<include>>` (kèm lý do).
  - Ít nhất MỘT quan hệ `<<extend>>` (kèm lý do).

---

### Câu 3: Đặc tả Use Case (1.5 điểm)

Viết đặc tả Use Case đầy đủ cho use case **'Đặt lịch hẹn' (Book Appointment)**. Điền đầy đủ các trường: Điều kiện trước (Pre-condition), Điều kiện sau (Post-condition), Luồng chính (Basic Flow), Luồng thay thế (Alternative Flow), và Luồng ngoại lệ (Exception Flow).

---

### Câu 4: Yêu cầu phi chức năng — NFR (1.0 điểm)

- Xác định và phân loại ít nhất **BỐN** NFR từ case study vào các danh mục chất lượng (Performance, Security, Availability, Scalability). Viết một tiêu chí chấp nhận đo lường được cho mỗi NFR. **(0.6 điểm)**
- Xác định **HAI** NFR có thể xung đột với nhau. Giải thích sự xung đột và đề xuất chiến lược cân bằng (trade-off) cụ thể. **(0.4 điểm)**

---

### Câu 5: Sơ đồ Lớp — Class Diagram (1.5 điểm)

- Xác định ít nhất **SÁU** lớp miền (domain class) chính cho SHCMS. Mỗi lớp chỉ định ít nhất ba thuộc tính (kèm kiểu dữ liệu) và hai phương thức. **(0.6 điểm)**
- Vẽ sơ đồ Lớp UML đầy đủ bao gồm: **(0.9 điểm)**
  - Quan hệ kế thừa (Generalization) — ví dụ: User là lớp cha.
  - Ít nhất HAI quan hệ association có nhãn multiplicity.
  - Ít nhất MỘT quan hệ aggregation HOẶC composition (kèm lý do bằng văn bản).
  - Ít nhất MỘT quan hệ dependency.

---

### Câu 6: AI trong Lập trình (1.0 điểm)

#### Kịch bản A — AppointmentService.java (0.5 điểm)

Phương thức Java sau đây dùng để đặt lịch hẹn. Nó chứa **BA** lỗi logic hoặc nghiệp vụ.

```java
public class AppointmentService {
    public boolean bookAppointment(Patient patient, Doctor doctor, Slot slot) {
        // 1. Kiểm tra bác sĩ đã được đặt trong khung giờ này chưa
        if (doctor.getSchedule().contains(slot)) { 
            return false; // Bug 1: Logic bị ngược hoặc sai
        }
        
        // 2. Kiểm tra bệnh nhân đã có lịch hẹn khác trong cùng khung giờ chưa
        if (patient.getAppointments().stream().anyMatch(a -> a.getSlot().equals(slot))) {
            System.out.println("Patient busy");
            // Bug 2: Thiếu lệnh thoát logic hoặc return sai
        }

        // 3. Lưu lịch hẹn
        Appointment appt = new Appointment(patient, doctor, slot);
        appointmentRepo.save(appt); 
        // Bug 3: Thiếu cập nhật trạng thái cho các entity liên quan
        return true;
    }
}
```

**Nhiệm vụ:**
- Viết AI Prompt để Review Code.
- Xác định 3 bugs dựa trên logic.
- Viết AI Prompt để sửa bugs.

#### Kịch bản B — PatientDataService.java (0.5 điểm)

Phương thức này lấy lịch sử bệnh án. Nó chứa **HAI** lỗi logic và **MỘT** lỗ hổng bảo mật nghiêm trọng.

```java
public class PatientDataService {
    public List<Record> getMedicalHistory(String patientId, String authToken) {
        // Truy vấn cơ sở dữ liệu
        String sql = "SELECT * FROM records WHERE patient_id = " + patientId; // Lỗi bảo mật
        List<Record> history = db.executeNativeQuery(sql);

        // Bảo vệ: Token xác thực phải được xác minh
        if (authToken == null) { // Lỗi logic 1: Logic bị ngược
            return history; 
        }

        // Bảo vệ: Logic kiểm tra dữ liệu có tồn tại không
        if (!history.isEmpty()) { // Lỗi logic 2: Điều kiện sai khi trả dữ liệu
            return null;
        }

        return history;
    }
}
```

**Nhiệm vụ:**
- Viết AI Prompt để Review Bảo mật/Logic.
- Xác định cả 3 vấn đề (gọi tên lỗ hổng bảo mật).
- Viết AI Prompt để sửa code dùng Parameterized Queries.

---

### Câu 7: Kiểm thử — Testing (1.5 điểm)

- Ánh xạ bốn giai đoạn kiểm thử (Unit, Integration, System, Acceptance) vào SHCMS. Nêu: Kiểm thử cái gì, Ai chịu trách nhiệm, và Loại kiểm thử (Black-box/White-box). **(0.5 điểm)**
- Viết **BA** test case cho use case **'Xem kết quả xét nghiệm' (View Lab Results)**, bao gồm: **(1.0 điểm)**
  - Kịch bản thành công (Happy-path).
  - Kịch bản biên / trường hợp đặc biệt (Boundary / edge-case).
  - Kịch bản lỗi / phủ định (Negative / error) — ví dụ: truy cập trái phép.

---

**HẾT ĐỀ**
