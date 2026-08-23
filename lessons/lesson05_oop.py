from turtle import position


class Student:
    school_name = "ABC School"  # Class variable shared by all instances

    def __init__(self, name:str):
        self.name = name # Instance variable unique to each instance

student1 = Student("Alice")
student2 = Student("Bob")

print("Lesson 5: Object-Oriented Programming (OOP)")
print(f"Student 1: {student1.name}, School: {student1.school_name}")
print(f"Student 2: {student2.name}, School: {student2.school_name}")

print(f"Instance Method and Class Method Example:")

class Car:
    car_manufacturer = "Sedan"  # Class variable
    def __init__(self, make:str, model:str):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Car Make: {self.make}, Model: {self.model}"
    @classmethod
    def car_type(cls):
        #return "This is a car class."
        print(f"This is a {cls.car_manufacturer} class.")

car1 = Car("Toyota", "Camry")
print(car1.display_info())       
print(Car.car_type())
#print(Car.display_info())  # Calling instance method using class name and instance
#TypeError: Car.display_info() missing 1 required positional argument: 'self'

# Static Methods
print(f"Static Method Example:")

class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        return a + b

result = MathUtils.add_numbers(5, 3)
print(f"Result of addition: {result}")

# inheritance , Method Overriding
print(f"Inheritance Example:")

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"
    def eat(self):
        return "Dog eats"

dog = Dog()
print(dog.speak())  # Output: Dog barks
print(dog.eat())    # Output: Dog eats

# Polymorphism
print(f"Polymorphism Example:") 

class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

# This function accepts any object with a quack method
def make_it_quack(obj):
    obj.quack()

make_it_quack(Duck())    # Output: Quack, quack!
make_it_quack(Person())  # Output: I'm pretending to be a duck!

# Encapsulation
print(f"Encapsulation Example:")  

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)  # Deposited: 500, New Balance: 1500   

## super() function
print(f"super() Function Example:")

class Parent:
    def greet(self):
        return "Hello from Parent"  

class Child(Parent):
    def greet(self):
        parent_greeting = super().greet()  # Call the parent class method
        return f"{parent_greeting} and Hello from Child"    

child = Child()
print(child.greet())  # Output: Hello from Parent and Hello from Child

## Super() with init    
print(f"super() with __init__ Example:")

class Base:
    def __init__(self, name):
        self.name = name    

class Derived(Base):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent class __init__
        self.age = age  

derived_instance = Derived("Alice", 25)
print(f"Name: {derived_instance.name}, Age: {derived_instance.age}")  #

## simple inheritance hierarchy.

class Employee:
    def __init__(self, name:str):
        self.name = name

    def work(self):
        return f"{self.name} is working."    

class AIEngineer(Employee):
    def __init__(self, name:str, specialization:str):
        super().__init__(name)
        self.specialization = specialization

    def buildingBot(self):
        print(f"{self.name} is developing AI algorithms.")

engineer = AIEngineer("John", "Machine Learning")              
print(engineer.work())  # Output: John is working.
engineer.buildingBot()  # Output: John is developing AI algorithms. 

