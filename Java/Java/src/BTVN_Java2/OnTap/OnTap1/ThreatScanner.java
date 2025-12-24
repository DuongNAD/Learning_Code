package BTVN_Java2.OnTap.OnTap1;

import java.util.Random;

public class ThreatScanner extends Thread {
    private ThreatBox threatBox;
    private String[] list = {"Malware", "Ransomware", "Phishing", "Spyware"};

    public ThreatScanner(ThreatBox threatBox) {
        this.threatBox = threatBox;
    }

    @Override
    public void run() {
        synchronized (threatBox) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            String threat = list[new Random().nextInt(list.length)];
            threatBox.threat = threat;
            threatBox.isGenerated = true;

            System.out.println(threat);

            threatBox.notify();
        }
    }
}
