# IFT458
# Project Deliverable 5
# pd5.py

import urllib.request
import json

def getStockData(symbol):
    try:
        stockURL = 'http://www.alphavantage.co/query?function=GLOBAL_QUOTE&apikey=apidemo&symbol='+symbol

        connection = urllib.request.urlopen(stockURL)
        stockJSON = connection.read().decode()

        print("JSON  String: ",stockJSON)

        stockDictionary = json.loads(stockJSON)

        return stockDictionary
    except Exception as stockError:
        raise Exception("Error retrieving stock price",stockError)

def main():

    while True:

        symbol = input("Please enter stock ticker >> ")

        if symbol == 'quit':
            exit()
        else:
            try:
                stockInfoDict = getStockData(symbol)

                topNode = stockInfoDict.get("Global Quote")

                print("The current price of",symbol,"is:", topNode['05. price'])

            except Exception as stockError:
                print("Error",stockError)


if __name__ == "__main__":
    main()
