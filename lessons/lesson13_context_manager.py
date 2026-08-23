''' Context managers are Python objects that automate resource management 
by ensuring setup and cleanup actions run precisely when needed. They are typically invoked 
using the with statement, which replaces complex try...finally block patterns'''
from pathlib import Path

file_path=Path("context.txt")


with open("context.txt","w",encoding='utf-8') as file:
    file.write("Hello it is a test file on context manager")
# The file is automatically closed right here, even if an error occurs.

# Test with Path lib library
with file_path.open("a",encoding='utf-8') as file:
    file.write("\nThis is writing using path lib library method of accessing file")

# file get closed even there is an exception
''' Context managers guarantee resource cleanup; 
exception handling determines what happens to the exception.
when exception raised the execution stopped , so if you want to continue we have to handle it with try except'''

try:
    with open("context.txt","r",encoding='utf-8') as file:
        data=file.read()
        print("Inside with",file.closed)
        print(data)
        raise ValueError("Something went wrong but file get closed") # Execution stops here 
except ValueError as e:
    print("caught",e)    

print("Outside with",file.closed)

###$$$$$ Context Manager Internals $$$$$$$$$$$$###########
print("*"*15,"Context Manager Internals","*"*15)
''' A context manager is based on two special methods: 
__enter__()
__exit__()
Conceptually:
with resource as value:
    ...
is roughly equivalent to:
value = resource.__enter__()

try:
    ...
finally:
    resource.__exit__(...)

You don't normally need to call these methods yourself.        
'''
## Create Your Own Context Manager

class Mycontext:

    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the Context")       

with Mycontext():
    print("Inside Context")

#Suppose an exception occurs: execution The __exit__() method gets called during cleanup.
with Mycontext():
    print("Inside")
    #raise ValueError("somehting went wrong")  # this line can be commented when testing

''' The __exit__ method receives:
def __exit__(
    self,
    exc_type,
    exc_value,
    traceback
):
If there is no exception:
exc_type = None
exc_value = None
traceback = None
If an exception occurs, these contain information about it.
'''
# contextlib — Easier Way ⭐
# Python provides: contextlib 
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Starting")
    yield 
    print("Cleaning up")

with my_context():
    print("Doing work")    

## Exception Handling with @contextmanager
from contextlib import contextmanager

@contextmanager
def temporary_model(model):

    print(f"Using model: {model}")

    try:
        yield
    finally:
        print("Restoring previous model")

with temporary_model("gpt-4.1"):
    print("Calling LLM")          