package BTVN.Day1;

import java.util.Scanner;

public class TinhTienDien {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap so dien: ");
        int soDien = scanner.nextInt();
        if(soDien<0){
            System.out.println("So dien khong hop le");
        }
        else if(soDien<50){
            System.out.println("So tien: " + soDien*1000);
        }
        else{
            System.out.println("So tien: " + 50*1000 + (soDien - 50)*1200);
        }
    }
}
