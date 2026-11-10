import chromadb

client = chromadb.PersistentClient(
    path=r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\09_persistent_rag\data\chroma_db"
)

collections = client.list_collections()

print("Number of collections:", len(collections))

for collection in collections:
    print("Collection:", collection.name)