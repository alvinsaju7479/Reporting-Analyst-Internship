import os
import pandas as pd

RAW_FOLDER = "data/raw"
OUTPUT_FILE = "reports/Data_Quality_Report.xlsx"

report = []

for file in sorted(os.listdir(RAW_FOLDER)):

    path = os.path.join(RAW_FOLDER, file)

    try:

        if file.endswith(".csv"):
            df = pd.read_csv(path)

        elif file.endswith(".xlsx"):
            df = pd.read_excel(path)

        else:
            continue

        total_cells = df.shape[0] * df.shape[1]
        missing = int(df.isnull().sum().sum())
        duplicates = int(df.duplicated().sum())

        quality = round(((total_cells - missing) / total_cells) * 100, 2)

        report.append({
            "Dataset": file,
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Missing Values": missing,
            "Duplicate Rows": duplicates,
            "Quality Score (%)": quality
        })

    except Exception as e:
        print(file, e)

quality_df = pd.DataFrame(report)

quality_df.to_excel(OUTPUT_FILE, index=False)

print("\nData Quality Report Created Successfully")