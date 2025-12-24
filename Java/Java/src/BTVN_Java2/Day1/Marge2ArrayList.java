package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Arrays;

public class Marge2ArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> list1 = new ArrayList<Integer>(Arrays.asList(1,2,3,4,5));
        ArrayList<Integer> list2 = new ArrayList<Integer>(Arrays.asList(6,7,8,9,10));

        list1.addAll(list2);
        System.out.println(list1);
    }
}
