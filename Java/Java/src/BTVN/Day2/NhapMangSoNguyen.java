package BTVN.Day2;

import java.util.Arrays;
import java.util.Scanner;

public class NhapMangSoNguyen {
    public static void main(String[] args) {
        Scanner scanner =new Scanner(System.in);
        System.out.print("Nhap so phan tu cua mang: ");
        int a = scanner.nextInt();
        if(a<=0){
            System.out.println("So phan tu cua mang khong hop le! So phan tu >= 1 ");
        }
        int[] input = new int[a];
        for(int i =0;i<a;i++){
            System.out.printf("Phan tu thu %d: ", i+1);
            input[i] = scanner.nextInt();
        }
        Arrays.sort(input);
        System.out.println("Phan tu nho nhat: " + input[0]);
        int sum = 0;
        int k = 0;
        for (int j =0;j<a;j++){
            if(input[j]%3 == 0){
                sum = sum +input[j];
                k++;
            }
        }
        if (k > 0) {
            System.out.println("Trung binh cong cac so chia het cho 3: " + (float) sum / k);
        } else {
            System.out.println("Trong mảng không có số nào chia hết cho 3.");
        }
    }
}
