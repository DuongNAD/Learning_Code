public class Employee {
    String name;
    float salary;

    Employee(){
        name ="No";
        salary=0;
    }   
    Employee(String name,float salary){
        name = name;
        salary = salary;
    }

    void show(){
        System.out.println("Name: " + name + " - Salary: " + salary);
    }
}