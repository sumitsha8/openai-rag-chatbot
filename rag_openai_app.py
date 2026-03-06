import os
import pdfplumber
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# OpenAI
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# -------------------
# Environment Variables
# -------------------
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
FAISS_DIR = os.environ.get("FAISS_DIR", ".faiss_index")

# -------------------
# Streamlit UI
# -------------------
st.header("📄 DevMagic Bot")

with st.sidebar:
    st.title("DevMagic Bot")

    load_existing = st.checkbox("Load Existing FAISS Index", value=True)
    rebuild_index = st.checkbox("Rebuild Index From Uploaded PDF")

    file = st.file_uploader("Upload PDF (only needed if rebuilding)", type="pdf")
    st.caption(f"FAISS directory: `{FAISS_DIR}`")

# -------------------
# Step 1: Load FAISS index (Cheap: No embedding)
# -------------------
vector_store = None

if load_existing:
    if os.path.isdir(FAISS_DIR):
        try:
            embeddings_loader = OpenAIEmbeddings(
                model="text-embedding-3-small",
                openai_api_key=OPENAI_API_KEY
            )
            vector_store = FAISS.load_local(
                FAISS_DIR,
                embeddings_loader,
                allow_dangerous_deserialization=True
            )
            st.success("Loaded existing FAISS index (no cost).")
        except Exception as e:
            st.error(f"Failed to load FAISS index: {e}")
    else:
        st.warning("No FAISS index found. Upload PDF + enable Rebuild Index.")

# -------------------
# Step 2: Rebuild Index 
# -------------------
if rebuild_index and file is not None:
    if not OPENAI_API_KEY:
        st.error("Missing OPENAI_API_KEY environment variable.")
        st.stop()

    st.warning("⚠️ Rebuilding the index will use OpenAI embedding tokens.")

    # Extract PDF text
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)

    # Embeddings 
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY
    )

    # Build FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)
    os.makedirs(FAISS_DIR, exist_ok=True)
    vector_store.save_local(FAISS_DIR)

    st.success(f"Rebuilt FAISS index ({len(chunks)} chunks). Saved to {FAISS_DIR}")

# -------------------
# Step 3: Stop if no index exists
# -------------------
if vector_store is None:
    st.info("Load an index or rebuild one from a PDF.")
    st.stop()

# -------------------
# Step 4: Build RAG chain (Cheap: uses gpt‑4o-mini)
# -------------------
def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 4})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    max_tokens=600,
    openai_api_key=OPENAI_API_KEY
)

prompt = ChatPromptTemplate.from_messages([
    ("system",
        "You are a helpful assistant answering questions about a PDF document and PDF is about to dix development enviornment and keep stable for developers.\n\n"
        "Guidelines:\n"
        "1. Provide complete, well-explained answers using the context below.\n"
        "2. Include relevant details, numbers, and explanations to give a thorough response.\n"
        "3. If the context mentions related information, include it to give fuller picture.\n"
        "4. Only use information from the provided context - do not use outside knowledge.\n"
        "5. Summarize long information, ideally in bullets where needed\n"
        "6. If the information is not in the context, say so politely.\n\n"
        "Context:\n{context}"),
    ("human", "{question}")
])

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()} 
    | prompt 
    | llm 
    | StrOutputParser()
)

# -------------------
# Step 5: User asks a question
# -------------------
question = st.text_input("Ask a question to fix development enviornment")

if question:
    response = chain.invoke(question)
    st.write(response)
