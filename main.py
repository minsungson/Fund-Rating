import yfinance as yf

symbol = input("Enter the ticker you would like a rating of: ")

ticker = yf.Ticker(symbol)
start='2020-09-15',
end='2020-11-15',

print(ticker.info)