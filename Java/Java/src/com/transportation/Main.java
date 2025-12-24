package com.transportation;

import java.util.Scanner;
import com.transportation.managers.VehicleManager;

public class Main {
    private static Scanner scanner =  new Scanner(System.in);

    public static void main(String[] args) {
        VehicleManager vehicleManager = new VehicleManager();

        while(true){
            System.out.println("-------------------------------------------");
            System.out.println("=== VEHICLE MANAGEMENT MENU ===");
            System.out.println("-------------------------------------------");
            System.out.println("1. Input Cars");
            System.out.println("2. Input Motobikes");
            System.out.println("3. Display All Cars (Sorted by Price DESC");
            System.out.println("4. Display Motorbikes (Filter by Engine Type");
            System.out.println("5. Exit");
            System.out.println("-------------------------------------------");
            System.out.println(">>> Mời chọn các chức năng từ 1 - 5: ");

            int luaChon = 0;

            try {
                luaChon = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Lỗi: Lựa chọn phải là một con số. Vui lòng thử lại.");
                continue;
            }

            switch (luaChon) {
                case 1:
                    vehicleManager.inputCars(scanner);
                    break;
                case 2:
                    vehicleManager.inputMotorbikes(scanner);
                    break;
                case 3:
                    vehicleManager.filterBikesByEngineType(scanner);
                    break;
                case 4:
                    vehicleManager.displayCarsSortedByPriceDesc();
                    break;
                case 5:
                    System.out.println("Cảm ơn đã xử dụng chương trình. Tạm biệt!");
                    System.exit(0);
                default:
                    System.out.println("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.");
                    break;
            }
            System.out.println("\n(Nhấn Enter để tiếp tục...)");
            scanner.nextLine();
        }
    }
}
