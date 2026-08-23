print("\n========== Functions ==========\n")
def greet(name):
    print(f"Hello, {name}! Welcome to the lesson on functions.")

greet("Allabakash")
greet("Alice")

# Exercise: 1
def square(number):
    return number * number

result = square(5)
print(result)

# Exercise: 2
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

name = full_name("John", "Doe")
print(name)

# Exercise: 3
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False

print("\n========== Default Arguments ==========\n")

def greet_with_default(name="Guest"):
    print(f"Hello, {name}! Welcome to the lesson on default arguments.")

greet_with_default("Alice")
greet_with_default()  # Uses the default value "Guest"

print("\n========== *args ==========\n")
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))  # 6
print(sum_numbers(4, 5, 6, 7))  # 22    

def return_values(*args):
    return args

print(return_values(1, 2, 3))  # (1, 2, 3)  tuple values
print(return_values("a", "b", "c"))  # ("a", "b", "c")  

print("\n========== **kwargs ==========\n")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")


def return_values_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))


return_values_kwargs(name="Allabakash", age=40, city="Bangalore")  # <class 'dict'>    
