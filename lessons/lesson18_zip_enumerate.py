''' zip() combines items from multiple iterables based on their positions.
The zip() function in Python combines elements from multiple iterables 
(like lists, tuples, or strings) into a single iterator of tuples.
 It pairs the first elements of each iterable together, then the second elements, and so on, 
 working exactly like a mechanical zipper.

The Python enumerate() function is a built-in tool that adds a counter to an 
iterable (like a list, tuple, or string) and returns it as an enumerate object. 
It eliminates the need to manually create and increment index tracking variables 
inside your loops

🛠️ Basic Syntax
enumerate(iterable, start=0)

iterable: Any object that supports iteration (e.g., lists, strings, dictionaries).
start (optional): The integer value where the counter begins. It defaults to 0


Any()
The Python any() function returns True if at least one element in an iterable is truthy, 
and False if all elements are falsy or if the iterable is empty.
It is a built-in tool commonly used to check conditions across arrays, lists, or
sets without writing verbose loops.

any() function is highly efficient because it uses short-circuit evaluation.
 This means it stops scanning the iterable the absolute moment it finds the first True value. 
 It will not check the remaining items, saving memory and processing time.

'''

print(f"⭐         ZIP Function            ⭐")

names=["John","Rob","David"]
scores =[78.5,89.4,66.5]

for key, value in zip(names,scores):
    #print(f"{key}:{value}")
    print(key,value)

result=zip(names,scores)
print(result)  

print("convert into list")
print(list(result))

print("Handling Unequal Lengths")

''' By default, zip() stops as soon as the shortest input iterable is exhausted. 
Any remaining elements in the longer iterables are ignored.

strict=True (Python 3.10+): Raises a ValueError if the iterables are not of equal length.

'''

letters=["A","B","C","D","E"]
index=[1,2,3]

print(list(zip(letters,index)))
#zip(letters, index, strict=True)  # Raises ValueError

''' itertools.zip_longest(): Fills in missing values with a placeholder (None by default) 
so no data is dropped.'''

from itertools import zip_longest
print(list(zip_longest(letters,index,fillvalue="_")))

print("Creating Dictionaries")
''' You can pass a zipped object directly into the dict() constructor to quickly 
pair keys and values'''

user_dict=dict(zip(names,scores))
print(user_dict)

print("Unzipping a List")
''' There is no separate unzip() function, but you can reverse the process by using the 
unpacking operator * inside zip()'''

pairs = [("A", 1), ("B", 2), ("C", 3)]

print(*pairs)
letters, numbers = zip(*pairs)
print(letters)  # Output: ('A', 'B', 'C')
print(numbers)  # Output: (1, 2, 3)

l1,l2,l3=zip([1,2,3],[10,20,30],[100,200,300])
print(l1)
print(l2)
print(l3)

print()
print(f"⭐  enumerate  Function   ⭐")

for index,name in enumerate(names):
    print(index,name)

print("Start Index set to 1 instead of default 0")
for index,name in enumerate(names,start=1):
    print(index,name)    

print("enumerate with string")
for index,name in enumerate("Hello"):
    print(index,name)

print("Converting directly into a List of Tuples")
enum=enumerate(names,start=5)
print(enum)
paired_list=list(enum) 
print(paired_list)   
print(list(enumerate("DIWALI")))

print("enumerate with Dictionary")

dic={"name":"Rob","age":40,"location":"UK"}

for index,item in enumerate(dic):
    print(index,item)
print(list(enumerate(dic)))    

print("with out enumerate")

models = ["OpenAI", "Groq", "Ollama"]

for i in range(len(models)):
    print(i,models[i])

print()
print(f"⭐  Any  Function   ⭐")    

''' The Python any() function returns True if at least one element in an iterable is truthy,
 and False if all elements are falsy or if the iterable is empty.
 It is a built-in tool commonly used to check conditions across 
 arrays, lists, or sets without writing verbose loops.
 💡 Understanding Truthy vs FalsyTo use any(), it helps to know how Python evaluates the elements:
 Truthy values: Non-zero numbers, non-empty strings, True, and filled collections.
 Falsy values: 0, None, False, empty strings "", and empty collections [].'''

# At least one True exists
print(any([False, False, True]))  # Output: True

# All are False
print(any([False, False, False])) # Output: False

# Empty list returns False
print(any([]))                    # Output: False

print("2. With Mixed Data Types (Truthy/Falsy values)")
# 'Hello' and 5 are truthy, 0 and False are falsy
print(any([0, "", False, 5]))      # Output: True (because 5 is truthy)
print(any([0, "", False]))         # Output: False

print("1. Checking If a Condition Matches Any Item")
'''  You can pair any() with a generator expression to see if any element in 
a collection passes a specific test.'''
numbers =[1,2,3,5,7,9,10]
has_even=any(x%2==0 for x in numbers)
print(has_even) # Output: True (because of 10)

print("2. Validating User Input")

password="Password123"

## Check if there is at least one digit
has_digit=any(char.isdigit() for char in password)
print(has_digit)

print()
print("3. Checking for Forbidden Words")
''' Scan a text string to see if it includes any blacklisted or banned terms. '''
banned_words = ["spam", "scam", "fake"]
user_message = "Check out this free scam offer!"

# Check if any banned word is in the message
is_spam = any(word in user_message for word in banned_words)
print(is_spam)  # Output: True