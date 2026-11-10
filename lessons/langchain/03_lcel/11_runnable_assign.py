''' RunnableAssign is useful when you already have a dictionary and want to 
add new fields to it without losing the existing fields.'''

from langchain_core.runnables import RunnableLambda,RunnableAssign

# Add a new field to the existing dictionary

chain= RunnableAssign(
    {
        "uppercase_topic":RunnableLambda(lambda x: x["topic"].upper())
    }
)

input_data= {
    "topic":"Langchain",
    "number":2
}

result=chain.invoke(input_data)

print(result)

''' 
output : 
{'topic': 'Langchain', 'number': 2, 'uppercase_topic': 'LANGCHAIN'}

'''