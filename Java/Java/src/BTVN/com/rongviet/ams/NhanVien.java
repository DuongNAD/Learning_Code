package BTVN.com.rongviet.ams;

import java.util.Scanner;

public class NhanVien {

    private String maNV;
    private String hoTen;
    private double luong;

    public NhanVien(){

    }

    public NhanVien(String maNV, String hoTen, double luong) {
        this.maNV = maNV;
        this.hoTen = hoTen;
        this.luong = luong;
    }

    public String getMaNV() {
        return maNV;
    }
    public void setMaNV(String maNV) {
        this.maNV = maNV;
    }
    public String getHoTen() {
        return hoTen;
    }
    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }
    public double getLuong() {
        return luong;
    }
    public void setLuong(double luong) {
        this.luong = luong;
    }

    public double getThuNhap(){
        return this.luong;
    }

    public double getThueTN(){
        double thuNhap = this.getThuNhap();
        double thue = 0;

        if(thuNhap<9000000){
            thue = 0;
        }
        else if(thuNhap>9000000 && thuNhap<15000000){
            thue = (thuNhap - 9000000) * 0.1;
        }
        else if(thuNhap>15000000){
            thue = 600000 + (thuNhap - 15000000) * 0.12;
        }
        return thue;
    }

    public void output() {
        System.out.println("Mã nhân viên: " + this.maNV);
        System.out.println("Họ tên: " + this.hoTen);
        System.out.println("Thu nhập: " + this.getThuNhap());
        System.out.println("Thuế thu nhập: " + this.getThueTN());
        System.out.println("Thu nhập ròng: " + (this.getThuNhap() - this.getThueTN()));
    }

    public void input(Scanner scanner){
        System.out.println("Nhập mã nhân viên: ");
        this.maNV = scanner.nextLine();
        System.out.println("Nhập họ tên: ");
        this.hoTen = scanner.nextLine();
        System.out.println("Nhập lương cơ bản: ");
        this.luong = Double.parseDouble(scanner.nextLine());
    }
}
