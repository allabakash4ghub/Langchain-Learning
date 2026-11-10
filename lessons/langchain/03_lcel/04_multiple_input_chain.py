from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


load_dotenv()


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in {number} simple sentences."
)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    max_completion_tokens=100
)


output_parser = StrOutputParser()


chain = prompt | llm | output_parser


response = chain.invoke(
    {
        "topic": "RAG",
        "number": 2
    }
)


print(response)