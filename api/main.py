#FastAPI Entry Point
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
import schemas

app = FastAPI(title="Ethiomed Analytical API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/reports/top-products", response_model=List[schemas.TopProduct])
def top_products(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_top_products(db, limit)

@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivity])
def channel_activity(channel_name: str, db: Session = Depends(get_db)):
    return crud.get_channel_activity(db, channel_name)

@app.get("/api/search/messages", response_model=List[schemas.MessageResult])
def search_messages(query: str, db: Session = Depends(get_db)):
    if not query:
        raise HTTPException(status_code=400, detail="Query string cannot be empty.")
    return crud.search_messages(db, query)

## Run the API
#- uvicorn main:app --reload
#visit swagger for the api endpoints com