import fitz
import os

PDF_FOLDER = "data/raw_pdfs"
OUTPUT_FOLDER = "data/extracted_text"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_text(pdf_name):
    path = os.path.join(PDF_FOLDER, pdf_name)
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

files = [
    "pra_own_funds.pdf",
    "corep_instructions.pdf",
    "crr.pdf"
]

for file in files:
    content = extract_text(file)
    out_file = file.replace(".pdf", ".txt")
    with open(os.path.join(OUTPUT_FOLDER, out_file), "w", encoding="utf-8") as f:
        f.write(content)

print("Text extraction completed!")
