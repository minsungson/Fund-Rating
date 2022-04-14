import yfinance as yf
from colorama import Fore, Back
import os
os.system("clear")
ticker = yf.Ticker("msft")

print("" + Back.WHITE + Fore.BLACK + " Basic Investor Info for " + ticker.info["shortName"] + " (" + ticker.info["symbol"] + ") \n")
key = {"Type: ": "quoteType", "Sector: ": "sector", "Country: ": "country", "Trading Time Zone: ": "exchangeTimezoneShortName: ", "Trading Currency: ": "financialCurrency: ", "ISIN: ": "isin", "Current Price: ": "regularMarketPrice", "Summary: ": "longBusinessSummary"}
for i, m in key.items():
    print(i + str(ticker.info.get(m)))

# symbol
# regularMarketPrice