''' In Python, *args and **kwargs allow a function to accept a variable number of arguments,
meaning you can pass as many inputs into the function as you want

1. *args (Positional Arguments)The *args syntax lets your function accept any number of 
positional arguments (inputs passed without names).
Python packs all these extra arguments into a tuple.
The single asterisk (*) is the actual operator; args is just a standard naming convention

2. **kwargs (Keyword Arguments)The **kwargs syntax lets your function accept any number of 
keyword arguments (inputs passed as name=value pairs).
Python packs these named arguments into a dictionary, where keys are argument names and 
values are the passed data.The double asterisk (**) is what triggers this feature; 
kwargs is just a conventional name.

3. Combining Both
You can use standard arguments, *args, and **kwargs together in a single function signature. 
However, Python enforces a strict order that you must follow to avoid a SyntaxError:
1.Standard positional arguments
2.*args
3.**kwargs

'''
print(f"⭐ *args (Positional Arguments) and \nPassed values captured in tuple ⭐")
def add_numbers(*args):
    print(args)
    print(type(args))
    total=sum(args)
    print(total)

add_numbers(5,6,4)    

# we can perform sum operation on iterables, same happens in the above 
print(sum([1,2,3,4]))
print(sum((1,2,3,4)))

print()
print(f"⭐ **kwargs — Multiple Keyword Arguments and \npassed keyword arguments captured in dictionary  ⭐")

def show_details(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print("\n# You can loop through them:")
    for key,value in kwargs.items():
        print(f"{key}:{value}")

show_details(
    name="Allabakash D",
    location= "Bangalore",
    job="software"
)    

print("\n3. Using Both Together")

def demo(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)

demo(10,20,test="arguments",purpose="learn")    

print("5. Argument Order")

def create_user(name,*skills,active=True,**kwargs):
    print(name)
    print(skills)
    print(active)
    print(kwargs)

create_user("Allabakash D","Data Science","Python",active=True,experience=6)    

print("6. Very Important: Unpacking with *")
numbers=[10,20,30,40]
print(*numbers)

# You can pass a list to a function:
def add(a,b,c,d):
    return a+b+c+d
print(add(*numbers))

print("7. Dictionary Unpacking with **")
def create_user(name,age):
    print(name,age)

user={
    "name" :"Rocky",
    "age":40
}    
create_user(**user)
## this is nothing but a create_user(name="Rocky", age=40)