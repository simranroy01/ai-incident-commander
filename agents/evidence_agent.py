from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

VECTOR_DB_PATH = "vectorstore"

def get_evidence_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    vectordb = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=OpenAIEmbeddings()
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 4}
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa

