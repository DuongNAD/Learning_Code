package Java2.Day4.B2;

import java.io.Serializable;

public class Student implements Serializable {
    private static final long serialVersionUID = -266706354210367639L;
    private int id;
    private String name;
    private transient int age;

    public Student(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
    @Override
    public String toString() {
        return "Student [id=" + id + ", name=" + name + ", age=" + age + "]";
    }
}
