import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from loguru import logger

load_dotenv()

API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

DATA_DIR = Path("data/raw/telegram_messages")

CHANNELS = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma"
]

client = TelegramClient("scraper", API_ID, API_HASH)

async def scrape_channel(channel_url):
    await client.start()
    channel = await client.get_entity(channel_url)
    messages = []

    logger.info(f"Scraping {channel.title}")
    async for msg in client.iter_messages(channel, limit=200):
        messages.append(msg.to_dict())

    today = datetime.now().strftime("%Y-%m-%d")
    channel_name = channel.username or channel.title.replace(" ", "_")
    out_path = DATA_DIR / today / f"{channel_name}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    logger.success(f"Saved {len(messages)} messages to {out_path}")

if __name__ == "__main__":
    with client:
        for ch in CHANNELS:
            client.loop.run_until_complete(scrape_channel(ch))


# Logs channel name, number of messages, errors (rate limits, etc.)
#
# Saves scraped messages as data/raw/telegram_messages/YYYY-MM-DD/channel_name.json
  ###How to Run the Project
#1.Build and start the containers:
 #- docker-compose up --build
#2.Run the scraper inside the container:
  #-docker exec -it <api_container_name> python scrape/telegram_scraper.py
