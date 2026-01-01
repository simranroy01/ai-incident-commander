import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = "data/incident_reports"
VECTOR_DB_PATH = "vectorstore"

def ingest_incidents():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".md"):
            loader = TextLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=120
    )

    chunks = splitter.split_documents(documents)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()

    print(f"Ingested {len(chunks)} incident chunks")

if __name__ == "__main__":
    ingest_incidents()
