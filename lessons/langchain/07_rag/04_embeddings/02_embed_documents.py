''' embed_query() vs embed_documents()
embed_query() --> Used for a single search query:
embed_documents() -->Used for multiple documents/chunks:
'''
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model= "text-embedding-3-small"
)

texts = [
    "LangChain is used to build LLM applications.",
    "RAG retrieves relevant information from documents.",
    "Embeddings convert text into numerical vectors."
]

vectors = embeddings.embed_documents(texts)

print(f"Number of documents/texts: {len(texts)}")
print(f"Number of vectors: {len(vectors)}")
print(f"Length of each vector: {len(vectors[0])}")
print(f"Type of vectors: {type(vectors)}")
print(f"Vectors: {vectors}")

for i, vector in enumerate(vectors):
    print(f"vector length for document {i+1}: {len(vector)}")
    print(f"Vector for document {i+1}: {vector[1:4]}")  # Displaying a slice of the vector for brevity