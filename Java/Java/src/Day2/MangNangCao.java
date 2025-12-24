package Day2;

import java.util.Arrays;

public class MangNangCao {
    public static void main(String[] args) {
        int[] a = {9,8,3,7,3,9,4,2};
        Arrays.sort(a);
        System.out.println("Mang goc: " + Arrays.toString(a));

        int  i = Arrays.binarySearch(a, 8);
        System.out.println("Vi tri cua so 8: " + i);
        Arrays.fill(a,0);
        System.out.println("Sau fill: " + Arrays.toString(a));
    }
}
