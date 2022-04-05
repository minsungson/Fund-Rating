from locale import currency
import yfinance as yf
import os
from datetime import date
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def stockInfo():
    os.system("clear")
    print(f"" + Back.WHITE + Fore.BLACK + " Basic Information about " + symbol + " ")
    print(f"\nStock name: " + Fore.YELLOW + ticker.info["shortName"])
    print(f"Sector: " + Fore.YELLOW + ticker.info["sector"])
    print(f"Country: " + Fore.YELLOW + ticker.info["country"])
    print(f"Exchange Time Zone: " + Fore.YELLOW + ticker.info["exchangeTimezoneName"])
    print(f"Currency: " + Fore.YELLOW + ticker.info["financialCurrency"])
    cont()

def financialData():
    print(f"" + Back.WHITE + Fore.BLACK + " Financial Information about " + symbol + " \n")
    rawData = ticker.history(period="7d")
    print(rawData)
    cont()

def cont():
    input("\nPress [ENTER] to continue ")
    os.system("clear")

def run():
    os.system("clear")
    global symbol, ticker
    symbol = input("Enter the ticker you would like a rating of: ")
    ticker = yf.Ticker(symbol)
    stockInfo()
    financialData()

run()