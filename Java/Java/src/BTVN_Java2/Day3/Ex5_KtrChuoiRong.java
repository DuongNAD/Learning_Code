package BTVN_Java2.Day3;

import java.util.Scanner;
import java.util.function.Predicate;

public class Ex5_KtrChuoiRong {
    public static void main(String[] args) {
        System.out.println("Nhap chuoi: ");
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();

        Predicate<String> isStringEmty = s_input -> s_input.isEmpty();

        boolean result = isStringEmty.test(s);

        System.out.println("--- KẾT QUẢ KIỂM TRA CHUỖI RỖNG (isEmpty) ---");
        System.out.println("Chuỗi vừa nhập là: \"" + s + "\"");

        if (result) {
            System.out.println("Kết quả: Chuỗi là RỖNG (TRUE).");
        } else {
            System.out.println("Kết quả: Chuỗi KHÔNG rỗng (FALSE).");
        }
    }
}
