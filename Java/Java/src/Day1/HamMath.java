package Day1;

public class HamMath {
    static void main() {
        int min = 5;
        int max = 12;
        int a = (int)(Math.random() * (max - min)+1) +min;
        System.out.printf("a = %d\n",a);
        System.out.printf("a = %f",Math.sqrt(a));
    }
}
