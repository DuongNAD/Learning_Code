using System;

public class Trip : ITrip
{
    public string Id { get; set; } 
    private string destination;
    private int durationDays;
    private float costPerDay;
    private string transportMode;

    public string Destination
    {
        get { return destination; }
        set
        {
            if (string.IsNullOrWhiteSpace(value) || value.Length < 3 || value.Length > 50)
                throw new ArgumentException("Destination must be between 3 and 50 characters.");
            destination = value;
        }
    }

    public int DurationDays
    {
        get { return durationDays; }
        set
        {
            if (value <= 0)
                throw new ArgumentException("Duration must be greater than 0.");
            durationDays = value;
        }
    }

    public float CostPerDay
    {
        get { return costPerDay; }
        set
        {
            if (value <= 0)
                throw new ArgumentException("Cost per day must be greater than 0.");
            costPerDay = value;
        }
    }

    public string TransportMode
    {
        get { return transportMode; }
        set
        {
            if (value != "Air" && value != "Train" && value != "Bus" && value != "Car")
                throw new ArgumentException("Transport mode must be one of: Air, Train, Bus, Car.");
            transportMode = value;
        }
    }

    public Trip() { }

    public Trip(string id, string destination, int durationDays, float costPerDay, string transportMode)
    {
        Id = id;
        Destination = destination;
        DurationDays = durationDays;
        CostPerDay = costPerDay;
        TransportMode = transportMode;
    }

    public virtual float CalculateTotalCost()
    {
        return DurationDays * CostPerDay;
    }

    public virtual void DisplayTripDetails()
    {
        Console.WriteLine($"[ID: {Id}] Trip to {Destination} for {DurationDays} days via {TransportMode} costs a total of ${CalculateTotalCost()}.");
    }
}
