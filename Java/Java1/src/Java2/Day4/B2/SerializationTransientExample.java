package Java2.Day4.B2;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class SerializationTransientExample {
    public static void main(String[] args) throws Exception {
        ObjectOutputStream oos = null;
        try {
            oos = new ObjectOutputStream(new FileOutputStream("src/Java2/Day4/B2/Student.txt"));
            Student student = new Student(1,"gpcoder.com",28);
            oos.writeObject(student);
            oos.flush();
        }
        catch (IOException ex) {
            ex.printStackTrace();
        }
        finally {
            oos.close();
        }
    }
}
