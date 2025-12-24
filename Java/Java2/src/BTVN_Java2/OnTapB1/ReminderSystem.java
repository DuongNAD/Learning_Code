package BTVN_Java2.OnTapB1;

import java.util.HashMap;
import java.util.Map;

public class ReminderSystem {
    private Map<String,Integer> studentMaps;

    private final Object lock = new Object();
    private String overdueStudentName = null;
    ReminderSystem(){
        studentMaps = new HashMap<>();
    }
    public void addReminder(String student, int dayLeft){
        studentMaps.put(student,dayLeft);

    }
    public void start(){
        CountDownNotifierThread countDownNotifierThread = new CountDownNotifierThread();
        FinalWarningThread finalWarningThread = new FinalWarningThread();

        countDownNotifierThread.start();
        finalWarningThread.start();
    }
    class CountDownNotifierThread extends Thread{
        @Override
        public void run() {
            for(Map.Entry<String,Integer> entry:studentMaps.entrySet()){

                String student = entry.getKey();
                int dayLeft = entry.getValue();

                while(dayLeft > 0) {
                    System.out.printf("Reminder: %s has %d days left to pay.\n", student, dayLeft);
                    dayLeft--;
                    try {
                        Thread.sleep(1000);
                    }
                    catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
                synchronized (lock) {
                    overdueStudentName = student;
                    lock.notify();
                }

            }
        }
    }
    class FinalWarningThread extends Thread{
        @Override
        public void run() {
            synchronized (lock) {
                while (overdueStudentName == null) {
                    try {
                        lock.wait();
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
                System.out.printf("Final Warning: %s payment is overdue!", overdueStudentName);
            }
        }
    }
    public static void main(String[] args) {
        ReminderSystem reminderSystem = new ReminderSystem();
        reminderSystem.addReminder("John",5);
        reminderSystem.start();
    }
}
