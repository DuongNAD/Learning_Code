package BTVN.Day5;

import java.io.*;
import java.util.*;

public class QuanLyPhuongTien {
    private PhuongTienGiaoThong[] danhSachPhuongTien = new PhuongTienGiaoThong[100];
    private int soLuongHienTai = 0;

    // Định nghĩa tên file để dễ quản lý
    private static final String OTO_FILE = "otos.csv";
    private static final String XEMAY_FILE = "xemays.csv";
    private static final String XETAI_FILE = "xetais.csv";

    // =================================================================
    // CHỨC NĂNG 1: THÊM PHƯƠNG TIỆN (Đã hoàn thiện)
    // =================================================================
    public void themPhuongTien(Scanner scanner) {
        if (soLuongHienTai >= danhSachPhuongTien.length) {
            System.out.println("Lỗi: Danh sách đã đầy, không thể thêm mới!");
            return;
        }
        System.out.println("Mời Anh chọn loại phương tiện muốn thêm:");
        System.out.println("1. Ô tô\n2. Xe máy\n3. Xe tải");
        System.out.print("Lựa chọn của Anh: ");
        int loaiXe = Integer.parseInt(scanner.nextLine());
        System.out.println("\n--- NHẬP THÔNG TIN CHUNG ---");
        String soXe = nhapSoXe(scanner);
        String nhaSanXuat = nhapNhaSanXuat(scanner);
        int namSanXuat = nhapNamSanXuat(scanner);
        System.out.print("Nhập màu xe: ");
        String mauXe = scanner.nextLine();
        System.out.println("\n--- NHẬP THÔNG TIN CHỦ XE ---");
        ChuXe chuXe = nhapThongTinChuXe(scanner);
        PhuongTienGiaoThong phuongTienMoi = null;
        switch (loaiXe) {
            case 1:
                System.out.println("\n--- NHẬP THÔNG TIN RIÊNG CỦA Ô TÔ ---");
                System.out.print("Nhập số chỗ ngồi: ");
                int soChoNgoi = Integer.parseInt(scanner.nextLine());
                System.out.print("Nhập kiểu động cơ: ");
                String kieuDongCo = scanner.nextLine();
                phuongTienMoi = new Oto(soXe, nhaSanXuat, namSanXuat, mauXe, chuXe, soChoNgoi, kieuDongCo);
                break;
            case 2:
                System.out.println("\n--- NHẬP THÔNG TIN RIÊNG CỦA XE MÁY ---");
                System.out.print("Nhập công suất (cc): ");
                int congSuat = Integer.parseInt(scanner.nextLine());
                phuongTienMoi = new XeMay(soXe, nhaSanXuat, namSanXuat, mauXe, chuXe, congSuat);
                break;
            case 3:
                System.out.println("\n--- NHẬP THÔNG TIN RIÊNG CỦA XE TẢI ---");
                System.out.print("Nhập trọng tải (tấn): ");
                double trongTai = Double.parseDouble(scanner.nextLine());
                phuongTienMoi = new XeTai(soXe, nhaSanXuat, namSanXuat, mauXe, chuXe, trongTai);
                break;
            default:
                System.out.println("Lựa chọn không hợp lệ!");
                return;
        }
        danhSachPhuongTien[soLuongHienTai] = phuongTienMoi;
        soLuongHienTai++;
        System.out.println("\n=> Đã thêm phương tiện thành công!");
    }

    // =================================================================
    // CHỨC NĂNG 2: TÌM KIẾM THEO SỐ XE (Đã hoàn thiện)
    // =================================================================
    public void timKiemTheoSoXe(Scanner scanner) {
        if (soLuongHienTai == 0) { System.out.println("Danh sách rỗng."); return; }
        System.out.print("Nhập số xe cần tìm: ");
        String soXeTim = scanner.nextLine();
        boolean timThay = false;
        for (int i = 0; i < soLuongHienTai; i++) {
            if (danhSachPhuongTien[i].getSoXe().equalsIgnoreCase(soXeTim)) {
                System.out.println("Đã tìm thấy phương tiện:");
                danhSachPhuongTien[i].hienThiThongTin();
                timThay = true;
                break;
            }
        }
        if (!timThay) {
            System.out.println("Không tìm thấy phương tiện nào với số xe: " + soXeTim);
        }
    }

    // =================================================================
    // CHỨC NĂNG 3: TÌM KIẾM THEO CMND
    // =================================================================
    public void timKiemTheoCMND(Scanner scanner) {
        if (soLuongHienTai == 0) { System.out.println("Danh sách rỗng."); return; }
        System.out.print("Nhập số CMND của chủ xe cần tìm: ");
        String cmndTim = scanner.nextLine();
        boolean timThay = false;
        System.out.println("\n--- KẾT QUẢ TÌM KIẾM ---");
        for (int i = 0; i < soLuongHienTai; i++) {
            if (danhSachPhuongTien[i].getChuXe().getSoCCCD().equals(cmndTim)) {
                danhSachPhuongTien[i].hienThiThongTin();
                timThay = true;
            }
        }
        if (!timThay) {
            System.out.println("Không tìm thấy phương tiện nào thuộc về chủ xe có CMND: " + cmndTim);
        }
    }

    // =================================================================
    // CHỨC NĂNG 4: XÓA THEO NHÀ SẢN XUẤT
    // =================================================================
    public void xoaTheoNhaSanXuat(Scanner scanner) {
        if (soLuongHienTai == 0) { System.out.println("Danh sách rỗng."); return; }
        System.out.print("Nhập tên nhà sản xuất cần xóa tất cả xe: ");
        String hangCanXoa = scanner.nextLine();

        int newIndex = 0;
        int soXeDaXoa = 0;
        // Duyệt qua danh sách, chỉ giữ lại những xe KHÔNG thuộc hãng cần xóa
        for (int i = 0; i < soLuongHienTai; i++) {
            if (!danhSachPhuongTien[i].getNhaSanXuat().equalsIgnoreCase(hangCanXoa)) {
                danhSachPhuongTien[newIndex] = danhSachPhuongTien[i];
                newIndex++;
            }
        }
        soXeDaXoa = soLuongHienTai - newIndex;
        soLuongHienTai = newIndex; // Cập nhật lại số lượng xe hiện tại

        if (soXeDaXoa > 0) {
            System.out.println("Đã xóa thành công " + soXeDaXoa + " xe của nhà sản xuất " + hangCanXoa);
        } else {
            System.out.println("Không tìm thấy xe nào của nhà sản xuất " + hangCanXoa + " để xóa.");
        }
    }

    // =================================================================
    // CHỨC NĂNG 5: TÌM HÃNG NHIỀU XE NHẤT
    // =================================================================
    public void timHangNhieuXeNhat() {
        if (soLuongHienTai == 0) { System.out.println("Danh sách rỗng."); return; }

        Map<String, Integer> demHang = new HashMap<>();
        // Đếm số lượng xe cho mỗi hãng
        for (int i = 0; i < soLuongHienTai; i++) {
            String tenHang = danhSachPhuongTien[i].getNhaSanXuat();
            demHang.put(tenHang, demHang.getOrDefault(tenHang, 0) + 1);
        }

        // Tìm hãng có số lượng lớn nhất trong Map
        String hangNhieuNhat = null;
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : demHang.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                hangNhieuNhat = entry.getKey();
            }
        }
        System.out.println("Nhà sản xuất có nhiều xe nhất là: " + hangNhieuNhat + " (" + maxCount + " xe).");
    }

    // =================================================================
    // CHỨC NĂNG 6: SẮP XẾP GIẢM DẦN THEO SỐ XE
    // =================================================================
    public void sapXepGiamDanTheoSoXe() {
        if (soLuongHienTai < 2) { System.out.println("Danh sách không đủ phần tử để sắp xếp."); return; }

        // Sử dụng Arrays.sort với một Comparator tùy chỉnh
        Arrays.sort(danhSachPhuongTien, 0, soLuongHienTai, new Comparator<PhuongTienGiaoThong>() {
            @Override
            public int compare(PhuongTienGiaoThong xe1, PhuongTienGiaoThong xe2) {
                // so sánh ngược để có thứ tự giảm dần
                return xe2.getSoXe().compareTo(xe1.getSoXe());
            }
        });

        System.out.println("Đã sắp xếp danh sách theo số xe giảm dần. Dưới đây là danh sách sau khi sắp xếp:");
        hienThiTatCa();
    }

    // =================================================================
    // CHỨC NĂNG 7: LƯU RA FILE CSV
    // =================================================================
    public void luuRaFileCsv() {
        try (
                BufferedWriter otoWriter = new BufferedWriter(new FileWriter(OTO_FILE));
                BufferedWriter xeMayWriter = new BufferedWriter(new FileWriter(XEMAY_FILE));
                BufferedWriter xeTaiWriter = new BufferedWriter(new FileWriter(XETAI_FILE))
        ) {
            for (int i = 0; i < soLuongHienTai; i++) {
                PhuongTienGiaoThong pt = danhSachPhuongTien[i];
                ChuXe cx = pt.getChuXe();
                // Chuỗi thông tin chung
                String commonData = String.join(",",
                        pt.getSoXe(), pt.getNhaSanXuat(), String.valueOf(pt.getNamSanXuat()), pt.getMauXe(),
                        cx.getSoCCCD(), cx.getHoTen(), cx.getEmail()
                );

                if (pt instanceof Oto) {
                    Oto oto = (Oto) pt;
                    String otoData = commonData + "," + oto.getSoChoNgoi() + "," + oto.getKieuDongCo();
                    otoWriter.write(otoData);
                    otoWriter.newLine();
                } else if (pt instanceof XeMay) {
                    XeMay xemay = (XeMay) pt;
                    String xeMayData = commonData + "," + xemay.getCongSuat();
                    xeMayWriter.write(xeMayData);
                    xeMayWriter.newLine();
                } else if (pt instanceof XeTai) {
                    XeTai xetai = (XeTai) pt;
                    String xeTaiData = commonData + "," + xetai.getTrongTai();
                    xeTaiWriter.write(xeTaiData);
                    xeTaiWriter.newLine();
                }
            }
            System.out.println("Đã lưu thành công danh sách phương tiện ra các file CSV.");
        } catch (IOException e) {
            System.err.println("Lỗi khi ghi file: " + e.getMessage());
        }
    }

    // =================================================================
    // CHỨC NĂNG 8: ĐỌC TỪ FILE CSV
    // =================================================================
    public void docTuFileCsv() {
        soLuongHienTai = 0; // Xóa danh sách hiện tại trước khi đọc
        docFile(OTO_FILE, "Oto");
        docFile(XEMAY_FILE, "XeMay");
        docFile(XETAI_FILE, "XeTai");
        System.out.println("Đã đọc xong dữ liệu từ các file. Danh sách hiện tại:");
        hienThiTatCa();
    }

    private void docFile(String tenFile, String loaiXe) {
        try (BufferedReader reader = new BufferedReader(new FileReader(tenFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] data = line.split(",");
                if (soLuongHienTai >= danhSachPhuongTien.length) {
                    System.err.println("Danh sách đầy, không thể đọc thêm từ file.");
                    break;
                }
                // Dữ liệu chung: soXe, nhaSX, namSX, mauXe, cmnd, ten, email
                ChuXe chuXe = new ChuXe(data[4], data[5], data[6]);
                PhuongTienGiaoThong pt = null;
                switch (loaiXe) {
                    case "Oto":
                        pt = new Oto(data[0], data[1], Integer.parseInt(data[2]), data[3], chuXe,
                                Integer.parseInt(data[7]), data[8]);
                        break;
                    case "XeMay":
                        pt = new XeMay(data[0], data[1], Integer.parseInt(data[2]), data[3], chuXe,
                                Integer.parseInt(data[7]));
                        break;
                    case "XeTai":
                        pt = new XeTai(data[0], data[1], Integer.parseInt(data[2]), data[3], chuXe,
                                Double.parseDouble(data[7]));
                        break;
                }
                if (pt != null) {
                    danhSachPhuongTien[soLuongHienTai++] = pt;
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Thông báo: không tìm thấy file " + tenFile + ", bỏ qua.");
        } catch (IOException e) {
            System.err.println("Lỗi khi đọc file " + tenFile + ": " + e.getMessage());
        }
    }

    // =================================================================
    // CHỨC NĂNG 9: THỐNG KÊ SỐ LƯỢNG XE
    // =================================================================
    public void thongKeSoLuongXe() {
        if (soLuongHienTai == 0) { System.out.println("Danh sách rỗng."); return; }

        int otoCount = 0;
        int xeMayCount = 0;
        int xeTaiCount = 0;

        for (int i = 0; i < soLuongHienTai; i++) {
            if (danhSachPhuongTien[i] instanceof Oto) {
                otoCount++;
            } else if (danhSachPhuongTien[i] instanceof XeMay) {
                xeMayCount++;
            } else if (danhSachPhuongTien[i] instanceof XeTai) {
                xeTaiCount++;
            }
        }

        System.out.println("--- BẢNG THỐNG KÊ SỐ LƯỢNG XE ---");
        System.out.println("Tổng số xe đang quản lý: " + soLuongHienTai);
        System.out.println("- Số lượng Ô tô: " + otoCount);
        System.out.println("- Số lượng Xe máy: " + xeMayCount);
        System.out.println("- Số lượng Xe tải: " + xeTaiCount);
    }

    // =================================================================
    // PHƯƠNG THỨC HỖ TRỢ HIỂN THỊ
    // =================================================================
    public void hienThiTatCa() {
        if (soLuongHienTai == 0) {
            System.out.println("Danh sách phương tiện đang rỗng.");
            return;
        }
        System.out.println("\n--- DANH SÁCH TẤT CẢ PHƯƠNG TIỆN ---");
        for (int i = 0; i < soLuongHienTai; i++) {
            danhSachPhuongTien[i].hienThiThongTin();
        }
    }

    // =================================================================
    // CÁC PHƯƠNG THỨC TRỢ GIÚP NHẬP LIỆU (HELPER METHODS)
    // =================================================================
    private String nhapSoXe(Scanner scanner) {
        String soXe;
        while (true) {
            System.out.print("Nhập số xe (đúng 5 ký tự): ");
            soXe = scanner.nextLine();
            boolean daTonTai = false;
            for (int i = 0; i < soLuongHienTai; i++) {
                if (danhSachPhuongTien[i].getSoXe().equalsIgnoreCase(soXe)) {
                    daTonTai = true;
                    break;
                }
            }
            if (soXe.length() != 5) { System.out.println("Lỗi: Số xe phải có đúng 5 ký tự. Vui lòng nhập lại."); }
            else if (daTonTai) { System.out.println("Lỗi: Số xe này đã tồn tại. Vui lòng nhập lại."); }
            else { break; }
        }
        return soXe;
    }

    private String nhapNhaSanXuat(Scanner scanner) {
        String nhaSanXuat;
        List<String> danhSachHang = Arrays.asList("Honda", "Yamaha", "Toyota", "Suzuki");
        while (true) {
            System.out.print("Nhập nhà sản xuất (Honda, Yamaha, Toyota, Suzuki): ");
            nhaSanXuat = scanner.nextLine();
            boolean hopLe = false;
            for (String hang : danhSachHang) {
                if (hang.equalsIgnoreCase(nhaSanXuat)) {
                    hopLe = true;
                    nhaSanXuat = hang;
                    break;
                }
            }
            if (hopLe) { break; }
            else { System.out.println("Lỗi: Nhà sản xuất không hợp lệ. Vui lòng nhập lại."); }
        }
        return nhaSanXuat;
    }

    private int nhapNamSanXuat(Scanner scanner) {
        int nam;
        int namHienTai = java.time.Year.now().getValue();
        while (true) {
            System.out.print("Nhập năm sản xuất (> 2000 và <= " + namHienTai + "): ");
            try {
                nam = Integer.parseInt(scanner.nextLine());
                if (nam > 2000 && nam <= namHienTai) { break; }
                else { System.out.println("Lỗi: Năm sản xuất không hợp lệ. Vui lòng nhập lại."); }
            } catch (NumberFormatException e) {
                System.out.println("Lỗi: Vui lòng nhập một số hợp lệ cho năm sản xuất.");
            }
        }
        return nam;
    }

    private ChuXe nhapThongTinChuXe(Scanner scanner) {
        String soCmnd;
        while (true) {
            System.out.print("Nhập số CCCD của chủ xe (đúng 12 số): ");
            soCmnd = scanner.nextLine();
            boolean daTonTai = false;
            for (int i = 0; i < soLuongHienTai; i++) {
                if (danhSachPhuongTien[i].getChuXe().getSoCCCD().equals(soCmnd)) {
                    daTonTai = true;
                    break;
                }
            }
            if (!soCmnd.matches("\\d{12}")) { System.out.println("Lỗi: Số CMND phải là 12 chữ số."); }
            else if (daTonTai) { System.out.println("Lỗi: Số CMND này đã tồn tại."); }
            else { break; }
        }
        System.out.print("Nhập họ tên chủ xe: ");
        String hoTen = scanner.nextLine();
        String email;
        while (true) {
            System.out.print("Nhập email chủ xe: ");
            email = scanner.nextLine();
            if (email.matches("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$")) { break; }
            else { System.out.println("Lỗi: Định dạng email không hợp lệ. Vui lòng nhập lại."); }
        }
        return new ChuXe(soCmnd, hoTen, email);
    }
}