using System;

namespace PracticalExam3
{
    public class Product : IProduct
    {
        private string _name;
        private string _category;
        private float _price;
        private float _discountRate;

        public string Name { get { return _name; } set { _name = value; } }
        public string Category { get { return _category; } set { _category = value; } }
        public float Price { get { return _price; } set { _price = value; } }
        public float DiscountRate { get { return _discountRate; } set { _discountRate = value; } }

        public Product() {}
        
        public Product(string name, string category, float price, float discountRate)
        {
            _name = name;
            _category = category;
            _price = price;
            _discountRate = discountRate;
        }

        public float CalculateDiscount()
        {
            return _price * (_discountRate / 100f);
        }

        public virtual float GetFinalPrice()
        {
            return _price - CalculateDiscount();
        }

        public virtual void DisplayProductInfo()
        {
            Console.WriteLine($"Product: {Name}");
            Console.WriteLine($"Category: {Category}");
            Console.WriteLine($"Price: ${Price}");
            Console.WriteLine($"Discount: ${CalculateDiscount()}");
            Console.WriteLine($"Final Price: ${GetFinalPrice()}");
        }
    }
}
