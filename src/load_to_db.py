import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("enhanced_healthcare.csv")

# Connect to SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect("healthcare.db")

# Save DataFrame to a table named 'patients'
df.to_sql("patients", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("✅ Data loaded into 'healthcare.db' (table: patients)")
