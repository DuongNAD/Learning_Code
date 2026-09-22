using System;

public class LuxuryTrip : Trip
{
    private float luxuryTaxRate;

    public float LuxuryTaxRate
    {
        get { return luxuryTaxRate; }
        set
        {
            if (value < 0)
                throw new ArgumentException("Luxury tax rate cannot be negative.");
            luxuryTaxRate = value;
        }
    }

    public LuxuryTrip() : base()
    {
        LuxuryTaxRate = 15.0f; 
    }

    public LuxuryTrip(string id, string destination, int durationDays, float costPerDay, string transportMode, float luxuryTaxRate = 15.0f)
        : base(id, destination, durationDays, costPerDay, transportMode)
    {
        LuxuryTaxRate = luxuryTaxRate;
    }

    public override float CalculateTotalCost()
    {
        float baseCost = DurationDays * CostPerDay;
        return baseCost + (baseCost * LuxuryTaxRate / 100);
    }

    public override void DisplayTripDetails()
    {
        Console.WriteLine($"[ID: {Id}] Luxury trip to {Destination} for {DurationDays} days via {TransportMode} costs a total of ${CalculateTotalCost()}.");
    }
}
