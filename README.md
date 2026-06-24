# 🤖 PDF RAG Chatbot using Gemini API & Streamlit

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about a PDF document through an interactive Streamlit web interface.

The chatbot retrieves the most relevant information from the PDF using semantic search and then uses Google's Gemini API to generate accurate, context-aware responses.

This project demonstrates the complete RAG workflow, including document processing, embedding generation, vector search, and LLM-powered answer generation.

---

## Features

✅ Interactive Streamlit chat interface

✅ PDF-based question answering

✅ Semantic search using embeddings

✅ FAISS vector database for fast retrieval

✅ Gemini API for response generation

✅ Cached document processing for improved performance

✅ Beginner-friendly implementation without LangChain

---

## Tech Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Frontend        | Streamlit             |
| LLM             | Gemini API            |
| Embeddings      | Sentence Transformers |
| Vector Database | FAISS                 |
| PDF Processing  | PyPDF                 |
| Language        | Python                |

---

## Project Structure

```text
chatbot/
│
├── data/
│   └── notes.pdf
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd chatbot
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install streamlit
pip install google-genai
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
pip install numpy
```

---

## Getting a Gemini API Key

1. Visit Google AI Studio.
2. Create an API key.
3. Copy the generated API key.
4. Replace the placeholder value inside `app.py`.

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

---

## Running the Application

Place your PDF file inside the `data` folder:

```text
data/notes.pdf
```

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

Default URL:

```text
http://localhost:8501
```

---

## How It Works

### Step 1: PDF Extraction

The chatbot extracts text from the PDF document using PyPDF.

### Step 2: Text Chunking

The extracted text is divided into smaller chunks for efficient retrieval.

### Step 3: Embedding Generation

Sentence Transformers converts each chunk into vector embeddings.

### Step 4: Vector Storage

Embeddings are stored in a FAISS vector index.

### Step 5: Query Processing

When a user asks a question:

* The query is converted into an embedding.
* FAISS retrieves the most relevant chunks.
* Retrieved chunks are combined into context.

### Step 6: Response Generation

The context and user query are sent to Gemini, which generates a final answer.

---

## RAG Pipeline

```text
User Question
       │
       ▼
Query Embedding
       │
       ▼
FAISS Similarity Search
       │
       ▼
Relevant Chunks Retrieved
       │
       ▼
Gemini API
       │
       ▼
Generated Response
       │
       ▼
Displayed in Streamlit UI
```

---

## Example Use Cases

* Academic Notes Q&A
* Research Paper Assistant
* Technical Documentation Search
* Company Knowledge Base
* Study Material Chatbot

---

## Future Improvements

* Upload PDFs dynamically
* Multiple PDF support
* Chat history persistence
* Conversation memory
* ChromaDB integration
* LangChain integration
* Hybrid search
* Source citations
* Agentic RAG workflows

---

## Learning Outcomes

This project helped me understand:

* Retrieval-Augmented Generation (RAG)
* Text Chunking Strategies
* Embeddings and Semantic Search
* Vector Databases (FAISS)
* Prompt Engineering
* Gemini API Integration
* Streamlit Application Development
* End-to-End AI Application Building

---

## Author

**Suminder Singh**

B.Tech Computer Science Engineering

Aspiring Data Analyst | Machine Learning Enthusiast | Generative AI Learner

---

## License

This project is open-source and available under the MIT License.
