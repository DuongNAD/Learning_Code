package BTVN.Day1;

import java.util.Scanner;

public class PtrBac1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap a = ");
        float a = scanner.nextFloat();
        System.out.print("Nhap b = ");
        float b = scanner.nextFloat();

        if (a == 0) {
            if (b== 0){
                System.out.println("Phuong trinh vo so nghiem");
            }
            else{
                System.out.println("Phuong trinh vo nghiem");
            }
        }
        else{
            float nghiem = -(b/a);
            System.out.printf("Phuong trinh co nghiem x = %.2f",nghiem);
        }
    }
}
