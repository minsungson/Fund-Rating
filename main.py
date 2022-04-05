import yfinance as yf

ticker = yf.Ticker("VUSA")
start='2020-09-15',
end='2020-11-15',

print(ticker.info)