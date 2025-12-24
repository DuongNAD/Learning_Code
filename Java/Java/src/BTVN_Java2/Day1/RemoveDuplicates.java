package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;

public class RemoveDuplicates {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2,2, 3, 4,4, 5, 6, 7, 8,8, 9, 10));
        System.out.println("List: \n" + numbers);

        Set<Integer> set = new LinkedHashSet<>(numbers);
        numbers.clear();

        numbers.addAll(set);

        System.out.println("List: \n" + numbers);

    }
}
