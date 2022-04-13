import yfinance as yf
import sys
import os
import colorama
import pandas as pd
import numpy as np
from colorama import Fore, Back
colorama.init(autoreset=True)


def stockInfo():
    os.system("clear")
    print("" + Back.WHITE + Fore.BLACK + " Basic Investor Info for " + ticker.info["shortName"] + " \n")
    # print("Sector: " + Fore.YELLOW + ticker.info["sector"])
    if "sector" in ticker.info:
        print("Sector: " + Fore.YELLOW + ticker.info["sector"])
    else:
        print("Sector: " + Fore.RED + "N/A")
    if "country" in ticker.info:
        print("Country: " + Fore.YELLOW + ticker.info["country"])
    else:
        print("Country: " + Fore.RED + "N/A")
    if "exchangeTimezoneName" in ticker.info:
        print("Trading Time Zone: " + Fore.YELLOW + ticker.info["exchangeTimezoneName"])
    else:
        print("Trading Time Zone: " + Fore.RED + "N/A")
    if "financialCurrency" in ticker.info:
        print("Trading Currency: " + Fore.YELLOW + ticker.info["financialCurrency"])
    else:
        print("Trading Currrency: " + Fore.RED + "N/A")
    if "isin" in ticker.info:
        print("ISIN: " + Fore.YELLOW + ticker.info["isin"])
    else:
        print("ISIN: " + Fore.RED + "N/A")
    if "major_shareholders" in ticker.info:
        print("Major Shareholders: " + Fore.YELLOW + ticker.info["major_shareholders"])
    else:
        print("Major Shareholders: " + Fore.RED + "N/A")
    if "institutional_holders" in ticker.info:
        print("Institutional Holders:" + Fore.YELLOW + ticker.info["institutional_holders"])
    else:
        print("Institutional Holders: " + Fore.RED + "N/A")
    if "dividend" in ticker.info:
        print("Latest Dividend Payment: " + Fore.YELLOW + ticker.info["dividend"])
    else:
        print("Latest Dividend Payment: " + Fore.RED + "N/A")

    cont()

def financialData():
    print("" + Back.WHITE + Fore.BLACK + " Financial Information about " + ticker.info["shortName"] + " \n")
    global pastOpen
    pastOpen = ticker.history(period="7d")
    print(pastOpen[["Open"]]) # regularMarketOpen
    global df
    df = pd.DataFrame(pastOpen)
    global sigma
    sigma = df["Open"].sum()
    if df.empty:
        print("\nyFinance does not hold data for this stock/fund!")
        cont()
        again()
    cont()

def calculation():
    print("" + Back.WHITE + Fore.BLACK + " Statistical Analysis for " + ticker.info["shortName"] + " \n")
    print("Σx =", sigma)
    global mean
    mean = sigma/7
    print(" x̄ =", mean)
    print(" n =", len(df.axes[0]))
    global stdev
    stdev = df["Open"].std()
    print(" σ =", int(stdev), "(to the nearest integer)")
    cont()

def output():
    lowStdev = mean - stdev
    highStdev = mean + stdev
    print("The standard deviation for the past week is " + Fore.YELLOW + str(int(stdev)) + Fore.RESET + " and the current market price is " + Fore.YELLOW + str(ticker.info["regularMarketPrice"]) + ticker.info["financialCurrency"] + ".\n")
    if ticker.info["regularMarketPrice"] > highStdev:
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
            print("Invalid option, try again")
            cont()

def cont():
    input("\nPress [ENTER] to continue ")
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