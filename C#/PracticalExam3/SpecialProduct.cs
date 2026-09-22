using System;

namespace PracticalExam3
{
    public class SpecialProduct : Product
    {
        private float _specialRate;
        
        public float SpecialRate { get { return _specialRate; } set { _specialRate = value; } }

        public SpecialProduct(string name, string category, float price, float discountRate, float specialRate)
            : base(name, category, price, discountRate)
        {
            _specialRate = specialRate;
        }

        public override float GetFinalPrice()
        {
            return Price - CalculateDiscount() + (Price * (_specialRate / 100f));
        }

        public override void DisplayProductInfo()
        {
            Console.WriteLine($"Product: {Name} (Special)");
            Console.WriteLine($"Category: {Category}");
            Console.WriteLine($"Price: ${Price}");
            Console.WriteLine($"Discount: ${CalculateDiscount()}");
            float specialCharge = Price * (_specialRate / 100f);
            Console.WriteLine($"Special Charge: ${specialCharge}");
            Console.WriteLine($"Final Price: ${GetFinalPrice()}");
        }
    }
}
