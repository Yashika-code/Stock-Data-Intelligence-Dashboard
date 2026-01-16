from pydantic import BaseModel
from datetime import date

class StockResponse(BaseModel):
    date: date
    open: float
    close: float
    high: float
    low: float
    daily_return: float
    ma_7: float

    class Config:
        orm_mode = True
