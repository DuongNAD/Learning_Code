package BTVN_Java2.Day5;

public class CountRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i <10; i++) {
            String ThreadName = Thread.currentThread().getName();
            System.out.println(ThreadName + (i+1));

            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
