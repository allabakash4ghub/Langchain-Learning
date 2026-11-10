from sentence_transformers import CrossEncoder
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


# --------------------------------------------------
# 1. Load existing Chroma database
# --------------------------------------------------

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = Chroma(
    collection_name="langchain",
    persist_directory="chroma_db",
    embedding_function=embedding_model,
)


# --------------------------------------------------
# 2. User query
# --------------------------------------------------

query = "What are the main evaluation metrics used for classification models?"


# --------------------------------------------------
# 3. Retrieve more candidates
# --------------------------------------------------

candidates = vector_store.similarity_search_with_score(
    query,
    k=8
)


print("\n========== VECTOR SEARCH RESULTS ==========\n")

for i, (document, score) in enumerate(candidates, start=1):

    print(f"Rank {i}")
    print(f"Vector score : {score}")
    print(f"Source      : {document.metadata.get('source')}")
    print(f"Page        : {document.metadata.get('page_label')}")
    print(f"Content     : {document.page_content[:250]}")
    print("-" * 80)


# --------------------------------------------------
# 4. Load Cross-Encoder reranker
# --------------------------------------------------

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


# --------------------------------------------------
# 5. Create query-document pairs
# --------------------------------------------------

pairs = [
    (query, document.page_content)
    for document, _ in candidates
]


# --------------------------------------------------
# 6. Calculate reranker scores
# --------------------------------------------------

reranker_scores = reranker.predict(pairs)


# --------------------------------------------------
# 7. Combine documents with reranker scores
# --------------------------------------------------

reranked_results = list(
    zip(
        [document for document, _ in candidates],
        reranker_scores
    )
)


# --------------------------------------------------
# 8. Sort by reranker score
# --------------------------------------------------

reranked_results = sorted(
    reranked_results,
    key=lambda x: x[1],
    reverse=True
)


# --------------------------------------------------
# 9. Display reranked results
# --------------------------------------------------

print("\n========== RERANKED RESULTS ==========\n")

for i, (document, score) in enumerate(
    reranked_results,
    start=1
):

    print(f"Rank {i}")
    print(f"Reranker score : {score}")
    print(f"Source        : {document.metadata.get('source')}")
    print(f"Page          : {document.metadata.get('page_label')}")
    print(f"Content       : {document.page_content[:250]}")
    print("-" * 80)