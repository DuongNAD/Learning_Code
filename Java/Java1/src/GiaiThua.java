import java.util.Scanner;

public class GiaiThua {

    public static long factorial_DeQuy(int n) {
        if (n <= 1) {
            return 1;
        }
        return (long) n * factorial_DeQuy(n - 1);
    }

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

    public static void main(String[] args) {
        System.out.println("--- BÀI TẬP 4: GIAI THỪA ---");
        Scanner sc = new Scanner(System.in);
        int n_fact = sc.nextInt();
        System.out.println("Giai thừa (Đệ quy):  " + factorial_DeQuy(n_fact));
        System.out.println("Giai thừa (Vòng lặp): " + factorial_VongLap(n_fact));
    }
}