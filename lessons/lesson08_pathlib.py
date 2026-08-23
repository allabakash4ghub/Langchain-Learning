''' The Python pathlib library is a built-in module that provides an object-oriented 
approach to handling file system paths. Introduced in Python 3.4, it treats paths as
actual objects rather than plain text strings. This makes code cleaner, more readable,
 and automatically cross-platform compatible across Windows, macOS, and Linux'''

'''Key Features
Intuitive Path Joining: Uses the / operator to join paths instead of using os.path.join().
Built-in I/O Methods: Reads or writes file contents directly using .read_text() or .write_text().
Easy Attributes: Extracts file components instantly using .name, .stem, or .suffix.
Directory Management: Simplifies directory searches via .glob() or .rglob().'''

#The Old Way — os.path

import os

file_path =os.path.join("folder", "subfolder", "file.txt")
print(file_path)  # folder/subfolder/file.txt
file_path1=os.path.join("data", "input", "data.csv")
print(file_path1)  # data/input/data.csv

#Modern Way — pathlib

from pathlib import Path

file_path2 = Path("folder") / "subfolder" / "file.txt"
print(file_path2)  # folder/subfolder/file.txt
file_path3 = Path("data") / "input" / "data.csv"
print(file_path3)  # data/input/data.csv
print(type(file_path2))  # <class 'pathlib.PosixPath'> on Linux/macOS or <class 'pathlib.WindowsPath'> on Windows
'''The / operator is overloaded by Path to combine path components.
It does not mean mathematical division here.'''
# Current Working Directory

cwd=Path.cwd()
print(cwd)  # Prints the current working directory

# Absolute vs Relative Paths
relative_path = Path("folder/subfolder/file.txt")
absolute_path = relative_path.resolve()
print(absolute_path)  # Prints the absolute path to the file
'''Generally, relative paths are preferable inside a project. 
Because another developer might clone your project to a different location on their system.
so instead of Instead of: Path("E:/GenAI/Langchain-Learning/data/report.pdf")  use 
Path("data") / "report.pdf"'''

# Creating Directories
#path_to_create = Path("new_folder/subfolder")
path_to_create = Path("pathlib_demo")
path_to_create.mkdir(parents=True, exist_ok=True)  # Creates the directory and any necessary parent directories
print(f"Directory created at: {path_to_create.resolve()}")
'''The parents=True argument allows the creation of parent directories if they don't exist.
The exist_ok=True argument prevents an error if the directory already exists.'''
## Listing Files
directory_path = Path("pathlib_demo")  # if you provide current working directory, it will throw error, so provide the directory name
for file in directory_path.iterdir():
    print(file)  # Prints each file and directory in the 'pathlib_demo' directory

#test_path = Path("lessons") this one throws error since the lessons directory is not present in the current working directory, so we need to create it first
test_path = Path(".")  # This indicates the current directory or you can also use Path.cwd() to get the current working directory

for file in test_path.iterdir():
    print(file)  # Prints all Python files in the 'lessons' directory

print(Path.cwd())
print(Path(__file__).parent)    

py_files = Path(".").rglob("*.py")  # This will find all Python files in the current directory
for file in py_files:
    print(file)  # Prints all Python files in the current directory and its subdirectories

# create a file in pathlib_demo folder and read the content 
fpath=Path("demo.txt")    
fpath.touch()
fpath.write_text("Hello World ! , it is test file")

fpath.write_text("Hello from Python! , test file",encoding="utf-8")  #For production applications, I recommend explicitly specifying UTF-8:

# read 
content=fpath.read_text(encoding='utf-8')
print(content)

# Building Paths Dynamically

test_filename = "claims.pdf"
path=Path("data")/test_filename

print(path)