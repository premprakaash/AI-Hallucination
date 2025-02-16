import csv
import PyPDF2
import chromadb

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Creates/loads DB
# collection = chroma_client.get_or_create_collection(name="pdf_collection")
collection = chroma_client.get_or_create_collection(name="pdf_Fact")

# Step 1: Extract text from PDF
with open("facts.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    text = []
    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            cleaned_text = page_text.replace('"', '').replace('“', '').replace('”', '')
            sentences = cleaned_text.split(".")  # Split text into sentences
            
            # Step 2: Save extracted text to CSV
            text.extend([(f"Page {page_num+1}", sentence.strip()) for sentence in sentences if sentence.strip()])

# Step 3: Save extracted text to CSV
with open("outputfact.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Page", "Text"])  # Header
    writer.writerows(text)  # Write all extracted text

print("PDF data saved to CSV successfully!")

# Step 4: Store data in ChromaDB
for i, (page, sentence) in enumerate(text):
    collection.add(
        ids=[f"doc_{i}"],
        metadatas=[{"page": page}],
        documents=[sentence]
    )

print("CSV data stored in ChromaDB successfully!")

results = collection.query(
    query_texts=["sample"],
    n_results=1
)

