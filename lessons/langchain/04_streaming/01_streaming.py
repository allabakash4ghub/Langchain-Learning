''' 
Streaming in LangChain allows you to surface live output, 
such as individual tokens or intermediate tool calls, to your frontend instead of waiting for
the full response to finish generating.

LangChain implements a streaming system to surface real-time updates.
Streaming is crucial for enhancing the responsiveness of applications built on LLMs. 
By displaying output progressively, even before a complete response is ready, 
streaming significantly improves user experience (UX), particularly when dealing with 
the latency of LLMs.

| Method     | Behavior                     | Typical use       |
| ---------- | ---------------------------- | ----------------- |
| `invoke()` | Waits for complete result    | Normal processing |
| `stream()` | Returns output progressively | Chat UIs          |
| `batch()`  | Processes multiple inputs    | Multiple requests |


'''
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


load_dotenv()

prompt=ChatPromptTemplate.from_template(
    "Explain the {topic} in 5 sentences."
)

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1,
    max_tokens=200
)

output_parser=StrOutputParser()

chain= prompt | llm | output_parser

print("\nStreaming response:\n")

for chunk in chain.stream(
    {"topic": "Human evolution"}
):
    #print(chunk.content,end="",flush=True)  This is used if output_parser is not used
    print(chunk,end="",flush=True)

print("\n")