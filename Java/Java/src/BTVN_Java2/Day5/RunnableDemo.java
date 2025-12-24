package BTVN_Java2.Day5;

public class RunnableDemo {
    public static void main(String[] args) {
        System.out.println("---- START ----");

        MyThread myThread = new MyThread();
        Thread thread1 = new Thread(myThread);
        Thread thread2 = new Thread(myThread);

        thread1.start();
        thread2.start();

        System.out.println("---- END ----");
    }
}
