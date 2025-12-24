package Day3;

import java.util.Scanner;

public class Employee {
    public String fullname;
    public double salary;

    public void input() {
        Scanner scanner =  new Scanner(System.in);
        System.out.print(" >> Full Name: ");
        this.fullname = scanner.nextLine();

        System.out.print(" >> Salary: ");
        this.salary = scanner.nextDouble();
    }

    public void output() {
        System.out.println(" >> Full Name: " + fullname);
        System.out.println(" >> Salary: " + salary);
    }

    public static void main(String[] args) {
        Employee employee1 = new Employee();
        employee1.input();
        employee1.output();
        System.out.println("Hello");
    }
}
