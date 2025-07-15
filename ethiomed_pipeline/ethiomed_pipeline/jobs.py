from dagster import job
from ops import (
    scrape_telegram_data,
    load_raw_to_postgres,
    run_dbt_transformations,
    run_yolo_enrichment,
)

@job
def ethiomed_data_pipeline():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()

    #then  Launch Dagster UI
    #From your root directory:
    # -dagster dev
    #Open: http://localhost:3000, You’ll see your job (ethiomed_data_pipeline) in the UI and be able to run it manually or inspect logs and status.

