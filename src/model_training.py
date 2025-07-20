import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("enhanced_healthcare.csv")

# Define target and features
target = "BillingCategory"
features = ['Age', 'Gender', 'Admission Type', 'Medical Condition', 'StayDuration', 'IsSeniorCitizen']

X = df[features]
y = df[target]

# Preprocessing
categorical = ['Gender', 'Admission Type', 'Medical Condition']
numerical = ['Age', 'StayDuration', 'IsSeniorCitizen']

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
], remainder='passthrough')

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print("Classification Report:\n")
print(classification_report(y_test, y_pred))