import pandas as pd

# Load the data
df = pd.read_csv("healthcare_dataset.csv")

# Optional: Drop unnamed index column if it exists
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# Convert date columns to datetime
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], errors='coerce')
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], errors='coerce')

# Feature Engineering
df["StayDuration"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
df["IsSeniorCitizen"] = df["Age"] > 60
df["AdmissionYear"] = df["Date of Admission"].dt.year

# Billing category (Low / Medium / High)
df["BillingCategory"] = pd.qcut(df["Billing Amount"], q=3, labels=["Low", "Medium", "High"])

# Save cleaned dataset
df.to_csv("enhanced_healthcare.csv", index=False)

print("✅ Data cleaned and saved as 'enhanced_healthcare.csv'")
