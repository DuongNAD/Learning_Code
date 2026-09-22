using System;
using System.Collections.Generic;

public class TourManagement
{
    private List<TourPackage> packages;

    public TourManagement()
    {
        packages = new List<TourPackage>();
    }

    public void AddPackage(TourPackage newPackage)
    {
        if (packages.Exists(p => p.PackageId == newPackage.PackageId))
        {
            throw new ArgumentException("A tour package with this ID already exists.");
        }
        packages.Add(newPackage);
        Console.WriteLine("Tour package added successfully!");
    }

    public void ViewPackages()
    {
        if (packages.Count == 0)
        {
            Console.WriteLine("No tour packages available in the system.");
            return;
        }

        Console.WriteLine("\n=== ALL TOUR PACKAGES ===");
        foreach (var pkg in packages)
        {
            pkg.DisplayPackageDetails();
        }
    }

    public void UpdatePackage(int id, float newPrice, int newGroupSize)
    {
        TourPackage pkgToUpdate = packages.Find(p => p.PackageId == id);
        if (pkgToUpdate != null)
        {
            pkgToUpdate.PricePerPerson = newPrice;
            pkgToUpdate.GroupSize = newGroupSize;
            Console.WriteLine("Tour package updated successfully!");
        }
        else
        {
            Console.WriteLine($"Tour package with ID {id} not found.");
        }
    }

    public void DeletePackage(int id)
    {
        TourPackage pkgToRemove = packages.Find(p => p.PackageId == id);
        if (pkgToRemove != null)
        {
            packages.Remove(pkgToRemove);
            Console.WriteLine("Tour package deleted successfully!");
        }
        else
        {
            Console.WriteLine($"Tour package with ID {id} not found.");
        }
    }

    public void CalculateCostById(int id)
    {
        TourPackage pkg = packages.Find(p => p.PackageId == id);
        if (pkg != null)
        {
            Console.WriteLine($"The total cost for Package ID {id} is: ${pkg.CalculatePackageCost()}");
        }
        else
        {
            Console.WriteLine($"Tour package with ID {id} not found.");
        }
    }
}
