package BTVN_Java2.Day1;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SetIntersection {
    public static void main(String[] args) {
        Set<Integer> set1 = new HashSet<>(Arrays.asList(1,2,3,4,5,6));
        Set<Integer> set2 = new HashSet<>(Arrays.asList(3,4,5,6,7,8,9));
        Set<Integer> set3 = new HashSet<>(Arrays.asList(5,6,7,8,9,10,11));

        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        intersection.retainAll(set3);

        System.out.println("Intersection: " + intersection);
    }
}
