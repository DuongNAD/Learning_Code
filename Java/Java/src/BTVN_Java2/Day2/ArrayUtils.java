package BTVN_Java2.Day2;

import java.util.List;

public class ArrayUtils {
    public static <T> void swap (T[] array, int i,int j) {
        if(i >= 0 && i<array.length && j >= 0 && j<array.length) {
            T temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
    public static <T> void printList (List<T> list) {
        for (T t : list) {
            System.out.print(t + " ");
        }
        System.out.println();
    }
}
