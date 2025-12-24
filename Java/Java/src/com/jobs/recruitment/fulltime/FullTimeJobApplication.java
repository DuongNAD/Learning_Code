package com.jobs.recruitment.fulltime;

import com.jobs.recruitment.JobApplication;

import java.util.Scanner;

public class FullTimeJobApplication extends JobApplication {
    private double annualSalary;
    private String jobLocation;

    public double getAnnualSalary() {
        return annualSalary;
    }
    public void setAnnualSalary(double annualSalary) {
        this.annualSalary = annualSalary;
    }
    public String getJobLocation() {
        return jobLocation;
    }
    public void setJobLocation(String jobLocation) {
        this.jobLocation = jobLocation;
    }

    public FullTimeJobApplication() {

    }

    public FullTimeJobApplication(String applicationID, String jobTitle, String applicationDate, int numberOfApplication,double annualSalary, String jobLocation) {
        super(applicationID, jobTitle, applicationDate, numberOfApplication);
        this.annualSalary = annualSalary;
        this.jobLocation = jobLocation;
    }

    @Override
    public void input(){
        Scanner scanner =new Scanner(System.in);
        System.out.println("Enter Application ID: ");
        setApplicationID(scanner.next());

        System.out.println("Enter Job Title: ");
        setJobTitle(scanner.next());

        System.out.println("Enter Application Date: ");
        setApplicationDate(scanner.next());

        System.out.println("Enter Number of Applications: ");
        setNumberOfApplications(scanner.nextInt());

        System.out.println("Enter Annual Salary: ");
        setAnnualSalary(scanner.nextDouble());
        scanner.nextLine();

        System.out.println("Enter Job Location: ");
        setJobLocation(scanner.next());

    }

    @Override
    public void display(){
        System.out.println("Application ID: " + getApplicationID());
        System.out.println("Job Title: " + getJobTitle());
        System.out.println("Application Date: " + getApplicationDate());
        System.out.println("Number of Applications: " + getNumberOfApplications());
        System.out.println("Annual Salary: " + getAnnualSalary());
        System.out.println("Job Location: " + getJobLocation());
    }



}
