package BTVN_Java2.Day1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class ShuffleList {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        System.out.print("Nhap so luong phan tu: ");
        int n = scanner.nextInt();
        ArrayList<Integer> numbers1 = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            int value = scanner.nextInt();
            numbers1.add(value);
        }

        System.out.println("Truoc khi xao: " + numbers1);
        Collections.shuffle(numbers1);
        System.out.println("Sau khi xao: " + numbers1);
    }
}
