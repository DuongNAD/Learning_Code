package Day6;// package day8; // Tên package có thể khác tùy dự án của Anh

public class Student {
    String name;
    int age;

    // Đây là một biến static. Nó thuộc về LỚP Student,
    // không thuộc về bất kỳ đối tượng student1 hay student2 nào.
    // Tất cả các đối tượng Student sẽ chia sẻ chung biến này.
    static int x = 0;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}