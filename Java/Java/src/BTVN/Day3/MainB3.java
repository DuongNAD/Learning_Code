package BTVN.Day3;

import java.util.Scanner;

public class MainB3 {
    public static void main(String[] args) {
        SanPhamB3 sp1 = new SanPhamB3("Sách Lập Trình Java", 250000);
        SanPhamB3 sp2 = new SanPhamB3("Bàn phím cơ", 1500000, 150000);
        System.out.println("====== THÔNG TIN SẢN PHẨM ======");

        System.out.println("\n--- Sản phẩm 1 (Không giảm giá) ---");
        sp1.xuat();
        System.out.println("\n--- Sản phẩm 2 (Có giảm giá) ---");
        sp2.xuat();
    }
}
