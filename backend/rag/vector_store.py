import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from backend.rag.embeddings import load_embeddings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATA_PATH = os.path.join(BASE_DIR, "data")
FAISS_PATH = os.path.join(BASE_DIR, "faiss_index")

all_documents = []


# LOAD PDFs
for class_folder in os.listdir(DATA_PATH):

    class_path = os.path.join(DATA_PATH, class_folder)

    if os.path.isdir(class_path):

        for pdf_file in os.listdir(class_path):

            if pdf_file.endswith(".pdf"):

                pdf_path = os.path.join(class_path, pdf_file)

                print(f"Loading: {pdf_path}")

                loader = PyPDFLoader(pdf_path)

                documents = loader.load()

                # ADD METADATA
                for doc in documents:

                    doc.metadata["class"] = class_folder
                    doc.metadata["subject"] = pdf_file.replace(".pdf", "")

                all_documents.extend(documents)


print(f"\nLoaded {len(all_documents)} pages")


# CHUNKING
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(all_documents)

print(f"Created {len(chunks)} chunks")


# EMBEDDINGS
embeddings = load_embeddings()


# CREATE VECTOR STORE
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)


# SAVE VECTOR STORE
vectorstore.save_local(FAISS_PATH)

print("\nFAISS vector database created successfully.")