from locale import currency
import yfinance as yf
import os
from datetime import datetime, timedelta
import colorama
import pandas as pd
from colorama import Fore, Back
colorama.init(autoreset=True)

startDate = datetime.today()
endDate = startDate + \
    timedelta(days=7)

class stock():
    def __init__(self, sector, country, exchangeTimezoneName, financialCurrency, ISIN, majorHolders, instututionalHolders):
        self.sector = sector
        self.country = country
        self.exchangeTimezoneName = exchangeTimezoneName
        self.financialCurrency = financialCurrency
        self.ISIN = ISIN
        self.major_holders = majorHolders
        self.institutional_holders = instututionalHolders

    def getStats(self):
        return [self.sector, self.country, self.exchangeTimezoneName, self.financialCurrency, self.ISIN, self.major_holders, self.institutional_holders]

def stockInfo():
    os.system("clear")
    ticker.getStats()
    # print("" + Back.WHITE + Fore.BLACK + " Basic Information about " + ticker.info["shortName"] + " \n")
    # print("Sector: " + Fore.YELLOW + ticker.info["sector"])
    # print("Country: " + Fore.YELLOW + ticker.info["country"])
    # print("Exchange Time Zone: " + Fore.YELLOW + ticker.info["exchangeTimezoneName"])
    # print("Currency: " + Fore.YELLOW + ticker.info["financialCurrency"])
    # print("ISIN: " + Fore.YELLOW + ticker.info["financialCurrency"])
    cont()

# def financialData():
#     print("" + Back.WHITE + Fore.BLACK + " Financial Information about " + ticker.info["shortName"] + " \n")
#     # global rawData
#     # rawData = ticker.history(period="7d")
#     # print(rawData[["Open"]])
#     cont()

# # def calculation():
# #     df = pd.DataFrame(rawData)
# #     list = df['Open'].values.tolist()
# #     # sigma = rawData.sum()
# #     # print("Σ open =", sigma)
# #     # print("     x̄ =", sigma/7)
# #     print(type(rawData))

# def cont():
#     input("\nPress [ENTER] to continue ")
#     os.system("clear")

def run():
    os.system("clear")
    global symbol, ticker
    # symbol = input("Enter the ticker you would like a rating of: ")
    symbol = "GOOGL" # set static for debugging
    ticker = yf.Ticker(symbol)
    ticker = stock(self.sector, self.country, self.exchangeTimezoneName, self.financialCurrency, self.ISIN, self.major_holders, self.institutional_holders)
    stockInfo()
    # financialData()
    # calculation()

run()

# ticker = yf.Ticker("GOOGL")
# print(ticker.isin)