package BTVN_Java2.Day6.Ex2;

public class Main {
    public static void main(String[] args) {
        CountRunnable c1 = new CountRunnable();
        CountRunnable c2 = new CountRunnable();

        Thread t1 = new Thread(c1);
        Thread t2 = new Thread(c2);

        t1.setName("Thread 1");
        t2.setName("Thread 2");

        t1.start();
        t2.start();
    }
}
