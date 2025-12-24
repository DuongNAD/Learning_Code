package BTVN_Java2.OnTap.OnTap1;

import java.util.HashMap;
import java.util.Map;

public class AlertNotifier extends Thread{
    private ThreatBox threatBox;

    public static Map<String, String> level = new HashMap<String, String>();
    static {
        level.put("Malware", "High");
        level.put("Ransomware", "Critical");
        level.put("Phishing", "Medium");
        level.put("Spyware", "Low");
    }

    public AlertNotifier(ThreatBox threatBox){
        this.threatBox = threatBox;
    }

    @Override
    public void run(){
        synchronized (threatBox){
            while (!threatBox.isGenerated){
                try {
                    threatBox.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

            }
            String levelDangerous = level.get(threatBox.threat);
            System.out.println("Dangerous: " + threatBox.threat + " - "+ levelDangerous);
        }
    }
}
