from langchain_core.runnables import RunnableSequence,RunnableLambda

# normal functions

def add_exclamation(text):
    return text+"!"

def to_uppercase(text):
    return text.upper()

# Step 2: Convert functions into Runnables

add_exclamation_runnable=RunnableLambda(add_exclamation)
to_uppercase_runnable=RunnableLambda(to_uppercase)

# Step 3: Create a sequence
chain=RunnableSequence(
    first=add_exclamation_runnable,
    last=to_uppercase_runnable
)

''' The above code is equivalent to 
chain = (
    add_exclamation_runnable
    | uppercase_runnable
)

'''


chain2=(add_exclamation_runnable | to_uppercase_runnable)

# Step 4: Invoke the chain
response=chain.invoke("Hello Langchain")

response2=chain2.invoke("This is test")

print(response)
print(type(response))
print(response2)