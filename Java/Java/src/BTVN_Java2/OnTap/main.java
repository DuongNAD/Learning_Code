package BTVN_Java2.OnTap;

import java.util.InputMismatchException;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        StudentManager studentManager = new StudentManager();
        Scanner scanner = new Scanner(System.in);
        int choice = 0;
        do  {

            System.out.println("\n===== STUDENT MANAGEMENT SYSTEM =====");
            System.out.println("1. Add New Student");
            System.out.println("2. Save Students to File");
            System.out.println("3. Display All Students (from File)");
            System.out.println("4. Search Student by Course");
            System.out.println("0. Exit");
            System.out.print("Please enter your choice: ");
            try{
                choice = scanner.nextInt();
            }
            catch(InputMismatchException e){
                System.out.println("Please enter a valid choice");
            }
            switch (choice) {
                case 1:
                    studentManager.addStudent();
                    break;
                case 2:
                    studentManager.saveToFile();
                    break;
                case 3:
                    studentManager.readFromFile();
                    break;
                case 4:
                    studentManager.searchByCourse();
                    break;
                case 0:
                    System.out.println("Thank You!");
                    break;
                    default:
                        System.out.println("Invalid choice");
            }
        }
        while (choice != 0);
    }
}
