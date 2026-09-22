using System;
using System.Collections.Generic;
using System.Linq;

namespace PracticalExam3
{
    public class ProductTest
    {
        private List<Product> _products = new List<Product>();

        public void Run()
        {
            while (true)
            {
                Console.WriteLine("\n=== PRODUCT MANAGEMENT MENU ===");
                Console.WriteLine("1. Add New Product");
                Console.WriteLine("2. Display All Products");
                Console.WriteLine("3. Update Product");
                Console.WriteLine("4. Delete Product");
                Console.WriteLine("5. Search for a Product");
                Console.WriteLine("6. Exit");
                Console.Write("Your choice: ");
                
                string choice = Console.ReadLine();
                Console.WriteLine();
                
                switch (choice)
                {
                    case "1":
                        AddProduct();
                        break;
                    case "2":
                        DisplayProducts();
                        break;
                    case "3":
                        UpdateProduct();
                        break;
                    case "4":
                        DeleteProduct();
                        break;
                    case "5":
                        SearchProduct();
                        break;
                    case "6":
                        Console.WriteLine("Exiting program...");
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        private void ValidateInput(out string name, out string category, out float price, out float discount)
        {
            while (true)
            {
                try
                {
                    Console.Write("Enter Product Name: ");
                    name = Console.ReadLine();
                    if (string.IsNullOrWhiteSpace(name))
                        throw new Exception("Name cannot be empty or null.");
                        
                    Console.Write("Enter Category: ");
                    category = Console.ReadLine();
                    if (string.IsNullOrWhiteSpace(category))
                        throw new Exception("Category cannot be empty or null.");

                    Console.Write("Enter Price: ");
                    if (!float.TryParse(Console.ReadLine(), out price) || price <= 0)
                        throw new Exception("Price must be greater than 0.");

                    Console.Write("Enter Discount Rate (%): ");
                    if (!float.TryParse(Console.ReadLine(), out discount) || discount > 50 || discount < 0)
                        throw new Exception("Discount rate must not exceed 50% and cannot be negative.");

                    // If we made it here, no exception was thrown, valid input!
                    break;
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error: {ex.Message}");
                    Console.WriteLine("Please re-enter valid input.\n");
                }
            }
        }

        private void AddProduct()
        {
            Console.WriteLine("--- Add New Product ---");
            ValidateInput(out string name, out string category, out float price, out float discount);
            
            // Additional flexibility for SpecialProduct
            Console.Write("Is this a Special Product? (y/n): ");
            string specialOpt = Console.ReadLine();
            if (!string.IsNullOrEmpty(specialOpt) && specialOpt.Trim().ToLower() == "y")
            {
                Console.Write("Enter Special Rate (%): ");
                if (float.TryParse(Console.ReadLine(), out float specialRate))
                {
                    SpecialProduct sp = new SpecialProduct(name, category, price, discount, specialRate);
                    _products.Add(sp);
                }
                else
                {
                    Console.WriteLine("Invalid Special Rate. Falling back to normal Product.");
                    _products.Add(new Product(name, category, price, discount));
                }
            }
            else
            {
                _products.Add(new Product(name, category, price, discount));
            }
            
            Console.WriteLine("Product added successfully!");
        }

        private void DisplayProducts()
        {
            Console.WriteLine("--- Display All Products ---");
            if (_products.Count == 0)
            {
                Console.WriteLine("No products available.");
                return;
            }
            
            foreach (var product in _products)
            {
                product.DisplayProductInfo();
                Console.WriteLine("-------------------------");
            }
        }

        private void UpdateProduct()
        {
            Console.WriteLine("--- Update Product ---");
            Console.Write("Enter the product name to update: ");
            string searchName = Console.ReadLine();
            
            var product = _products.FirstOrDefault(p => p.Name.Equals(searchName, StringComparison.OrdinalIgnoreCase));
            if (product != null)
            {
                Console.WriteLine("Product found. Please enter new details:");
                ValidateInput(out string name, out string category, out float price, out float discount);
                
                product.Name = name;
                product.Category = category;
                product.Price = price;
                product.DiscountRate = discount;
                
                if (product is SpecialProduct sp)
                {
                    Console.Write("Enter new Special Rate (%): ");
                    if (float.TryParse(Console.ReadLine(), out float specialRate))
                    {
                        sp.SpecialRate = specialRate;
                    }
                }

                Console.WriteLine("Product updated successfully!");
            }
            else
            {
                Console.WriteLine("Error: Product not found.");
            }
        }

        private void DeleteProduct()
        {
            Console.WriteLine("--- Delete Product ---");
            Console.Write("Enter the product name to delete: ");
            string searchName = Console.ReadLine();
            
            var product = _products.FirstOrDefault(p => p.Name.Equals(searchName, StringComparison.OrdinalIgnoreCase));
            if (product != null)
            {
                _products.Remove(product);
                Console.WriteLine("Product deleted successfully!");
            }
            else
            {
                Console.WriteLine("Error: Product not found.");
            }
        }

        private void SearchProduct()
        {
            Console.WriteLine("--- Search Product ---");
            Console.Write("Enter the product name to search: ");
            string searchName = Console.ReadLine();
            
            var product = _products.FirstOrDefault(p => p.Name.Equals(searchName, StringComparison.OrdinalIgnoreCase));
            if (product != null)
            {
                Console.WriteLine("\nProduct Details:");
                product.DisplayProductInfo();
            }
            else
            {
                Console.WriteLine("Product not found.");
            }
        }
    }
}
