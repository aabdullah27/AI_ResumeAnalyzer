import streamlit as st
import os
import tempfile
import faiss
from llama_index.core import VectorStoreIndex, Document
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.core import Settings  # Import Settings directly
from pypdf import PdfReader
from docx import Document as DocxDocument

# Set up Streamlit page
st.set_page_config(page_title="Resume Analyzer 📝", layout="wide")
st.title("Resume Analyzer 📝")

# Sidebar for API key input
with st.sidebar:
    st.header("Configuration ⚙️")
    groq_api_key = st.text_input("Enter your Groq API Key 🔑", type="password")

    # File uploader
    uploaded_file = st.file_uploader("Upload your resume (PDF, DOCX, or TXT) 📄", type=["pdf", "docx", "txt"])

    analyze_button = st.button("Analyze Resume 🔍")

# Main content area
if not groq_api_key:
    st.warning("⚠️ Please enter your Groq API key in the sidebar.")
elif not uploaded_file:
    st.warning("⚠️ Please upload a resume file in the sidebar.")
elif analyze_button:
    with st.spinner("Analyzing your resume... ⏳"):
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name

        # Extract text from the file
        if uploaded_file.type == "application/pdf":
            pdf_reader = PdfReader(temp_file_path)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = DocxDocument(temp_file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:  # Assume it's a text file
            with open(temp_file_path, 'r') as file:
                text = file.read()

        # Clean up the temporary file
        os.unlink(temp_file_path)

        # Set up RAG components
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")
        Settings.embed_model = embed_model  # Set the embedding model in the Settings

        # Create a FAISS index
        d = 768  # Dimension (you can adjust this based on your embedding model)
        faiss_index = faiss.IndexFlatL2(d)

        # Create the FAISS vector store
        vector_store = FaissVectorStore(faiss_index=faiss_index)

        # Initialize the Groq model with an appropriate model name
        groq_model_name = "gemma2-9b-it"  # Replace with the actual model name you want to use
        llm = Groq(api_key=groq_api_key, model=groq_model_name)

        # Set the embedding model in Settings directly
        Settings.llm = llm

        # Create documents and index
        documents = [Document(text=text)]
        index = VectorStoreIndex.from_documents(
            documents,
            vector_store=vector_store
        )

        # Query the index
        query_engine = index.as_query_engine()
        response = query_engine.query(
            '''Based on this resume, please provide the top 3 job titles or roles that would be most suitable for this candidate, without any explanations.
               Ensure that the titles are listed in order of suitability, using numbering (1., 2., 3.). 
               Additionally, specify the industry or sector the candidate is targeting, such as technology, finance, healthcare, or marketing, to refine the suggestions.
            '''
        )

        # Display results
        st.header("Suitable Job Titles 🎯")
        st.write(response.response)

st.sidebar.markdown("---")
st.sidebar.markdown("Created with Streamlit, LlamaIndex, FAISS, and Groq 💡 By ABDULLAH 🗿")
