#### type hints.py #### Type Hints in Python

def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

result = add_numbers(5, 3)
print(result)

print(add_numbers("Hello", "World"))  # type hint do not enforce type checking at runtime, but it can
#help with static analysis and code readability.

#Basic Built-in Types
x: int
y: str = "Hello, World!"
z: float = 3.14

# Boolean type hint
is_active : bool = True
flag: bool = False

#Collections
list_of_ints: list[int] = [1, 2, 3, 4, 5]
cities : list[str] = ["New York", "Los Angeles", "Chicago"]
list_of_floats: list[float] = [1.1, 2.2, 3.3]

# tuple type hint
coordinates: tuple[float, float] = (40.7128, -74.0060)

# dictionary type hint
person: dict[str, str] = {"name": "Alice", "city": "New York"}
student_scores: dict[str, int] = {"Alice": 90, "Bob": 85, "Charlie": 95}

