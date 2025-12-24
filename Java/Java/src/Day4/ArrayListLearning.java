package Day4;


import java.util.ArrayList;
import java.util.Collections;

public class ArrayListLearning {
    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList();
        a.add("Cuong");
        a.add("Tuan");
        a.add("Phuong");
        a.add("Hong");
        a.add(1,"Hanh");
        a.set(0,"Teo");
        a.remove(3);
        a.remove("Phuong");

        int x = a.size() - a.indexOf("Phuong");
        System.out.println(x);

        for(int i=0;i<a.size();i++){
            System.out.println(a.get(i));
        }

        a.removeAll(Collections.singleton("Teo"));
        System.out.println("\n");
        for(String name :a){
            System.out.println(name);
        }
    }
}