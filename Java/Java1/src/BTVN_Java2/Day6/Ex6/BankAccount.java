package BTVN_Java2.Day6.Ex6;

public class BankAccount {
    private int balance = 0;

    public BankAccount(int balance) {
        this.balance = balance;
    }

    public synchronized void deposit(int amount) {
        balance += amount;
        System.out.println("Nạp: " + amount);
        System.out.println("Số tiền trong tài khoản: " + balance);
        notifyAll();
    }

    public synchronized void withdraw(int amount) {
        if (balance >= amount) {
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            balance -= amount;
            System.out.println("Rút thành công " +amount + " -> Số dư: " + balance);
        }
        else {
            System.out.println("Rút thất bại. Số dư không đủ: " + balance);
        }
    }
}
