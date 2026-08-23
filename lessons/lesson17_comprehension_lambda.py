print("⭐ 1. List Comprehension ⭐")

print("# Normal approach:")
numbers=[2,4,5,6,7,8]
square=[]
for num in numbers:
    sqn=num**2
    square.append(sqn)
print(square)    

print("Using list comprehension:")

sqrs=[num**2 for num in numbers]
print(sqrs)

# General syntax   new_list = [expression for item in iterable]

print("2. List Comprehension with Condition")
'''# syntax 
 new_list = [
    expression
    for item in iterable
    if condition
]

Esay Rule :
Filter:
[value for value in data if condition]

If-else transformation:
[value_if_true if condition else value_if_false for value in data]

'''
even = [even for even in numbers if even % 2 ==0 ]
print(even)

print()
print("3. if-else Inside a List Comprehension")

ClassType =[ "even" if num % 2 == 0 else "odd" for num in numbers]
print(ClassType)

print()
print("⭐ 4. Dictionary Comprehension ⭐")

print ("Normal dictionary creation")

dic_squares={}
for num in numbers:
    dic_squares[num]=num**2

print(dic_squares)    

print("Using dictionary comprehension:")

dict_comp={num:num**2 for num in numbers}
print(dict_comp)

print("5. Set Comprehension , which removed the repeated results")

set_number=[2,4,2,4,5,6,5]
unique_squares={num**2 for num in set_number}
print(unique_squares)

print("6. Generator Expression")

numbers2=[1,2,3,4]
gen=(num**2 for num in numbers2)
print(gen)

for sqr in gen:
    print(sqr,end=" ")

print("⭐ Part 2: Lambda Functions ⭐")
''' A lambda is a small anonymous function.
General syntax:  lambda arguments: expression
'''

print("Normal function")

def square(num):
    return num**2
print(square(9))

print(" Lambda function")

squareL= lambda num : num**2

print(squareL(9))

print("8. Lambda with Multiple Arguments")

add = lambda a,b,c: a+b+c

print(add(4,5,1))

print("9. lambda with sorted() ⭐")

users=[{"name": "Raj", "age": 25},
       {"name": "Bheem", "age": 35},
       {"name": "Rocky", "age": 40}
       ]
sorted_users= sorted(users,key=lambda user : user["age"])

''' lambda receives each item at a time 

iterartion 1 - user = {"name": "John", "age": 35}    → 35
iterartion 2 - user = {"name": "Alice", "age": 25}   → 25
iterartion 3 - user = {"name": "Bob", "age": 30}     → 30'''

print(sorted_users)

print("10. lambda with map()")
''' In Python, map() transforms elements in an iterable, while filter() extracts elements 
 based on a condition. Both are built-in, higher-order functions that return lazy iterators 
 rather than lists, meaning they process data efficiently on demand'''
''' Genaral syntax  map(function,iterable)
filter(function, iterable)

'''
squares=map(lambda x:x**2 , numbers)
print(squares)
print(type(squares))
print(list(squares))

print("11. lambda with filter()")

even_numbers=filter(lambda num: num %2 == 0 ,numbers)
print(even_numbers)
print(list(even_numbers))

print("12. Real AI/Data Example ⭐")
## Suppose your chatbot returns documents with relevance scores:
documents = [
    {"text": "Python basics", "score": 0.75},
    {"text": "LangChain tutorial", "score": 0.92},
    {"text": "SQL guide", "score": 0.81}
]
ranked_documents=sorted(documents,
                        key= lambda doc : doc["score"],
                        reverse=True)
print(ranked_documents)
print(type(ranked_documents))

for doc in ranked_documents:
    print(
        doc["text"],
        doc["score"]
    )
# This is similar to ranking search results in a RAG application.
 
print("⭐ SORTED example ⭐")   

lst=[5,4,3,8,9,1]
tup=(8.11,0,20,5)
sets={50,20,70,10}
dic= {"apple": 1.5, "orange": 0.8, "banana": 1.2}
words = ["banana", "pie", "apple", "kiwi"]
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]

lst_sort=sorted(lst)
print(lst_sort)
print(sorted(lst,reverse=True))
print(sorted("python"))
print(sorted(tup))
print(sorted(words,key=len))
sorted_students=sorted(students,
                       key=lambda student : student[1])
print(sorted_students)

print(sorted(dic))