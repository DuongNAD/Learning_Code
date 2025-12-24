package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class FindKthSmallest {
    public static void main(String[] args) {
        System.out.print("Nhap phan tu nho thu n muon tim: ");
        Scanner scanner =new Scanner(System.in);
        int n = scanner.nextInt();
        ArrayList<Integer> numbers1 = new ArrayList(Arrays.asList(10, 2,3, 23, 34, 15, 6, 14, 12, 9, 11));
        Collections.sort(numbers1);
        int find = numbers1.get(n-1);
        System.out.println("List: " + numbers1);
        System.out.println(n + "th smallest: " + find);
    }
}
