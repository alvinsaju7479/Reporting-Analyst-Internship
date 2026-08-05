import os
import pandas as pd

RAW_FOLDER = "data/raw"
OUTPUT_FILE = "reports/Data_Dictionary.xlsx"

rows = []

for file in sorted(os.listdir(RAW_FOLDER)):

    path = os.path.join(RAW_FOLDER, file)

    try:
        if file.endswith(".csv"):
            df = pd.read_csv(path)

        elif file.endswith(".xlsx"):
            df = pd.read_excel(path)

        else:
            continue

        for column in df.columns:

            rows.append({
                "Dataset": file,
                "Column": column,
                "Data Type": str(df[column].dtype),
                "Missing Values": int(df[column].isnull().sum()),
                "Unique Values": int(df[column].nunique()),
                "Example Value": str(df[column].dropna().iloc[0]) if not df[column].dropna().empty else ""
            })

    except Exception as e:
        print(file, e)

dictionary = pd.DataFrame(rows)

dictionary.to_excel(OUTPUT_FILE, index=False)

print(f"\nData Dictionary saved to {OUTPUT_FILE}")