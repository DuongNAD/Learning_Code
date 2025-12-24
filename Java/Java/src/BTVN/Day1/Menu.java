package BTVN.Day1;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String tiepTuc;

        do {
            System.out.println("\n----- CHUONG TRINH -----");
            System.out.println("1. Giai phuong trinh bac nhat");
            System.out.println("2. Giai phuong trinh bac hai");
            System.out.println("3. Tinh tien dien");
            System.out.println("-------------------------");
            System.out.print(">> Nhap lua chon cua ban: ");
            int luachon = scanner.nextInt();

            switch (luachon) {
                case 1:
                    System.out.print("Nhap a = ");
                    float aPtrB1 = scanner.nextFloat();
                    System.out.print("Nhap b = ");
                    float bPtrB1 = scanner.nextFloat();

                    if (aPtrB1 == 0) {
                        if (bPtrB1 == 0) {
                            System.out.println("Phuong trinh vo so nghiem");
                        } else {
                            System.out.println("Phuong trinh vo nghiem");
                        }
                    } else {
                        float nghiem = -(bPtrB1 / aPtrB1);
                        System.out.printf("Phuong trinh co nghiem x = %.2f", nghiem);
                    }
                    break;
                case 2:
                    System.out.print("Nhap a = ");
                    float aPtrB2 = scanner.nextFloat();
                    System.out.print("Nhap b = ");
                    float bPtrB2 = scanner.nextFloat();
                    System.out.print("Nhap c = ");
                    float cPtrB2 = scanner.nextFloat();

                    float delta = (float) Math.pow(bPtrB2, 2) - 4 * aPtrB2 * cPtrB2;
                    if (delta < 0) {
                        System.out.println("Nhap trinh vo nghiem");
                    } else if (delta == 0) {
                        System.out.printf("Nhap trinh co nghiem kep x = %f", -bPtrB2 / (2 * aPtrB2));
                    } else {
                        System.out.printf("x1 = %.2f\n", (-bPtrB2 + Math.sqrt(delta)) / (2 * aPtrB2));
                        System.out.println("x2 = " + (-bPtrB2 - Math.sqrt(delta)) / (2 * aPtrB2));
                    }
                    break;
                case 3:
                    System.out.print("Nhap so dien: ");
                    int soDien = scanner.nextInt();
                    if (soDien < 0) {
                        System.out.println("So dien khong hop le");
                    } else if (soDien < 50) {
                        System.out.println("So tien: " + soDien * 1000);
                    } else {
                        System.out.println("So tien: " + 50 * 1000 + (soDien - 50) * 1200);
                    }
                    break;
                default:
                    System.out.println("Lua chon khong hop le");
            }
            System.out.print("\nBan co muon tiep tuc khong? (nhap 'y' de tiep tuc): ");
            tiepTuc = scanner.next();
        }
        while (tiepTuc.equalsIgnoreCase("y"));
        System.out.println("Da thoat chuong trinh");
        scanner.close();
    }
}
