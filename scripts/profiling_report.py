import os
import pandas as pd

RAW_FOLDER = "data/cleaned"
OUTPUT = "reports/Profiling_Report.xlsx"

writer = pd.ExcelWriter(OUTPUT, engine="openpyxl")

for file in sorted(os.listdir(RAW_FOLDER)):

    path = os.path.join(RAW_FOLDER, file)

    try:

        if file.endswith(".csv"):
            df = pd.read_csv(path)

        elif file.endswith(".xlsx"):
            df = pd.read_excel(path)

        else:
            continue

        profile = df.describe(include="all").transpose()

        sheet = file[:31]   # Excel sheet name limit

        profile.to_excel(writer, sheet_name=sheet)

    except Exception as e:
        print(file, e)

writer.close()

print("Profiling Report Created")