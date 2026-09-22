package JavaClassDay3;

import java.util.Scanner;

public class Student {
    private String code;
    private String name;
    private int bYear;
    private String address;

    public Student(String code, String name, int bYear, String address) {
        this.code = code;
        this.name = name;
        this.bYear = bYear;
        this.address = address;
    }

    public Student(){

    }

    public String getCode() {
        return code;
    }
    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getbYear() {
        return bYear;
    }
    public void setbYear(int bYear) {
        this.bYear = bYear;
    }
    public String getAddress() {
        return address;
    }
    public void setAddress(String address) {
        this.address = address;
    }

    public void input() {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Enter your code: ");
            code = sc.nextLine();
            System.out.print("Enter your name: ");
            name = sc.nextLine();
            System.out.print("Enter your bYear: ");
            bYear = Integer.parseInt(sc.nextLine());
            System.out.print("Enter your address: ");
            address = sc.nextLine();
        }
        catch (NumberFormatException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void output() {
        System.out.println("Code : " + code + " - " + name + " - " + bYear + " - " + address);
    }

}
