import csv
import PyPDF2

# Open the PDF
with open("sample.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            # Normalize different types of quotes and replace them
            cleaned_text = page_text.replace('"', '').replace('“', '').replace('”', '').replace('"','')            
            text.extend(cleaned_text.split("."))  # Split text into sentences

# Save extracted text to CSV
with open("output.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    for line in text:
        writer.writerow([line.strip()])  # Remove leading/trailing spaces and write

print("PDF data saved to CSV successfully!")
