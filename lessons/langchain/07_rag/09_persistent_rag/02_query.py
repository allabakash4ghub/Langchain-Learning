from click import prompt
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()

# -----------------------------------
# Configuration
# -----------------------------------

CROMA_PATH = r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\09_persistent_rag\data\chroma_db"

# -----------------------------------
# 1. Create embedding model
# -----------------------------------
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small"
)

# -----------------------------------
# 2. Load existing Chroma database
# -----------------------------------

vector_store = Chroma(
    persist_directory=CROMA_PATH,
    embedding_function=embeddings
)

# -----------------------------------
# 3. Create Retriever
# -----------------------------------

retriever = vector_store.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k": 3}
)

# -----------------------------------
# 4. Create LLM
# -----------------------------------
llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_completion_tokens=100
)

# -----------------------------------
# 5. Create Prompt
# -----------------------------------
prompt = ChatPromptTemplate.from_template(
    template= """
     You are an helpful assistant and answer the user's question only from the provided context,
     if the answer is not available in the context, say:
     "I don't have enough information in the provided documents."

     context :
     {context}

     question :
     {question}

     answer :

"""
)

# -----------------------------------
# Format Documents
# -----------------------------------

def format_docs(documents):

    formatted_docs = []

    for doc in documents:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        formatted_docs.append(
            f"Source: {source}\n"
            f"Content: {doc.page_content}"
        )

    return "\n\n".join(formatted_docs) 

# -----------------------------------
# 6. Create RAG Chain
# -----------------------------------

rag_chain =(
    {
        "context":retriever|format_docs,
        "question":RunnablePassthrough()

    }
    |prompt
    |llm
)

# -----------------------------------
# 7. Ask a Question
# -----------------------------------

query="How many annual leave days do employees receive?"

response=rag_chain.invoke(query)  

print(f"query:{query}")
print(f"response:{response.content}")

query="How many quarterly leave days do employees receive?"

response=rag_chain.invoke(query)  

print(f"query:{query}")
print(f"response:{response.content}")


""" response :
query:How many annual leave days do employees receive?
response:Employees receive 20 days of annual leave per year.
query:How many quarterly leave days do employees receive?
response:I don't have enough information in the provided documents.

"""