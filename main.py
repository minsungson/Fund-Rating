from locale import currency
import yfinance as yf
import os
from datetime import date
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

os.system("clear")
global symbol
symbol = input("Enter the ticker you would like a rating of: ")
os.system("clear")

ticker = yf.Ticker(symbol)
start='2020-09-15',
end='2020-11-15',

shortName = ticker.info["shortName"]
tz = ticker.info["exchangeTimezoneName"]
country = ticker.info["country"]
currencyS = ticker.info["financialCurrency"]
sector = ticker.info["sector"]


def stockInfo():
    print(f"" + Back.WHITE + Fore.BLACK + " Basic Information about " + symbol + " ")
    print(f"\nStock name: " + Fore.YELLOW + shortName)
    print(f"Sector: " + Fore.YELLOW + sector)
    print(f"Country: " + Fore.YELLOW + country)
    print(f"Exchange Time Zone: " + Fore.YELLOW + tz)
    print(f"Currency: " + Fore.YELLOW + currencyS)
    cont()

def financialData():
    print(f"" + Back.WHITE + Fore.BLACK + " Financial Information about " + symbol + " \n")
    d1 = ticker.history(period="7d")
    print(d1)

def cont():
    input("\nPress [ENTER] to continue ")
    os.system("clear")

stockInfo()
financialData()