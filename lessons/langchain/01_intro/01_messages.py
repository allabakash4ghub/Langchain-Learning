from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

''' We  have following messages 
HumanMessage
AIMessage
SystemMessage
ToolMessage
BaseMessage   
Refer URL for documentation - https://reference.langchain.com/python/langchain-core/messages?utm_source=chatgpt.com'''

#System message -gives instructions to the AI

system_message=SystemMessage(content="You are a helpful python Tutor")

# Human message - Message from the Human 

human_message=HumanMessage(content="what is langchain?")

# AI message -- response from AI
ai_message=AIMessage(content="Langchain is a framework for building LLM applications")

print(f"system message : {system_message}")
print(f"\nHuman Message :  {human_message}")
print(f"\nAI Message: {ai_message}")

print(type(system_message))

## Check Keys

print("Check API Keys")

import os

if os.getenv("OPENAI_API_KEY"):
    print("OpenAI Key found")
else:
    print("OpenAI Key not found")

if os.getenv("GROQ_API_KEY"):
    print("GROQ Key found")
else:
    print("GROQ Key not found")