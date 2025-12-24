package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Collections;

public class SortStringList {
    public static void main(String[] args) {
        ArrayList<String> alphabetically = new ArrayList<>();

        alphabetically.add("Java 8 in Action");
        alphabetically.add("Laptop Stand");
        alphabetically.add("Clean Code");
        alphabetically.add("Spring Boot Guide");
        alphabetically.add("Electronics");

        System.out.println("Alphabetically List: \n" + alphabetically);

        Collections.sort(alphabetically);

        System.out.println("Sort Alphabetically List: \n" + alphabetically);
    }
}
