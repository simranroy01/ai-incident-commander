from graph import app

def main():
    print("AI Incident Commander")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nIncident Query: ")

        if query.lower() == "exit":
            break

        result = app.invoke({"query": query})

        print("\nResponse:")
        print(result["response"])

if __name__ == "__main__":
    main()
