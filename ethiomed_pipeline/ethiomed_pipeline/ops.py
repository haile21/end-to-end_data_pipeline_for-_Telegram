from dagster import op
import subprocess

@op
def scrape_telegram_data():
    subprocess.run(["python", "scrape/telegram_scraper.py"], check=True)

@op
def load_raw_to_postgres():
    subprocess.run(["python", "etl/load_raw_to_pg.py"], check=True)

@op
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "ethiomed_dbt"], check=True)

@op
def run_yolo_enrichment():
    subprocess.run(["python", "detect/object_detection.py"], check=True)

