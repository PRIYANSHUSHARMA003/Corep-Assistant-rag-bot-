import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

CHUNKS_FOLDER = "data/chunks"
FAISS_INDEX_PATH = "faiss_index.bin"
DOCS_PATH = "documents.pkl"

print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = []

# Load all chunk files
for file in os.listdir(CHUNKS_FOLDER):
    if file.endswith(".txt"):
        with open(os.path.join(CHUNKS_FOLDER, file), "r", encoding="utf-8") as f:
            documents.append(f.read())

print(f"Loaded {len(documents)} documents")

# Create embeddings
embeddings = model.encode(documents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, FAISS_INDEX_PATH)

# Save documents
with open(DOCS_PATH, "wb") as f:
    pickle.dump(documents, f)

print("Embeddings & index created successfully!")
