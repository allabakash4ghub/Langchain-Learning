# from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate


# ============================================================
# 1. LLM
# ============================================================

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )
# llm=ChatGoogleGenerativeAI(
#     model="gemini-3.8-flash",
#     temperature=0.1,
#     max_tokens=500
# )

llm=ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0.1,
    max_tokens=500
)


# ============================================================
# 2. Load existing Chroma vector database
# ============================================================

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)


# ============================================================
# 3. Create Retriever
# ============================================================

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)


# ============================================================
# 4. User Question
# ============================================================

question = "How do I know whether my classifier is performing well?"


print("=" * 70)
print("USER QUESTION")
print("=" * 70)

print(question)


# ============================================================
# 5. Generate Multiple Search Queries
# ============================================================

query_prompt = ChatPromptTemplate.from_template(
    """
    Generate 4 different search queries that could help
    retrieve documents relevant to the user's question.

    Each query should approach the question from a
    slightly different perspective.

    Do not include numbering.
    Do not include bullets.
    Do not include quotation marks.

    Return exactly 4 queries, one query per line.

    User question:
    {question}
    """
)


response = llm.invoke(
    query_prompt.format_messages(
        question=question
    )
)


# Convert LLM response into Python list

queries = [
    line.strip()
    for line in response.content[0]["text"].splitlines()
    if line.strip()
]


print("\n" + "=" * 70)
print("GENERATED SEARCH QUERIES")
print("=" * 70)

for i, query in enumerate(queries, start=1):
    print(f"{i}. {query}")


# ============================================================
# 6. Retrieve Documents for Every Query
# ============================================================

all_documents = []

for query in queries:

    documents = retriever.invoke(query)

    all_documents.extend(documents)


print("\n" + "=" * 70)
print("RETRIEVAL SUMMARY")
print("=" * 70)

print("Number of queries:", len(queries))

print(
    "Documents retrieved per query:",
    4
)

print(
    "Total retrieved documents:",
    len(all_documents)
)


# ============================================================
# 7. Remove Duplicate Documents
# ============================================================

unique_documents = {}

for document in all_documents:

    # For this learning exercise we use page_content
    # as a temporary unique identifier.

    document_id = document.page_content

    if document_id not in unique_documents:

        unique_documents[document_id] = document


documents = list(unique_documents.values())


print(
    "Unique documents after deduplication:",
    len(documents)
)


# ============================================================
# 8. Display Retrieved Documents
# ============================================================

print("\n" + "=" * 70)
print("RETRIEVED DOCUMENTS")
print("=" * 70)


for i, document in enumerate(documents, start=1):

    metadata = document.metadata

    source = metadata.get(
        "source",
        "Unknown"
    )

    page = metadata.get(
        "page_label",
        metadata.get(
            "page",
            "Unknown"
        )
    )

    print("\n" + "-" * 70)

    print(f"Document {i}")

    print("Source:", source)

    print("Page:", page)

    print("\nContent:")

    print(document.page_content)


# ============================================================
# 9. Build Context for LLM
# ============================================================

context = "\n\n".join(
    document.page_content
    for document in documents
)


# ============================================================
# 10. Final Answer Prompt
# ============================================================

answer_prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful question-answering assistant.

    Answer the user's question using ONLY the information
    provided in the context.

    Do not use outside knowledge.

    If the context does not contain enough information
    to answer the question, clearly say that the
    information is not available in the provided documents.

    User question:
    {question}

    Context:
    {context}

    Provide a concise and accurate answer.
    """
)


# ============================================================
# 11. Generate Final Answer
# ============================================================

answer = llm.invoke(
    answer_prompt.format_messages(
        question=question,
        context=context
    )
)


# ============================================================
# 12. Display Final Answer
# ============================================================

print("\n" + "=" * 70)
print("FINAL ANSWER")
print("=" * 70)

print(answer.content[0]["text"])


# ============================================================
# 13. Display Sources
# ============================================================

print("\n" + "=" * 70)
print("SOURCES")
print("=" * 70)


for i, document in enumerate(documents, start=1):

    metadata = document.metadata

    source = metadata.get(
        "source",
        "Unknown"
    )

    page = metadata.get(
        "page_label",
        metadata.get(
            "page",
            "Unknown"
        )
    )

    print(
        f"[Source {i}] "
        f"{source} | Page {page}"
    )
	
	
