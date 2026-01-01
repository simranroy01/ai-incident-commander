from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient
from langchain_openai import ChatOpenAI

client = MongoClient("mongodb://localhost:27017/")
db = client["incident_memory"]
collection = db["history"]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def store_memory(query, answer):
    summary_prompt = f"""
    Summarize this interaction in one sentence for future incident reference.

    Query: {query}
    Answer: {answer}
    """

    summary = llm.invoke(summary_prompt).content
    collection.insert_one({"summary": summary})

def retrieve_memory():
    memories = collection.find().limit(5)
    return [m["summary"] for m in memories]
