# Basic exception
'''try :
    result = 20/0

except ZeroDivisionError as e:
    print("can not divide by Zero")   
    print(f"Error {e}") '''

'''
# Multiple Exceptions
try:
    value = int(input("Enter number: "))
    result = 100 / value
    print(result)

except ValueError:
    print("Please enter a number")

except ZeroDivisionError as e:
    print("Number cannot be zero")
    print(f"Observed Error in {e}")

else :  # else executes only when no exception occurs.
    print(f"result from else is {result}")
finally : #finally executes regardless of success or failure.
    print("Execution Completed and finally block executes always") '''

# Raising Your Own Exception

def divide(a:float,b:float) -> float:
    if b==0:
        raise ValueError("b can not be Zero")
    return a/b

print(divide(4,2))

## Custom Exceptions
class InvalidModelError(Exception):
    pass

def load_model(model:str):
    if model not in {"openai","groq","ollama"}:
        raise InvalidModelError(f"Unsupported Model:{model}")
    else:
        print(f"Selected model is {model}")

try:
    load_model(model="grok")

except InvalidModelError as e:
    print(e)    