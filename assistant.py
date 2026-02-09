import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# -----------------------
# Paths
# -----------------------
FAISS_INDEX_PATH = "faiss_index.bin"
DOCS_PATH = "documents.pkl"

MAX_CONTEXT_CHARS = 1500   # <<< IMPORTANT LIMIT

# -----------------------
# Load embedding model
# -----------------------
print("Loading embedding model...")
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# -----------------------
# Load FAISS index
# -----------------------
print("Loading FAISS index...")
index = faiss.read_index(FAISS_INDEX_PATH)

with open(DOCS_PATH, "rb") as f:
    documents = pickle.load(f)

# -----------------------
# Load Local LLM
# -----------------------
print("Loading HuggingFace LLM...")
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("\nCOREP Reporting Assistant\n")

# -----------------------
# Retrieve small context
# -----------------------
def retrieve_context(query, k=2):
    q_emb = embedder.encode([query])
    _, I = index.search(q_emb, k)

    text = ""
    for i in I[0]:
        text += documents[i] + "\n"

    return text[:MAX_CONTEXT_CHARS]   # <<< CUT SIZE

# -----------------------
# Ask LLM
# -----------------------
def ask_llm(question):
    context = retrieve_context(question)

    prompt = f"""
Answer the question using the context.

Context:
{context}

Question: {question}
Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"].split("Answer:")[-1].strip()

# -----------------------
# Chat Loop
# -----------------------
while True:
    question = input("Ask your question: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = ask_llm(question)
    print("\nAnswer:\n", answer)
    print("-" * 60)
