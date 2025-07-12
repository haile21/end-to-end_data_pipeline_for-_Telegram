# Shipping a Data Product: From Raw Telegram Data to an Analytical API

## 🧩 Overview

This project is a **modern data pipeline** designed to generate business insights on **Ethiopian medical businesses** by extracting and analyzing data from **public Telegram channels**. The platform is designed with scalability and reproducibility in mind, using tools like **Docker**, **PostgreSQL**, **dbt**, **YOLO**, and **FastAPI**.

## 🧠 Business Need

As a **Data Engineer at Kara Solutions**, your goal is to build a robust data infrastructure that enables insights into:

- 🔝 Top 10 frequently mentioned medical products across Telegram
- 💵 Price or availability variations of specific products
- 📷 Visual content trends (e.g., pills vs. creams)
- 📈 Daily and weekly posting trends for health topics

## 🔧 Solution Architecture

We are implementing a full **ELT (Extract, Load, Transform)** pipeline:

1. **Extract**: Scrape public Telegram medical channels using the Telegram API.
2. **Load**: Store raw data in a structured **Data Lake** (`JSON` format).
3. **Transform**: Use **dbt** to build a dimensional star schema in a **PostgreSQL** data warehouse.
4. **Enrich**: Apply **YOLO-based object detection** on scraped images.
5. **Expose**: Provide cleaned insights via a **FastAPI-based analytical API**.


## 📦 Project Structure

├── data/
│ └── raw/
│ └── telegram_messages/YYYY-MM-DD/channel_name.json
├── dbt/
│ └── models/
├── docker/
│ └── Dockerfile
├── docker-compose.yml
├── .env # Secrets (not committed)
├── .gitignore
├── requirements.txt
├── scrape/
│ └── telegram_scraper.py
├── detect/
│ └── object_detection.py
├── api/
│ └── main.py (FastAPI)
└── README.md 

## ✅ Deliverables

### 🗂 Task 0: Project Setup & Environment Management

- Initialize Git repository
- Create `requirements.txt` for dependencies
- Create `Dockerfile` and `docker-compose.yml` for containerization
- Create a `.env` file for secrets
- Add `.env` to `.gitignore`
- Load environment variables using `python-dotenv`

### 🛰 Task 1: Data Scraping & Collection

- Scrape data from Telegram channels:
  - [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
  - [Tikvah Pharma](https://t.me/tikvahpharma)
  - Other channels listed at: https://et.tgstat.com/medicine

- Collect images for object detection from visual-heavy channels:
  - [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)

- Store raw messages in structured JSON files:
data/raw/telegram_messages/YYYY-MM-DD/channel_name.json 

- Implement:
- Incremental scraping
- Logging for scraping history and errors (e.g., rate limits)

## 🔍 Coming Soon

- **Task 2**: Transform raw data into dimensional star schema using dbt
- **Task 3**: Apply YOLO for object detection on product images
- **Task 4**: Expose final analytics through a FastAPI REST API

## 🛡️ Security Notice

All secrets (e.g., API keys, DB credentials) must be stored in a `.env` file and excluded from version control via `.gitignore`.
