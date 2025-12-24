package Day2;

import java.util.Arrays;
import java.util.Scanner;

public class NhapSvXuatAlphabet {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] s = new String[5];
        System.out.println("Nhap ten 5 sinh vien: ");
        for(int  i = 0;i<5;i++){
            System.out.printf("Nhap sinh vien thu %d: ",i+1);
            s[i] = scanner.nextLine();
        }

        Arrays.sort(s);
        System.out.println("Danh sach sinh vien sau khi sap xep: ");
        for(String x: s){
            System.out.println(x);
        }
    }
}
