package BTVN_Java2.Day6.Ex4;

public class MyRunnable implements Runnable {

    private int count = 0;
    @Override
    public void run() {
        for(int i=0;i<1000;i++){
            count++;
        }
        System.out.println(Thread.currentThread().getName() + ": " + count);
    }
}
