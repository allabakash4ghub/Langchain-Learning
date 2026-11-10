from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()
# create a instance of OpenAIEmbeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
# -----------------------------------
# Documents we want to store
# -----------------------------------

texts = [
    "Employees receive 20 days of annual leave.",
    "Medical insurance covers hospitalization expenses.",
    "Customers can request a refund within 30 days."
]

# -----------------------------------
# Create the Vector Store
# -----------------------------------

vector_store =Chroma.from_texts(
    texts = texts,
    embedding = embeddings
)

print("Vector Store created successfully!") 
print("Type of vector_store:", type(vector_store))
print("Number of documents in vector_store:", len(vector_store._collection.get(include=["metadatas"])["metadatas"]))
print("metadata:",vector_store._collection.get(include=["metadatas"])["metadatas"])  # Print the metadata of each document
print(vector_store)

# -----------------------------------
# User Query
# -----------------------------------

query = "How long do I have to get my money back?"


# -----------------------------------
# Similarity Search
# -----------------------------------

results = vector_store.similarity_search(query)  # Here we can pass the k to control the number of results returned, default is 4
results2 = vector_store.similarity_search(query, k=2)  # Here we can pass the k to control the number of results returned, default is 4
# -----------------------------------
# Print Results
# -----------------------------------

print("Number of results found:", len(results))
print(results)

'''results output as follows:
[Document(id='90327a74-1a2a-4531-a4ce-e609f5a05c43', metadata={}, 
page_content='Customers can request a refund within 30 days.'), 
Document(id='5e25dfc6-985d-4542-ad0d-ba82b0b423f5', metadata={}, 
page_content='Employees receive 20 days of annual leave.'), 
Document(id='716f729f-e008-4c5a-bead-afb1a2aec34d', metadata={}, 
page_content='Medical insurance covers hospitalization expenses.')]
'''

for document in results:
    print("\n--- Document ---")
    print("Page Contents:", document.page_content)
    print("Metadata:", document.metadata)

print("Number of results found with k=2:", len(results2))
for document in results2:
    print("\n--- Document ---")
    print("Page Contents:", document.page_content)
    print("Metadata:", document.metadata)

print(f"Type of results:", type(results))    
print(f"Type of results elements:", type(results[0]))    

'''Here the similarity_search() gives you the matching Document objects, but not the scores.
For getting the scores along with the Dcouement objects , we can use the similarity_search_with_score()'''