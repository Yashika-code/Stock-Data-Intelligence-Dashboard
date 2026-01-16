import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from .models import StockData
import numpy as np

def load_stock(symbol: str, db: Session):
    end = datetime.today()
    start = end - timedelta(days=400)

    df = yf.download(symbol, start=start, end=end)

    # Reset index safely
    df.reset_index(inplace=True)

    # ---- SAFETY: flatten columns if MultiIndex ----
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Calculations
    df["Daily Return"] = (df["Close"] - df["Open"]) / df["Open"]
    df["MA7"] = df["Close"].rolling(7).mean()

    df.dropna(inplace=True)

    # Clear old data
    db.query(StockData).filter(StockData.symbol == symbol).delete()

    for _, row in df.iterrows():
        record = StockData(
            symbol=symbol,
            date=pd.to_datetime(row["Date"]).to_pydatetime().date(),  # ✅ FINAL FIX
            open=float(row["Open"]),
            close=float(row["Close"]),
            high=float(row["High"]),
            low=float(row["Low"]),
            volume=float(row["Volume"]),
            daily_return=float(row["Daily Return"]),
            ma_7=float(row["MA7"]),
        )
        db.add(record)

    db.commit()
