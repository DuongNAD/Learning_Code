class Person:
    name = 'Duong'
    age = 23

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Hello, My name is {self.name} and i am {self.age} years old")

if __name__ == '__main__':
    person = Person('Duong', '23')
    person.introduction()