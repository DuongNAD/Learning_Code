import java.util.Scanner;

public class DaoNguocChuoi {

    public static String reverse_DeQuy(String str) {
        if (str == null || str.length() <= 1) {
            return str;
        }
        return reverse_DeQuy(str.substring(1)) + str.charAt(0);
    }

    public static String reverse_VongLap(String str) {
        if (str == null) {
            return null;
        }
        String ketQua = "";
        for (int i = str.length() - 1; i >= 0; i--) {
            ketQua += str.charAt(i);
        }
        return ketQua;
    }

    public static void main(String[] args) {
        System.out.println("--- BÀI TẬP 3: ĐẢO CHUỖI ---");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Nhập chuỗi: ");
        String str = scanner.nextLine();
        System.out.println("Chuỗi gốc: " + str);
        System.out.println("Đảo (Đệ quy):  " + reverse_DeQuy(str));
        System.out.println("Đảo (Vòng lặp): " + reverse_VongLap(str));
    }
}