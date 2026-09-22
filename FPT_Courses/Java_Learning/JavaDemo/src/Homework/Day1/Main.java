/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Homework.Day1;

import java.util.Scanner;

/**
 *
 * @author DELL
 */
public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n =0;
        System.out.println("=== ARRAY MANAGER ===");
        System.out.print("Nhập số lượng phần tử của mảng (n): ");
        while (n <= 0) {
            System.out.print("Nhập số lượng phần tử của mảng (n > 0): ");
            try {
                n = Integer.parseInt(scanner.nextLine());
                if (n <= 0) System.out.println("Vui lòng nhập số dương!");
            } catch (NumberFormatException e) {
                System.out.println("Error: Vui lòng nhập một số nguyên hợp lệ (Invalid Integer).");
            }
        }
        ArrayService service = new ArrayService(n);

        service.InputArray(scanner);
        
        int choice = 0;

        do {
            System.out.println("\n---------------- MENU ----------------");
            System.out.println("1. Nhập lại mảng");
            System.out.println("2. Tính tổng Chẵn / Lẻ");
            System.out.println("3. Liệt kê số Nguyên Tố");
            System.out.println("4. Tìm Max / Min");
            System.out.println("5. Tìm vị trí Max thứ 2 và sắp xếp theo nguyên tắc");
            System.out.println("6. Đếm số lần xuất hiện");
            System.out.println("7. Thêm phần tử");
            System.out.println("8. Xóa phần tử");
            System.out.println("0. Thoát");
            System.out.println("--------------------------------------");
            System.out.print("Chọn chức năng: ");
            
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Lỗi: Vui lòng nhập số (Invalid Input)!");
                choice = -1; 
                continue; 
            }

            switch (choice) {
                case 1:
                    service.InputArray(scanner);
                    break;
                case 2:
                    service.SumNumber();
                    break;
                case 3:
                    service.CheckIsPrime();
                    break;
                case 4:
                    service.FindMaxMin();
                    break;
                case 5:
                    service.FindSecondMax();
                    break;
                case 6:
                    service.CountNumber(scanner);
                    break;
                case 7:
                    service.addNumber(scanner);
                    break;
                case 8:
                    service.deleteNumber(scanner);
                    break;
                case 0:
                    System.out.println("Thank you");
                    break;
                default:
                    System.out.println("Lựa chọn không hợp lệ, vui lòng chọn lại");
            }
            
        } while (choice != 0);
    }
}