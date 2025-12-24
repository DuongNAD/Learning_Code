package Day4;

public class Teacher extends Person {
    private int salary;

     Teacher(String name, int age, String address, int salary) {
        super(name, age, address);
        this.salary = salary;
    }

    public int getSalary() {
        return salary;
    }
    public void setSalary(int salary) {
         this.salary = salary;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Salary: " + this.salary);
    }
}
