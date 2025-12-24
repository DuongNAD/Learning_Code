package BTVN_Java2.OnTapB2;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class Fragrance {
    private Map<String, String> fragranceMap;
    private final Object lock = new Object();
    private Random random = new Random();
    Fragrance() {
        fragranceMap = new HashMap<>();
    }

    public void start() {
        synchronized (lock) {
            fragranceMap.clear();
        }
    }

    class randomFragrance extends Thread {
        @Override
        public void run() {
            String FragranceRandom;
            int randomNumber = random.nextInt(5) + 1;
            switch(randomNumber) {
                case 1:
                    FragranceRandom = "Lavande";
                    break;
                case 2:
                    FragranceRandom = "Rose";
                    break;
                case 3:
                    FragranceRandom = "Vanille";
                    break;
                case 4:
                    FragranceRandom = "Citron";
                    break;
                case 5:
                    FragranceRandom = "Jasmin";
                    break;
            }
        }
    }

    class translaterFragrance extends Thread {
        @Override
        public void run() {
            String Fragrance;

        }
    }
}
