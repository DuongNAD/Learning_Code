package BTVN_Java2.Day6.Ex2;

public class CountRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i <10; i++) {
            System.out.println(Thread.currentThread().getName() + ": Hello from thread " + (i+1));
        }
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {}
    }
}
