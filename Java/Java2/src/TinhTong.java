import java.util.Scanner;

public class TinhTong {

    public static long sum_DeQuy(int n) {
        if (n <= 0) {
            return 0;
        }
        return (long) n + sum_DeQuy(n - 1);
    }

    public static long sum_VongLap(int n) {
        long tong = 0;
        for (int i = 1; i <= n; i++) {
            tong += i;
        }
        return tong;
    }

    public static void main(String[] args) {
        System.out.println("--- BÀI TẬP 2: TÍNH TỔNG ---");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("Tổng (Đệ quy):  " + sum_DeQuy(n));
        System.out.println("Tổng (Vòng lặp): " + sum_VongLap(n));
    }
}