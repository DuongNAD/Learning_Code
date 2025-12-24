package BTVN_Java2.Day6.Ex5;

public class main {
    public static void main(String[] args) {

        MyRunnable sharedJob = new MyRunnable();

        Thread t1 = new Thread(sharedJob);
        Thread t2 = new Thread(sharedJob);
        Thread t3 = new Thread(sharedJob);
        Thread t4 = new Thread(sharedJob);
        Thread t5 = new Thread(sharedJob);

        t1.setName("Thread 1");
        t2.setName("Thread 2");
        t3.setName("Thread 3");
        t4.setName("Thread 4");
        t5.setName("Thread 5");

        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();
    }
}
