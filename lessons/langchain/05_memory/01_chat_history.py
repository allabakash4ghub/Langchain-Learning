from dotenv import load_dotenv
from langchain_core.messages import (SystemMessage,
                                     HumanMessage,
                                     AIMessage)
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(
     model="openai/gpt-oss-120b",
     temperature=0.1,
     max_tokens=80
)

messages=[
    SystemMessage(
        content="You are a helpful assistance"
    )
]

# First user question
messages.append(
    HumanMessage(
        content="My name is Bunny"
    )
)

print(messages)

response=llm.invoke(messages)
print(f"AI Full Response : {response.content}")

# Add AI response to history

messages.append(response)

print(f"After AI Message 1st Turn:{messages}")

# Second user question
messages.append(
    HumanMessage(
        content="What is my Name"

    )
)

print(f"Messages after 2nd Human Message:{messages}")

response=llm.invoke(messages)

print(f"AI Final message:{response.content}")