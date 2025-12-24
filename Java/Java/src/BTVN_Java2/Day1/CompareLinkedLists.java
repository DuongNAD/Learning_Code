package BTVN_Java2.Day1;

import java.util.Arrays;
import java.util.LinkedList;

public class CompareLinkedLists {
    public static void main(String[] args) {

        LinkedList<String> list1 = new LinkedList<>(Arrays.asList("A", "B", "C", "D"));
        LinkedList<String> list2 = new LinkedList<>(Arrays.asList("A", "B", "C", "D"));
        LinkedList<String> list3 = new LinkedList<>(Arrays.asList("D", "B", "A", "D"));

        boolean isEqual1 = list1.equals(list2);
        System.out.println("list1 == list2: " + isEqual1);
        boolean isEqual2 = list1.equals(list3);
        System.out.println("list1 == list3: " + isEqual2);
    }
}
