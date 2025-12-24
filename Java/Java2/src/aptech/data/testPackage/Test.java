package aptech.data.testPackage;

import aptech.data.manager.DocumentManager;

import java.util.Scanner;

public class Test {
    Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        DocumentManager documentManager = new DocumentManager();
        Test test = new Test();
        while(true) {
            System.out.println("-----------------------------------");
            System.out.println("=== Documents Management System ===");
            System.out.println("-----------------------------------");
            System.out.println("1. Add New Books");
            System.out.println("2. Display All Books");
            System.out.println("3. Search Books by Author Name ");
            System.out.println("4. Exit");
            System.out.println("-----------------------------------");
            System.out.println(">>> Choose 1 - 5: ");
            int luaChon =0;

            try {
                luaChon = Integer.parseInt(test.scanner.nextLine());
            }
            catch (NumberFormatException e) {
                System.out.println("Invalid input");
                continue;
            }

            switch (luaChon) {
                case 1:
                    documentManager.addDocument();
                    break;
                case 2:
                    documentManager.displayAllDocuments();
                    break;
                case 3:
                    documentManager.searchByAuthorName();
                    break;
                case 4:
                    System.out.println("Thank you for using this!");
                    System.exit(0);
                default:
                    System.out.println("Invalid selection please select from 1 - 4");
            }
        }
    }
}
