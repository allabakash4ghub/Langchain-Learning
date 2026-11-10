'''Before using a Vector Store, let's manually understand what happens in cosine similarity
'''
import math

def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = math.sqrt(sum(a ** 2 for a in vector_a))
    magnitude_b = math.sqrt(sum(b ** 2 for b in vector_b))
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    
    return dot_product / (magnitude_a * magnitude_b)

vector_1 = [0.2, 0.4]
vector_2 = [0.1, 0.5]

similarity = cosine_similarity(vector_1, vector_2)
print(f"Cosine Similarity: {similarity}")