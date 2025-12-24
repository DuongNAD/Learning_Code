package BTVN_Java2.Day4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LE_SumOdd {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9,10));

        int sumOdd = list.stream()
                .filter(n -> n %2 != 0)
                .mapToInt(Integer::intValue)
                .sum();
        System.out.println("Sum Odd: " + sumOdd);
    }
}
