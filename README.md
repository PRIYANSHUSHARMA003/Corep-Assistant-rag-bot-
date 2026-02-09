# Corep-Assistant-rag-bot

📘 COREP Reporting Assistant (RAG-Based Regulatory Q&A System)

A Retrieval-Augmented Generation (RAG) based assistant that answers questions about COREP regulatory reporting using local PDF documents and free open-source language models.

This system:

Extracts text from regulatory PDFs

Creates vector embeddings

Stores them using FAISS

Retrieves relevant content

Generates answers using a local HuggingFace LLM

No paid APIs required.

🚀 Features

PDF text extraction

Sentence embeddings using Sentence Transformers

FAISS vector search

Local open-source LLM (DistilGPT2)

Fully offline after initial model download

CLI based interactive assistant

🧠 Architecture
PDFs → Text Extraction → Embeddings → FAISS Index → Retriever → LLM → Answer

📁 Project Structure
corep_assistant/
│
├── assistant.py        # Main chatbot
├── ingest.py           # Extracts text from PDFs
├── embeddings.py       # Creates embeddings & FAISS index
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_data/
│   └── sample_corep.pdf

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/corep_assistant.git
cd corep_assistant

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run
Step 1: Extract Text
python ingest.py

Step 2: Create Embeddings
python embeddings.py

Step 3: Start Assistant
python assistant.py

💬 Example Usage
Ask your question: How should retained earnings be reported?

Answer:
Retained earnings should be reported as part of Common Equity Tier 1 capital,
after verification by independent auditors and after deducting foreseeable
dividends.

📦 Models Used

sentence-transformers/all-MiniLM-L6-v2

distilgpt2

Downloaded automatically from HuggingFace.

🛑 GitHub Upload Rules

Do NOT upload:

venv/
data/
docs/
faiss_index.bin
documents.pkl
.env


These files are generated after running the system.

✅ Future Improvements

Replace DistilGPT2 with Mistral or Llama2

Add web UI (Streamlit)

Chunking optimization

Answer citation display

👨‍💻 Author

Priyanshu Sharma
