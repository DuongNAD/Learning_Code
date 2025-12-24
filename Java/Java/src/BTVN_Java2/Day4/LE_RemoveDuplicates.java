package BTVN_Java2.Day4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LE_RemoveDuplicates {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 6, 8));
        System.out.println("List: " + list);

        List<Integer> uniqueNumbers = list.stream()
                .distinct()
                .collect(Collectors.toList());

        System.out.println("Unique List: " + uniqueNumbers);
    }
}
