''' RunnableLambda is an important concept because it lets you use your normal
 Python functions inside an LCEL chain.'''

from annotated_types import UpperCase
from langchain_core.runnables import RunnableLambda

def to_uppercase(text):
    return text.upper()

# Convert the function into Runnable
UpperCase_runnable= RunnableLambda(to_uppercase)

# Invoke the Runnable

result= UpperCase_runnable.invoke("Hello Langchain")

print(result)
print(type(result))