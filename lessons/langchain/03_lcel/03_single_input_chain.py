from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


load_dotenv()


# Prompt with one input variable: {topic}
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in two simple sentences."
)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    max_completion_tokens=100
)


output_parser = StrOutputParser()


# Create the chain
chain = prompt | llm | output_parser


# Because there is only one input variable,
# we can directly pass a string
response = chain.invoke("LangChain")


print(response)