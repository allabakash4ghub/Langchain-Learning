"""BM25 = Best Matching 25

It is a keyword-based information retrieval algorithm.

Don't worry about the "25" too much. It refers to the particular BM25 ranking formulation; it does not mean 25 keywords or 25 documents.

BM25 answers a question like:

"How relevant is this document to my query based on the words appearing in both?"""

from pathlib import Path
from chromadb import Metadatas
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from openai import vector_stores
from rank_bm25 import BM25Okapi

# --------------------------------------------------
# 1. Load existing Chroma database
# --------------------------------------------------
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store=Chroma(
    collection_name="langchain",
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

# --------------------------------------------------
# 2. Get all documents from Chroma
# --------------------------------------------------

data=vector_store.get(
    include=["documents","metadatas"]
)

documents=[Document(page_content=text,metadata=metadata) for text,metadata in zip(data["documents"],data["metadatas"])]
print(f"Total documents/chunks: {len(documents)}")
print(f"Sample Document: {documents[1]}")


# --------------------------------------------------
# 3. User query
# --------------------------------------------------

query = "What are the main evaluation metrics used for classification models?"
#query = "What are the recommendations to deploy AI systems in industries?"

# --------------------------------------------------
# 4. Tokenize documents
# --------------------------------------------------
tokenized_documents = [
    document.page_content.lower().split() for document in documents]

# --------------------------------------------------
# 5. Create BM25 index
# --------------------------------------------------
bm25 = BM25Okapi(tokenized_documents)

print(f"type of bm25:{type(bm25)}")
# --------------------------------------------------
# 6. Tokenize query
# --------------------------------------------------

tokenized_query = query.lower().split()
print(f"tokenized_query:{tokenized_query}")

# -------------------------------------
# 7. Calculate BM25 scores
# --------------------------------------------------

scores = bm25.get_scores(tokenized_query)
print(f"type of scores : {type(scores)}")
# --------------------------------------------------
# 8. Sort documents by BM25 score
# --------------------------------------------------

ranked_results = sorted(
    zip(documents, scores),
    key=lambda x: x[1],
    reverse=True
)

# --------------------------------------------------
# 9. Display results
# --------------------------------------------------

print("\n========== BM25 RESULTS ==========\n")

for rank, (document, score) in enumerate(
    ranked_results[:8],
    start=1
):

    print(f"Rank {rank}")
    print(f"BM25 score : {score}")
    print(
        f"Source     : "
        f"{document.metadata.get('source')}"
    )
    print(
        f"Page       : "
        f"{document.metadata.get('page_label')}"
    )
    print(
        f"Content    : "
        f"{document.page_content[:300]}"
    )
    print("-" * 80)