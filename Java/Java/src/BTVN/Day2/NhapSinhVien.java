package BTVN.Day2;

import java.util.Scanner;

public class NhapSinhVien {
    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);
        System.out.print("Nhap so sinh vien: ");
        int n = scanner.nextInt();
        scanner.nextLine();
        String[] name = new String[n];
        double[] mark = new double[n];
        String[] hocLuc = new String[n];

        for(int i =0;i<n;i++){
            System.out.println("Nhap sinh vien thu: " + (i+1));
            System.out.print("Ten sinh vien: ");
            name[i] = scanner.nextLine();
            System.out.print("Diem sinh vien: ");
            mark[i] = scanner.nextDouble();
            scanner.nextLine();
            if (mark[i] >= 8.0) {
                hocLuc[i] = "Giỏi";
            } else if (mark[i] >= 6.5) {
                hocLuc[i] = "Khá";
            } else if (mark[i] >= 5.0) {
                hocLuc[i] = "Trung bình";
            } else {
                hocLuc[i] = "Yếu";
            }
        }
        for(int  i =0;i<n-1;i++){
            for(int j = i+1; j<n;j++){
                if(mark[i] > mark[j] || (mark[i] == mark[j] && name[i].compareTo(name[j]) > 0)){
                    double temp = mark[i];
                    mark[i] = mark[j];
                    mark[j] = temp;

                    String temptName = name[i];
                    name[i] = name[j];
                    name[j] = temptName;

                    String temptHocLuc = hocLuc[i];
                    hocLuc[i] = hocLuc[j];
                    hocLuc[j] = temptHocLuc;
                }
            }
        }
        System.out.println("\n--- DANH SÁCH SAU KHI SẮP XẾP ---");
        for (int i = 0; i < n; i++) {
            System.out.printf("Sinh viên: %s - Điểm: %.1f - Học lực: %s\n",
                    name[i], mark[i], hocLuc[i]);
        }

    }
}
