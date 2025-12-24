package BTVN.Day1;

import java.util.Scanner;

public class PtrBac2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap a = ");
        float a = scanner.nextFloat();
        System.out.print("Nhap b = ");
        float b = scanner.nextFloat();
        System.out.print("Nhap c = ");
        float c = scanner.nextFloat();

        float delta = (float)Math.pow(b,2) - 4*a*c;
        if(delta<0){
            System.out.println("Nhap trinh vo nghiem");
        }
        else if(delta == 0){
            System.out.printf("Nhap trinh co nghiem kep x = %f",-b/(2*a));
        }
        else{
            System.out.printf("x1 = %.2f\n",(-b+Math.sqrt(delta))/(2*a));
            System.out.println("x2 = " + (-b-Math.sqrt(delta))/(2*a));
        }
    }
}
