package BTVN.com.rongviet.ams;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    private static ArrayList<NhanVien> danhSachNhanVien = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while(true){
            System.out.println("\n+---------------------------------------------------+");
            System.out.println("|     CHƯƠNG TRÌNH QUẢN LÝ NHÂN SỰ CTY RỒNG VIỆT     |");
            System.out.println("+---------------------------------------------------+");
            System.out.println("| 1. Nhập danh sách nhân viên (Y1)                  |");
            System.out.println("| 2. Xuất danh sách nhân viên (Y2)                  |");
            System.out.println("| 3. Tìm và hiển thị nhân viên theo mã (Y3)         |");
            System.out.println("| 4. Xóa nhân viên theo mã (Y4)                     |");
            System.out.println("| 5. Cập nhật thông tin nhân viên theo mã (Y5)      |");
            System.out.println("| 6. Tìm các nhân viên theo khoảng lương (Y6)        |");
            System.out.println("| 7. Sắp xếp nhân viên theo họ và tên (Y7)          |");
            System.out.println("| 8. Sắp xếp nhân viên theo thu nhập (Y8)           |");
            System.out.println("| 9. Xuất 5 nhân viên có thu nhập cao nhất (Y9)     |");
            System.out.println("| 0. Kết thúc chương trình                          |");
            System.out.println("+---------------------------------------------------+");
            System.out.print(">> Mời chọn chức năng (0-9): ");

            int luaChon = Integer.parseInt(scanner.nextLine());

            switch (luaChon) {
                case 1:
                    nhapDanhSach();
                    break;
                case 2:
                    xuatDanhSach();
                    break;
                case 3:
                    timNhanVienTheoMa();
                    break;
                case 4:
                    xoaNhanVienTheoMa();
                    break;
                case 5:
                    capNhatThongTinTheoMa();
                    break;
                case 6:
                    timNhanVienTheoKhoangThuNhap();
                    break;
                case 7:
                    sapXepTheoHoTen();
                    break;
                case 8:
                    sapXepTheoThuNhap();
                    break;
                case 9:
                    xuat5NhanVienThuNhapCaoNhat();
                    break;
                case 0:
                    System.out.println("Cảm ơn đã xử dụng chương trình. Tạm biệt!");
                    System.exit(0);
                default:
                    System.out.println("Lựa chọn không hợp lệ. Vui lòng chọn lại");
            }
        }
    }


    public static void nhapDanhSach(){
        System.out.println("--- 1. Nhập danh sách nhân viên ---");
        while(true){
            System.out.println("Chọn loại nhân viên (1: Hành chính, 2: Tiếp thị, 3: Trưởng phòng, 0: Quay lại menu chính):");
            int loai = getIntInput("Mời chọn loại nhân viên");

            NhanVien nv = null;

            switch (loai) {
                case 1:
                    nv = new NhanVien();
                    break;
                case 2:
                    nv = new TiepThi();
                    break;
                case 3:
                    nv = new TruongPhong();
                    break;
                case 0:
                    return;
                default:
                    System.out.println("Lựa chọn không hợp lệ. Vui lòng chọn lại.");
                    continue;
            }
            try {
                nv.input(scanner);
                danhSachNhanVien.add(nv);
                System.out.println(">>> Thêm nhân viên thành công!");
            } catch (NumberFormatException e) {
                System.out.println("LỖI: Đã nhập sai định dạng số (lương/doanh số/...). Vui lòng nhập lại từ đầu cho nhân viên này.");
            }

            System.out.print("Bạn có muốn nhập tiếp nhân viên khác không? (Y/N): ");
            if (!scanner.nextLine().equalsIgnoreCase("Y")) {
                break;
            }
        }
    }

    public static void  xuatDanhSach(){
        System.out.println("--- 2. Xuất danh sách nhân viên ---");
        if(danhSachNhanVien.isEmpty()){
            System.out.println("Danh sách nhân viên đang rỗng");
            return;
        }

        for(NhanVien nv : danhSachNhanVien){
            nv.output();
            System.out.println("--------------------------------------");
        }
    }

    public static void  timNhanVienTheoMa(){
        System.out.println("--- 3. Tìm nhân viên theo mã ---");
        System.out.print("Nhập mã nhân viên cần tìm: ");
        String maTim = scanner.nextLine();

        NhanVien nvTim = timTheoMa(maTim);

        if(nvTim != null){
            System.out.println("Tìm thấy nhân viên");
            nvTim.output();
        }

        else {
            System.out.println("Không tìm thấy nhân viên có mã: " + maTim);
        }
    }

    public static void  xoaNhanVienTheoMa(){
        System.out.println("--- 4. Xóa nhân viên theo mã ---");
        System.out.println("Nhập mã nhân viên cần xóa: ");
        String maXoa = scanner.nextLine();

        NhanVien nvXoa = timTheoMa(maXoa);

        if(maXoa != null){
            danhSachNhanVien.remove(maXoa);
            System.out.println("Đã xóa nhân viên có mã: " + maXoa);
        }
        else{
            System.out.println("Không tìm thấy nhn viên có mã: " + maXoa);
        }
    }

    public static void capNhatThongTinTheoMa(){
        System.out.println("--- 5. Cập nhật thông tin theo mã ---");
        System.out.println("Nhập mã nhân viên cần cập nhật: ");
        String maCapNhat = scanner.nextLine();

        NhanVien nvCapNhat = timTheoMa(maCapNhat);

        if(nvCapNhat != null){
            System.out.println("Tìm thấy! Mời cập nhật thông tin (Mã NV không đổi):");
            nvCapNhat.output();
            System.out.println("--- Nhập thông tin mới ---");

            System.out.print("Nhập họ tên mới: ");
            nvCapNhat.setHoTen(scanner.nextLine());
            nvCapNhat.setLuong(getDoubleInput("Nhập lương cơ bản mới: ", 0));

            if(nvCapNhat instanceof TiepThi){
                TiepThi tiepThi = (TiepThi)nvCapNhat;
                tiepThi.setDoanhSo(getDoubleInput("Nhập doanh số mới: ",0));
                tiepThi.setHueHong(getDoubleInput("Nhập hoa hồng mới (từ 0 -> 1): ", 0));
            }
            else if(nvCapNhat instanceof TruongPhong){
                TruongPhong truongphong = (TruongPhong)nvCapNhat;
                truongphong.setTrachNhiem(getDoubleInput("Nhập lương trách nhiệm mới: ",0));
            }

            System.out.println(">>> Cập nhật thông tin thành công");
        }
        else{
            System.out.println("Không tìm thấy nhân viên nào có mã: " + maCapNhat);
        }
    }

    public static void timNhanVienTheoKhoangThuNhap(){
        System.out.println("--- 6. Tìm nhân viên theo khoảng thu nhập ---");
        if(danhSachNhanVien.isEmpty()){
            System.out.println("Danh sách rỗng");
            return;
        }

        double min = getDoubleInput("Nhập thu nhập tối thiểu: ",0);
        double max = getDoubleInput("Nhập thu nhập tối đa: ",min);

        boolean timThay = false;
        System.out.println("--- Kết quả tìm kiếm ---");

        for(NhanVien nv : danhSachNhanVien){
            if(nv.getThuNhap() >= min && nv.getThuNhap() <= max){
                nv.output();
                System.out.println("------------------------");
                timThay = true;
            }
        }
        if(!timThay){
            System.out.println("Không tìm thấy nhân viên nào có thu nhập trong khoảng này.");
        }
    }

    public static double getDoubleInput(String prompt, double min){
        while(true){
            try{
                System.out.println(prompt);
                double value = Double.parseDouble(scanner.nextLine());
                if(value < min){
                    System.out.printf("Lỗi: Giá trị phải lớn hơn hoặc bằng %.0f.\n", min);
                }
                else {
                    return value;
                }
            }
            catch (NumberFormatException e){
                System.out.println("Lỗi: Vui lòng nhập một con số hợp lệ");
            }
        }
    }

    public static void sapXepTheoHoTen(){
        System.out.println("--- 7. Sắp xếp nhân viên theo họ tên ---");
        if(danhSachNhanVien.isEmpty()){
            System.out.println("Danh sách rỗng");
            return;
        }

        danhSachNhanVien.sort(Comparator.comparing(NhanVien::getHoTen));
        System.out.println("Đã sắp xếp danh sách theo họ tên. Bạn có thể chọn chức năng 2 để xem lại.");
    }

    public static void sapXepTheoThuNhap(){
        System.out.println("--- 8. Sắp xếp nhân viên theo thu nhập ---");
        if(danhSachNhanVien.isEmpty()){
            System.out.println("Danh sách rỗng");
            return;
        }

        danhSachNhanVien.sort(Comparator.comparing(NhanVien::getThuNhap));
        System.out.println("Đã sắp xếp danh sách theo họ tên. Bạn có thể chọn chức năng 2 để xem lại.");
    }

    public static void xuat5NhanVienThuNhapCaoNhat(){
        System.out.println("--- 9. Xuất 5 nhân viên có thu nhập cao nhất ---");
        if(danhSachNhanVien.isEmpty()){
            System.out.println("Danh sách rỗng");
            return;
        }

        danhSachNhanVien.sort(Comparator.comparing(NhanVien::getThuNhap).reversed());

        int count = Math.min(5, danhSachNhanVien.size());
        System.out.printf("--- Top %d nhân viên thu nhập cao nhất ---\n", count);
        for (int i = 0; i < count; i++) {
            System.out.printf("TOP %d:\n", i + 1);
            danhSachNhanVien.get(i).output();
            System.out.println("-----------------");
        }
    }

    private static double getDoubleInput(String prompt, double min, double max) {
        while (true) {
            try {
                System.out.print(prompt);
                double value = Double.parseDouble(scanner.nextLine());
                if (value < min || value > max) {
                    System.out.printf("Lỗi: Giá trị phải nằm trong khoảng từ %.2f đến %.2f.\n", min, max);
                } else {
                    return value;
                }
            } catch (NumberFormatException e) {
                System.out.println("Lỗi: Vui lòng nhập một CON SỐ hợp lệ.");
            }
        }
    }

    private static NhanVien timTheoMa(String maNV){
        for(NhanVien nv : danhSachNhanVien){
            if(nv.getMaNV().equalsIgnoreCase(maNV)){
                return nv;
            }
        }
        return null;
    }

    public static int getIntInput(String prompt){
        while (true){
            try{
                System.out.println(prompt);
                return Integer.parseInt(scanner.nextLine());
            }
            catch (NumberFormatException e){
                System.out.println("Lỗi: Vui lòng nhập 1 số nguyên hợp lệ");
            }
        }
    }
}
