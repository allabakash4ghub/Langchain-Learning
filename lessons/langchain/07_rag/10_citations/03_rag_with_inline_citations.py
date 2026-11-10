from dotenv import load_dotenv
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

- Use the source labels such as [Source 1], [Source 2]
  when citing information.
- Place the citation immediately after the statement
  supported by that source.
- You may cite multiple sources when necessary.
- Do not invent source numbers.
- Do not cite a source unless the provided context
  supports the statement.
- If the question asks for a list, include all relevant
  items found in the context.
- Do not use outside knowledge.

If the answer cannot be found in the context, say:

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

def format_docs_with_sources(documents):

    formatted_docs = []

    for i, document in enumerate(documents, start=1):

        formatted_docs.append(
            f"[Source {i}]\n"
            f"{document.page_content}"
        )

    return "\n\n".join(formatted_docs)


# --------------------------------------------------
# 6. Create source information
# --------------------------------------------------

def format_source_metadata(documents):

    sources = []

    for i, document in enumerate(documents, start=1):

        metadata = document.metadata

        sources.append(
            {
                "id": i,
                "source": metadata.get(
                    "source",
                    "Unknown"
                ),
                "page": metadata.get(
                    "page_label",
                    metadata.get("page", "Unknown")
                )
            }
        )

    return sources

# --------------------------------------------------
# 7. RAG chain
# -------------------------------------------------

rag_chain = (

    {
        "question": RunnablePassthrough(),
        "documents": retriever
    }

    # ---------------------------------------------
    # Add source-labelled context
    # ---------------------------------------------

    | RunnablePassthrough.assign(
        context=lambda x:
            format_docs_with_sources(
                x["documents"]
            )
    )

    # ---------------------------------------------
    # Generate answer
    # ---------------------------------------------

    | RunnablePassthrough.assign(
        answer=prompt | llm
    )

    # ---------------------------------------------
    # Create final result
    # ---------------------------------------------

    | RunnableLambda(
        lambda x: {
            "answer": x["answer"].content,
            "sources": format_source_metadata(
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

    print(
        f"[Source {source['id']}] "
        f"{source['source']} - "
        f"Page {source['page']}"
    )