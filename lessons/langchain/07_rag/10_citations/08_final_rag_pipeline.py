from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder


# ============================================================
# CONFIGURATION
# ============================================================

USE_QUERY_REWRITE = True

VECTOR_TOP_K = 8
BM25_TOP_K = 8
RERANK_TOP_K = 3

RRF_K = 60


# ============================================================
# 1. LOAD VECTOR STORE
# ============================================================

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = Chroma(
    collection_name="langchain",
    persist_directory="chroma_db",
    embedding_function=embedding_model,
)


# ============================================================
# 2. LOAD ALL DOCUMENTS FOR BM25
# ============================================================

data = vector_store.get(
    include=["documents", "metadatas"]
)

documents = [
    Document(
        page_content=text,
        metadata=metadata
    )
    for text, metadata in zip(
        data["documents"],
        data["metadatas"]
    )
]

print(
    f"Total documents/chunks: {len(documents)}"
)


# ============================================================
# 3. USER QUERY
# ============================================================

original_query = (
    "How do I know whether my classifier "
    "is performing well?"
)


# ============================================================
# 4. QUERY TRANSFORMATION
# ============================================================

if USE_QUERY_REWRITE:

    rewrite_llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    rewrite_prompt = ChatPromptTemplate.from_template(
        """
You are a query rewriting assistant for a RAG system.

Rewrite the user's question into a concise,
standalone search query suitable for document retrieval.

Rules:
- Preserve the original meaning.
- Do not answer the question.
- Include important technical concepts.
- Return only the rewritten query.

User question:
{question}
"""
    )

    rewrite_chain = rewrite_prompt | rewrite_llm

    rewrite_response = rewrite_chain.invoke(
        {
            "question": original_query
        }
    )

    search_query = rewrite_response.content.strip()

else:

    search_query = original_query


print("\n========== QUERY ==========")

print(f"Original : {original_query}")
print(f"Search   : {search_query}")


# ============================================================
# 5. VECTOR SEARCH
# ============================================================

vector_results = (
    vector_store.similarity_search_with_score(
        search_query,
        k=VECTOR_TOP_K
    )
)


print("\n========== VECTOR SEARCH ==========")

for rank, (document, score) in enumerate(
    vector_results,
    start=1
):

    print(
        f"Rank {rank} | "
        f"Score {score:.4f} | "
        f"Page {document.metadata.get('page_label')}"
    )


# ============================================================
# 6. BM25 SEARCH
# ============================================================

tokenized_documents = [
    document.page_content.lower().split()
    for document in documents
]

bm25 = BM25Okapi(
    tokenized_documents
)

tokenized_query = (
    search_query.lower().split()
)

bm25_scores = bm25.get_scores(
    tokenized_query
)

bm25_results = sorted(
    zip(documents, bm25_scores),
    key=lambda x: x[1],
    reverse=True
)


print("\n========== BM25 SEARCH ==========")

for rank, (document, score) in enumerate(
    bm25_results[:BM25_TOP_K],
    start=1
):

    print(
        f"Rank {rank} | "
        f"Score {score:.4f} | "
        f"Page {document.metadata.get('page_label')}"
    )


# ============================================================
# 7. RRF HYBRID SEARCH
# ============================================================

rrf_scores = {}

document_lookup = {
    document.page_content: document
    for document in documents
}


# -------------------------
# Vector contribution
# -------------------------

for rank, (document, _) in enumerate(
    vector_results,
    start=1
):

    document_id = document.page_content

    rrf_scores[document_id] = (
        rrf_scores.get(document_id, 0)
        + 1 / (RRF_K + rank)
    )


# -------------------------
# BM25 contribution
# -------------------------

for rank, (document, _) in enumerate(
    bm25_results[:BM25_TOP_K],
    start=1
):

    document_id = document.page_content

    rrf_scores[document_id] = (
        rrf_scores.get(document_id, 0)
        + 1 / (RRF_K + rank)
    )


# -------------------------
# Sort RRF results
# -------------------------

hybrid_results = sorted(
    rrf_scores.items(),
    key=lambda x: x[1],
    reverse=True
)


print("\n========== HYBRID SEARCH ==========")

for rank, (document_id, score) in enumerate(
    hybrid_results,
    start=1
):

    document = document_lookup[document_id]

    print(
        f"Rank {rank} | "
        f"RRF {score:.6f} | "
        f"Page {document.metadata.get('page_label')}"
    )

    if rank >= VECTOR_TOP_K:
        break


# ============================================================
# 8. TAKE HYBRID CANDIDATES
# ============================================================

candidate_documents = [
    document_lookup[document_id]
    for document_id, _ in hybrid_results[:VECTOR_TOP_K]
]


# ============================================================
# 9. CROSS-ENCODER RERANKER
# ============================================================

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


pairs = [
    (
        search_query,
        document.page_content
    )
    for document in candidate_documents
]


reranker_scores = reranker.predict(
    pairs
)


reranked_results = sorted(
    zip(
        candidate_documents,
        reranker_scores
    ),
    key=lambda x: x[1],
    reverse=True
)


# ============================================================
# 10. SELECT FINAL DOCUMENTS
# ============================================================

final_documents = [
    document
    for document, score
    in reranked_results[:RERANK_TOP_K]
]


print("\n========== RERANKED RESULTS ==========")

for rank, (document, score) in enumerate(
    reranked_results[:RERANK_TOP_K],
    start=1
):

    print(
        f"\nRank {rank}"
    )

    print(
        f"Reranker score : {score:.4f}"
    )

    print(
        f"Source : "
        f"{document.metadata.get('source')}"
    )

    print(
        f"Page   : "
        f"{document.metadata.get('page_label')}"
    )

    print(
        f"Content: "
        f"{document.page_content[:500]}"
    )


# ============================================================
# 11. FORMAT CONTEXT FOR LLM
# ============================================================

context_parts = []

for i, document in enumerate(
    final_documents,
    start=1
):

    context_parts.append(
        f"[Source {i}]\n"
        f"{document.page_content}"
    )


context = "\n\n".join(
    context_parts
)


# ============================================================
# 12. FINAL LLM
# ============================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


answer_prompt = ChatPromptTemplate.from_template(
    """
You are a question-answering assistant.

Answer the user's question using ONLY the
provided context.

Rules:
- Do not use outside knowledge.
- If the context does not contain the answer,
  say that the information is not available
  in the provided documents.
- Cite supporting sources using [Source 1],
  [Source 2], etc.
- Do not invent source numbers.
- Keep the answer concise.

Question:
{question}

Context:
{context}
"""
)


answer_chain = answer_prompt | llm


# ============================================================
# 13. GENERATE ANSWER
# ============================================================

response = answer_chain.invoke(
    {
        "question": original_query,
        "context": context
    }
)


print("\n========== FINAL ANSWER ==========\n")

print(response.content)


# ============================================================
# 14. SOURCE METADATA
# ============================================================

print("\n========== SOURCES ==========\n")

for i, document in enumerate(
    final_documents,
    start=1
):

    print(
        f"[Source {i}] "
        f"{document.metadata.get('source')} "
        f"- Page "
        f"{document.metadata.get('page_label')}"
    )