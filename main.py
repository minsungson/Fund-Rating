import yfinance as yf
import os
from datetime import datetime, timedelta
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

startDate = datetime.today()
endDate = startDate - timedelta(days=7)

def stockInfo():
    os.system("clear")
    print(f"" + Back.WHITE + Fore.BLACK + " Basic Information about " + ticker.info["shortName"] + " \n")
    print(f"Sector: " + Fore.YELLOW + ticker.info["sector"])
    print(f"Country: " + Fore.YELLOW + ticker.info["country"])
    print(f"Exchange Time Zone: " + Fore.YELLOW + ticker.info["exchangeTimezoneName"])
    print(f"Currency: " + Fore.YELLOW + ticker.info["financialCurrency"])
    cont()

def financialData():
    print(f"" + Back.WHITE + Fore.BLACK + " Financial Information about " + ticker.info["shortName"] + " \n")
    rawData = ticker.info["regularMarketPreviousClose"] # latest market close
    print(rawData)
    cont()

def cont():
    input("\nPress [ENTER] to continue ")
    os.system("clear")

def run():
    os.system("clear")
    global symbol, ticker
    # symbol = input("Enter the ticker you would like a rating of: ")
    symbol = "GOOGL" # set static for debugging
    ticker = yf.Ticker(symbol)
    stockInfo()
    financialData()

run()