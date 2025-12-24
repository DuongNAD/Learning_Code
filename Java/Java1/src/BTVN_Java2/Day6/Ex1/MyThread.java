package BTVN_Java2.Day6.Ex1;

public class MyThread extends Thread {
    @Override
    public void run() {
        for (int i = 0; i <5; i++) {
            System.out.println(this.getName() + ": Hello from thread " + i);
            try {
                Thread.sleep(500);
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
