import yfinance as yf
import colorama
from colorama import Fore, Back
import os
colorama.init(autoreset=True)
os.system("clear")
ticker = yf.Ticker("msft")

print("" + Back.WHITE + Fore.BLACK + " Basic Investor Info for " + ticker.info["shortName"] + " (" + ticker.info["symbol"] + ") \n")
key = {"Type: ": "quoteType", "Sector: ": "sector", "Country: ": "country", "Trading Time Zone: ": "exchangeTimezoneShortName: ", "Trading Currency: ": "financialCurrency: ", "ISIN: ": "isin", "Current Price: ": "regularMarketPrice", "Summary: ": "longBusinessSummary"}
for i, m in key.items():
    if ticker.info.get(m) == None:
        print(i + Fore.RED + str(ticker.info.get(m)))
    else:
        print(i + Fore.YELLOW + str(ticker.info.get(m)))


# symbol
# regularMarketPrice