package BTVN_Java2.Day4;

import java.util.Scanner;

@FunctionalInterface
interface CalculateSum {
    int sum(int a, int b);
}

public class LE_Sum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("x = ");
        int x = scanner.nextInt();
        System.out.print("y = ");
        int y = scanner.nextInt();

        CalculateSum sumCalculator = (a,b) -> a +b ;

        int result = sumCalculator.sum(x, y);
        System.out.println("Sum = " + result);
    }
}
