'''' Iterable = something you can iterate over or Something you can loop over:
e.g number =[1,2,3],text="Hello"
Iterator = something that gives or produce the next value. 
An iterator is an object that gives you items one at a time.
How it works
__iter__() → returns the iterator
__next__() → returns the next item
StopIteration → signals that iteration is finished

Generator = an easy way to create an iterator using yield'''

print(f"⭐ Iterator example ⭐")
numbers=[10,20,30,40] # This is iterable
iterator = iter(numbers)  # This is iterator object

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator)) # This raises StopItereation exception

print()
print(f"⭐ 4. What does a for loop do internally? ⭐")

''' When you write:
numbers = [10, 20, 30]

for number in numbers:
    print(number)

Conceptually, Python does something like below example:    
This is also why generators work naturally inside for loops.
'''
numbers2=[1,2,3,4]
iterator = iter(numbers2)

while True:
    try:
        number=next(iterator)
        print(number)
    except StopIteration:
        break    

print()
print(f"⭐ 7. Custom Iterator ⭐")

''' An object does not automatically become an iterator just because it is a class object.

It becomes usable as an iterator because the class implements special methods:

__iter__()
__next__()

The key concept

Think of NumberIterator as a normal Python class that follows a special contract.

Python says:

If an object provides the appropriate special methods, I know how to use it for iteration.
So, numbers = NumberIterator() is indeed a class object, but because it implements:
__iter__()
__next__()

Python can treat that object as an iterator.

This is similar to your earlier OOP learning:

Class
  ↓
Object
  ↓
Special methods implemented
  ↓
Python gives the object special behavior

__init__()   → object initialization
__str__()    → str(object)
__len__()    → len(object)
__iter__()   → iter(object)
__next__()   → next(object)

So the class object itself hasn't "magically changed"; 
by implementing Python's iterator protocol, it gains iterator behavior.

'''

class NumberIterator:
    def __init__(self):
        self.current=1

    def __iter__(self):
        return self   

    def __next__(self):
        if self.current > 3 :
            raise StopIteration

        value=self.current
        self.current +=1
        return value

numbers = NumberIterator()
for num in numbers:
    print(num)           