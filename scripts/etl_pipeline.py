from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():

    print("=" * 60)
    print("REPORTING ANALYTICS ETL PIPELINE")
    print("=" * 60)

    datasets = extract_data()

    transformed, log = transform_data(datasets)

    load_data(transformed)

    log.to_csv("reports/etl_log.csv", index=False)

    print("\nETL completed successfully")
    print("Log saved to reports/etl_log.csv")

if __name__ == "__main__":
    run_pipeline()