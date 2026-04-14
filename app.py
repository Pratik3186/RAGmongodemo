from pymongo import MongoClient
import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load env
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
collection = client["sample_mflix"]["RAGpdf"]

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

# 🔥 ADD THIS FUNCTION
def get_query_results(query):
    query_embedding = embeddings.embed_query(query)

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": query_embedding,
                "numCandidates": 100,
                "limit": 3
            }
        },
        {
            "$project": {
                "text": 1,
                "_id": 0
            }
        }
    ]

    results = list(collection.aggregate(pipeline))
    return results

import streamlit as st

# Your existing functions
# make sure these are imported or present:
# - get_query_results()
# - embeddings / MongoDB setup

from transformers import pipeline

# Load LLM (only once)
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="google/flan-t5-small",
        max_new_tokens=200,
        device=-1
    )

llm = load_model()

# ---------------- UI ----------------
st.set_page_config(page_title="RAG App", layout="wide")

st.title("🧠 Agentic RAG with MongoDB + HuggingFace")

query = st.text_input("Ask a question:")

if st.button("Submit") and query:

    with st.spinner("Retrieving and generating answer..."):

        # Retrieve documents
        context_docs = get_query_results(query)

        context_string = " ".join([doc["text"] for doc in context_docs])

        # Prompt
        prompt = f"""
        Answer the question using ONLY the context below.
        If not found, say "I don't know".

        Context:
        {context_string}

        Question:
        {query}
        """

        # Generate answer
        response = llm(prompt)
        answer = response[0]["generated_text"].replace(prompt, "")

    st.subheader("✅ Answer")
    st.write(answer)

    st.subheader("📄 Retrieved Documents")
    for doc in context_docs:
        st.write(doc["text"])