# Fund Rating
Using past market performance, the script will calculate the standard deviation from the past week, and will then advise buy, sell or hold. The Yahoo Finance API is used, so there may be some limitations on which funds, stocks or shares are able to be scraped, with a further limitation of 100 scrapes per 24 hours at 300 scrapes per minute.

\* **Past performance is not a reliable indicator of future returns. This script does not provide financial advice.** \*

## Installation
1. Install the yahooFinance API 
``` 
pip3 install yFinance 
```
2. Run main.py and enter your ticker symbol with the region designation (such as VUSA.**L** or VUSA.**AS**) to ensure the correct region specific fund is selected.
