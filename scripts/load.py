import os
import pandas as pd
from sqlalchemy import create_engine, text

DB_USER = "alvinsaju"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "reporting_analytics"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def load_data(datasets):

    with engine.begin() as conn:
        conn.execute(text("DROP VIEW IF EXISTS vw_financial_summary CASCADE;"))
        conn.execute(text("DROP VIEW IF EXISTS vw_employee_performance CASCADE;"))
        conn.execute(text("DROP VIEW IF EXISTS vw_kpi_summary CASCADE;"))

    for name, df in datasets.items():

        table = (
            os.path.splitext(name)[0]
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
        )

        df.to_sql(table, engine, if_exists="replace", index=False)
        print(f"Loaded {table}")

    with engine.begin() as conn:
        sql = open("sql/04_views.sql", "r").read()
        conn.execute(text(sql))

    print("Views recreated successfully")