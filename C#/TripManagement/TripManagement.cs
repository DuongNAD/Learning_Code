using System;
using System.Collections.Generic;

public class TripManagement
{
    private List<Trip> trips;

    public TripManagement()
    {
        trips = new List<Trip>();
    }

    public void AddTrip(Trip newTrip)
    {
        if (trips.Exists(t => t.Id == newTrip.Id))
        {
            throw new ArgumentException("A trip with this ID already exists.");
        }
        trips.Add(newTrip);
        Console.WriteLine("Trip added successfully!");
    }

    public void ViewTrips()
    {
        if (trips.Count == 0)
        {
            Console.WriteLine("No trips available in the system.");
            return;
        }

        Console.WriteLine("\n=== ALL TRIPS ===");
        foreach (var trip in trips)
        {
            trip.DisplayTripDetails();
        }
    }

    public void UpdateTrip(string id, int newDuration, float newCostPerDay)
    {
        Trip tripToUpdate = trips.Find(t => t.Id == id);
        if (tripToUpdate != null)
        {
            tripToUpdate.DurationDays = newDuration;
            tripToUpdate.CostPerDay = newCostPerDay;
            Console.WriteLine("Trip updated successfully!");
        }
        else
        {
            Console.WriteLine($"Trip with ID {id} not found.");
        }
    }

    public void DeleteTrip(string id)
    {
        Trip tripToRemove = trips.Find(t => t.Id == id);
        if (tripToRemove != null)
        {
            trips.Remove(tripToRemove);
            Console.WriteLine("Trip deleted successfully!");
        }
        else
        {
            Console.WriteLine($"Trip with ID {id} not found.");
        }
    }

    public void CalculateTotalCostById(string id)
    {
        Trip tripToCalc = trips.Find(t => t.Id == id);
        if (tripToCalc != null)
        {
            Console.WriteLine($"The total cost for Trip ID {id} is: ${tripToCalc.CalculateTotalCost()}");
        }
        else
        {
            Console.WriteLine($"Trip with ID {id} not found.");
        }
    }
}
