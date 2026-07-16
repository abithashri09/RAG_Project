import os
import streamlit as st
from pypdf import PdfReader

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="My Notes RAG",
    page_icon="📚",
    layout="wide"
)

st.title("📚 My Notes RAG")
st.write("Ask questions about your PDF notes!")


# ------------------------------------------------
# LOAD PDF FILES
# ------------------------------------------------

pdf_folder = "data"

pdf_files = sorted([
    f for f in os.listdir(pdf_folder)
    if f.endswith(".pdf")
])


# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.title("📂 My Notes")

    st.caption("Browse your uploaded PDF notes.")

    st.metric("Total PDFs", len(pdf_files))

    st.divider()

    st.subheader("📄 PDFs Found")

    if pdf_files:
        for pdf in pdf_files:
            st.success(pdf)
    else:
        st.warning("No PDFs Found")

    st.divider()

    st.subheader("📖 PDF Preview")

    for pdf in pdf_files:

        pdf_path = os.path.join(pdf_folder, pdf)

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + " "

        clean_text = " ".join(text.split())

        with st.expander(pdf):
            st.write(clean_text[:600] + "...")


# ------------------------------------------------
# LOAD EMBEDDING MODEL
# ------------------------------------------------

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ------------------------------------------------
# LOAD VECTOR DATABASE
# ------------------------------------------------

db = FAISS.load_local(
    "vectorstore",
    embedding,
    allow_dangerous_deserialization=True
)


# ------------------------------------------------
# LOAD OLLAMA
# ------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# ------------------------------------------------
# ASK QUESTION
# ------------------------------------------------

st.header("🤖 Ask Your Notes")

question = st.text_input(
    "Enter your question",
    placeholder="Example: What is User Interface?"
)


if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        docs = db.similarity_search(question, k=3)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are an AI assistant.

Answer ONLY using the information below.

If the answer is not found, say:

'I couldn't find that information in your notes.'

Notes:
{context}

Question:
{question}

Answer:
"""

        with st.spinner("Generating Answer..."):

            response = llm.invoke(prompt)

        st.success("Answer Generated")

        st.subheader("🤖 AI Answer")

        st.write(response.content)

        with st.expander("📄 Source Chunks", expanded=True):

            for i, doc in enumerate(docs, start=1):

                source_text = " ".join(doc.page_content.split())

                st.markdown(f"### 📄 Chunk {i}")

                st.write(source_text)

                st.text_area(
                    label=f"Source {i}",
                    value=source_text,
                    height=180,
                    disabled=True,
                    key=f"chunk_{i}"
                )

        st.divider()