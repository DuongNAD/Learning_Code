using System;

public class Program
{
    public static void Main()
    {
        TourManagement management = new TourManagement();
        bool isRunning = true;

        while (isRunning)
        {
            Console.WriteLine("\n=== TOUR MANAGEMENT MENU ===");
            Console.WriteLine("1. Add New Tour Package / Luxury Tour Package");
            Console.WriteLine("2. View All Tour Packages");
            Console.WriteLine("3. Update Tour Package Details");
            Console.WriteLine("4. Delete Tour Package");
            Console.WriteLine("5. Calculate Total Package Cost");
            Console.WriteLine("6. Exit");
            Console.Write("Your choice: ");

            string choice = Console.ReadLine();

            try
            {
                switch (choice)
                {
                    case "1":
                        AddNewPackageFlow(management);
                        break;
                    case "2":
                        management.ViewPackages();
                        break;
                    case "3":
                        Console.Write("Enter Package ID to update: ");
                        int updateId = int.Parse(Console.ReadLine());
                        Console.Write("Enter new Price per person: ");
                        float newPrice = float.Parse(Console.ReadLine());
                        Console.Write("Enter new Group Size: ");
                        int newSize = int.Parse(Console.ReadLine());
                        management.UpdatePackage(updateId, newPrice, newSize);
                        break;
                    case "4":
                        Console.Write("Enter Package ID to delete: ");
                        int deleteId = int.Parse(Console.ReadLine());
                        management.DeletePackage(deleteId);
                        break;
                    case "5":
                        Console.Write("Enter Package ID to calculate total cost: ");
                        int calcId = int.Parse(Console.ReadLine());
                        management.CalculateCostById(calcId);
                        break;
                    case "6":
                        isRunning = false;
                        Console.WriteLine("Exiting program. Goodbye!");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please select from 1 to 6.");
                        break;
                }
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Please enter a valid numerical value.");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }
        }
    }

    private static void AddNewPackageFlow(TourManagement management)
    {
        Console.Write("Enter Package ID: ");
        int id = int.Parse(Console.ReadLine());

        Console.Write("Enter Destination: ");
        string dest = Console.ReadLine();

        Console.Write("Enter Duration (days): ");
        int days = int.Parse(Console.ReadLine());

        Console.Write("Enter Price per person: ");
        float price = float.Parse(Console.ReadLine());

        Console.Write("Enter Group Size: ");
        int size = int.Parse(Console.ReadLine());

        Console.Write("Is this a luxury tour package? (y/n): ");
        string isLuxury = Console.ReadLine().ToLower();

        if (isLuxury == "y")
        {
            Console.Write("Enter Luxury Tax Rate (e.g., 12 for 12%): ");
            float tax = float.Parse(Console.ReadLine());
            LuxuryTourPackage luxury = new LuxuryTourPackage(id, dest, days, price, size, tax);
            management.AddPackage(luxury);
        }
        else
        {
            TourPackage standard = new TourPackage(id, dest, days, price, size);
            management.AddPackage(standard);
        }
    }
}
