package BTVN_Java2.Day6.Ex6;

public class MyRunnable_withdraw implements Runnable {
    private BankAccount account;
    private int amount;

    public MyRunnable_withdraw(BankAccount account, int amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void run(){
        account.withdraw(amount);
    }
}
