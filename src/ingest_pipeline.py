import pandas as pd
import os
import logging
from datetime import datetime

# ========== CONFIGURATION ==========
RAW_FILE_PATH = "healthcare_dataset.csv"
DEST_PATH = "raw_data/healthcare_dataset_ingested.csv"
LOG_FILE = "logs/ingestion.log"

# Ensure folders exist
os.makedirs("logs", exist_ok=True)
os.makedirs("raw_data", exist_ok=True)

# ========== SET UP LOGGING ==========
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ========== VALIDATION FUNCTION ==========
def validate_data(df: pd.DataFrame) -> bool:
    required_columns = [
        "Name", "Age", "Gender", "Blood Type", "Medical Condition",
        "Date of Admission", "Doctor", "Hospital", "Insurance Provider",
        "Billing Amount", "Room Number", "Admission Type",
        "Discharge Date", "Medication", "Test Results"
    ]

    # Column check
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        logging.error(f"Missing columns: {missing}")
        return False

    # Data type sanity check (basic)
    if not pd.api.types.is_numeric_dtype(df["Age"]):
        logging.error("Column 'Age' is not numeric.")
        return False

    if not pd.api.types.is_numeric_dtype(df["Billing Amount"]):
        logging.error("Column 'Billing Amount' is not numeric.")
        return False

    logging.info("Data validation passed.")
    return True

# ========== INGESTION FUNCTION ==========
def ingest_data():
    try:
        df = pd.read_csv(RAW_FILE_PATH)
        logging.info(f"Loaded file: {RAW_FILE_PATH} with {len(df)} rows.")

        if validate_data(df):
            df.to_csv(DEST_PATH, index=False)
            logging.info(f"Data ingested and saved to {DEST_PATH}")
        else:
            logging.warning("Ingestion aborted due to validation failure.")

    except Exception as e:
        logging.error(f"Ingestion failed: {e}")

# ========== MAIN ==========
if __name__ == "__main__":
    logging.info("Ingestion started.")
    ingest_data()
    logging.info("Ingestion script completed.")