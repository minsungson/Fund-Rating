import yfinance as yf

ticker = yf.Ticker("GOOGL")

key = ("sector", "country", "exchangeTimezoneName", "financialCurrency", "isin", "majorHolders", "instututionalHolders")
for i in key:
    print(ticker.info.get(i))