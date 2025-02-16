import chromadb

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Creates/loads DB
collection = chroma_client.get_or_create_collection(name="pdf_Fact")

results = collection.query(
    query_texts=["how many roller coasters are there in north america"],
    n_results=1
)
print(results)