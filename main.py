import requests

url = "https://yfapi.net/v6/finance/quote"

ticker = input("Enter the ticker you would like a rating of: ")

querystring = {"symbols": ticker}

headers = {
    'x-api-key': "YCTzB50g5m3n2HUE6R8lYpSKCnzRF4BL4W1GAd00"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)