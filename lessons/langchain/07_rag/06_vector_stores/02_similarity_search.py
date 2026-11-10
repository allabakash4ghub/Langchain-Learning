from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# create an instance of Embedding Model
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small"
)

# -----------------------------------
# Documents
# -----------------------------------

texts = [
    "Employees receive 20 days of annual leave.",
    "Medical insurance covers hospitalization expenses.",
    "Customers can request a refund within 30 days."
]

#Create a vector store

vector_store = Chroma.from_texts(
    texts = texts,
    embedding = embeddings
)

# -----------------------------------
# Query
# -----------------------------------

query = "How long do I have to get my money back?"

# -----------------------------------
# Similarity Search with Scores
# -----------------------------------


results_with_scores = vector_store.similarity_search_with_score(query, k=3)

print(f"Query : {query}")

print(results_with_scores)
'''
[(Document(id='b8ecf9ef-dbf1-40b3-b41d-97e67ab8e0e0', metadata={}, 
page_content='Customers can request a refund within 30 days.'), 1.0324314832687378), 
(Document(id='89a06f7d-abf2-4f58-a7a9-63080c181d4e', metadata={}, 
page_content='Employees receive 20 days of annual leave.'), 1.5930906534194946),
(Document(id='f96bd00c-0503-41db-a6fa-5c7c77954b2e', metadata={}, 
page_content='Medical insurance covers hospitalization expenses.'), 1.646815299987793)]
'''

for document,score in results_with_scores:
    print(f"\n--- Document ---")
    print(f"Page Contents: {document.page_content}")
    print(f"Score: {score}")

results_with_vectors = vector_store.similarity_search_with_vectors(query, k=3)
print(f"results_with_vectors: {results_with_vectors}")    

'''
results_with_vectors: [(Document(id='4ad7108f-82fd-41ae-8c35-6b7b857d4146', metadata={}, page_content='Customers can request a refund within 30 days.'), array([-0.04589844,  0.06039429, -0.00857544, ..., -0.00332451,
        0.02571106,  0.00791931], shape=(1536,))), (Document(id='c8e4189b-0e91-40b5-8ebd-610dc4133cf7', metadata={}, page_content='Employees receive 20 days of annual leave.'), array([-0.01641846,  0.03283691,  0.06988525, ..., -0.02737427,
       -0.01264191,  0.01155853], shape=(1536,))), (Document(id='1b30b2ae-5c18-46fc-8250-9762974a0b0c', metadata={}, page_content='Medical insurance covers hospitalization expenses.'), array([-0.02864075, -0.02238464,  0.03204346, ...,  0.00559616,
       -0.01302338,  0.02285767], shape=(1536,)))]

'''

''' 
similarity_search_with_score()

is generally a distance value, depending on the configured collection/search space.

So conceptually:

Lower score → closer vectors → better match
Higher score → farther vectors → weaker match

'''