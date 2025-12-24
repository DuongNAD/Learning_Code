package Java2.Day4;

public class ThreadDemoTest {
    public static void main(String args[]) {
        System.out.println("Main thread running... ");
        ThreadDemo T1 = new ThreadDemo("Thread-1-HR-Database");
        T1.start(); // Bắt đầu chạy luồng T1

        ThreadDemo T2 = new ThreadDemo("Thread-2-Send-Email");
        T2.start(); // Bắt đầu chạy luồng T2

        System.out.println("==> Main thread stopped!!! ");
    }
}