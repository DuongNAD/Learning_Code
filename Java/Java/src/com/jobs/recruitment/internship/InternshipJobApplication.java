package com.jobs.recruitment.internship;

import com.jobs.recruitment.JobApplication;

import java.util.Scanner;

public class InternshipJobApplication extends JobApplication {
    private int durationMonths;
    private double stipend;

    public InternshipJobApplication() {}

    public InternshipJobApplication(String applicationID, String jobTitle, String applicationDate, int numberOfApplication,int durationMonths, double stipend) {
        super(applicationID, jobTitle, applicationDate, numberOfApplication);
        this.durationMonths = durationMonths;
        this.stipend = stipend;
    }

    public int getDurationMonths() {
        return durationMonths;
    }
    public void setDurationMonths(int durationMonths) {
        this.durationMonths = durationMonths;
    }
    public double getStipend() {
        return stipend;
    }
    public void setStipend(double stipend) {
        this.stipend = stipend;
    }

    public double calculateTotalStipend() {
        return this.durationMonths * this.stipend;
    }

    @Override
    public void input() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Application ID: ");
        setApplicationID(scanner.nextLine());

        System.out.println("Enter Job Title: ");
        setJobTitle(scanner.nextLine());

        System.out.println("Enter Application Date: ");
        setApplicationDate(scanner.nextLine());

        System.out.println("Enter Number of Applications: ");
        setNumberOfApplications(scanner.nextInt());

        System.out.println("Enter Duration Months: ");
        setDurationMonths(scanner.nextInt());

        System.out.println("Enter Stipend: ");
        setStipend(scanner.nextDouble());
        scanner.nextLine();
    }

    public void display() {
        System.out.println("Application ID: " + getApplicationID());
        System.out.println("Job Title: " + getJobTitle());
        System.out.println("Application Date: " + getApplicationDate());
        System.out.println("Number of Applications: " + getNumberOfApplications());
        System.out.println("Duration Months: " + getDurationMonths());
        System.out.println("Stipend: " + getStipend());

        System.out.println("Estimated Total Stipend: "+ calculateTotalStipend());
    }
}
