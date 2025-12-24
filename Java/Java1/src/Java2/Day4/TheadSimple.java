package Java2.Day4;

public class TheadSimple extends Thread{
    public void run(){
        System.out.println("thead is running ....");
    }


    public static void main(String[] args){
        TheadSimple thread1 = new TheadSimple();
        thread1.start();
    }
}
