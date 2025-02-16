import chromadb

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Uses local storage

# Create or get a collection
collection = chroma_client.get_or_create_collection(name="my_collection")

# Add data (id + metadata)
# collection.add(
#     ids=["1", "2"],
#     documents=["Hello world", "This is a test document"],
#     metadatas=[{"category": "greeting"}, {"category": "test"}]
# )

# Query the collection
results = collection.query(
    query_texts=["world"],
    n_results=1
)

print(results)