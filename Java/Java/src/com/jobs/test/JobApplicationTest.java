package com.jobs.test;

import com.jobs.recruitment.fulltime.FullTimeJobApplication;
import com.jobs.recruitment.internship.InternshipJobApplication;

import java.util.*;

public class JobApplicationTest {
    private static Scanner scanner = new Scanner(System.in);
    private static List<FullTimeJobApplication> fullTimeApps = new ArrayList<>();
    private static List<InternshipJobApplication> internshipApps = new ArrayList<>();

    public static void main(String[] args) {
        while (true) {
            System.out.println("-----------------------------------------------------");
            System.out.println("======== MENU DRIVEN PROGTAM =======");
            System.out.println("-----------------------------------------------------");
            System.out.println("Please select: ");
            System.out.println("1. Input information for n Full-Time Job Applications");
            System.out.println("2. Input information for n Internship Job Applications");
            System.out.println("3. Input information for n Full-Time Job Applications (Sorted by annual salary descending)");
            System.out.println("4. Display information of n Internship Job Applications (Sorted by duration months ascending)");
            System.out.println("5. Exit");
            System.out.println("Your choice (1 -5): ");

            int choice = 0;

            // 3. Dùng try-catch để bắt lỗi nếu người dùng nhập chữ
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Error: Invalid input. Please enter a number.");
                continue; // Bỏ qua lần lặp này và hiện lại menu
            }

            switch (choice) {
                case 1:
                    inputFullTimeJobApplication();
                    break;
                    case 2:
                        inputInternshipApplications();
                        break;
                        case 3:
                            displaySortedFullTime();
                            break;
                            case 4:
                                displaySortedInternship();
                                break;
                                case 5:
                                    System.exit(0);
                                    default:
                                        System.out.println("Invalid choice. Please select from 1 to 5.");

            }
        }
    }

    public static void inputFullTimeJobApplication(){
        System.out.println("--- 1. Input Full-Time Job Applications ---");
        System.out.println("Enter number of applications: ");
        int n =0;
        try {
            n = Integer.parseInt(scanner.nextLine());
        }
        catch (NumberFormatException e) {
            System.out.println("Error: Invalid input. Please enter a number.");
            return;
        }

        for(int i=0;i<n;i++){
            System.out.println("\n--- Entering Applications " +(i+1)+ " ---");
            FullTimeJobApplication app = new FullTimeJobApplication();
            app.input();
            fullTimeApps.add(app);
        }

        System.out.println(n + " full-time application(s) added.");
    }

    public static void inputInternshipApplications() {
        System.out.println("\n--- 2. Input Internship Job Applications ---");
        System.out.print("Enter number of applications: ");
        int n = 0;
        try {
            n = Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number. Returning to menu.");
            return;
        }

        for (int i = 0; i < n; i++) {
            System.out.println("\n--- Entering Application " + (i + 1) + " ---");
            InternshipJobApplication app = new InternshipJobApplication();
            app.input();
            internshipApps.add(app);
        }
        System.out.println(n + " internship application(s) added.");
    }

    public static void displaySortedFullTime(){
        System.out.println("\n--- 3. Sorted Full-Time Job Applications ---");
        if(fullTimeApps.isEmpty()){
            System.out.println("No applications found.");
            return;
        }

        Collections.sort(fullTimeApps, new Comparator<FullTimeJobApplication>() {

            @Override
            public int compare(FullTimeJobApplication o1, FullTimeJobApplication o2) {

                double salary1 = o1.getAnnualSalary();
                double salary2 = o2.getAnnualSalary();
                return Double.compare(salary2, salary1);
            }
        });

        for (FullTimeJobApplication app : fullTimeApps) {
            app.display();
        }
    }

    public static void displaySortedInternship(){
        System.out.println("\n--- 4. Sorted Internship Job Applications ---");
        if(internshipApps.isEmpty()){
            System.out.println("No applications found.");
            return;
        }
        Collections.sort(internshipApps, new  Comparator<InternshipJobApplication>() {
            @Override
            public int compare(InternshipJobApplication app1, InternshipJobApplication app2) {
                double durationMonths1 = app1.getDurationMonths();
                double durationMonths2 = app2.getDurationMonths();
                return Double.compare(durationMonths1, durationMonths2);
            }
        });

        for (InternshipJobApplication app : internshipApps) {
            app.display();
        }
    }
}
