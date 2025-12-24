package BTVN_Java2.Day1;

import java.util.*;

public class FindFrequency {
    public static void main(String[] args) {
        ArrayList<Integer> numbers1 = new ArrayList(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 1, 3 ,5 ,6, 7,1,1));
        System.out.println("List goc: " + numbers1);

        Set<Integer> numbers2 = new HashSet<>(numbers1);

        System.out.println("Tan suat xuat hien: ");
        for(Integer number : numbers2) {
            int count = Collections.frequency(numbers1, number);
            System.out.println(number + " : " + count);
        }
    }
}
