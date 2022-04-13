import yfinance as yf
import pandas as pd

ticker = yf.Ticker("GOOGL")

key = {"sector", "country", "exchangeTimezoneName", "financialCurrency", "isin", "majorHolders", "instututionalHolders"}
for i in key:
    print(ticker.info.get(key, "doesnt exist"))