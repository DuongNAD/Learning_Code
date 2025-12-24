package BTVN_Java2.OnTap.OnTap1;

public class MainB2 {
    public static void main(String[] args) throws InterruptedException {
        for (int i = 1; i <= 3; i++) {
            System.out.println("=== RUN " + i + " ===");

            ThreatBox box = new ThreatBox();

            ThreatScanner threatScanner = new ThreatScanner(box);
            AlertNotifier alertNotifier = new AlertNotifier(box);

            threatScanner.start();
            alertNotifier.start();

            threatScanner.join();
            alertNotifier.join();
        }

        System.out.println("=== END ===");
    }
}
