package BTVN_Java2.Day3;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Ex4_LocSoLe {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        System.out.println("Danh sach goc");
        System.out.println(numbers);

        List<Integer> oddNumbers = numbers.stream()
                .filter(n -> n%2 != 0)
                .collect(Collectors.toList());
        System.out.println("\n--- Danh sách số le ---");
        System.out.println(oddNumbers);
    }
}
