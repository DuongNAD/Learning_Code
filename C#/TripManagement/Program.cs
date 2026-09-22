using System;

public class Program
{
    public static void Main()
    {
        TripManagement management = new TripManagement();
        bool isRunning = true;

        while (isRunning)
        {
            Console.WriteLine("\n=== TRIP MANAGEMENT MENU ===");
            Console.WriteLine("1. Add New Trip / Luxury Trip");
            Console.WriteLine("2. View All Trips");
            Console.WriteLine("3. Update Trip Details");
            Console.WriteLine("4. Delete Trip");
            Console.WriteLine("5. Calculate Total Cost");
            Console.WriteLine("6. Exit");
            Console.Write("Your choice: ");

            string choice = Console.ReadLine();

            try
            {
                switch (choice)
                {
                    case "1":
                        AddNewTripFlow(management);
                        break;
                    case "2":
                        management.ViewTrips();
                        break;
                    case "3":
                        Console.Write("Enter Trip ID to update: ");
                        string updateId = Console.ReadLine();
                        Console.Write("Enter new Duration (days): ");
                        int newDuration = int.Parse(Console.ReadLine());
                        Console.Write("Enter new Cost per day: ");
                        float newCost = float.Parse(Console.ReadLine());
                        management.UpdateTrip(updateId, newDuration, newCost);
                        break;
                    case "4":
                        Console.Write("Enter Trip ID to delete: ");
                        string deleteId = Console.ReadLine();
                        management.DeleteTrip(deleteId);
                        break;
                    case "5":
                        Console.Write("Enter Trip ID to calculate total cost: ");
                        string calcId = Console.ReadLine();
                        management.CalculateTotalCostById(calcId);
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
                Console.WriteLine("Error: Please enter a valid number format.");
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

    private static void AddNewTripFlow(TripManagement management)
    {
        Console.Write("Enter Trip ID: ");
        string id = Console.ReadLine();

        Console.Write("Enter Destination: ");
        string dest = Console.ReadLine();

        Console.Write("Enter Duration (days): ");
        int days = int.Parse(Console.ReadLine());

        Console.Write("Enter Cost per day: ");
        float cost = float.Parse(Console.ReadLine());

        Console.Write("Enter Transport Mode (Air, Train, Bus, Car): ");
        string mode = Console.ReadLine();

        Console.Write("Is this a luxury trip? (y/n): ");
        string isLuxury = Console.ReadLine().ToLower();

        if (isLuxury == "y")
        {
            Console.Write("Enter Luxury Tax Rate (e.g., 15 for 15%): ");
            float tax = float.Parse(Console.ReadLine());
            LuxuryTrip luxuryTrip = new LuxuryTrip(id, dest, days, cost, mode, tax);
            management.AddTrip(luxuryTrip);
        }
        else
        {
            Trip standardTrip = new Trip(id, dest, days, cost, mode);
            management.AddTrip(standardTrip);
        }
    }
}
