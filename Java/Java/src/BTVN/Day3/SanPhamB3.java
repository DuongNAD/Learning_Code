package BTVN.Day3;

import java.util.Scanner;

public class SanPhamB3 {

    private String tenSp;
    private double donGia;
    private double giamGia;

    public SanPhamB3(String tenSp, double donGia) {
        this(tenSp, donGia, 0);
    }

    public SanPhamB3(){

    }

    public SanPhamB3(String tenSp, double donGia, double giamGia) {
        this.tenSp = tenSp;
        this.donGia = donGia;
        this.giamGia = giamGia;
    }

    public void input() {
        Scanner scanner=new Scanner(System.in);

        System.out.println(">> Mời bạn nhập thông tin sản phẩm <<");
        System.out.print("Tên sản phẩm: ");
        this.tenSp = scanner.nextLine();

        System.out.print("Nhập đơn giá: ");
        this.donGia = scanner.nextDouble();

        System.out.print("Nhập giam gia: ");
        this.giamGia = scanner.nextDouble();
    }

    public String getTenSp() {
        return this.tenSp;
    }
    public void setTenSp(String tenSp) {
        this.tenSp = tenSp;
    }

    public double getDonGia() {
        return this.donGia;
    }
    public void setDonGia(double donGia) {
        this.donGia = donGia;
    }

    public double getGiamGia() {
        return this.giamGia;
    }
    public void setGiamGia(double giamGia) {
        this.giamGia = giamGia;
    }

    public void xuat() {
        System.out.println(">> Tên sản phẩm: " + this.tenSp);
        System.out.println(">> Đơn giá: " + this.donGia);
        System.out.println(">> Giảm giá: " + this.giamGia);
    }
}