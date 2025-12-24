package Day1;

import java.util.Scanner;

public class LuyThua {
    static void main() {
        Scanner scanner = new Scanner(System.in);

        float a = scanner.nextFloat();
        float b = scanner.nextFloat();

        System.out.printf("%f\n",a);
        System.out.printf("%f\n",b);
        System.out.printf("%f\n",Math.pow(a,b));
        System.out.printf("%f\n", Math.min(a,b));
    }
}
