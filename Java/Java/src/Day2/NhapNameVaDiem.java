package Day2;

import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class NhapNameVaDiem {
    public static void  main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap so luong sinh vien: ");
        int number_students = scanner.nextInt();
        scanner.nextLine();

        String[] name = new String[number_students];
        Double[] point = new Double[number_students];

        for (int i = 0; i < number_students; i++) {
            System.out.printf("Nhap ten va diem sinh vien thu %d\n", i + 1);
            System.out.print("Nhap ten: ");
            name[i] = scanner.nextLine();
            System.out.print("Nhap diem: ");
            point[i] = scanner.nextDouble();
            scanner.nextLine();
        }
        for (int i = 0;i<number_students-1;i++){
            for(int  j = i+1; j<number_students;j++){
                if(point[j] > point[i] || (Objects.equals(point[j], point[i]) && name[i].compareTo(name[j]) > 0)){
                    double temp = point[j];
                    point[j] = point[i];
                    point[i] = temp;

                    String tempTen = name[j];
                    name[j] = name[i];
                    name[i] = tempTen;
                }

            }
        }

        for(int i = 0;i<number_students;i++){
            System.out.println(name[i] + " " + point[i]);
        }
    }
}
