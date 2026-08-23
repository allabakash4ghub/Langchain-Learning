# LangChain Learning

This repository contains my hands-on learning journey for **Python, Generative AI, LangChain, RAG, LangGraph, and Production AI**.

The project is organized into modules. Each lesson includes practical Python code and examples created while learning the concepts.

---

# Project Setup

## Technologies Used

- Python 3.12
- UV for Python package and environment management
- VS Code
- Git and GitHub

## Virtual Environment

The project uses a `.venv` virtual environment.

To activate the environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run Python files using:

```powershell
uv run .\main.py
```

Or from the `lessons` folder:

```powershell
uv run .\lesson01_functions.py
```

---

# 📚 Learning Roadmap

## Module 1 – Professional Python Environment

Completed the basic Python project and development environment setup.

Topics covered:

- Python installation
- UV package manager
- Creating a virtual environment
- Activating a virtual environment
- VS Code Python interpreter configuration
- `pyproject.toml`
- `uv.lock`
- `.python-version`
- `.gitignore`
- Git initialization
- Git branch configuration
- Project structure

---

# 🐍 Module 2 – Modern Python for AI Engineers

This module focuses on modern Python concepts that are important for AI and Generative AI application development.

## Lesson 1 – Python Functions

Topics covered:

- Function definition
- Function parameters
- Return values
- Default parameters
- Keyword arguments
- Function reuse

File:

```text
lessons/lesson01_functions.py
```

---

## Lesson 2 – Type Hints

Topics covered:

- Type hints for variables
- Function parameter type hints
- Return type hints
- Static type checking
- Pylance type checking in VS Code
- Understanding that Python type hints are not runtime type enforcement

Example:

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

File:

```text
lessons/lesson02_type_hints.py
```

---

## Lesson 2.2 – Advanced Type Hints

Topics covered:

- `Optional`
- `Union`
- Pipe (`|`) syntax
- `list`
- `dict`
- `tuple`
- `Any`
- Type checking behavior
- Static checking vs runtime behavior

Example:

```python
def display_value(value: int | str) -> None:
    print(value)
```

File:

```text
lessons/lesson03_advanced_type_hints.py
```

---

## Lesson 3 – Classes and Objects

Topics covered:

- Classes
- Objects
- `__init__`
- Instance attributes
- Instance methods
- `self`
- Object creation

File:

```text
lessons/lesson04_classes.py
```

---

## Lesson 4 – Advanced Classes and OOP

Topics covered:

- Inheritance
- Method overriding
- `super()`
- Encapsulation
- Properties
- `@property`
- `@staticmethod`
- `@classmethod`
- Instance methods vs class methods vs static methods

File:

```text
lessons/lesson05_oop.py
```

---

## Lesson 5 – Dataclasses

Topics covered:

- `@dataclass`
- Automatic `__init__`
- Default values
- Type hints with dataclasses
- Cleaner data model creation

Example:

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
```

File:

```text
lessons/lesson06_dataclasses.py
```

---

## Lesson 6 – Enums

Topics covered:

- `Enum`
- Named constant values
- Avoiding hard-coded values
- Using enums in applications

File:

```text
lessons/lesson07_enum.py
```

---

## Lesson 7 – pathlib

Topics covered:

- `Path`
- File paths
- Directory creation
- File creation
- Reading files
- Listing files and directories
- Relative vs absolute paths

File:

```text
lessons/lesson08_pathlib.py
```

---

## Lesson 8 – Exception Handling

Topics covered:

- `try`
- `except`
- `finally`
- `ValueError`
- `ZeroDivisionError`
- Handling multiple exceptions
- Understanding exception flow

Example:

```python
try:
    value = int(input("Enter number: "))
    result = 100 / value
    print(result)

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("Number cannot be zero")
```

File:

```text
lessons/lesson09_exceptions.py
```

---

## Lesson 9 – Logging

Topics covered:

- Python `logging` module
- Logging levels
- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`
- Logging instead of using only `print()`

---

## Lesson 11 – Async / Await

Topics covered:

- `async def`
- `await`
- Coroutines
- `asyncio.run()`
- Concurrent asynchronous execution
- Understanding asynchronous programming

This is particularly important for AI applications that perform multiple API or LLM calls.

---

## Lesson 12 – Decorators

Topics covered:

- Functions as objects
- Functions inside functions
- Returning functions
- Decorator functions
- `@decorator` syntax
- `functools.wraps`

Use cases:

- Logging
- Authentication
- Timing functions
- Retry logic
- API frameworks
- AI application monitoring

---

## Lesson 13 – Context Managers

Topics covered:

- `with` statement
- Automatic resource cleanup
- File handling
- `__enter__`
- `__exit__`
- Exception behavior with context managers

Example:

```python
with open("context.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)
```

---

## Lesson 14 – Generators

Topics covered:

- `yield`
- Generator functions
- Lazy evaluation
- Memory-efficient processing
- Generator iteration

This is useful when working with large datasets or processing data in chunks.

---

## Lesson 15 – Iterators

Topics covered:

- Iterable vs Iterator
- `iter()`
- `next()`
- `__iter__()`
- `__next__()`
- Custom iterator classes
- How `for` loops work internally

Example concept:

```python
numbers = NumberIterator()

for number in numbers:
    print(number)
```

---

## Lesson 16 – `*args` and `**kwargs`

Topics covered:

- Variable positional arguments using `*args`
- Variable keyword arguments using `**kwargs`
- Flexible function parameters
- Argument unpacking

---

## Lesson 17 – Comprehensions and Lambda Functions

Topics covered:

- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Lambda functions
- Using lambda with `sorted()`
- Custom sorting using the `key` parameter

Example:

```python
sorted_users = sorted(
    users,
    key=lambda user: user["age"]
)
```

---

## Lesson 19 – Python Modules, Packages, and Imports

Topics covered:

- Python modules
- Python packages
- Import statements
- Importing functions
- Creating custom modules
- Creating packages
- `__init__.py`
- `__pycache__`
- `.pyc` files
- Understanding how Python imports and caches compiled bytecode

Example structure:

```text
lessons/
│
├── calculator.py
│
└── mypackage/
    ├── __init__.py
    └── greetings.py
```

Example imports:

```python
import calculator
```

```python
from calculator import add
```

```python
from mypackage.greetings import say_hello
```

---

# 🤖 Module 3 – LangChain

## Next Module

The next phase of learning will focus on **LangChain**.

Planned topics include:

- Introduction to LangChain
- LangChain architecture
- Chat models
- Prompt templates
- Messages
- Chains
- Output parsers
- LCEL (LangChain Expression Language)
- Runnables
- Structured output
- Memory concepts
- Tools
- Agents
- Model integrations

The project is configured with the following LangChain packages:

- `langchain`
- `langchain-openai`
- `langchain-groq`
- `langchain-ollama`
- `python-dotenv`

This will allow learning with different LLM providers and models.

---

# 📄 Module 4 – RAG

Future topics:

- RAG architecture
- Document loaders
- Text splitting
- Embeddings
- Vector databases
- Retrieval
- Semantic search
- Retrieval chains
- RAG evaluation

---

# 🔀 Module 5 – LangGraph

Future topics:

- LangGraph fundamentals
- Nodes
- Edges
- State
- Conditional routing
- Multi-agent workflows
- Agent orchestration

---

# ☁️ Module 6 – Production AI

Future topics:

- FastAPI
- AI application architecture
- API development
- Docker
- Deployment
- Observability
- Logging
- Tracing
- Monitoring
- Production AI architecture

---

# Project Structure

Current project structure:

```text
Langchain-Learning/
│
├── .venv/
├── lessons/
│   ├── __pycache__/
│   ├── mypackage/
│   ├── pathlib_demo/
│   ├── calculator.py
│   ├── context.txt
│   ├── demo.txt
│   ├── generator.txt
│   ├── lesson01_functions.py
│   ├── lesson02_type_hints.py
│   ├── lesson03_advanced_type_hints.py
│   ├── lesson04_classes.py
│   ├── lesson05_oop.py
│   ├── lesson06_dataclasses.py
│   ├── lesson07_enum.py
│   ├── lesson08_pathlib.py
│   └── additional lesson files
│
├── .env
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# Environment Variables

Sensitive values such as API keys should be stored in the `.env` file.

Example:

```text
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

The `.env` file should not be pushed to GitHub.

---

# Running the Project

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the main application:

```powershell
uv run main.py
```

Run a specific lesson:

```powershell
cd lessons
uv run .\lesson01_functions.py
```

---

# Learning Goal

The goal of this repository is to build a strong foundation in:

1. Modern Python
2. LangChain
3. RAG
4. LangGraph
5. Production Generative AI

Each concept is learned through practical examples and hands-on coding.

---

# Current Progress

- [x] Module 1 – Professional Python Environment
- [x] Module 2 – Modern Python for AI Engineers
- [ ] Module 3 – LangChain
- [ ] Module 4 – RAG
- [ ] Module 5 – LangGraph
- [ ] Module 6 – Production AI

---

**Next Step: Module 3 – LangChain 🚀**
