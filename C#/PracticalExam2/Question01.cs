using System;

namespace PracticalExam2
{
    public interface IEmployee
    {
        double CalculateBonus(string designation, int tenure, double salary);
        void DisplayDetails();
    }

    public class Employee : IEmployee
    {
        private string _employeeName;
        private int _yearsOfService;
        
        protected double _bonus;

        public string designation;
        public double salary;

        public string EmployeeName
        {
            get { return _employeeName; }
            set 
            { 
                if (!string.IsNullOrEmpty(value) && value.Length >= 6 && value.Length <= 40)
                    _employeeName = value;
                else
                    Console.WriteLine("Warning: EmployeeName length must be from 6 to 40 characters. Value not set.");
            }
        }

        public int YearsOfService
        {
            get { return _yearsOfService; }
            set 
            { 
                if (value >= 0 && value <= 60)
                    _yearsOfService = value;
                else
                    Console.WriteLine("Warning: YearsOfService must be between 0 and 60. Value not set.");
            }
        }

        public virtual double CalculateBonus(string designation, int tenure, double salary)
        {
            if (designation == "Manager")
            {
                if (tenure <= 5)
                    _bonus = salary * 1.5;
                else
                    _bonus = salary * 2;
            }
            else if (designation == "Engineer")
            {
                if (tenure <= 5)
                    _bonus = salary;
                else
                    _bonus = salary * 2;
            }
            else if (designation == "Technician")
            {
                if (tenure <= 3)
                    _bonus = salary * 0.25;
                else if (tenure > 3 && tenure <= 5)
                    _bonus = salary * 0.5;
                else
                    _bonus = salary * 2;
            }
            else
            {
                _bonus = 0;
            }

            return _bonus;
        }

        public virtual void DisplayDetails()
        {
            Console.WriteLine($"Name: {EmployeeName}");
            Console.WriteLine($"Designation: {designation}");
            Console.WriteLine($"Years of Service: {YearsOfService}");
            Console.WriteLine($"Salary: {salary}");
            Console.WriteLine($"Calculate Bonus: {_bonus}");
            Console.WriteLine($"Total Income: {salary + _bonus}");
        }
    }

    public class NewEmployee : Employee
    {
        public override double CalculateBonus(string designation, int tenure, double salary)
        {
            if (designation == "Teacher")
            {
                if (tenure <= 3)
                    _bonus = salary * 3;
                else
                    _bonus = salary * 4;
                    
                return _bonus;
            }
            else
            {
                return base.CalculateBonus(designation, tenure, salary);
            }
        }

        public override void DisplayDetails()
        {
            Console.WriteLine("\n--- New Employee Details ---");
            base.DisplayDetails();
        }
    }

    public class EmployeeTest
    {
        public static void Run()
        {
            NewEmployee emp = new NewEmployee();

            Console.Write("Enter Employee Name: ");
            emp.EmployeeName = Console.ReadLine();

            Console.Write("Enter Years of Service: ");
            if (int.TryParse(Console.ReadLine(), out int tenure))
            {
                emp.YearsOfService = tenure;
            }

            Console.WriteLine("\nMenu to select the designation:");
            Console.WriteLine("1 - Manager");
            Console.WriteLine("2 - Engineer");
            Console.WriteLine("3 - Technician");
            Console.WriteLine("4 - Teacher");
            Console.Write("Select an option (1-4): ");
            
            string choice = Console.ReadLine();

            if (choice == "1")
            {
                emp.designation = "Manager";
                emp.salary = 5000;
            }
            else if (choice == "2")
            {
                emp.designation = "Engineer";
                emp.salary = 4000;
            }
            else if (choice == "3")
            {
                emp.designation = "Technician";
                emp.salary = 3000;
            }
            else if (choice == "4")
            {
                emp.designation = "Teacher";
                emp.salary = 2000;
            }
            else
            {
                Console.WriteLine("Invalid option selected");
                return;
            }

            emp.CalculateBonus(emp.designation, emp.YearsOfService, emp.salary);
            emp.DisplayDetails();
        }
    }
}
