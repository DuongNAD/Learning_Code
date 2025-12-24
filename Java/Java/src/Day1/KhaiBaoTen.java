package Day1;

import java.util.Scanner;

public class KhaiBaoTen {
    static void main() {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        int age =scanner.nextInt();

        System.out.println("Họ và tên: Nguyễn Anh Dương");
        System.out.printf("Họ và tên: %s\n",name);
        System.out.printf("Tuổi: %d\n",19);
        System.out.print("Rất vui được gặp bạn");
    }
}
