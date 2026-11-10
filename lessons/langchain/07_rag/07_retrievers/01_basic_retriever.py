'''
A retriever in LangChain is an interface that takes a text query and returns a list of 
relevant documents. [1] (https://docs.langchain.com/oss/javascript/integrations/retrievers)
What a Retriever Does - Acts as a bridge between a user's question and external data sources.
Accepts a string query as input. Outputs a list of text objects (Document objects) containing 
the matching information and metadata.
Follows LangChain's standard Runnable interface, making it easy to plug into chains and 
RAG (Retrieval-Augmented Generation) workflows. [1] (https://medium.com/@adatiyavinayshaileshbhai/retrievers-in-langchain-the-art-of-finding-the-right-stuff-732dea9f0e9b), [2] (https://www.geeksforgeeks.org/artificial-intelligence/retrieval-in-langchain/), [3] (https://medium.com/@ravi0dubey/retrievers-in-langchain-88d42e0a2ace), [4] (https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever), [5] (https://docs.langchain.com/oss/javascript/integrations/retrievers)Retriever vs. Vector StoreVector Store: A database that stores and indexes data using mathematical vectors (embeddings). It requires the ability to store and write data. [1] (https://www.comet.com/site/blog/retrieval-part-3-langchain-retrievers/), [2] (https://www.geeksforgeeks.org/artificial-intelligence/retrieval-in-langchain/)Retriever: A broader interface. It only needs to return documents, not necessarily store them. [1] (https://docs.langchain.com/oss/javascript/integrations/retrievers)While vector stores can be turned into retrievers (using methods like .as_retriever()),
a retriever can also fetch data from search APIs, SQL databases, or Wikipedia without being a vector store itself. [1] (https://www.youtube.com/watch?v=uGjJhCYgaxs&t=11), [2] (https://www.youtube.com/watch?v=Yg3klzw9tyY), [3] (https://docs.langchain.com/oss/javascript/integrations/retrievers)Common Types of RetrieversVector Store Retriever: Fetches chunks using basic similarity search or Maximal Marginal Relevance (MMR) from a vector database.
Multi-Query Retriever: Uses a large language model to rewrite a single user question into multiple variations to improve search coverage.Parent Document Retriever: Searches through small text chunks for accuracy, but returns the larger parent document for richer context.Self-Query Retriever: Translates natural language into metadata filters and keyword queries automatically

'''

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma 

load_dotenv()

# create en embedding model instance 
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

# vector store instance
vector_store =Chroma.from_texts(
    texts =texts,
    embedding = embeddings
)

# create a retriever instance from the vector store
retriever = vector_store.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k": 2}
)

# -----------------------------------
# Query
# -----------------------------------

query = "How long do I have to get my money back?"

# -----------------------------------
# Retrieve relevant documents
# -----------------------------------

results =retriever.invoke(query)

# -----------------------------------
# Print results
# -----------------------------------

print("Query:")
print(query)

print("\nRetrieved Documents:")

print(f"Number of results found: {len(results)}")
print(f"Results: {results}")
print(f"Type of results: {type(results)}")

'''
Results: [Document(id='db7c19c7-2553-4171-bf47-8e44cfdc7263', metadata={}, page_content='Customers can request a refund within 30 days.'), Document(id='f00645c4-f6ca-4668-aa7f-8bdd302b3f99', metadata={}, page_content='Employees receive 20 days of annual leave.')]
Type of results: <class 'list'>

'''

print("\nRetrieved Documents:")

for i, document in enumerate(results):

    print(f"\n--- Document {i + 1} ---")

    print(document.page_content)

    print("\nMetadata:")
    print(document.metadata)

'''
search_type="similarity"  : Finds the absolute closest matches to your query.
Converts the query to a vector and returns the top (K) documents with the highest semantic similarity score
Best Used For - Direct, factual questions where the answer likely sits within a few heavily redundant chunks

search_type="mmr" (Maximal Marginal Relevance) : Balances relevance to the query with diversity among the results.
Fetches a larger pool of candidate documents first, then iteratively selects texts that are close to the query but different from already selected texts.
Best Used For - Summarization, research, or open-ended queries where you want a broad overview and want to avoid duplicate information.

A Quick Analogy
Imagine you ask for recommendations on "the best sci-fi movies":
similarity might give you: Star Wars Episode IV, Star Wars Episode V, and Star Wars Episode VI. 
(Highly accurate, but highly redundant).
mmr might give you: Star Wars Episode IV, The Matrix, and Interstellar. 
(Still highly accurate, but gives you a much wider variety of perspectives).

| Vector Store                                | Retriever                          |
| ------------------------------------------- | ---------------------------------- |
| Stores vectors                              | Retrieves relevant documents       |
| Provides storage/search operations          | Provides a retrieval interface     |
| `similarity_search()`                       | `invoke()`                         |
| Can expose vector-store-specific operations | Uses a more standardized interface |

'''
