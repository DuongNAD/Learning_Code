package BTVN.Day3;

import java.util.Scanner;

public class SanPhamB4 {

    private String tenSp;
    private double donGia;
    private double giamGia;

    public void input(){
        Scanner scanner =  new Scanner(System.in);
        System.out.print("Nhap ten san pham: ");
        tenSp = scanner.nextLine();
        System.out.print("Nhap don gia: ");
        donGia = scanner.nextDouble();
        System.out.print("Nhap giam gia: ");
        giamGia = scanner.nextDouble();
    }

    public String getTenSp() {
        return tenSp;
    }
    public void setTenSp(String tenSp) {
        this.tenSp = tenSp;
    }

    public double getDonGia() {
        return donGia;
    }
    public void setDonGia(double donGia) {
        this.donGia = donGia;
    }
    public double getGiamGia() {
        return giamGia;
    }
    public void setGiamGia(double giamGia) {
        this.giamGia = giamGia;
    }

    public void output(){
        System.out.println(">> Ten san pham: " + tenSp);
        System.out.println(">> Don gia: " + donGia);
        System.out.println(">> Giam gia: " + giamGia);
    }
}
