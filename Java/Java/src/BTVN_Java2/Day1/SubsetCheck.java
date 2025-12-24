package BTVN_Java2.Day1;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SubsetCheck {
    public static void main(String[] args) {
        Set<Integer> bigSet = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        Set<Integer> smallSet = new HashSet<>(Arrays.asList(1, 2, 8));
        Set<Integer> otherSet = new HashSet<>(Arrays.asList(1, 2, 5, 99));

        boolean isSubset1 = bigSet.containsAll(smallSet);
        System.out.println("smallSet la tap con cua bigSet: " + isSubset1);

        boolean isSubset2 = bigSet.containsAll(otherSet);
        System.out.println("otherSet la tap con cua bigSet: " + isSubset2);
    }
}
