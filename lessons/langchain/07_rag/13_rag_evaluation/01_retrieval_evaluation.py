# ============================================================
# RAG Retrieval Evaluation
# Precision@K, Recall@K and MRR
# ============================================================


# ------------------------------------------------------------
# Evaluation dataset
# ------------------------------------------------------------

evaluation_data = [

    {
        "question": "What metrics are used for classification?",
        "relevant_documents": {"D3"},
        "retrieved_documents": ["D8", "D2", "D3", "D7", "D9"]
    },

    {
        "question": "What is F1-score?",
        "relevant_documents": {"D3"},
        "retrieved_documents": ["D3", "D5", "D8", "D2", "D9"]
    },

    {
        "question": "How should imbalanced classification be evaluated?",
        "relevant_documents": {"D3"},
        "retrieved_documents": ["D5", "D8", "D3", "D9", "D2"]
    }
]


# ------------------------------------------------------------
# Precision@K
# ------------------------------------------------------------

def precision_at_k(retrieved_documents, relevant_documents, k):

    top_k = retrieved_documents[:k]

    relevant_retrieved = sum(
        1
        for document in top_k
        if document in relevant_documents
    )

    return relevant_retrieved / k


# ------------------------------------------------------------
# Recall@K
# ------------------------------------------------------------

def recall_at_k(retrieved_documents, relevant_documents, k):

    top_k = retrieved_documents[:k]

    relevant_retrieved = sum(
        1
        for document in top_k
        if document in relevant_documents
    )

    return relevant_retrieved / len(relevant_documents)


# ------------------------------------------------------------
# Reciprocal Rank
# ------------------------------------------------------------

def reciprocal_rank(retrieved_documents, relevant_documents):

    for rank, document in enumerate(
        retrieved_documents,
        start=1
    ):

        if document in relevant_documents:

            return 1 / rank

    return 0


# ------------------------------------------------------------
# Evaluate each question
# ------------------------------------------------------------

precision_scores = []
recall_scores = []
rr_scores = []


for item in evaluation_data:

    question = item["question"]

    relevant_documents = item["relevant_documents"]

    retrieved_documents = item["retrieved_documents"]

    precision = precision_at_k(
        retrieved_documents,
        relevant_documents,
        k=5
    )

    recall = recall_at_k(
        retrieved_documents,
        relevant_documents,
        k=5
    )

    rr = reciprocal_rank(
        retrieved_documents,
        relevant_documents
    )

    precision_scores.append(precision)

    recall_scores.append(recall)

    rr_scores.append(rr)

    print("\n" + "=" * 70)

    print("QUESTION:")
    print(question)

    print("\nRelevant documents:")
    print(relevant_documents)

    print("\nRetrieved documents:")
    print(retrieved_documents)

    print("\nPrecision@5:", precision)

    print("Recall@5:", recall)

    print("Reciprocal Rank:", rr)


# ------------------------------------------------------------
# Calculate averages
# ------------------------------------------------------------

precision_at_5 = sum(precision_scores) / len(
    precision_scores
)

recall_at_5 = sum(recall_scores) / len(
    recall_scores
)

mrr = sum(rr_scores) / len(
    rr_scores
)


# ------------------------------------------------------------
# Final results
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("OVERALL RETRIEVAL EVALUATION")
print("=" * 70)

print(
    "Average Precision@5:",
    precision_at_5
)

print(
    "Average Recall@5:",
    recall_at_5
)

print(
    "MRR:",
    mrr
)