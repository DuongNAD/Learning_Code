package BTVN_Java2.Day8;

public class ThreadSafeLazyInitizedSingleton {
    private static ThreadSafeLazyInitizedSingleton instance;
    private ThreadSafeLazyInitizedSingleton() {

    }
    public static ThreadSafeLazyInitizedSingleton getInstance() {
        if(instance == null) {
            instance = new ThreadSafeLazyInitizedSingleton();
        }
        return instance;
    }

}
