import JavaClassDay3.Goat;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter name: ");
        String name = sc.nextLine();
        System.out.print("Enter weight: ");
        int weight = sc.nextInt();
        Goat g = new Goat(name, weight);

        System.out.println("1. Test getName()");
        System.out.println("2. Test setWeight()");
        System.out.print("Enter TC (1 or 2): ");
        int choice = sc.nextInt();

        System.out.println("OUTPUT:");

        if (choice == 1) {
            System.out.println(g.getName());
        } else if (choice == 2) {
            System.out.print("Enter new weight: ");
            int newW = sc.nextInt();
            g.setWeight(newW);
            System.out.println(g.getWeight());
        }
    }
}