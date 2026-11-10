from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from rank_bm25 import BM25Okapi


# ==================================================
# 1. Load Chroma
# ==================================================

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = Chroma(
    collection_name="langchain",
    persist_directory="chroma_db",
    embedding_function=embedding_model,
)


# ==================================================
# 2. Get all documents
# ==================================================

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

print(f"Total documents/chunks: {len(documents)}")


# ==================================================
# 3. Query
# ==================================================

query = (
    "What are the main evaluation metrics "
    "used for classification models?"
)


# ==================================================
# 4. VECTOR SEARCH
# ==================================================

vector_results = vector_store.similarity_search_with_score(
    query,
    k=8
)


print("\n========== VECTOR SEARCH ==========\n")

for rank, (document, score) in enumerate(
    vector_results,
    start=1
):

    print(
        f"Rank {rank} | "
        f"Score {score:.4f} | "
        f"Page {document.metadata.get('page_label')}"
    )


# ==================================================
# 5. BM25 SEARCH
# ==================================================

tokenized_documents = [
    document.page_content.lower().split()
    for document in documents
]

bm25 = BM25Okapi(tokenized_documents)

tokenized_query = query.lower().split()

bm25_scores = bm25.get_scores(tokenized_query)


bm25_results = sorted(
    zip(documents, bm25_scores),
    key=lambda x: x[1],
    reverse=True
)


print("\n========== BM25 SEARCH ==========\n")

for rank, (document, score) in enumerate(
    bm25_results[:8],
    start=1
):

    print(
        f"Rank {rank} | "
        f"Score {score:.4f} | "
        f"Page {document.metadata.get('page_label')}"
    )


# ==================================================
# 6. RRF FUNCTION
# ==================================================

def reciprocal_rank_fusion(
    vector_results,
    bm25_results,
    k=60
):

    rrf_scores = {}

    # ----------------------------------------------
    # Vector ranking contribution
    # ----------------------------------------------

    for rank, (document, _) in enumerate(
        vector_results,
        start=1
    ):

        document_id = document.page_content

        rrf_scores[document_id] = (
            rrf_scores.get(document_id, 0)
            + 1 / (k + rank)
        )


    # ----------------------------------------------
    # BM25 ranking contribution
    # ----------------------------------------------

    for rank, (document, _) in enumerate(
        bm25_results[:8],
        start=1
    ):

        document_id = document.page_content

        rrf_scores[document_id] = (
            rrf_scores.get(document_id, 0)
            + 1 / (k + rank)
        )


    return rrf_scores


# ==================================================
# 7. Calculate RRF scores
# ==================================================

rrf_scores = reciprocal_rank_fusion(
    vector_results,
    bm25_results,
    k=60
)


# ==================================================
# 8. Create document lookup
# ==================================================

document_lookup = {
    document.page_content: document
    for document in documents
}


# ==================================================
# 9. Sort by RRF score
# ==================================================

hybrid_results = sorted(
    rrf_scores.items(),
    key=lambda x: x[1],
    reverse=True
)


# ==================================================
# 10. Display Hybrid Results
# ==================================================

print("\n========== HYBRID SEARCH (RRF) ==========\n")

for rank, (document_id, score) in enumerate(
    hybrid_results[:8],
    start=1
):

    document = document_lookup[document_id]

    print(f"Rank {rank}")
    print(f"RRF score : {score:.6f}")
    print(
        f"Source    : "
        f"{document.metadata.get('source')}"
    )
    print(
        f"Page      : "
        f"{document.metadata.get('page_label')}"
    )
    print(
        f"Content   : "
        f"{document.page_content[:250]}"
    )
    print("-" * 80)