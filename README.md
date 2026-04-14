# 🧠 Agentic RAG with MongoDB & HuggingFace

A hands-on implementation of an **Agentic Retrieval-Augmented Generation (RAG)** system that intelligently decides when to retrieve information before generating responses — built using **MongoDB Atlas Vector Search, HuggingFace models, and Streamlit UI**.

---

## 🚀 Overview

This project explores how modern AI systems work beyond simple API calls by building a **decision-based RAG pipeline**:
DECIDE → RETRIEVE → GENERATE


Instead of always retrieving documents, the system first determines whether external knowledge is required — making it more efficient and realistic.

---

## 🏗️ Architecture
User Query
↓
Decision Node (Rule-based)
↓
YES → Vector Search (MongoDB)
NO → Skip Retrieval
↓
Context Building
↓
LLM (HuggingFace)
↓
Final Answer


---

## 🔍 Features

- 🧠 Agentic Workflow (Decision-based RAG)
- 📦 MongoDB Atlas Vector Search
- 🔎 Semantic Retrieval using Embeddings
- 🤖 HuggingFace Models (No Paid APIs)
- 💻 Streamlit UI for interaction
- ⚡ Fully local and cost-efficient setup

---

## 🛠️ Tech Stack

- Python  
- MongoDB Atlas (Vector Database)  
- Sentence Transformers (HuggingFace)  
- Transformers  
- Streamlit  

---

## 📂 Project Structure
RAGmongodemo/
│── app.py # Streamlit UI
│── requirements.txt # Dependencies
│── rag.ipynb # Development notebook
│── .env.example # Environment variable template
│── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/RAGmongodemo.git
cd RAGmongodemo

🧠 How It Works
1. Data Processing
Load PDF documents
Split into chunks
Convert into embeddings
2. Vector Storage
Store embeddings in MongoDB
Create vector index
3. Retrieval
Convert query → embedding
Perform semantic search
Retrieve top-k documents
4. Generation
Combine retrieved context
Pass to LLM
Generate final answer

Query: "What is MongoDB AI program?"

→ Decision: Retrieval needed  
→ Vector Search: Top 3 documents  
→ LLM: Generates final answer  

🚧 Challenges Faced
Managing dependency conflicts (LangChain + HuggingFace)
Handling embedding generation efficiently
Debugging MongoDB vector search queries
Structuring an agentic workflow
📈 Future Improvements
Replace rule-based decision with LLM-based reasoning
Improve UI (chat-style interface)
Add document upload feature
Optimize retrieval accuracy (reranking)
🎯 Key Learnings
How embeddings represent semantic meaning
How vector databases enable similarity search
How RAG pipelines work in real-world systems
Importance of modular AI architecture


🤝 Contributing

Feel free to fork this repo and experiment with your own improvements!

⭐ Acknowledgment

This project was built as part of my learning journey into RAG systems, vector databases, and agentic AI workflows.

📬 Connect

If you found this useful, feel free to connect or give a ⭐ to the repo!