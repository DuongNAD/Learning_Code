package com.exercise.entity;

public class Employee {
    private String employeeNo;
    private String employeeName;
    private String placeOfWork;
    private String phoneNo;

    public Employee() {
    }

    public Employee(String employeeNo, String employeeName, String placeOfWork, String phoneNo) {
        this.employeeNo = employeeNo;
        this.employeeName = employeeName;
        this.placeOfWork = placeOfWork;
        this.phoneNo = phoneNo;
    }

    public String getEmployeeNo() {
        return employeeNo;
    }

    public void setEmployeeNo(String employeeNo) {
        this.employeeNo = employeeNo;
    }

    public String getEmployeeName() {
        return employeeName;
    }

    public void setEmployeeName(String employeeName) {
        this.employeeName = employeeName;
    }

    public String getPlaceOfWork() {
        return placeOfWork;
    }

    public void setPlaceOfWork(String placeOfWork) {
        this.placeOfWork = placeOfWork;
    }

    public String getPhoneNo() {
        return phoneNo;
    }

    public void setPhoneNo(String phoneNo) {
        this.phoneNo = phoneNo;
    }
}
