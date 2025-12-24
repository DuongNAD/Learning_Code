package Day5;

import java.util.Scanner;

public class SinhVien {
    private String hoTen;
    private Double diemTB;

    public SinhVien() {

    }

    public SinhVien(String hoTen, Double diemTB){
        this.hoTen=hoTen;
        this.diemTB=diemTB;
    }

    public String getHoTen() {
        return hoTen;
    }
    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public Double getDiemTB() {
        return diemTB;
    }
    public void setDiemTB(Double diemTB) {
        if (diemTB >= 0 && diemTB <= 10) { // Ví dụ về kiểm tra tính hợp lệ
            this.diemTB = diemTB;
        } else {
            System.out.println("Điểm không hợp lệ! Điểm phải từ 0 đến 10.");
            System.exit(0);
        }
    }

    public void nhap(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap ho ten: ");
        setHoTen(scanner.nextLine());

        System.out.print("Nhap diem tb: ");
        setDiemTB(scanner.nextDouble());
    }

    public void xuat() {
        System.out.println("Ho va ten: " +hoTen);
        System.out.println("Nhap diem tb: " +diemTB);
        System.out.println("Xep loa: " + xepLoai());
    }

    public String xepLoai(){
         if(diemTB>=9){
             return "Gioi";
         }
         if(diemTB>=7){
             return "Kha";
         }
         if(diemTB>=4){
             return "Trung binh";
         }
         return "Yeu";
    }
}
