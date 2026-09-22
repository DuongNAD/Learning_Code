using System;

namespace PracticalExam
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("\n--- EXAM RUNNER ---");
                Console.WriteLine("1. Run Question 01");
                Console.WriteLine("2. Run Question 02");
                Console.WriteLine("3. Run Question 03");
                Console.WriteLine("0. Exit");
                Console.Write("Select an option: ");
                
                string choice = Console.ReadLine();
                Console.WriteLine();
                
                switch (choice)
                {
                    case "1":
                        Question01.Run();
                        break;
                    case "2":
                        Question02.Run();
                        break;
                    case "3":
                        Question03.Run();
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
