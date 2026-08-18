import os
import pandas as pd
from sqlalchemy import create_engine

# -------------------------
# PostgreSQL Connection
# -------------------------

DB_USER = "alvinsaju"
DB_PASSWORD = ""          # Leave empty unless you set one
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "reporting_analytics"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

DATA_FOLDER = "data/cleaned"

for file in sorted(os.listdir(DATA_FOLDER)):

    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(DATA_FOLDER, file))

    elif file.endswith(".xlsx"):
        df = pd.read_excel(os.path.join(DATA_FOLDER, file))

    else:
        continue

    table = (
        os.path.splitext(file)[0]
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )

    print(f"Loading {table}")

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

print("\nAll datasets imported successfully.")