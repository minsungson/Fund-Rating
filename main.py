import yfinance as yf
import sys
import os
import colorama
import pandas as pd
from colorama import Fore, Back
colorama.init(autoreset=True)

def stockInfo():
    os.system("clear")
    print("" + Back.WHITE + Fore.BLACK + " Basic Info about " + ticker.info["shortName"] + " (" + ticker.info["symbol"] + ") \n")
    key = {"Type: ": "quoteType", "Sector: ": "sector", "Country: ": "country", "Trading Time Zone: ": "exchangeTimezoneShortName: ", "Trading Currency: ": "financialCurrency: ", "ISIN: ": "isin", "Current Price: ": "regularMarketPrice", "Summary: ": "longBusinessSummary"}
    for i, m in key.items():
        if ticker.info.get(m) == None:
            print(i + Fore.RED + str(ticker.info.get(m)))
        else:
            print(i + Fore.YELLOW + str(ticker.info.get(m)))
    global pastOpen
    pastOpen = ticker.history(period = "7d")
    global df
    df = pd.DataFrame(pastOpen)
    cont()

def financialData():
    print("" + Back.WHITE + Fore.BLACK + " Market Open Price of the Past " + str(len(df.axes[0])) + " Days for " + ticker.info["symbol"] + " \n")
    if df.empty == False:
        print(pastOpen[["Open"]])
        global sigma
        sigma = df["Open"].sum()
    else:
        quotetype = str(ticker.info["quoteType"])
        print(Fore.RED + "\nyFinance does not hold data for this " + quotetype.lower() + "!")
        cont()
        again()
    cont()

def calculation():
    print("" + Back.WHITE + Fore.BLACK + " Statistical Analysis for " + ticker.info["shortName"] + " \n")
    print("Σx =", sigma)
    global mean
    mean = sigma/len(df.axes[0])
    print(" x̄ =", mean)
    print(" n =", len(df.axes[0]))
    global stdev
    stdev = df["Open"].std()
    print(" σ =", int(stdev))
    cont()

def output():
    lowStdev = mean - stdev
    highStdev = mean + stdev
    print("The standard deviation for the past week is " + Fore.YELLOW + str(int(stdev)) + Fore.RESET + " and the current market price is " + Fore.YELLOW + str(ticker.info["regularMarketPrice"]) + ticker.info["financialCurrency"] + ".\n")
    if lowStdev <= ticker.info["regularMarketPrice"] <= highStdev:
        print("As the current market price is between than 1 Std. Dev. above and below the mean," + Fore.RED + " Hold")    
    elif ticker.info["regularMarketPrice"] > highStdev:
        print("As the current market price is greater than 1 Std. Dev. above the mean," + Fore.RED + " Sell")
    elif ticker.info["regularMarketPrice"] < lowStdev:
        print("As the current market price is greater than 1 Std. Dev. below the mean," + Fore.RED + " Buy")
    elif ticker.info["regularMarketPrice"] < 2*lowStdev:
        print("As the current market price is greater than 2 Std. Dev. below the mean," + Fore.RED + " Strong buy")
    elif ticker.info["regularMarketPrice"] > 2*highStdev:
        print("As the current market price is greater than 2 Std. Dev. above the mean," + Fore.RED + " Strong Sell")
    cont()

def again():
    while True:
        wieder = input("Would you like to check another stock/fund? [y/n]: ")
        if wieder == "y":
            run()
            break
        elif wieder == "n":
            sys.exit()
        else:
            print("Invalid option, try again.")
            cont()

def cont():
    input("\nPress [ENTER] to continue")
    os.system("clear")

def run():
    while True:
        os.system("clear")
        global symbol, ticker
        symbol = input("Enter a ticker symbol: ")
        ticker = yf.Ticker(symbol)
        os.system("clear")
        if (ticker.info['regularMarketPrice'] == None):
            print("Cannot get info on " + Fore.RED + symbol + Fore.RESET + ", it probably does not exist.\n\nTry again.")
            cont()
        else:
            stockInfo()
            break
    financialData()
    calculation()
    output()
    again()


run()