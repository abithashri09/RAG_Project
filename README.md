# My Notes RAG

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF notes and ask questions in natural language. The application retrieves relevant information from the uploaded documents using semantic search and generates accurate answers with a local Large Language Model (LLM).

---

## Features

- Upload one or multiple PDF documents
- Extract text from PDFs automatically
- Split documents into manageable text chunks
- Semantic search using HuggingFace embeddings
- FAISS vector database for fast retrieval
- AI-powered question answering with Ollama
- Simple and interactive Streamlit interface
- Runs completely on your local machine

---

##  Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **HuggingFace Embeddings**
- **FAISS**
- **Ollama**
- **PyPDF**

---

## Project Structure

```text
my-rag-project/
│── app.py
│── create_vectorstore.py
│── requirements.txt
│── README.md
│
├── notes/
│     ├── sample1.pdf
│     └── sample2.pdf
│
├── data/
│
└── screenshots/
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/my-rag-project.git
cd my-rag-project
```

### 2. Create a virtual environment

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download Ollama and install a supported model.

```bash
ollama pull llama3
```

### 5. Create the vector database

```bash
python create_vectorstore.py
```

### 6. Run the application

```bash
streamlit run app.py
```

---

##  How It Works

1. Upload one or more PDF notes.
2. Extract text from the uploaded documents.
3. Split the text into smaller chunks.
4. Generate embeddings using HuggingFace.
5. Store embeddings in a FAISS vector database.
6. Ask questions about the uploaded notes.
7. Retrieve the most relevant document chunks.
8. Generate an AI-powered response using Ollama.

---

## Example Questions

- What is Retrieval-Augmented Generation?
- Summarize Chapter 2.
- Explain the key concepts in Unit 4.
- What are the advantages of cloud computing?
- Define machine learning.

---

## Learning Outcomes

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Document Embeddings
- LangChain Framework
- Local Large Language Models
- Streamlit Application Development

---

## Future Enhancements

- Support for Word and PowerPoint files
- Chat history
- Source citations
- Multiple embedding models
- Cloud deployment
- User authentication
- Voice-based queries

---

## Author

**Abithashri P S**

Computer Science Engineering Student

