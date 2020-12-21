from os import close
from fastapi import FastAPI

from .utils import get_close_data

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome, my child"}

@app.get("/api/tickers/{tickers}")
async def alpha_vantage(tickers: str):
    tickers = [t.strip() for t in tickers.split(",")]
    close_data = get_close_data(tickers)
    return close_data