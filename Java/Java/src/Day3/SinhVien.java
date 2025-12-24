package Day3;

import java.util.Scanner;

public class SinhVien {
    public String name;
    public double mark;
    public String hocLuc;
    public void input() {
        Scanner scanner =new Scanner(System.in);
        System.out.print("Nhap ten: ");
        name=scanner.nextLine();
        System.out.print("Nhap diem: ");
        mark=scanner.nextDouble();
    }
    public void check() {
        if (mark >= 8.0) {
            this.hocLuc = "Giỏi";
        } else if (mark >= 6.5) {
            this.hocLuc = "Khá";
        } else if (mark >= 5.0) {
            this.hocLuc = "Trung bình";
        } else {
            this.hocLuc = "Yếu";
        }
    }
    public void output() {
        System.out.println(" >> Full Name: " + name);
        System.out.println(" >> Mark: " + mark);
        System.out.println(" >> Hoc luc: " + hocLuc);
        check();
    }

    public static void main(String[] args) {
        SinhVien newStudent =  new SinhVien();
        newStudent.input();
        newStudent.output();
    }
}
