import sqlite3
import os

DB_PATH = "db/incidents.db"

def init_db():
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            domain TEXT,
            service TEXT,
            severity TEXT,
            duration_minutes INTEGER,
            incident_type TEXT
        )
    """)


    conn.commit()
    conn.close()
    print("Incident database initialized")

if __name__ == "__main__":
    init_db()
