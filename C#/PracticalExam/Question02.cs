using System;
using System.Collections.Generic;

namespace PracticalExam
{
    class Question02
    {
        public static void PrintNumbersInRange(List<int> numbers, int lowerLimit, int upperLimit)
        {
            foreach (int number in numbers)
            {
                if (number >= lowerLimit && number <= upperLimit)
                {
                    Console.WriteLine(number);
                }
            }
        }

        public static void Run()
        {
            List<int> numbers = new List<int>();
            numbers.Add(3);
            numbers.Add(2);
            numbers.Add(6);
            numbers.Add(-1);
            numbers.Add(5);
            numbers.Add(1);

            Console.WriteLine("The numbers in the range [0, 5]");
            PrintNumbersInRange(numbers, 0, 5);

            Console.WriteLine("The numbers in the range [3, 10]");
            PrintNumbersInRange(numbers, 3, 10);
        }
    }
}
