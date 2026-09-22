using System;

public class TourPackage : ITourPackage
{
    private int packageId;
    private string destination;
    private int durationDays;
    private float pricePerPerson;
    private int groupSize;

    public int PackageId
    {
        get { return packageId; }
        set { packageId = value; }
    }

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

    public float PricePerPerson
    {
        get { return pricePerPerson; }
        set
        {
            if (value <= 0)
                throw new ArgumentException("Price per person must be greater than 0.");
            pricePerPerson = value;
        }
    }

    public int GroupSize
    {
        get { return groupSize; }
        set
        {
            if (value <= 0)
                throw new ArgumentException("Group size must be greater than 0.");
            groupSize = value;
        }
    }

    public TourPackage() { }

    public TourPackage(int id, string dest, int days, float price, int size)
    {
        PackageId = id;
        Destination = dest;
        DurationDays = days;
        PricePerPerson = price;
        GroupSize = size;
    }

    public virtual float CalculatePackageCost()
    {
        return PricePerPerson * GroupSize;
    }

    public virtual void DisplayPackageDetails()
    {
        Console.WriteLine($"[ID: {PackageId}] Tour to {Destination} for {DurationDays} days with a group of {GroupSize} people costs a total of ${CalculatePackageCost()}.");
    }
}
