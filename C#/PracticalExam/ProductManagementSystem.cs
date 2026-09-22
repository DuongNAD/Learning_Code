using System;
using System.Collections.Generic;
using System.Linq;

namespace PracticalExam
{
    // Question 1: Create an Interface
    public interface IProduct
    {
        float CalculateDiscount();
        float GetFinalPrice();
        void DisplayProductInfo();
    }

    // Question 1: Implement the IProduct Interface in the Product Class
    public class Product : IProduct
    {
        // Private fields (inferred from the requirements)
        private string name;
        private string category;
        private float price;
        private float discountRate;

        // Public properties to access the private fields
        public string Name { get => name; set => name = value; }
        public string Category { get => category; set => category = value; }
        public float Price { get => price; set => price = value; }
        public float DiscountRate { get => discountRate; set => discountRate = value; }

        public Product() { }

        public Product(string name, string category, float price, float discountRate)
        {
            this.name = name;
            this.category = category;
            this.price = price;
            this.discountRate = discountRate;
        }

        // Calculates the discount based on the price and discount rate
        public virtual float CalculateDiscount()
        {
            return price * (discountRate / 100);
        }

        // Calculates the final price after applying the discount
        public virtual float GetFinalPrice()
        {
            return price - CalculateDiscount();
        }

        // Displays all product details
        public virtual void DisplayProductInfo()
        {
            Console.WriteLine($"Product: {name}");
            Console.WriteLine($"Category: {category}");
            Console.WriteLine($"Price: ${price}");
            Console.WriteLine($"Discount: ${CalculateDiscount()}");
            Console.WriteLine($"Final Price: ${GetFinalPrice()}");
        }
    }

    // Question 1: Create a Subclass SpecialProduct
    public class SpecialProduct : Product
    {
        // Additional field (inferred for special calculation)
        private float specialRate;

        public float SpecialRate { get => specialRate; set => specialRate = value; }

        public SpecialProduct() : base() { }

        public SpecialProduct(string name, string category, float price, float discountRate, float specialRate) 
            : base(name, category, price, discountRate)
        {
            this.specialRate = specialRate;
        }

        // Override the GetFinalPrice() method
        public override float GetFinalPrice()
        {
            return Price - CalculateDiscount() + (Price * specialRate / 100);
        }

        // Display extended details for SpecialProduct
        public override void DisplayProductInfo()
        {
            base.DisplayProductInfo();
            Console.WriteLine($"Special Rate: {specialRate}%");
            Console.WriteLine($"Special Charge: ${Price * specialRate / 100}");
        }
    }

    // Question 3, 4, 5
    public class ProductTest
    {
        // Maintain a list of products
        private List<Product> products = new List<Product>();

        // Question 2: Exception Handling and Validation
        public static bool ValidateInput(string name, string category, float price, float discountRate)
        {
            try
            {
                if (string.IsNullOrWhiteSpace(name) || string.IsNullOrWhiteSpace(category))
                {
                    throw new ArgumentException("Name or Category cannot be empty or null.");
                }
                if (price <= 0)
                {
                    throw new ArgumentException("Price must be greater than 0.");
                }
                if (discountRate < 0 || discountRate > 50)
                {
                    throw new ArgumentException("Discount rate must not exceed 50%.");
                }
                return true;
            }
            catch (Exception ex)
            {
                // Display error message if validation fails
                Console.WriteLine($"Error: {ex.Message}");
                return false;
            }
        }

        // Question 3: Add Product
        public void AddProduct()
        {
            while (true)
            {
                Console.Write("Enter Product Name: ");
                string name = Console.ReadLine();

                Console.Write("Enter Category: ");
                string category = Console.ReadLine();

                Console.Write("Enter Price: ");
                float price;
                float.TryParse(Console.ReadLine(), out price);

                Console.Write("Enter Discount Rate (%): ");
                float discountRate;
                float.TryParse(Console.ReadLine(), out discountRate);

                // Use ValidateInput() to ensure valid inputs
                if (ValidateInput(name, category, price, discountRate))
                {
                    // Create an instance of Product
                    Product p = new Product(name, category, price, discountRate);
                    products.Add(p);
                    Console.WriteLine("Product added successfully!");
                    break; // Exit loop on success
                }
                else
                {
                    // Validation failed, iterate loop to prompt re-entry
                    Console.WriteLine("Please re-enter valid input.\n");
                }
            }
        }

        // Question 3: Display Products
        public void DisplayProducts()
        {
            if (products.Count == 0)
            {
                Console.WriteLine("No products to display.");
                return;
            }

            // Loop through the list and display details
            foreach (var p in products)
            {
                Console.WriteLine("-----------------------");
                p.DisplayProductInfo();
            }
            Console.WriteLine("-----------------------");
        }

        // Question 4: Update a Product
        public void UpdateProduct()
        {
            Console.Write("Enter the name of the product to update: ");
            string name = Console.ReadLine();
            
            // Search for the product ignoring string case
            var product = products.FirstOrDefault(p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase));

            if (product != null)
            {
                while (true)
                {
                    Console.WriteLine("Enter new details:");
                    Console.Write("Enter Product Name: ");
                    string newName = Console.ReadLine();

                    Console.Write("Enter Category: ");
                    string category = Console.ReadLine();

                    Console.Write("Enter Price: ");
                    float price;
                    float.TryParse(Console.ReadLine(), out price);

                    Console.Write("Enter Discount Rate (%): ");
                    float discountRate;
                    float.TryParse(Console.ReadLine(), out discountRate);

                    if (ValidateInput(newName, category, price, discountRate))
                    {
                        product.Name = newName;
                        product.Category = category;
                        product.Price = price;
                        product.DiscountRate = discountRate;
                        Console.WriteLine("Product updated successfully!");
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Please re-enter valid input.\n");
                    }
                }
            }
            else
            {
                Console.WriteLine("Product not found.");
            }
        }

        // Question 4: Delete a Product
        public void DeleteProduct()
        {
            Console.Write("Enter the name of the product to delete: ");
            string name = Console.ReadLine();
            var product = products.FirstOrDefault(p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase));

            if (product != null)
            {
                products.Remove(product);
                Console.WriteLine("Product deleted successfully!");
            }
            else
            {
                Console.WriteLine("Product not found.");
            }
        }

        // Question 5: Search for a Product
        public void SearchProduct()
        {
            Console.Write("Enter the name of the product to search: ");
            string name = Console.ReadLine();
            var product = products.FirstOrDefault(p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase));

            if (product != null)
            {
                Console.WriteLine("-----------------------");
                product.DisplayProductInfo();
                Console.WriteLine("-----------------------");
            }
            else
            {
                Console.WriteLine("Product not found.");
            }
        }

        // Run the menu program
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
    }
}
