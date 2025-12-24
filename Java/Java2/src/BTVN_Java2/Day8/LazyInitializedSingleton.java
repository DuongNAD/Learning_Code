package BTVN_Java2.Day8;

public class LazyInitializedSingleton {
    private static LazyInitializedSingleton instance;

    private LazyInitializedSingleton() {}
    public static LazyInitializedSingleton getInstance() {
        if (instance == null) {
            instance = new LazyInitializedSingleton();
        }
        return instance;
    }
    public static void main(String[] args) {
        LazyInitializedSingleton singleton = LazyInitializedSingleton.getInstance();
        if(singleton == null) {
            System.out.println("New");
        }
            System.out.println("Already Initialized");
    }
}
