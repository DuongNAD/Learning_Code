package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class FindSecondLargest {
    public static void main(String[] args) {
        ArrayList<Integer> numbers1 = new ArrayList<>(Arrays.asList(1, 22, 3, 14, 26, 27, 27, 9, 10, 10,20));

        if (numbers1.size() < 2) {
            System.out.println("List không đủ phần tử để tìm số lớn nhì.");
            return;
        }

        Collections.sort(numbers1);
        Collections.reverse(numbers1);
        int max = numbers1.get(0);
        Integer maxSecond = null;
        for(int i = 0; i < numbers1.size(); i++){
            if(numbers1.get(i) < max){
                maxSecond = numbers1.get(i);
                break;
            }
        }

        System.out.println("List: \n" + numbers1);
        System.out.println("Second Largest: " + maxSecond);
    }
}
