import os
import pandas as pd

CLEAN_FOLDER = "data/cleaned"
OUTPUT_SQL = "sql/02_create_tables.sql"

# Maps pandas dtypes to PostgreSQL types
def map_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "DOUBLE PRECISION"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"
    else:
        return "TEXT"

sql_statements = []

for file in sorted(os.listdir(CLEAN_FOLDER)):

    if not (file.endswith(".csv") or file.endswith(".xlsx")):
        continue

    path = os.path.join(CLEAN_FOLDER, file)

    if file.endswith(".csv"):
        df = pd.read_csv(path, nrows=100)
    else:
        df = pd.read_excel(path, nrows=100)

    table_name = (
        os.path.splitext(file)[0]
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )

    sql = f'DROP TABLE IF EXISTS "{table_name}" CASCADE;\n'
    sql += f'CREATE TABLE "{table_name}" (\n'

    columns = []

    for col in df.columns:

        pg_type = map_dtype(df[col].dtype)

        column = f'    "{col}" {pg_type}'

        # Candidate primary key
        if col == "Record_ID":
            column += " PRIMARY KEY"

        columns.append(column)

    sql += ",\n".join(columns)
    sql += "\n);\n"

    sql_statements.append(sql)

with open(OUTPUT_SQL, "w") as f:
    f.write("\n".join(sql_statements))

print("SQL schema generated successfully!")