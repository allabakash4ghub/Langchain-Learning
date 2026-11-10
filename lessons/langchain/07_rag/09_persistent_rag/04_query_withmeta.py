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

CHROMA_PATH = (
    r"E:\GenAI\Langchain-Learning\lessons\langchain"
    r"\07_rag\09_persistent_rag\data\chroma_db"
)


# -----------------------------------
# 1. Create Embedding Model
# -----------------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# -----------------------------------
# 2. Load Existing Chroma Database
# -----------------------------------

vector_store = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)


# -----------------------------------
# 3. Create Retriever
# -----------------------------------

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# -----------------------------------
# 4. Create LLM
# -----------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_completion_tokens=150
)


# -----------------------------------
# 5. Create Prompt
# -----------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Answer the user's question using only the provided context.

If the answer is not available in the context, say:

"I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
)


# -----------------------------------
# 6. Format Documents
# -----------------------------------

def format_docs(documents):

    return "\n\n".join(
        document.page_content
        for document in documents
    )


# -----------------------------------
# 7. RAG Chain
# -----------------------------------

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)


# -----------------------------------
# 8. Ask Question
# -----------------------------------

query = "How many annual leave days do employees receive?"

response = rag_chain.invoke(query)


print("\n================================")
print("Query")
print("================================")

print(query)


print("\n================================")
print("Answer")
print("================================")

print(response.content)


# -----------------------------------
# 9. Retrieve Documents Separately
# -----------------------------------

documents = retriever.invoke(query)


print("\n================================")
print("Sources")
print("================================")


for document in documents:

    source = document.metadata.get(
        "source",
        "Unknown"
    )

    print(f"- {source}")