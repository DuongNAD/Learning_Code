package BTVN.com.rongviet.ams;

import java.util.Scanner;

public class TiepThi extends NhanVien{
    private double doanhSo;
    private double hueHong;

    public TiepThi(){

    }

    public TiepThi(String maNV, String hoTen, double luong, double doanhSo, double hueHong){
        super(maNV,hoTen,luong);
        this.doanhSo = doanhSo;
        this.hueHong = hueHong;
    }

    public double getDoanhSo(){
        return this.doanhSo;
    }
    public double getHueHong(){
        return this.hueHong;
    }
    public void setDoanhSo(double doanhSo){
        this.doanhSo = doanhSo;
    }
    public void setHueHong(double hueHong){
        this.hueHong = hueHong;
    }

    public double getThuNhap(){
        return super.getThuNhap() + (this.doanhSo * this.hueHong);
    }

    @Override
    public void output()
    {
        System.out.println("--- Thông tin Nhân viên Tiếp thị ---");
        System.out.println("Mã nhân viên: " + super.getMaNV());
        System.out.println("Họ tên: " + super.getHoTen());
        System.out.println("Lương cơ bản: "+ super.getLuong());
        System.out.println("Doanh số: " + this.getDoanhSo());
        System.out.println("Hoa hồng: " + this.getHueHong());

        System.out.printf(" - Tổng thu nhập: %,.0f VND\n", this.getThuNhap());
        System.out.printf(" - Thuế TNCN: %,.0f VND\n", this.getThueTN());
        System.out.printf(" - Thu nhập ròng: %,.0f VND\n", (this.getThuNhap() - this.getThueTN()));
    }

    @Override
    public void input(Scanner scanner) {
        super.input(scanner);
        System.out.println("Nhập doanh số: " + this.getDoanhSo());
        this.doanhSo = Double.parseDouble(scanner.nextLine());
        System.out.println("Nhập tỉ lệ hoa hồng (ví dụ 0.1): " + this.getHueHong());
        this.hueHong = Double.parseDouble(scanner.nextLine());
    }
}
