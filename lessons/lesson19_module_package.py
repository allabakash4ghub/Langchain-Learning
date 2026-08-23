''' Modules and packages are Python's primary tools for organizing code, 
maximizing reusability, and managing large-scale software projects.A module is simply 
a single Python file containing executable code, while a package is a directory or folder 
containing multiple modules grouped together.'''

''' Built-in vs External ResourcesStandard Library: 
Python ships with pre-installed built-in modules like math, datetime, and sys.
Third-Party Packages: Millions of open-source packages (like numpy or requests) are built 
by developers worldwide. You can download and install them using the pip install package_name
 command in your terminal.'''

print("1. Working with Modules")
'''' Any Python file you create is automatically a module. 
For example, if you save a file as calculator.py, your module name is calculator.
So, A module is simply a Python file (.py file).'''

''' 2. Different Ways to Import '''
print(f"Method 1: Import the entire module")
''' Standard Import: Requires prefixing functions with the module name'''
import calculator
print(calculator.add(5,10))

print(f"Method 2: Import a specific function")

''' Specific Import: Imports specific functions directly into the script'''
from calculator import add 

print(add(40,50))

print(f"Method 3: Import multiple items")
from calculator import add,subtraction
print(f"Addition Result:",add(45.5,20.6))
print(f"Subtraction Result:",subtraction(45.5,20.6))

print(f"Method 4: Alias")
''' You can give an imported module a shorter name:'''

import calculator as calc

print(f"Addition using Alias: {calc.add(15,80)}")


print()
print("2. Working with Packages")
''' 3. What is a Package?
A package is a folder containing related Python modules.
For example: 

my_project/
│
├── main.py
│
├── agents/
│   ├── __init__.py
│   ├── sql_agent.py
│   └── rag_agent.py
│
└── utils/
    ├── __init__.py
    ├── logger.py
    └── config.py

Here,  agents and  utils are packages

'''

from mypackage.greetings import say_hello

say_hello("Hero")

''' 6. How Does Python Find the Module? 
When you write:

from my_package.calculator import add
Python looks for:
Current project
       ↓
my_package
       ↓
calculator.py
       ↓
add()

Conceptually :

my_package.calculator
      │         │
      │         └── calculator.py
      │
      └── folder/package

The dot (.) represents the path through the package structure.      

Very Important: import Executes a File 

Because when Python imports a module for the first time, 
it executes the top-level code in that module.

The if __name__ == "__main__" Pattern ⭐⭐⭐⭐⭐

so , when we import the module , it get executed fully even if there are any 
function calles inside it, so to avoid it we define the function main() and 
check for __name__ as "__main__"in the modules, such that it won't execute unnecessarily invocations.

'''
print(f" __name__  value name : {__name__}")

from mypackage.greetings import say_hello

def main():
    print("Testing the __name__ condition")
    say_hello("main test")


if __name__ == "__main__":
    main()

''' 10. Why This Is Important?

This is a common project pattern:

# main.py
from agents.sql_agent import run_sql_agent
from agents.rag_agent import run_rag_agent

def main():
    print("Starting chatbot")

if __name__ == "__main__":
    main()

This allows:

Importing modules without unwanted execution
Keeping reusable functions/classes separate
Having a clean application entry point    

'''    

''' __pycache__ is created per folder, but .pyc files are mainly generated for
 Python modules that are imported. Files you execute directly as the main script
  typically won't appear there as .pyc files.
  
  Generally, a .pyc file is created when that Python file is imported or executed in 
  a way that causes Python to compile/cache it.'''