using System;

public class LuxuryTourPackage : TourPackage
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

    public LuxuryTourPackage() : base()
    {
        LuxuryTaxRate = 12.0f;
    }

    public LuxuryTourPackage(int id, string dest, int days, float price, int size, float taxRate = 12.0f) 
        : base(id, dest, days, price, size)
    {
        LuxuryTaxRate = taxRate;
    }

    public override float CalculatePackageCost()
    {
        float baseCost = PricePerPerson * GroupSize;
        float taxAmount = baseCost * LuxuryTaxRate / 100;
        return baseCost + taxAmount;
    }

    public override void DisplayPackageDetails()
    {
        Console.WriteLine($"[ID: {PackageId}] Luxury tour to {Destination} for {DurationDays} days with a group of {GroupSize} people costs a total of ${CalculatePackageCost()}.");
    }
}
