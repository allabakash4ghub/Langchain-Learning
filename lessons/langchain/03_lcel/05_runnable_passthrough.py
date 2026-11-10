''' RunnablePassthrough useful when the input is required to use multiple places with out changing
As the name suggests, it simply passes the input through without changing it.

# Why is it useful?
Imagine a future RAG application.
Your input is:
"What is LangChain?"
You need that same input for two purposes:

Purpose 1: Retrieve context
Question
   ↓
Retriever
   ↓
Relevant Documents / Context

Purpose 2: Keep the original question
Question
   ↓
Pass unchanged
   ↓
Original Question

Then combine both:

                    ┌──→ Retriever ──→ Context
User Question ──────┤
                    └──→ Passthrough ─→ Question
                                      │
                         Context + Question
                                      ↓
                                   Prompt

This is why RunnablePassthrough is extremely common in RAG.
'''

from langchain_core.runnables import RunnablePassthrough

passthrough = RunnablePassthrough()
result=passthrough.invoke("Hello Langchain")
print(result)
print(type(result))
