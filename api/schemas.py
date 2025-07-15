#Pydantic Response Models
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TopProduct(BaseModel):
    product: str
    mentions: int

class ChannelActivity(BaseModel):
    date: date
    message_count: int

class MessageResult(BaseModel):
    message_id: int
    message_date: date
    text: str
    channel: str
