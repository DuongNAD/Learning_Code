package BTVN_Java2.Day4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;

public class LE_AverageNumber {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(2,9,20,12,30));

        Function<List<Integer>, Double> findAverage = (input) -> {
            if (list == null || list.isEmpty())
                return 0.0;

            return list.stream()
                    .mapToDouble(i -> i)
                    .average()
                    .orElse(0.0);
        };

        double result = findAverage.apply(list);
        System.out.println("Average Score: " + result);
    }
}
