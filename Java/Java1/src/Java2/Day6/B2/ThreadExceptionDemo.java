package Java2.Day6.B2;

public class ThreadExceptionDemo {
    public static void main(String[] args) {
        System.out.println("==> Main thread running ...");

        Thread t1 = new Thread(new WorkingThread());
        Thread.setDefaultUncaughtExceptionHandler(new Thread.UncaughtExceptionHandler(){
            @Override
            public void uncaughtException(Thread t, Throwable e) {
                System.out.println("#Thread: " + e);
                System.out.println("#Thread exeption message: " + e.getMessage());
            }
        });

        t1.start();
    }
}
