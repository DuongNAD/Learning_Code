package Java2.Day4.B2;

import java.io.FileInputStream;
import java.io.ObjectInput;
import java.io.ObjectInputStream;

public class DeserializationTransientExample {
    public static void main(String[] args) throws Exception {
        ObjectInputStream ois = null;
        try{
            ois = new ObjectInputStream(new FileInputStream("src/Java2/Day4/B2/student.txt"));
            Student student = (Student) ois.readObject();
            System.out.println(student);
        }
        catch(Exception e){
            e.printStackTrace();
        }
        finally{
            ois.close();
        }

    }
}
