package Java2.Day6.B3;

public class ShareMemory {
    public synchronized
    void printData(String threadName) {
        for (int i = 1; i <= 5; i++) {
            System.out.println(threadName + ": " + i);
        }
    }
}