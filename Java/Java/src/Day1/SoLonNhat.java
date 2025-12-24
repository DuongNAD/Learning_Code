package Day1;

import java.util.Scanner;

public class SoLonNhat {
    static void main() {


    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();
    int c = scanner.nextInt();
    int lonNhat = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);

        System.out.printf("%d",lonNhat);
}
}
