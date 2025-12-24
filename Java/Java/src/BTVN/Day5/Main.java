package BTVN.Day5;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        QuanLyPhuongTien quanLy = new QuanLyPhuongTien();

        System.out.println("CHÀO MỪNG TỚI HỆ THỐNG QUẢN LÝ PHƯƠNG TIỆN GIAO THÔNG");

        int luaChon;
        do {
            System.out.println("\n============== MENU ==============");
            System.out.println("1. Thêm phương tiện giao thông");
            System.out.println("2. Tìm kiếm theo số xe");
            System.out.println("3. Tìm phương tiện theo CMND chủ xe");
            System.out.println("4. Xóa phương tiện theo nhà sản xuất");
            System.out.println("5. Tìm nhà sản xuất có nhiều xe nhất");
            System.out.println("6. Sắp xếp xe theo số xe giảm dần");
            System.out.println("7. Lưu danh sách xe ra file CSV");
            System.out.println("8. Đọc dữ liệu từ file CSV");
            System.out.println("9. Thống kê số lượng theo loại xe");
            System.out.println("10. Thoát chương trình");
            System.out.println("==================================");
            System.out.print("Mời Anh nhập lựa chọn: ");

            try {
                luaChon = Integer.parseInt(scanner.nextLine());

                switch (luaChon) {
                    case 1:
                        quanLy.themPhuongTien(scanner);
                        break;
                    case 2:
                        quanLy.timKiemTheoSoXe(scanner);
                        break;
                    case 3:
                        quanLy.timKiemTheoCMND(scanner);
                        break;
                    case 4:
                        quanLy.xoaTheoNhaSanXuat(scanner);
                        break;
                    case 5:
                        quanLy.timHangNhieuXeNhat();
                        break;
                    case 6:
                        quanLy.sapXepGiamDanTheoSoXe();
                        break;
                    case 7:
                        quanLy.luuRaFileCsv();
                        break;
                    case 8:
                        quanLy.docTuFileCsv();
                        break;
                    case 9:
                        quanLy.thongKeSoLuongXe();
                        break;
                    case 10:
                        System.out.println("Cảm ơn Anh đã sử dụng chương trình. Tạm biệt!");
                        break;
                    default:
                        System.out.println("Lựa chọn không hợp lệ, vui lòng chọn lại từ 1-10.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Lỗi: Vui lòng nhập một số nguyên!");
                luaChon = 0;
            }

        } while (luaChon != 10);


    }
}