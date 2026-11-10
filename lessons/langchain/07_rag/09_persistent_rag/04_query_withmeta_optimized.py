from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableLambda
)

load_dotenv()


# --------------------------------------------------
# 1. Load existing vector database
# --------------------------------------------------

CHROMA_PATH = (
    r"E:\GenAI\Langchain-Learning\lessons\langchain"
    r"\07_rag\09_persistent_rag\data\chroma_db"
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)


# --------------------------------------------------
# 2. Create Retriever
# --------------------------------------------------

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# --------------------------------------------------
# 3. Create LLM
# --------------------------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_completion_tokens=150
)


# --------------------------------------------------
# 4. Prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful company policy assistant.

Answer the question using only the provided context.

If the answer is not present in the context,
say:

"I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
)


# --------------------------------------------------
# 5. Format retrieved documents
# --------------------------------------------------

def format_docs(documents):

    return "\n\n".join(
        document.page_content
        for document in documents
    )


# --------------------------------------------------
# 6. Format source information
# --------------------------------------------------

def format_sources(documents):

    sources = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        page = document.metadata.get("page")

        item = {
            "source": source,
            "page": page
        }

        if item not in sources:
            sources.append(item)

    return sources

# --------------------------------------------------
# 7. RAG Chain
# --------------------------------------------------

rag_chain = (
    {
        "question": RunnablePassthrough(),
        "documents": retriever
    }

    # Create context from retrieved documents
    | RunnablePassthrough.assign(
        context=lambda x: format_docs(x["documents"])
    )

    # Generate answer while preserving documents
    | RunnablePassthrough.assign(
        answer=prompt | llm
    )

    # Create final result
    | RunnableLambda(
        lambda x: {
            "answer": x["answer"].content,
            "sources": format_sources(x["documents"])
        }
    )
)


# --------------------------------------------------
# 8. Query
# --------------------------------------------------

query = "How many annual leave days do employees receive?"


# --------------------------------------------------
# 9. Invoke ONCE
# --------------------------------------------------

result = rag_chain.invoke(query)


# --------------------------------------------------
# 10. Display result
# --------------------------------------------------

print("\n================================")
print("Query")
print("================================")
print(query)

print("\n================================")
print("Answer")
print("================================")
print(result["answer"])

print("\n================================")
print("Sources")
print("================================")

for source in result["sources"]:
    print(source)