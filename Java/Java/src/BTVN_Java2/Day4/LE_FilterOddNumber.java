package BTVN_Java2.Day4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class LE_FilterOddNumber {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9,10));
        System.out.println("Chuoi ban dau: " + list);

        Predicate<Integer> isOdd = i -> i % 2 != 0;
        List<Integer> result = list.stream()
                .filter(isOdd)
                .collect(Collectors.toList());
        System.out.println("Chuoi Odd: "  + result);
    }
}
