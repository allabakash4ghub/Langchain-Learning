from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_openai import output_parsers

load_dotenv()

# Normal Python function

def clean_text(text):
    return text.strip().lower()

# Convert it into a Runnable

clean_topic_runnable=RunnableLambda(clean_text)

# Create the prompt
prompt=ChatPromptTemplate.from_template(
    "Explain the {topic} in two simple sentences"
)

# Create the LLM
llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1,
    max_tokens=80
)

# Create output parser
output_parser=StrOutputParser()

# Create the chain
chain=(
    clean_topic_runnable
    |RunnableLambda(lambda topic: {"topic":topic})
    |prompt
    |llm
    |output_parser
)

# Execute the chain
response=chain.invoke("   LangChain Expression Language   ")

print(response)
print(f"type of response :{type(response)} ")

print("\nIs it a string?")
print(isinstance(response, str))