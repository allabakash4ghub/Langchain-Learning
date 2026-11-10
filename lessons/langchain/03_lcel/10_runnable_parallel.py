from langchain_core.runnables import RunnableLambda,RunnableParallel

# normal functions

def add_exclamation(text):
    return text+"!"

def to_uppercase(text):
    return text.upper()

def reverse_text(text):
    return text[::-1]


# Step 2: Convert functions into Runnables



# add_exclamation_runnable=RunnableLambda(add_exclamation)
# to_uppercase_runnable=RunnableLambda(to_uppercase)

# Step 3: Convert functions to runnable
chain=RunnableParallel(
    exclamation=RunnableLambda(add_exclamation),
    uppercase=RunnableLambda(to_uppercase),
    reverse=RunnableLambda(reverse_text)
)



# Step 4: Invoke the chain
response=chain.invoke("Hello Langchain")




print(response)
print(type(response))




# chain2=(add_exclamation_runnable | to_uppercase_runnable)
# response2=chain2.invoke("This is test")
# print(response2)