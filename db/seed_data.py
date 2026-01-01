import sqlite3

DB_PATH = "db/incidents.db"

INCIDENTS = [
    ("2024-03-22", "payment", "payment-db", "High", 41, "db_timeout"),
    ("2024-06-09", "payment", "payment-api", "High", 27, "deploy_bug"),
    ("2024-09-17", "payment", "payment-api", "Medium", 54, "rate_limit"),
    ("2024-11-04", "payment", "payment-cache", "Medium", 33, "cache_failure"),
    ("2025-01-08", "payment", "payment-api", "Medium", 46, "latency_regression")
]

def seed_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO incidents (date, domain, service, severity, duration_minutes, incident_type)
                       VALUES (?, ?, ?, ?, ?, ?)
    """, INCIDENTS)

    conn.commit()
    conn.close()
    print("Incident metrics inserted")

if __name__ == "__main__":
    seed_data()
