# Stocks and Funds Rating
Using past market performance, the script will calculate the standard deviation from the past week, and will then advise buy, sell or hold. The yFinance API is used, which is an unofficial Yahoo Finance scraping API so there are some limitations on what is able to be requested. Furthermore, as yFinance is not actively maintained, this script is subject to breaking if yFinance changes any of its layout.

\* **Past performance is not a reliable indicator of future returns. This script does not provide financial advice.** \*

## Installation
1. Install the dependancies 
``` 
pip3 install yFinance colorama pandas
```
2. Run main.py and enter your ticker symbol
