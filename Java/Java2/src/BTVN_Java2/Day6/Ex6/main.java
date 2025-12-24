package BTVN_Java2.Day6.Ex6;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        BankAccount sharedAccount =   new BankAccount(1000);

        Scanner scanner = new Scanner(System.in);
        int choice = -1;

        System.out.println("=== BANKING SYSTEM DEMO ===");

        while(true){
            System.out.println("\n--- Vui lòng chọn thao tác ---");
            System.out.println("1. Nạp tiền (Deposit)");
            System.out.println("2. Rút tiền (Withdraw)");
            System.out.println("3. Thoát (Exit)");
            System.out.print("Nhập lựa chọn: ");

            choice = scanner.nextInt();

            switch (choice){
                case 1:
                    System.out.print("Nhập số tiền muốn nạp: ");
                    int depositAmount = scanner.nextInt();
                    Thread tDeposit = new Thread(new MyRunnable_deposit(sharedAccount,depositAmount));
                    tDeposit.start();
                    try{
                        tDeposit.join();
                    }
                    catch(InterruptedException e){
                        System.out.println(e);
                    }
                    break;
                case 2:
                    System.out.print("Nhập số tiền muốn rút: ");
                    int withdrawAmount = scanner.nextInt();
                    Thread tWithdraw = new Thread(new MyRunnable_withdraw(sharedAccount,withdrawAmount));
                    tWithdraw.start();
                    try{
                        tWithdraw.join();
                    }
                    catch(InterruptedException e){
                        System.out.println(e);
                    }
                    break;
                case 3:
                    System.out.println("Tạm biệt!");
                    return;
                default:
                    System.out.println("Không hợp lệ. Mời nhập lại");
            }
        }
    }
}
