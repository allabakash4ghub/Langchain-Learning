''' 
chain.batch(inputs) does not stream the output. 
It executes the chain for multiple inputs and returns the results as a collection once the batch operation completes.


'''
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


load_dotenv()

prompt=ChatPromptTemplate.from_template(
    "Explain the {topic} in 3 sentences."
)

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1,
    max_tokens=150
)

output_parser=StrOutputParser()

chain= prompt | llm | output_parser

print("\nBatch response:\n")

input=[
    {"topic":"LangChain"},
    {"topic":"RAG"},
    {"topic":"Vector Database"}
]

response=chain.batch(inputs=input)


for topic, response in zip(input,response):
    print(f"\nTopic:{topic["topic"]}")
    print(f"Response:{response}")
          
