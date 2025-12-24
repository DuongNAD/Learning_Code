package com;

import com.system.LiteratureManager;

import java.util.Scanner;

public class Main {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        LiteratureManager literatureManager = new LiteratureManager();

        while(true) {
            System.out.println("------------------------------------");
            System.out.println("=== LITERATURE MENU ===");
            System.out.println("1. Add Literary Work");
            System.out.println("2. Show All Works");
            System.out.println("3. Find Longest Work");
            System.out.println("4. Exit");
            System.out.println("-------------------------------------");
            System.out.println(">>> Mời chọn các chức năng từ 1 - 4: ");

            int luaChon = 0;

            try {
                luaChon = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Lỗi: Lựa chọn phải là một con số. Vui lòng thử lại.");
                continue;
            }

            switch (luaChon) {
                case 1:
                    literatureManager.addWork();
                    break;
                case 2:
                    literatureManager.showWorks();
                    break;
                case 3:
                    literatureManager.findLongestWork();
                    break;
                case 4:
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
