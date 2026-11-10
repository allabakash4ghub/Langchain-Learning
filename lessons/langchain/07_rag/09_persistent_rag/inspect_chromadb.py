import chromadb

client = chromadb.PersistentClient(
    path=r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\09_persistent_rag\data\chroma_db"
)

collections = client.list_collections()

print(f"collections:{collections}")
print(f"collections structure:{dir(collections[0])}")

print(f"type of collections[0] : {type(collections[0])}")

print(f"useful public API details of collections[0]")
for item in dir(collections[0]):
    if not item.startswith("_"):
        print(item)

alldata = collections[0].get(
        include=["documents", "metadatas"]
    )

print(f"all keys under :{alldata.keys()}")        

for collection in collections:
    print("Collection:", collection.name)

    data = collection.get(
        include=["documents", "metadatas"]
    )

    print("Number of records:", len(data["documents"]))

    for i, doc in enumerate(data["documents"]):
        print(f"\n--- Chunk {i} ---")
        print(doc)
        print("Metadata:", data["metadatas"][i])