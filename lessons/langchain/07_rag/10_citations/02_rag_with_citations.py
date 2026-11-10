from dotenv import load_dotenv
from langchain_community import retrievers
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.runnables import (
    RunnablePassthrough,RunnableLambda
)

load_dotenv()

# --------------------------------------------------
# 1. Load vector database
# --------------------------------------------------
CHROMA_PATH = r"chroma_db"

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store=Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

# --------------------------------------------------
# 2. Create retriever
# --------------------------------------------------

retriever=vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":4}
)

# --------------------------------------------------
# 3. LLM
# --------------------------------------------------
llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_completion_tokens=150
)

# --------------------------------------------------
# 4. Prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI/ML knowledge assistant.

Answer the question using ONLY the provided context.

Important instructions:
- Identify all relevant information from the context.
- If the question asks for a list, include ALL items explicitly
  mentioned in the context that match the question.
- Do not omit relevant items just to make the answer shorter.
- Do not add information from outside the context.
- If the answer cannot be found in the context, say:
  "I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
)

# --------------------------------------------------
# 5. Format documents for LLM
# --------------------------------------------------

def format_docs(documents):

    return "\n\n".join(
        document.page_content
        for document in documents
    )


# --------------------------------------------------
# 6. Create source information
# --------------------------------------------------

def format_sources(documents):

    sources = []

    for document in documents:

        metadata = document.metadata

        source = metadata.get(
            "source",
            "Unknown"
        )

        page = metadata.get(
            "page_label",
            metadata.get("page", "Unknown")
        )

        source_info = {
            "source": source,
            "page": page
        }

        if source_info not in sources:
            sources.append(source_info)

    return sources

# --------------------------------------------------
# 7. RAG chain
# -------------------------------------------------

rag_chain=(
     {
         "question":RunnablePassthrough(),
         "documents":retriever         
     }
     # Add context while preserving documents
     |  RunnablePassthrough.assign(context = lambda x : format_docs(
         x["documents"] ))
    # Generate answer while preserving everything  
     | RunnablePassthrough.assign(
         answer= prompt | llm )  

     # Create final result
     
     | RunnableLambda (
         lambda x : {
             "answer":x["answer"].content,
             "sources": format_sources(
                 x["documents"]
             )
         }
     )      

)

# --------------------------------------------------
# 8. Query
# --------------------------------------------------

query = (
    "What are the main evaluation metrics "
    "used for classification models?"
)
# --------------------------------------------------
# 9. Invoke
# --------------------------------------------------

result = rag_chain.invoke(query)

# --------------------------------------------------
# 10. Display answer
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

for i, source in enumerate(
    result["sources"],
    start=1
):

    print(
        f"[Source {i}] "
        f"{source['source']} "
        f"- Page {source['page']}"
    )