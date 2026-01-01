from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType

DB_URI = "sqlite:///db/incidents.db"

def get_sql_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    db = SQLDatabase.from_uri(DB_URI)

    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
