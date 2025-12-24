package BTVN_Java2.OnTap.CosmeticProductOT;

import java.util.Arrays;
import java.util.List;
import java.util.Random;

class FragranceGenerator extends Thread {

    private final FragranceBox box;
    private final String[] fragrances = {
            "Lavande", "Rose", "Vanille", "Citron", "Jasmin"
    };

    public FragranceGenerator(FragranceBox box) {
        this.box = box;
    }

    @Override
    public void run() {
        synchronized (box) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            String generated = fragrances[new Random().nextInt(fragrances.length)];
            box.fragrance = generated;
            box.isGenerated = true;

            System.out.println("Generated (FR): " + generated);

            box.notify();
        }
    }
}
