import os
import pandas as pd

RAW_FOLDER = "data/raw"

print("=" * 70)
print("REPORTING ANALYST DATA PROFILER")
print("=" * 70)

for file in sorted(os.listdir(RAW_FOLDER)):

    path = os.path.join(RAW_FOLDER, file)

    try:

        if file.endswith(".csv"):
            df = pd.read_csv(path)

        elif file.endswith(".xlsx"):
            df = pd.read_excel(path)

        else:
            continue

        print("\n" + "=" * 70)
        print(f"Dataset : {file}")
        print("=" * 70)

        print(f"Rows       : {df.shape[0]}")
        print(f"Columns    : {df.shape[1]}")

        print("\nColumns")

        for col in df.columns:
            print(f" - {col}")

        print("\nMissing Values")

        print(df.isnull().sum())

        print("\nDuplicate Rows :", df.duplicated().sum())

    except Exception as e:
        print(f"Cannot read {file}")
        print(e)