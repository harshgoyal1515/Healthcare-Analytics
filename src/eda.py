import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("enhanced_healthcare.csv")

# Plot 1: Top 10 most common medical conditions
plt.figure(figsize=(10, 6))
df["Medical Condition"].value_counts().head(10).plot(kind="barh", color="skyblue")
plt.title("Top 10 Medical Conditions")
plt.xlabel("Number of Patients")
plt.tight_layout()
plt.savefig("eda_top_conditions.png")
plt.close()

# Plot 2: Billing Amount distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Billing Amount"], bins=30, kde=True, color="orange")
plt.title("Billing Amount Distribution")
plt.tight_layout()
plt.savefig("eda_billing_distribution.png")
plt.close()

# Plot 3: Stay Duration distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["StayDuration"], bins=20, color="green")
plt.title("Stay Duration Distribution")
plt.tight_layout()
plt.savefig("eda_stay_duration.png")
plt.close()

# Plot 4: Average billing by Admission Type
plt.figure(figsize=(10, 6))
df.groupby("Admission Type")["Billing Amount"].mean().sort_values().plot(kind="bar", color="purple")
plt.title("Average Billing Amount by Admission Type")
plt.ylabel("Average Billing (₹)")
plt.tight_layout()
plt.savefig("eda_avg_billing_by_type.png")
plt.close()

print("✅ EDA completed. Charts saved as PNG files.")
