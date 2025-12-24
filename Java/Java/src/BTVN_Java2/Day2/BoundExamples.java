package BTVN_Java2.Day2;

import java.util.List;

public class BoundExamples {
    public static double sumNumbers(List<? extends Number> list) {
        double sum = 0;
        for (Number number : list) {
            sum += number.doubleValue();
        }
        return sum;
    }

    public static void addNumbers(List<? super Integer> list) {
        for (int i = 0; i<5;i++) {
            list.add(i);
        }
    }

    public static <T extends Number & Comparable <T>> T min(List<T> list) {
        if(list == null || list.isEmpty()) {
            return null;
        }

        T minValue = list.get(0);
        for (T number : list) {
            if(number.compareTo(minValue) < 0) {
                minValue = number;
            }
        }
        return minValue;
    }
}
