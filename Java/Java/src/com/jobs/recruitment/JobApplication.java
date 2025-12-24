package com.jobs.recruitment;

public abstract class JobApplication {
    private String applicationID;
    private String jobTitle;
    private String applicationDate;
    private int numberOfApplications;

    public JobApplication() {}

    public JobApplication(String applicationID, String jobTitle, String applicationDate, int numberOfApplications) {
        this.applicationID = applicationID;
        this.jobTitle = jobTitle;
        this.applicationDate = applicationDate;
        this.numberOfApplications = numberOfApplications;
    }

    public String getApplicationID() {
        return applicationID;
    }
    public void setApplicationID(String applicationID) {
        this.applicationID = applicationID;
    }
    public String getJobTitle() {
        return jobTitle;
    }
    public void setJobTitle(String jobTitle) {
        this.jobTitle = jobTitle;
    }
    public String getApplicationDate() {
        return applicationDate;
    }
    public void setApplicationDate(String applicationDate) {
        this.applicationDate = applicationDate;
    }
    public int getNumberOfApplications() {
        return numberOfApplications;
    }
    public void setNumberOfApplications(int numberOfApplications) {
        this.numberOfApplications = numberOfApplications;
    }

    public abstract void input();
    public abstract void display();
}
