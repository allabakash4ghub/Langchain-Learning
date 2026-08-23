class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

print("Lesson 4: Classes")
print(Student)    

student1 = Student("Alice", 20)
print(student1.greet())
print(student1) #<__main__.Student object at 0x000001EAF8479C40>

#student2 =Student() #TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'age'

### Book Class Example:
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nPrice: ${self.price}")
        #return f"Title: {self.title}, Author: {self.author}, Price: ${self.price}"
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book1.display()

