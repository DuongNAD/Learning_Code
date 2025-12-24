package BTVN_Java2.OnTap.CosmeticProductOT;

import java.util.HashMap;
import java.util.Map;

class FragranceTranslator extends Thread {

    private final FragranceBox box;

    private static final Map<String, String> TRANSLATIONS = new HashMap<>();
    static {
        TRANSLATIONS.put("Lavande", "Lavender");
        TRANSLATIONS.put("Rose", "Rose");
        TRANSLATIONS.put("Vanille", "Vanilla");
        TRANSLATIONS.put("Citron", "Lemon");
        TRANSLATIONS.put("Jasmin", "Jasmine");
    }

    public FragranceTranslator(FragranceBox box) {
        this.box = box;
    }

    @Override
    public void run() {
        synchronized (box) {
            while (!box.isGenerated) {
                try {
                    box.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            String english = TRANSLATIONS.get(box.fragrance);
            System.out.println("Translated (EN): " + english);
        }
    }
}

