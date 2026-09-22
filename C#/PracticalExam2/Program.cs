using System;

namespace PracticalExam2
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("\n--- EXAM RUNNER ---");
                Console.WriteLine("1. Run Question 1 (EmployeeTest)");
                Console.WriteLine("2. Run Question 2 (PersonTest)");
                Console.WriteLine("0. Exit");
                Console.Write("Select an option: ");
                
                string choice = Console.ReadLine();
                Console.WriteLine();
                
                switch (choice)
                {
                    case "1":
                        EmployeeTest.Run();
                        break;
                    case "2":
                        PersonTest.Run();
                        break;
                    case "0":
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }
            }
        }
    }
}
