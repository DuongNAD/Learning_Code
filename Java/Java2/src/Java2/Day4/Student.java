package Java2.Day4;

import java.io.Serializable;

public class Student implements Serializable {
    private static final long serialVersionUID = 1427461703707854023L;

    private int id;
    private String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
