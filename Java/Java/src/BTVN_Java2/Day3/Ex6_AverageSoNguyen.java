package BTVN_Java2.Day3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.OptionalDouble;

public class Ex6_AverageSoNguyen {
    public static void main(String[] args) {
        List<Double> numbers = Arrays.asList(10.5, 20.0, 15.5, 5.0, 30.0);

        System.out.println("--- Danh sách số thực ---");
        System.out.println(numbers);

        OptionalDouble average = numbers.stream()
                .mapToDouble(d -> d.doubleValue())
                .average();
        double result = average.getAsDouble();
        System.out.println("Trung binh cong: " + result);
    }
}
