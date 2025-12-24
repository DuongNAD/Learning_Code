package Day4;

public class ThongTin {
    public static void main(String[] args) {
        Student student = new Student(3.5, "Nguyen Van A", 20, "Ha Noi");
        System.out.println("Thong tin hoc sinh");
        student.display();

        System.out.println("--------------------------------------");

        Teacher teacher = new Teacher("Tran Thi B", 35, "Da Nang", 5000);
        System.out.println("Thong tin giao vien");
        teacher.display();

    }
}
