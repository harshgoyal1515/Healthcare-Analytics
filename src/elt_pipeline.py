import pandas as pd
import sqlite3

# Extract and transform
df = pd.read_csv("enhanced_healthcare.csv")

# Load to SQLite
conn = sqlite3.connect("healthcare.db")
df.to_sql("patients", conn, if_exists="replace", index=False)
conn.close()

print("Data loaded into SQLite database as 'patients' table.")
