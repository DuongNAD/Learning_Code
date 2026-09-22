package Day1;

import java.util.Scanner;

public class Validation {
    private static final Scanner scanner = new Scanner(System.in);

    public static int checkInputInt() {
        while (true) {
            try {
                int result = Integer.parseInt(scanner.nextLine().trim());
                if (result <= 0) {
                    System.out.print("Please input a number greater than 0: ");
                    continue;
                }
                return result;
            } catch (NumberFormatException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
