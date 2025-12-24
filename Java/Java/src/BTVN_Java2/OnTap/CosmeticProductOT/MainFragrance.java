package BTVN_Java2.OnTap.CosmeticProductOT;

public class MainFragrance {
    public static void main(String[] args) throws InterruptedException {
        for(int i = 1;i<=3;i++){
            System.out.println("=== RUN " + i + " ===");

            FragranceBox box = new FragranceBox();

            FragranceGenerator generator1 = new FragranceGenerator(box);
            FragranceTranslator translator1 = new FragranceTranslator(box);

            generator1.start();
            translator1.start();

            generator1.join();
            translator1.join();

        }
        System.out.println("\nAll threads completed.");
    }
}
