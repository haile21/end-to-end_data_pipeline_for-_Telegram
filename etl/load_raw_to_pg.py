import os
import json
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "dbname": os.getenv("POSTGRES_DB")
}

RAW_DATA_DIR = Path("data/raw/telegram_messages")

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE SCHEMA IF NOT EXISTS raw;
            CREATE TABLE IF NOT EXISTS raw.telegram_messages (
                id BIGINT PRIMARY KEY,
                message JSONB,
                channel TEXT,
                scraped_at DATE
            );
        """)
    conn.commit()

def insert_messages(conn):
    for date_dir in RAW_DATA_DIR.iterdir():
        if not date_dir.is_dir():
            continue
        for file in date_dir.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                messages = json.load(f)

            channel = file.stem
            scraped_at = date_dir.name

            with conn.cursor() as cur:
                for msg in messages:
                    cur.execute("""
                        INSERT INTO raw.telegram_messages (id, message, channel, scraped_at)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING
                    """, (msg["id"], json.dumps(msg), channel, scraped_at))
            conn.commit()

if __name__ == "__main__":
    with psycopg2.connect(**DB_CONFIG) as conn:
        create_table(conn)
        insert_messages(conn)

#Run
## python etl/load_raw_to_pg.py
