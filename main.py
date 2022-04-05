from locale import currency
import yfinance as yf
import os
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

global shortName, tz, sector, country
shortName = ticker.info["shortName"]
tz = ticker.info["exchangeTimezoneName"]
country = ticker.info["country"]
currencyS = ticker.info["financialCurrency"]


def stockInfo():
    print(f"" + Back.WHITE + Fore.BLACK + "Stock Information")
    print(f"\nStock name: " + Fore.YELLOW + shortName)
    print(f"Exchange Time Zone: " + Fore.YELLOW + tz)
    print(f"Country: " + Fore.YELLOW + country)
    print(f"Currency: " + Fore.YELLOW + currencyS)
    cont()

def cont():
    input("\nPress [ENTER] to continue ")

stockInfo()