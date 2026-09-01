import os
import pandas as pd

DATA_FOLDER = "data/cleaned"

def extract_data():
    datasets = {}

    for file in sorted(os.listdir(DATA_FOLDER)):
        if not file.endswith(".xlsx"):
            continue

        path = os.path.join(DATA_FOLDER, file)
        datasets[file] = pd.read_excel(path)

        if file.endswith(".xlsx"):
            df = pd.read_excel(path)

        elif file.endswith(".csv"):
            df = pd.read_csv(path)

        else:
            continue

        datasets[file] = df

    print(f"Extracted {len(datasets)} datasets")

    return datasets