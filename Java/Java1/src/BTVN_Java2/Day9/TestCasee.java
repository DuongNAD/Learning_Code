package BTVN_Java2.Day9;

import java.util.Scanner;

public class TestCasee {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Product ID to check the Product lable: ");
        int productID = scanner.nextInt();
        switch(productID){
            case 101:
            case 102:
            case 103:
                System.out.print("Enter Product Name: ");
                break;
            case 104:
            case 105:
                System.out.print("Enter Product Price: ");
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + productID);
        }
    }
}
