using System;

namespace PracticalExam
{
    class Question01
    {
        public static void Run()
        {
            Console.Write("Enter the First number: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter the Second number: ");
            double num2 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter the third number: ");
            double num3 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter the fourth number: ");
            double num4 = Convert.ToDouble(Console.ReadLine());

            double average = (num1 + num2 + num3 + num4) / 4;

            Console.WriteLine($"The average of {num1}, {num2}, {num3}, {num4} is: {average}");
        }
    }
}
