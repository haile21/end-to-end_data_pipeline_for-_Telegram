import os
from pathlib import Path
from dotenv import load_dotenv
from ultralytics import YOLO
import psycopg2
import json

load_dotenv()

# PostgreSQL config
DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "dbname": os.getenv("POSTGRES_DB")
}

IMAGES_DIR = Path("data/raw/images")
model = YOLO("yolov8n.pt")  # You can use yolov8s.pt or yolov8m.pt as well

def extract_message_id(image_path):
    return int(image_path.stem)

def detect_objects(image_path):
    results = model(image_path)
    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "class_name": r.names[int(box.cls[0])],
                "confidence": float(box.conf[0])
            })
    return detections

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE SCHEMA IF NOT EXISTS raw;
            CREATE TABLE IF NOT EXISTS raw.image_detections (
                id SERIAL PRIMARY KEY,
                message_id BIGINT,
                class_name TEXT,
                confidence NUMERIC,
                detected_at TIMESTAMP DEFAULT NOW()
            );
        """)
    conn.commit()

def save_detections_to_db(conn, message_id, detections):
    with conn.cursor() as cur:
        for d in detections:
            cur.execute("""
                INSERT INTO raw.image_detections (message_id, class_name, confidence)
                VALUES (%s, %s, %s)
            """, (message_id, d["class_name"], d["confidence"]))
    conn.commit()

def run():
    with psycopg2.connect(**DB_CONFIG) as conn:
        create_table(conn)
        for image_file in IMAGES_DIR.rglob("*.jpg"):
            message_id = extract_message_id(image_file)
            detections = detect_objects(image_file)
            save_detections_to_db(conn, message_id, detections)
            print(f"Processed {image_file.name}: {len(detections)} objects")

if __name__ == "__main__":
    run()
