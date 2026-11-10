from langchain_core.runnables import RunnablePassthrough,RunnableParallel

chain = RunnableParallel( {
    "original":RunnablePassthrough(),
    "uppercase": lambda x:x.upper()
})

result= chain.invoke("Hello Langchain")

print(result)

## example 2 

chain =RunnableParallel( {
    "question": RunnablePassthrough(),
    "question_length": lambda x: len(x)
})

result = chain.invoke("What is RAG?")

print(result)

## other way of calling i.e. Alternative: Dictionary coercion inside an LCEL chain


chain = {
    "original":RunnablePassthrough(),
    "upper": lambda x :x.upper()
} | RunnablePassthrough()

result= chain.invoke("Test with other method")

print(f"Other Method {result} ")