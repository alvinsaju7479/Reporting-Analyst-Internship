import os
import pandas as pd
from datetime import datetime

RAW_FOLDER = "data/raw"
CLEAN_FOLDER = "data/cleaned"
OUTPUT_FILE = "reports/Cleaning_Log.xlsx"

log = []

for file in sorted(os.listdir(RAW_FOLDER)):

    raw_path = os.path.join(RAW_FOLDER, file)
    clean_path = os.path.join(CLEAN_FOLDER, file)

    if not os.path.exists(clean_path):
        continue

    try:

        if file.endswith(".csv"):
            raw = pd.read_csv(raw_path)
            clean = pd.read_csv(clean_path)

        elif file.endswith(".xlsx"):
            raw = pd.read_excel(raw_path)
            clean = pd.read_excel(clean_path)

        else:
            continue

        log.append({
            "Dataset": file,
            "Original Rows": len(raw),
            "Cleaned Rows": len(clean),
            "Missing Before": int(raw.isnull().sum().sum()),
            "Missing After": int(clean.isnull().sum().sum()),
            "Duplicates Before": int(raw.duplicated().sum()),
            "Duplicates After": int(clean.duplicated().sum()),
            "Cleaning Date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    except Exception as e:
        print(file, e)

pd.DataFrame(log).to_excel(OUTPUT_FILE, index=False)

print("Cleaning Log Created")