using System;

namespace PracticalExam3
{
    public interface IProduct
    {
        float CalculateDiscount();
        float GetFinalPrice();
        void DisplayProductInfo();
    }
}
