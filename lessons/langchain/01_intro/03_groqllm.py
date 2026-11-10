from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Load variables from .env
# This also allows other project-specific variables to be loaded.
load_dotenv()

# Create a the Groq model object 

llm=ChatGroq(
     model="openai/gpt-oss-120b",
     temperature=0.1,
     max_tokens=80
)

# Create a user message
message=HumanMessage(content="Explain LangChain in two simple sentences.")

# Send the message to the LLM, Here the input should be in list format which should contain 
# human,system and AI message
## Send a list of messages to the LLM
response=llm.invoke([message])

print(response)
# # Print the type of the returned object
# print("\nResponse Type:")
# print(type(response))

# # Print the actual response text
# print("\nLLM Response:")
# print(response.content)

# # Print token usage
# print("\nToken Usage:")
# print(response.usage_metadata)

# print("\nResponse Meta data")
# print(response.response_metadata)

