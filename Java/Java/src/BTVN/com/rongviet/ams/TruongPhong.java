package BTVN.com.rongviet.ams;

import java.util.Scanner;

public class TruongPhong extends NhanVien {
    private double trachNhiem;

    public TruongPhong() {

    }
    public TruongPhong(String maNV, String hoTen, double luong, double trachNhiem) {
        super(maNV, hoTen, luong);
        this.trachNhiem = trachNhiem;
    }

    public double getTrachNhiem() {
        return trachNhiem;
    }
    public void setTrachNhiem(double trachNhiem) {
        this.trachNhiem = trachNhiem;
    }

    public double getThuNhap(){
        return super.getLuong() + this.trachNhiem;
    }
    @Override
    public void input(Scanner scanner){
        super.input(scanner);

        System.out.println("Nhập lương trách nhiệm: ");
        this.trachNhiem = Double.parseDouble(scanner.nextLine());
    }

    @Override
    public void output(){
        System.out.println("--- Thông tin Trưởng phòng ---");
        System.out.println("Mã nhân viên: "+ super.getMaNV());
        System.out.println("Họ tên: "+ super.getHoTen());
        System.out.println("Lương cơ bản: "+ super.getLuong());
        System.out.println("Lương trách nhiệm: " + this.trachNhiem);
        System.out.println("Tổng thu nhập: "+ this.getThuNhap());
        System.out.println("Thuế thu nhập cá nhân: " + super.getThueTN());
        System.out.println("Thu nhập ròng: " + (this.getThuNhap()-super.getThueTN()));
    }
}
