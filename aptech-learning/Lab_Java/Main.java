import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== CAR SHOWROOM SALES CHECK SYSTEM ===");
        
        while (true) {
            System.out.println("\n--- New Customer Check ---");

            System.out.print("Name: ");
            String nameInput = scanner.nextLine();
 
            System.out.print("Color: ");
            String colorInput = scanner.nextLine();
            
            System.out.print("Price: ");
            String priceInput = scanner.nextLine();
            
            System.out.print("Today: ");
            String todayInput = scanner.nextLine();

            Car carEnum = Car.getCar(nameInput);
            Color colorEnum = Color.getColor(colorInput);
            Day dayEnum = Day.getDay(todayInput);

            try {
                CarValidation.checkCar(carEnum, colorEnum, dayEnum, priceInput);
                System.out.println("Sell Car Successful");
            } catch (ExceptionCar e) {
                System.out.println(e.getMessage());
            }
            System.out.print("Do you want find more?(Y/N): ");
            String findMoreChoice = scanner.nextLine().trim();
            if (findMoreChoice.equalsIgnoreCase("N")) {
                break;
            }
        }      
        System.out.println("\nThank you for using the Car Showroom Sales Check System!");
    }
}
