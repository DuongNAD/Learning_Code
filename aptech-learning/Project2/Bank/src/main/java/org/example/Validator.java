package org.example;

import java.util.Scanner;

public class Validator {
    public static final Scanner scanner = new Scanner(System.in);

    public static String inputString(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine();
    }


}
