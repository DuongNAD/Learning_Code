using System;
using System.Collections.Generic;
using System.Linq;

namespace PracticalExam
{
    public abstract class Teacher
    {
        public string Code { get; set; }
        public string Name { get; set; }

        public Teacher() { }

        public Teacher(string code, string name)
        {
            Code = code;
            Name = name;
        }

        public virtual void Show()
        {
            Console.WriteLine($"Code: {Code}, Name: {Name}, Salary: {GetSalary():N0}");
        }

        public abstract double GetSalary();
    }

    public class FulltimeTeacher : Teacher
    {
        public double SalaryCoefficient { get; set; }

        public FulltimeTeacher() : base() { }

        public FulltimeTeacher(string code, string name, double salaryCoefficient) : base(code, name)
        {
            SalaryCoefficient = salaryCoefficient;
        }

        public override double GetSalary()
        {
            return SalaryCoefficient * 2000000;
        }

        public override void Show()
        {
            Console.WriteLine($"[Full-time] Code: {Code}, Name: {Name}, Coefficient: {SalaryCoefficient}, Salary: {GetSalary():N0}");
        }
    }

    public class ParttimeTeacher : Teacher
    {
        public int NumberOfHours { get; set; }

        public ParttimeTeacher() : base() { }

        public ParttimeTeacher(string code, string name, int numberOfHours) : base(code, name)
        {
            NumberOfHours = numberOfHours;
        }

        public override double GetSalary()
        {
            return NumberOfHours * 180000;
        }

        public override void Show()
        {
            Console.WriteLine($"[Part-time] Code: {Code}, Name: {Name}, Hours: {NumberOfHours}, Salary: {GetSalary():N0}");
        }
    }

    class Question03
    {
        public static void Run()
        {
            List<Teacher> teachers = new List<Teacher>
            {
                new FulltimeTeacher("FT01", "Alice", 2.0),
                new FulltimeTeacher("FT02", "Bob", 3.5),
                new FulltimeTeacher("FT03", "Charlie", 2.8),
                new FulltimeTeacher("FT04", "David", 4.0),
                new FulltimeTeacher("FT05", "Eve", 2.5),
                new ParttimeTeacher("PT01", "Frank", 15),
                new ParttimeTeacher("PT02", "Grace", 25),
                new ParttimeTeacher("PT03", "Hank", 30),
                new ParttimeTeacher("PT04", "Ivy", 45), 
                new ParttimeTeacher("PT05", "Jack", 20)
            };

            Console.WriteLine("=== ALl TEACHERS INFORMATION ===");
            foreach (var teacher in teachers)
            {
                teacher.Show();
            }

            Console.WriteLine("\n=== TEACHERS WITH THE HIGHEST SALARY ===");
            double maxSalary = teachers.Max(t => t.GetSalary());
            var highestPaidTeachers = teachers.Where(t => t.GetSalary() == maxSalary);
            foreach (var teacher in highestPaidTeachers)
            {
                teacher.Show();
            }

            Console.WriteLine("\n=== PART-TIME TEACHERS (HOURS > 20) ===");
            int countPartTimeMoreThan20 = teachers.OfType<ParttimeTeacher>().Count(t => t.NumberOfHours > 20);
            Console.WriteLine($"Result: There are {countPartTimeMoreThan20} part-time teacher(s) with more than 20 hours.");

            Console.WriteLine("\n=== TOTAL HOURS OF PART-TIME TEACHERS ===");
            int totalHours = teachers.OfType<ParttimeTeacher>().Sum(t => t.NumberOfHours);
            Console.WriteLine($"Result: The total number of hours is {totalHours}.");
        }
    }
}
