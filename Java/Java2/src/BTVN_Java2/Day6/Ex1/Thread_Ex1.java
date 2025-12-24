package BTVN_Java2.Day6.Ex1;

public class Thread_Ex1 {
    public static void main(String[] args) {

        MyThread t1 =new MyThread();
        MyThread t2 =new MyThread();

        t1.setName("Thread 1");
        t2.setName("Thread 2");

        t1.start();
        t2.start();
    }
}
