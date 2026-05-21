# OCR-Based NCERT AI Doubt Solver

An AI-powered educational assistant that solves NCERT textbook doubts using OCR, RAG, vector databases, and LLMs.

---

# Features

- 📖 NCERT textbook question answering
- 🖼️ OCR-based image doubt solving
- 💬 Conversational AI tutor
- 🔍 Semantic search using FAISS
- 🧠 RAG-based contextual answering
- 🎯 Class and subject filtering
- ⚡ Streamlit interactive UI

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- Python
- LangChain

## Vector Database
- FAISS

## Embeddings
- sentence-transformers/all-MiniLM-L6-v2

## OCR
- Moondream

## LLM
- Gemma2 via Ollama

---

# Architecture

Image/Text Input
↓
OCR Extraction
↓
RAG Retrieval
↓
FAISS Vector Search
↓
Gemma2 LLM
↓
AI Tutor Response

---

# Installation

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

# Future Improvements

- Voice input
- Multi-language support
- Cloud deployment
- Faster retrieval
- Better OCR preprocessing

---

# Author

Deeptimayee Behera
