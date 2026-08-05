import os
import pandas as pd

RAW_FOLDER = "data/raw"
CLEAN_FOLDER = "data/cleaned"

os.makedirs(CLEAN_FOLDER, exist_ok=True)

for file in sorted(os.listdir(RAW_FOLDER)):

    path = os.path.join(RAW_FOLDER, file)

    try:

        if file.endswith(".csv"):
            df = pd.read_csv(path)

        elif file.endswith(".xlsx"):
            df = pd.read_excel(path)

        else:
            continue

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Fill missing numeric values
        numeric = df.select_dtypes(include="number").columns

        for col in numeric:
            df[col] = df[col].fillna(df[col].median())

        # Fill missing text values
        text = df.select_dtypes(include="object").columns

        for col in text:
            df[col] = df[col].fillna("Unknown")

        # Trim whitespace
        for col in text:
            df[col] = df[col].astype(str).str.strip()

        output = os.path.join(CLEAN_FOLDER, file)

        if file.endswith(".csv"):
            df.to_csv(output, index=False)
        else:
            df.to_excel(output, index=False)

        print(f"Cleaned: {file}")

    except Exception as e:
        print(file, e)

print("\nCleaning Complete")