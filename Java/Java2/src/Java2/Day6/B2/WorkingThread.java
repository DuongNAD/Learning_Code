package Java2.Day6.B2;

import java.util.Random;

public class WorkingThread implements Runnable{
    @Override
    public void run(){
        while(true){
            processSomething();
        }
    }

    private void processSomething(){
        try{
            System.out.println("Processing working thread");
            Thread.sleep(1000);
        }catch(InterruptedException e){
            e.printStackTrace();
        }

        Random rand = new Random();
        int i = rand.nextInt(100);

        if (i == 70) {
            throw new RuntimeException("Simulate an exception was not handled in the thread");
        }
    }
}
