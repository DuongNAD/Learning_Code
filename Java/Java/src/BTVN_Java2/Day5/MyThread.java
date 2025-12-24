package BTVN_Java2.Day5;

public class MyThread implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            String threadName = Thread.currentThread().getName();

            System.out.println(threadName + ": Đang chạy công việc...");

            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
