package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.LinkedList;

public class LinkedListAdd_Remove {
    public static void main(String[] args) {
        LinkedList<String> list =  new LinkedList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");
        list.add("e");

        System.out.println("List: " + list);
        list.remove("c");
        System.out.println("List: " + list);
        list.add("g");
        System.out.println("List: " + list);

        System.out.print("Doing tasks: ");
        for (String task : list) {
            System.out.print(task + " -> ");
        }
        System.out.println("Done!");
    }
}
