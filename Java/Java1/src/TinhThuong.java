import java.util.Scanner;

public class TinhThuong {

    public static long factorial_VongLap(int n) {
        long ketQua = 1;
        if (n <= 1) {
            return 1;
        }
        for (int i = 2; i <= n; i++) {
            ketQua *= i;
        }
        return ketQua;
    }

    public static long tinhTienThuong(long luong, int n) {
        return luong * factorial_VongLap(n);
    }

    public static void main(String[] args) {
        System.out.println("--- BÀI TẬP 1: TÍNH THƯỞNG ---");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhập lương: ");
        long luong = scanner.nextLong();
        System.out.print("Nhập số năm công tác: ");
        int soNam = scanner.nextInt();
        System.out.println("Lương: " + luong + ", số năm: " + soNam);

        System.out.println("Tiền thưởng: " + tinhTienThuong(luong, soNam));
    }
}