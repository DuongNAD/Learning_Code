package BTVN_Java2.Day9;

import java.util.Scanner;

public class EnhancedSwitchDemo3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Product ID to check the Product label: ");
        int productID = scanner.nextInt();
        System.out.println(getResultViaYield(productID));
    }
        private static String getResultViaYield(int id){
            String res = switch (id){
                case 001 -> "This id represents a smart television";
                case 002 -> "This id represents a smartphone";
                case 003,004 -> "This id represents a smart microphone";
                default -> "Sorry";
            };
            return res;
    }
}
