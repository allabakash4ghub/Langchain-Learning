## Data Classes example , we don't need to write __init__ method, it will be generated automatically by dataclass decorator. We can also add validation in __post_init__ method.

from dataclasses import dataclass,field

'''A Python dataclass is a built-in feature introduced in Python 3.7 
that simplifies creating classes primarily used to store data. 
By applying the @dataclass decorator from the dataclasses module to a class definition, 
Python automatically generates boilerplate code such as initialization (__init__), 
readable string representations (__repr__), and structural comparisons (__eq__)

Core Benefits : 
Automatic __init__: You do not have to write self.name = name manually.
Clean __repr__: Printing the object yields a readable format 
like Product(name='Laptop', price=999.0).
Easy Comparison: You can immediately check object equality (prod1 == prod2) based on 
their actual data rather than their memory addresses.
Type Hint Integration: It relies heavily on Python's type annotations to understand and structure the data fields

Powerful ConfigurationsThe decorator accepts optional arguments to easily modify class behavior:

frozen=True: Makes instances read-only and immutable, functioning similarly to a named tuple.
order=True: Automatically creates comparison methods (<, >, <=, >=) so objects can be sorted based on their field values.
default_factory: Allows the safe assignment of mutable defaults (like list or dict factories) without sharing data across instances
'''

@dataclass
class Person:
    name: str
    age: int
    city: str

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if not self.name:
            raise ValueError("Name cannot be empty")
        if not self.city:
            raise ValueError("City cannot be empty")

person1 = Person(name="Alice", age=30, city="New York")
print(person1)  # Person(name='Alice', age=30, city='New York   
#person2 = Person(name="Bob", age=-5, city="Los Angeles")  # ValueError: Age cannot be negative     
person3 = Person("Charlie", 25, "Chicago")
print(person3)  # Person(name='Charlie', age=25, city='Chicago')
person4 = Person(name="Alice", age=30, city="New York")
print(person1==person4)  # True, because dataclass generates __eq__ method based on fields ,
#for normal classes, we need to implement __eq__ method to compare objects based on fields and it retunrs False

class NormalPerson:
    def __init__(self, name: str):
        self.name = name


p1=NormalPerson("Alice")
p2=NormalPerson("Alice")

print(p1==p2)  # False, because NormalPerson class doesn't implement __eq__ method, so it compares object references

# with normal classes, we can implement __eq__ method to compare objects based on fields and it retunrs True
class NormalPersonWithEq:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, NormalPersonWithEq):
            return self.name == other.name
        return False

p3=NormalPersonWithEq("Alice")
p4=NormalPersonWithEq("Alice")

print(p3==p4)  # True, because NormalPersonWithEq class implements __eq__ method    

## Default Values in dataclasses, we can provide default values for fields in dataclasses, and we can also use default_factory to provide default values for mutable types like lists or dictionaries.

@dataclass
class PersonWithDefaults:
    name: str
    age: int = 0
    city: str = "Unknown"
    hobbies: list = None

    def __post_init__(self):  #Run this immediately after the auto-generated __init__().
        if self.hobbies is None:
            self.hobbies = []

person5 = PersonWithDefaults(name="David")
print(person5)  # PersonWithDefaults(name='David', age=0, city='Unknown', hobbies=[])

## defualt_factory example, we can use default_factory to provide default values for mutable types like lists or dictionaries.

@dataclass
class PersonWithDefaultFactory:
    name: str
    age: int = 0
    city: str = "Unknown"
    hobbies: list = field(default_factory=list)
    subscriptions: dict = field(default_factory=dict)

person6 = PersonWithDefaultFactory(name="Eve")
print(person6)  # PersonWithDefaultFactory(name='Eve', age=0, city='Unknown', hobbies=[], subscriptions={})

## Step 7 – Frozen Dataclass

@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int
    city: str

person7 = ImmutablePerson(name="Frank", age=40, city="San Francisco")
print(person7)  # ImmutablePerson(name='Frank', age=40, city='San Francisco')
# person7.age = 41  # This will raise FrozenInstanceError, because ImmutablePerson is a frozen dataclass, which means its instances are immutable and cannot be modified after creation.

