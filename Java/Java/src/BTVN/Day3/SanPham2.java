package BTVN.Day3;

import java.util.Scanner;

public class SanPham2 {
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
        return donGia * 0.1;
    }

    public void output() {
        System.out.println(">> Ten san pha.: " + tenSanPham);
        System.out.println(">> Gia san pham: " + donGia);
        System.out.println(">> Giam gia san pham: " + giamGia);
        System.out.println(">> Thue nhap khau: " + getThueNhapKhau());
    }

    public static void main(String[] args) {
        SanPham sanPham1 = new SanPham();
        SanPham2 sanPham2 = new SanPham2();
        System.out.println("Nhap thong tin cho san pham thu 1:");
        sanPham1.input();

        System.out.println("\nNhap thong tin cho san pham thu 2:");
        sanPham2.input();

        System.out.println("\n--- THONG TIN SAN PHAM ---");
        System.out.println("--- San pham 1 ---");
        sanPham1.output();
        System.out.println("--- San pham 2 ---");
        sanPham2.output();
    }
}
