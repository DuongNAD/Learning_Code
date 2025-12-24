package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class FindMaximumElement {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(6,9,2,12,55,23,1));

        int max = Collections.max(list);

        System.out.println("Danh sach: \n" + list);
        System.out.println("Maximum Element : " + max);
    }
}
