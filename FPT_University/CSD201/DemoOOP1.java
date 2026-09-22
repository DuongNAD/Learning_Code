public class DemoOOP1 {
    public static void main(String[] args) {
        Employee a,b;
        a = new Employee("T.Lam",20);
        b = new Employee();

        a.show();
        b.show();
        b.name = "DB7";
        b.salary = 15;
        b.show();
    }
}