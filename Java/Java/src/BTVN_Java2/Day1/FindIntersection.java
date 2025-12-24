package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Arrays;

public class FindIntersection {
    public static void main(String[] args) {
        ArrayList<Integer> numbers1 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        ArrayList<Integer> numbers2 = new ArrayList<>(Arrays.asList(11, 12, 13, 14, 15, 6, 7, 18, 9, 10));

        ArrayList<Integer> intersection = new ArrayList<>(numbers1);

        intersection.retainAll(numbers2);

        System.out.println("Giao 2 List: " + intersection);
    }
}
