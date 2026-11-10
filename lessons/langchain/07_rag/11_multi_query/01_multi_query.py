from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma

# --------------------------------------------------
# 1. LLM
# --------------------------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# --------------------------------------------------
# 2. Load existing Chroma database
# --------------------------------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vectorstore = Chroma(
    persist_directory="../10_citations/chroma_db",
    embedding_function=embeddings
)


# --------------------------------------------------
# 3. Retriever
# --------------------------------------------------

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)


# --------------------------------------------------
# 4. User question
# --------------------------------------------------

question = "How do I know whether my classifier is performing well?"


# --------------------------------------------------
# 5. Generate multiple queries
# --------------------------------------------------

query_prompt = ChatPromptTemplate.from_template(
    """
    Generate 4 different search queries that could help
    retrieve documents relevant to the user's question.

    User question:
    {question}

    Return only the 4 queries, one per line.
    """
)

response = llm.invoke(
    query_prompt.format_messages(
        question=question
    )
)

print(f"response : {response}")

queries = [
    line.strip()
    for line in response.content.splitlines()
    if line.strip()
]

print("\nGenerated queries:")

for i, query in enumerate(queries, start=1):
    print(f"{i}. {query}")


# --------------------------------------------------
# 6. Retrieve documents for every query
# --------------------------------------------------

all_documents = []

for query in queries:

    documents = retriever.invoke(query)

    all_documents.extend(documents)


print("\nTotal retrieved documents:")
print(len(all_documents))
print(f"first element in all_documents : {all_documents[0]} ")


# --------------------------------------------------
# 7. Remove duplicates
# --------------------------------------------------

unique_documents = {}

for document in all_documents:

    document_id = document.page_content

    if document_id not in unique_documents:
        unique_documents[document_id] = document


documents = list(unique_documents.values())


print("\nUnique documents:")
print(len(documents))


# --------------------------------------------------
# 8. Display documents
# --------------------------------------------------

for i, document in enumerate(documents, start=1):

    print("\n" + "=" * 70)

    print(f"Document {i}")

    print("Source:", document.metadata.get("source"))

    print(
        "Page:",
        document.metadata.get(
            "page_label",
            document.metadata.get("page")
        )
    )

    print("\n", document.page_content[:500])