from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
#from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate


# ============================================================
# 1. LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0
)


# ============================================================
# 2. Load existing Chroma database
# ============================================================

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorstore = Chroma(
    persist_directory="../11_multi_query/chroma_db",
    embedding_function=embeddings
)


# ============================================================
# 3. User Question
# ============================================================

question = "How do I know whether my classifier is performing well?"


print("=" * 70)
print("USER QUESTION")
print("=" * 70)

print(question)


# ============================================================
# 4. Generate Hypothetical Answer
# ============================================================

hyde_prompt = ChatPromptTemplate.from_template(
    """
    Write a hypothetical answer to the user's question.

    The answer should contain technical concepts and terminology
    that would likely appear in documents relevant to the question.

    Do not say that you are generating a hypothetical answer.
    Just write the answer.

    User question:
    {question}
    """
)


response = llm.invoke(
    hyde_prompt.format_messages(
        question=question
    )
)


hypothetical_answer = response.content[0]["text"]


print("\n" + "=" * 70)
print("HYPOTHETICAL ANSWER")
print("=" * 70)

print(hypothetical_answer)


# ============================================================
# 5. Embed the Hypothetical Answer
# ============================================================

hyde_embedding = embeddings.embed_query(
    hypothetical_answer
)


# ============================================================
# 6. Search Chroma using the HyDE embedding
# ============================================================

results = vectorstore.similarity_search_by_vector(
    hyde_embedding,
    k=4
)


# ============================================================
# 7. Display Retrieved Documents
# ============================================================

print("\n" + "=" * 70)
print("RETRIEVED DOCUMENTS")
print("=" * 70)


for i, document in enumerate(results, start=1):

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
# 8. Build Context
# ============================================================

context = "\n\n".join(
    document.page_content
    for document in results
)


# ============================================================
# 9. Generate Final Answer
# ============================================================

answer_prompt = ChatPromptTemplate.from_template(
    """
    Answer the user's question using ONLY the provided context.

    Do not use the hypothetical answer as evidence.

    If the context does not contain enough information,
    say that the information is not available in the
    provided documents.

    User question:
    {question}

    Context:
    {context}

    Provide a concise and accurate answer.
    """
)


answer = llm.invoke(
    answer_prompt.format_messages(
        question=question,
        context=context
    )
)


# ============================================================
# 10. Display Final Answer
# ============================================================

print("\n" + "=" * 70)
print("FINAL ANSWER")
print("=" * 70)

print(answer.content[0]["text"])


# ============================================================
# 11. Display Sources
# ============================================================

print("\n" + "=" * 70)
print("SOURCES")
print("=" * 70)


for i, document in enumerate(results, start=1):

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