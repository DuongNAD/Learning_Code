package BTVN_Java2.Day5;

public class CountRunnableDemo {
    public static void main(String[] args) {
        System.out.println("---- START ----");

        CountRunnable sharedJob = new CountRunnable();

        Thread t1 = new Thread(sharedJob);
        Thread t2 = new Thread(sharedJob);
        Thread t3 = new Thread(sharedJob);

        t1.setName("Luồng A");
        t2.setName("Luồng B");
        t3.setName("Luồng C");

        t1.start();
        t2.start();
        t3.start();

        System.out.println("---- END ----");
    }
}
