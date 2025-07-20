import pandas as pd

df = pd.read_csv("enhanced_healthcare.csv")

data_dict = []

for col in df.columns:
    dtype = str(df[col].dtype)
    sample = df[col].dropna().iloc[0] if not df[col].dropna().empty else "N/A"
    data_dict.append({
        "Field Name": col,
        "Data Type": dtype,
        "Description": "TBD",
        "Sample Value": sample
    })

df_dict = pd.DataFrame(data_dict)
df_dict.to_csv("data_dictionary.csv", index=False)
print("Data dictionary saved to data_dictionary.csv")