package BTVN_Java2.Day9;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import static java.util.Arrays.asList;

public class PredicateNotDemo {
    public static void main(String[] args) {
        List<Integer> sampleList = new ArrayList<>(asList(1,2,3,4,5,6,7,8,9,10));

        Predicate<Integer> findEven =  i -> i % 2 == 0;
        Predicate<Integer> findOdd = Predicate.not(findEven);
        List<Integer> evenNumbers =sampleList.stream().filter(findEven).collect(
                Collectors.toList());
        List<Integer> oddNumbers =sampleList.stream().filter(findOdd).collect(
                Collectors.toList());

        System.out.println("Here is the list of even numbers: " + evenNumbers);
        System.out.println("Here is the list of odd numbers: " + oddNumbers);
    }
}
