''' A generator produces values one at a time instead of creating all values in memory at once.'''
def generator():
    yield 1
    yield 2
    yield 3
    yield 4

gen =generator()    
print(gen) ## It prints the generator object address

for num in gen:
    print(num)

'''yield vs return
def normal():
    return 1
    return 2

Only 1 returned

def generator():
    yield 1
    yield 2

Produces: 1 2  one at a time    

 '''

print(f"## Generator Execution")

def numbers():
    print("Start")
    yield 1

    print("Continue")
    yield 2

    print("Finished")

gen_exe=numbers()    
print(next(gen_exe))
print(next(gen_exe)) 
#print(next(gen_exe)) # print Finished and raises StopIteration

''' You normally don't manually call next().  we use for loop
The for loop automatically calls next() until the generator is exhausted.'''

print("\n")
# Generator Expression, Generator expression → produces values lazily.
print ("*"*15,"Generator Comprehension","*"*15)
gen_numbers=(x for x in range(10))
for gen in gen_numbers:
    print(gen,end=" ")

###### List comprehension → creates the whole list.
list_numbers=[x for x in range(10)  ]  

print("\n")
print(f"#Exercise 4 ⭐⭐⭐ — GenAI-style")
print()
def generate_chunks():
    chunks=[
        "Langchain","helps","build","LLM",
        "Application"
    ]
    for chunk in chunks:
        yield chunk

for chunk in generate_chunks():
    print(chunk,end=" ")      

print("\n")
print(f"⭐ 8. Real AI Example — Reading a Large File ⭐")
print("#"*50)

''' Suppose you have a huge file: generator.txt instead of content = file.read() 
which loads everything into memory, you can process it line by line:'''

def read_lines(file_path:str):
    with open(file_path,encoding='utf-8') as file:
        for line in file:
            yield line

for line in read_lines("generator.txt"):
    print(line)            

print()
print(f"⭐ 11. Generator with Parameters ⭐")    

def count(start:int,end:int):
    for number in range(start,end+1):
        yield number

for number in count(1,5):
    print(number)        

print()
print(f"⭐ 12. Generator Type Hint with collection Module⭐")   
''' we The function produces integers one at a time.'''

from collections.abc import Iterator

def count2(start:int,end:int)->Iterator[int]:
    for num in range(start,end+1):
        yield num

for num in count2(1,3):
    print(num)        

print()
print(f"⭐ 13. Generator Type Hint  with typing module⭐")     
from typing import Generator

def count3(start:int,end:int)->Generator[int,None,None]:
    for num in range(start,end+1):
        yield num

for num in count3(1,3):
    print(num)        