package BTVN_Java2.Day6.Ex3;

public class Main {
    public static void main(String[] args) {
        MyRunnable r1 = new MyRunnable();
        MyRunnable r2 = new MyRunnable();

        Thread t1 = new Thread(r1);
        Thread t2 = new Thread(r2);

        t1.setName("Low");
        t2.setName("High");

        t1.setPriority(1);
        t2.setPriority(10);

        t1.start();
        t2.start();
    }
}
