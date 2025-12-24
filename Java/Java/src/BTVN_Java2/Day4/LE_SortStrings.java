package BTVN_Java2.Day4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class LE_SortStrings {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>(Arrays.asList("Java", "Python", "C++", "C#", "Ruby", "JavaScript"));

        System.out.println("List: " + list);

        Collections.sort(list, (s1,s2) -> s1.compareTo(s2));
        System.out.println("Sorted: " + list);
    }
}
