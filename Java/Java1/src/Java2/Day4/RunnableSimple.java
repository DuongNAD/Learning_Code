package Java2.Day4;

public class RunnableSimple implements Runnable {
    public void run() {
        System.out.println("thead is running....");
    }
    public static void main(String[] args) {
        RunnableSimple runnable = new RunnableSimple();
        Thread thread = new Thread(runnable);
        thread.start();
    }
}
