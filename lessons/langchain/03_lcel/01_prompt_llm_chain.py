# LCEL = LangChain Expression Language
#It provides a simple way to connect LangChain components using the pipe operator:
#Component 1 | Component 2 | Component 3   i.e. chain = prompt | llm

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load variables from .env 
load_dotenv()
# Step 1: Create a prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        (
         "system",
         "You are a helpful tutor. Explain the concepts in simple way "   
        ),
        (
            "human",
            "explain {topic} in {number} simple sentences"
        )

    ]
)

# Step 2: Create the LLM
llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_completion_tokens=80
)

# Step 3: Connect Prompt → LLM using LCEL

chain=prompt | llm

# Step 4: Execute the chain
response=chain.invoke(
    {
      "topic":"Langchain Expression Language" ,
      "number":2
    }
)

# Step 5: Print the response
print("\nResponse:")
print(response.content)

print("\nResponse type:")
print(type(response))

'''
Response:
Langchain Expression Language is a way to create and manipulate expressions in a 
programming context, allowing users to define complex logic in a straightforward manner.
It helps developers build applications that can understand and process natural language inputs
more effectively.

Response type:
<class 'langchain_core.messages.ai.AIMessage'>

'''