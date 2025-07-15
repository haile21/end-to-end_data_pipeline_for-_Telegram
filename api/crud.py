#Query Functions

from sqlalchemy.orm import Session
from sqlalchemy.sql import text

def get_top_products(db: Session, limit: int = 10):
    query = text("""
        SELECT detected_object_class AS product, COUNT(*) AS mentions
        FROM analytics.fct_image_detections
        GROUP BY detected_object_class
        ORDER BY mentions DESC
        LIMIT :limit
    """)
    return db.execute(query, {"limit": limit}).fetchall()

def get_channel_activity(db: Session, channel_name: str):
    query = text("""
        SELECT message_date::date AS date, COUNT(*) AS message_count
        FROM analytics.fct_messages
        WHERE channel = :channel_name
        GROUP BY date
        ORDER BY date
    """)
    return db.execute(query, {"channel_name": channel_name}).fetchall()

def search_messages(db: Session, keyword: str):
    query = text("""
        SELECT message_id, message_date, text, channel
        FROM analytics.fct_messages
        WHERE LOWER(text) LIKE :pattern
        LIMIT 50
    """)
    return db.execute(query, {"pattern": f"%{keyword.lower()}%"}).fetchall()
