using System;

namespace PracticalExam2
{
    public class Person
    {
        private string _IDCard;
        private string _name;
        private int _age;

        public string IDCard
        {
            get { return _IDCard; }
        }

        public string Name
        {
            get { return _name; }
        }

        public int Age
        {
            get { return _age; }
        }

        public Person(string idCard, string name, int age)
        {
            _IDCard = idCard;
            _name = name;
            _age = age;
        }
    }

    public class PersonVietNam
    {
        private Person[] _persons;

        public PersonVietNam(int length)
        {
            _persons = new Person[length];
        }

        public Person this[int index]
        {
            get 
            { 
                if (index >= 0 && index < _persons.Length)
                    return _persons[index]; 
                return null;
            }
            set 
            { 
                if (index >= 0 && index < _persons.Length)
                    _persons[index] = value; 
            }
        }

        public void DisplayDetails()
        {
            Console.WriteLine("\n--- Persons Details ---");
            for (int i = 0; i < _persons.Length; i++)
            {
                if (_persons[i] != null)
                {
                    Console.WriteLine($"Person[{i}] -> ID Card: {_persons[i].IDCard}, Name: {_persons[i].Name}, Age: {_persons[i].Age}");
                }
            }
        }
    }

    public class PersonTest
    {
        public static void Run()
        {
            Person p1 = new Person("0123456789", "Nguyen Van A", 25);
            Person p2 = new Person("9876543210", "Tran Thi B", 30);

            PersonVietNam pvn = new PersonVietNam(2);
            pvn[0] = p1;
            pvn[1] = p2;

            pvn.DisplayDetails();
        }
    }
}
