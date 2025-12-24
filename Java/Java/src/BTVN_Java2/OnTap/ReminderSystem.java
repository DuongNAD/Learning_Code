package BTVN_Java2.OnTap;

import java.util.HashMap;
import java.util.Map;

public class ReminderSystem {
    private Map<String, Integer> studentMaps;
    private final Object lock = new Object();
    private String overdueStudentName = null;

    ReminderSystem() {
        studentMaps = new HashMap<String, Integer>();
    }
    public void addReminder(String studentID, int reminder) {
        studentMaps.put(studentID, reminder);
    }

    public void start(){
        CountDownNotifierThread countDownNotifierThread = new CountDownNotifierThread();
        countDownNotifierThread.start();
        FinalWaringThread finalWaringThread = new FinalWaringThread();
        finalWaringThread.start();
    }

    class CountDownNotifierThread extends Thread {
        @Override
        public void run() {
            for(Map.Entry<String, Integer> entry : studentMaps.entrySet()) {
                String student = entry.getKey();
                int reminder = entry.getValue();

                while(reminder > 0){
                    System.out.printf("Reminder: %s has %d days left to pay.\n", student, reminder);
                    reminder --;
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
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

    class FinalWaringThread extends Thread {
        @Override
        public void run() {
            synchronized (lock) {
                while(overdueStudentName == null){
                    try {
                        lock.wait();
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
                System.out.printf("Final Waring: %s payment is overdue!",overdueStudentName);
            }
        }
    }

    public static void main(String[] args) {
        ReminderSystem reminderSystem = new ReminderSystem();
        reminderSystem.addReminder("John", 5);
        reminderSystem.start();
    }
}
