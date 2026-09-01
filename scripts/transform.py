import pandas as pd

def transform_data(datasets):

    transformed = {}
    log = []

    for name, df in datasets.items():

        rows_before = len(df)

        # Remove duplicates
        df = df.drop_duplicates()

        # Fill missing numeric values
        numeric = df.select_dtypes(include="number").columns

        df[numeric] = df[numeric].fillna(df[numeric].median())

        rows_after = len(df)

        transformed[name] = df

        log.append({
            "dataset": name,
            "rows": rows_after,
            "duplicates_removed": rows_before - rows_after,
            "missing_values": int(df.isnull().sum().sum())
        })

    log_df = pd.DataFrame(log)

    return transformed, log_df