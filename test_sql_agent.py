from agents.sql_agent import get_sql_agent

agent = get_sql_agent()

query = "How many payment incidents happened in 2024?"
result = agent.invoke(query)

print(result)
