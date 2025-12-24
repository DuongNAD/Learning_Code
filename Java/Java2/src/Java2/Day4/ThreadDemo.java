package Java2.Day4;

public class ThreadDemo extends Thread {
    private Thread t;
    private String threadName;

    // --- SỬA Ở ĐÂY (FIX HERE) ---
    ThreadDemo(String name) {
        // English: Assign the parameter 'name' to the field 'threadName'
        // Vietnamese: Gán tham số 'name' vào biến 'threadName'
        this.threadName = name; // Hoặc viết: threadName = name;

        System.out.println("Creating " + threadName);
    }
    // ----------------------------

    @Override
    public void run() {
        System.out.println("Running " + threadName);
        try {
            for (int i = 4; i > 0; i--) {
                System.out.println(threadName + ": " + i);
                Thread.sleep(50);
            }
        } catch (InterruptedException e) {
            System.out.println("Thread " + threadName + " interrupted");
        }
        System.out.println("Thread " + threadName + " exiting.");
    }

    public void start() {
        System.out.println("Starting " + threadName);
        if (t == null) {
            // Lúc này threadName đã có giá trị, không bị lỗi NullPointer nữa
            t = new Thread(this, threadName);
            t.start();
        }
    }
}