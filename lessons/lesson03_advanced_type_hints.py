# Advanced Type Hints in Python
from typing import Union, Optional, Any, List, Dict, Tuple, Callable, TypeVar, Generic,TypeAlias,Sequence,TypedDict

## test any  type 

def process_data(data:Any) -> None:
    if isinstance(data, str):
        print(f"Processing string data: {data}")
    elif isinstance(data, int):
        print(f"Processing integer data: {data}")
    elif isinstance(data, list):
        print(f"Processing list data: {data}")
    else:
        print("Unsupported data type")
        print(f"Received data of type: {type(data)} and value: {data}")

process_data("Hello, World!")   
process_data(42)
process_data([1, 2, 3, 4, 5])  
process_data({'key': 'value'})  # Unsupported data type         

## Optional

def greet_user(name: Optional[str]=None,email: Optional[str]=None) -> str|None:
    if name and email:
        return f"Hello, {name}! Your email is {email}."
    elif name:
        return f"Hello, {name}!"
    elif email:
        return f"Hello! Your email is {email}."
    else:
        return "Hello, Guest!"

print(greet_user("Alice", "alice@example.com"))  # Hello, Alice! Your email is alice@example.com.
print(greet_user("Bob"))  # Hello, Bob!
print(greet_user(email="charlie@example.com"))  # Hello! Your email is charlie@example.com.
print(greet_user())  # Hello, Guest!

def test_optional(name: str|None, age: int|None) -> None:
    if name is not None and age is not None:
        print(f"Name: {name}, Age: {age}")
    elif name is not None:
        print(f"Name: {name}, Age: Not provided")
    elif age is not None:
        print(f"Name: Not provided, Age: {age}")
    else:
        print("Name and Age are not provided")

test_optional("Alice", 30)  # Name: Alice, Age: 30
test_optional("Bob", None)  # Name: Bob, Age: Not provided
test_optional(None, 25)  # Name: Not provided, Age: 25
test_optional(None, None)  # Name and Age are not provided
#test_optional("Charlie")  # Name: Charlie, Age: Not provided TypeError: test_optional() missing 1 required positional argument: 'age'

## Union Example Sometimes a value can be one of several types.
def display(value: Union[int, str]) -> None:
    print(value)

display(100)
display("ABC")
display(3.14)  # TypeError: display() argument must be int or str, not float
display([1, 2, 3])  # TypeError: display() argument must be int or str, not list

def display_pipe(value: int|str) -> None:
    print(value)

display_pipe(100)
display_pipe("ABC") 
display_pipe(3.14)  # TypeError won't come: display_pipe() argument must be int or str, not float  
display_pipe([1, 2, 3])  # TypeError won't come: display_pipe() argument must be int or str, not list  

print(display_pipe.__annotations__)

## Literal example
from typing import Literal

def set_status(status: Literal["active", "inactive", "pending"]) -> None:
    print(f"Status set to: {status}")

set_status("active")    # Valid
set_status("inactive")  # Valid
set_status("pending")   # Valid
set_status("unknown")   # No TypeError: but argument must be one of the specified literals shows

## TypeAlias example Suppose you repeatedly write
#score: Union[int, float] in your code. You can create a type alias to simplify this.
Score: TypeAlias = Union[int, float]
def calculate_average(scores: List[Score]) -> Score:
    if not scores:
        raise ValueError("Scores list cannot be empty")
    return sum(scores) / len(scores)
print(calculate_average([90, 85.5, 78]))  # Valid
#print(calculate_average([90, 85.5, "78"]))  # No TypeError: but argument must be int or float shows

## Callable example
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(apply_function(lambda x, y: x + y, 5, 3))  # Returns 8

def greet(name: str) -> str:
    return f"Hello, {name}!"

def testcallable(func: Callable[[str], str], name: str) -> None:
    print(func(name))        

print(testcallable(greet, "Alice") ) # Hello, Alice!

## TypedDict 

class User(TypedDict):
    name: str
    age: int
    email: str

UserProfile: TypeAlias = User
print(UserProfile.__annotations__)  # {'name': <class 'str'>, 'age': <class 'int'>, 'email': <class 'str'>}    

test_user: User= {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}

test_user_profile: UserProfile = {
    "name": "Bob",
    "age": 25,
    "email": "bob@example.com"
}

test_user2: User= { "name": "Allabakash", "age":40, "email": "allabakash@example.com"}
print(test_user2)  # {'name': 'Allabakash', 'age': 40, 'email': 'allabakash@example.com'}
