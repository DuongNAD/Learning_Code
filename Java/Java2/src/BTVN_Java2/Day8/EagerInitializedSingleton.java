package BTVN_Java2.Day8;

public class EagerInitializedSingleton {
    private static final EagerInitializedSingleton instance = new EagerInitializedSingleton();
    private EagerInitializedSingleton() {

    }
    public static EagerInitializedSingleton getInstance() {
        return instance;
    }

    public static void main(String[] args) {
        EagerInitializedSingleton singleton = EagerInitializedSingleton.getInstance();
        EagerInitializedSingleton singleton2 = EagerInitializedSingleton.getInstance();
        EagerInitializedSingleton singleton3 = new EagerInitializedSingleton();
        EagerInitializedSingleton singleton4 = new EagerInitializedSingleton();
        if(singleton == singleton2) {
            System.out.println("==");
        }
        else {
            System.out.println("=/=");
        }
    }

}
