package BTVN_Java2.Day2;

public class Box <T>{
    private T value;

    public void  setValue(T value){
        this.value = value;
    }
    public T getValue(){
        return value;
    }

    public void printBox(){
        System.out.println("Value: " +value);
    }
}

