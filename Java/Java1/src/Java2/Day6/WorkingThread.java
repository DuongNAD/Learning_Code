package Java2.Day6;

public class WorkingThread extends Thread{
    public WorkingThread(String name){
        super(name);
    }
    public void run(){
        for(int i=0;i<5;i++){
            System.out.printf("Luồng: %s có độ ưu tiên là %d\n", this.getName(), this.getPriority());
        }
    }
}
