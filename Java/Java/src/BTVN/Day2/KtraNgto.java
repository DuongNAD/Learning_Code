package BTVN.Day2;

import java.util.Scanner;

public class KtraNgto {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap a = ");
        int a = scanner.nextInt();

        if(a<1){
            System.out.println("So kiem tra phai la so nguyen > 0");
            return;
        }
        for(int i =2;i<=a/2;i++){
            if(a%i ==0){
                System.out.println("So " + a + " khong phai la so nguyen to");
                return;
            }
        }
        System.out.println("So " +a+ " la so nguyen to");
    }
}
