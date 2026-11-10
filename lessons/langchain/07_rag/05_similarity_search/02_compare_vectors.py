import math

def cosine_similarity(vector_a,vector_b):
    dot_product = sum(a*b for a,b in zip(vector_a, vector_b))
    magnitude_a = math.sqrt(sum(a**2 for a in vector_a))
    magnitude_b = math.sqrt(sum(b**2 for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)

documents = {
    "Annual Leave policy": [0.2, 0.4],
    "Medical Insurance": [0.1, 0.5],
    "Refund policy": [0.3, 0.6]
}

query_vector = [0.15, 0.45]

results = []
for document, vector in documents.items():
    similarity_score = cosine_similarity(query_vector, vector)
    results.append((document, similarity_score))

print("\nSimilarity Results:\n")
for document, score in results:
    print(f"Document: {document}, Similarity Score: {score:.4f}")

print("\nSorted Results (by similarity score):\n")
sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
for document, score in sorted_results:
    print(f"Document: {document}, Similarity Score: {score:.4f}")

print(results)    
print(type(results))