package com.exercise.entity;

public class Contact {
    private int id;
    private String firstName;
    private String lastName;
    private int groupId;
    private String groupName; // for displaying join result
    private String phoneNumber;

    public Contact() {
    }

    public Contact(int id, String firstName, String lastName, int groupId, String phoneNumber) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.groupId = groupId;
        this.phoneNumber = phoneNumber;
    }

    public Contact(String firstName, String lastName, int groupId, String phoneNumber) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.groupId = groupId;
        this.phoneNumber = phoneNumber;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getGroupId() {
        return groupId;
    }

    public void setGroupId(int groupId) {
        this.groupId = groupId;
    }

    public String getGroupName() {
        return groupName;
    }

    public void setGroupName(String groupName) {
        this.groupName = groupName;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
}
