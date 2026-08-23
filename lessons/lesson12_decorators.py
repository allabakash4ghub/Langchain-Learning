'''A decorator in Python is a design pattern that allows you to modify or extend 
the behavior of a function or method without permanently changing its source code.'''

def decorator(func):
    def wraper():
        print("Before main function")
        func()
        print("After main function")

    return wraper   

def greet():
    print("Greet function")        

test=decorator(greet)   
test() 

## Using @ operator 

def decorator2(func):
    """ decorator 2 """
    def wraper():
        """ wraper function """
        print("Before main function")
        func()
       # print(f"function name:{__name__}")
       # print(f"function name:{__doc__}")
        print("After main function")
    return wraper    


@decorator2
def greet2():
    """ greet2 function """
    print("Hello Test Decorator function")      

greet2()

### Decorator with Arguments

def decorwithargs(func):
    def wraper(*args,**kwargs):
        """wraper doc string"""
        print("Main function start")
        result=func(*args,**kwargs)
        print("Main function ends")
        return result
    return wraper

@decorwithargs
def calculate(a,b):
    """" Calculate wrap string """
    return a*b

print(calculate(5,6))
print(calculate.__doc__)
print(calculate.__name__)

### functools.wraps ⭐⭐⭐⭐⭐
#with wrap functools 
''' functools.wraps is used to preserve the metadata of the original function when
 it is wrapped by a decorator. Without it, attributes such as __name__ and __doc__ are 
 replaced by those of the wrapper function. It also preserves the reference to the original 
 function through __wrapped__.'''
from functools import wraps
def decorator_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Doc string in wrapper function """
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@decorator_with_wraps
def add_numbers(a,b):
    """Doc string in add_numbers function """
    return a+b

print(f"sum of numbers:{add_numbers(5,6)}")
print(add_numbers.__doc__)
print(add_numbers.__name__)

##Real Example — Timing ⭐⭐⭐⭐⭐

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        result=func(*args,**kwargs)
        end=time.perf_counter()

        print(
            f"{func.__name__} took "
            f"{end-start:.2f} seconds"
        )
        return result
    return wrapper

@timer
def process_data():
    time.sleep(2)
    return "Done"

print(process_data())

''' Generalized Example'''

import time
def time_dec(base_fun):
    def enhanced_fun(*args,**kwargs):
        start_time=time.perf_counter()
        result=base_fun(*args,**kwargs)
        stop_time=time.perf_counter()
        print(f"Time taken to prepare : {stop_time-start_time:.2f} seconds")
        return result
    return enhanced_fun

# def brew_tea(tea_type,steep_time):
#     print("Making brew tea")
#     time.sleep(2)
#     print("brew tea ready")

# brew_tea_dec=time_dec(brew_tea)
# brew_tea_dec(tea_type="Brew",steep_time=2)

## Instead of above code , we can use below code
@time_dec
def brew_tea(tea_type,steep_time):
    print("Making brew tea")
    time.sleep(2)
    print("brew tea ready")

brew_tea(tea_type="Brew",steep_time=2)