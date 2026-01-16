from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from .database import SessionLocal, engine
from .models import Base, StockData
from .schemas import StockResponse
from .data_loader import load_stock
import os
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock Data Intelligence Dashboard")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DEFAULT_COMPANIES = {
    "INFY": "INFY.NS",
    "TCS": "TCS.NS",
    "RELIANCE": "RELIANCE.NS"
}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)

@app.on_event("startup")
def startup():
    db = SessionLocal()
    for symbol in DEFAULT_COMPANIES.values():
        load_stock(symbol, db)
    db.close()

# ------------------ APIs ------------------
@app.get("/")
def home():
    return {"message": "Stock Data Intelligence Dashboard API is running"}

@app.get("/companies")
def get_companies():
    return list(DEFAULT_COMPANIES.keys())

@app.get("/data/{symbol}", response_model=List[StockResponse])
def get_last_30_days(symbol: str, db: Session = Depends(get_db)):
    return (
        db.query(StockData)
        .filter(StockData.symbol == f"{symbol}.NS")
        .order_by(StockData.date.desc())
        .limit(30)
        .all()
    )

@app.get("/summary/{symbol}")
def get_summary(symbol: str, db: Session = Depends(get_db)):
    data = db.query(StockData).filter(
        StockData.symbol == f"{symbol}.NS"
    ).all()

    closes = [d.close for d in data]

    return {
        "52_week_high": max(closes),
        "52_week_low": min(closes),
        "average_close": sum(closes) / len(closes)
    }

@app.get("/compare")
def compare(symbol1: str, symbol2: str, db: Session = Depends(get_db)):
    def avg_return(sym):
        data = db.query(StockData).filter(
            StockData.symbol == f"{sym}.NS"
        ).all()
        return sum(d.daily_return for d in data) / len(data)

    return {
        symbol1: avg_return(symbol1),
        symbol2: avg_return(symbol2)
    }

@app.get("/summary/{symbol}")
def get_summary(symbol: str, db: Session = Depends(get_db)):
    data = db.query(StockData).filter(
        StockData.symbol == f"{symbol}.NS"
    ).all()

    closes = [d.close for d in data]
    returns = [d.daily_return for d in data]

    return {
        "52_week_high": max(closes),
        "52_week_low": min(closes),
        "average_close": sum(closes) / len(closes),
        "volatility_score": round(np.std(returns), 4)  # ✅ CUSTOM METRIC
    }
