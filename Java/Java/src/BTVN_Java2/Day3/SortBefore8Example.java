package BTVN_Java2.Day3;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class SortBefore8Example {
    public static void main (String[] args) {
        List<String> language = Arrays.asList("Java", "C#", "Python", "JavaScript", "C#", "Python");

        Collections.sort(language, (o1, o2) -> {
            int k = 10;
            return o1.compareTo(o2);
        });
        for(String s : language) {
            System.out.println(s);
        }
    }
}

@FunctionalInterface
interface Sayable{
    public String say();
}

class lambarSayable implements Sayable{
    @Override
    public String say() {
        return "I have nothing to say!";
    }
}
