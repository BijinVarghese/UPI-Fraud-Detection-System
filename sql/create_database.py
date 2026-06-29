import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("sql/upi_fraud.db")

# Load dataset
df = pd.read_csv("data/processed/upi_transactions_v2.csv")

# Use a smaller dataset for SQL (fast and GitHub-friendly)
df = df.sample(10000, random_state=42)

# Save to SQL
df.to_sql(
    "transactions",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Database Created Successfully!")
print("Rows inserted:", len(df))
