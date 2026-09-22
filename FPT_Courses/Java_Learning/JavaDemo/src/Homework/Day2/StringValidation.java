package Homework.Day2;

import java.util.Scanner;

public class StringValidation {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = "";
        boolean isValid = false;
        do {
            try {
                System.out.print("Input the string: ");
                input = scanner.nextLine();
                validateString(input);
                System.out.println("the string is " + input);
                isValid = true;

            } catch (Exception e) {
                System.out.println("the string is invalid");
            }

        } while (!isValid);

    }

    // 4. Requirement: Use throws clause
    public static void validateString(String s) throws Exception {
        if (!s.matches("HE\\d{3}")) {
            throw new Exception("Invalid format");
        }
    }
}