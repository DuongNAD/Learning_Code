package BTVN.Day3;

import java.util.Scanner;

public class SanPham {
    public String tenSanPham;
    public double donGia;
    public double giamGia;
    public void input() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap ten san pham: ");
        tenSanPham = scanner.nextLine();
        System.out.print("Nhap gia san pham: ");
        donGia = scanner.nextDouble();
        System.out.print("Nhap giam gia: ");
        giamGia = scanner.nextDouble();
    }

    public double getThueNhapKhau() {
        return donGia * 10/100;
    }

    public void output() {
        System.out.println(">> Ten san pha.: " + tenSanPham);
        System.out.println(">> Gia san pham: " + donGia);
        System.out.println(">> Giam gia san pham: " + giamGia);
        System.out.println(">> Thue nhap khau: " + getThueNhapKhau());
    }

    public static void main(String[] args) {
        SanPham sanPham1 = new SanPham();
        sanPham1.input();
        sanPham1.output();
    }
}
