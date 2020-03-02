# IFT458
# Project Deliverable 5
# pd5.py

import urllib.request
import json
import datetime


def getStockData(symbol):
    try:
        stockURL = 'http://www.alphavantage.co/query?function=GLOBAL_QUOTE&apikey=apidemo&symbol='+symbol

        connection = urllib.request.urlopen(stockURL)
        stockJSON = connection.read().decode()

        print("JSON  String: ", stockJSON)

        stockDictionary = json.loads(stockJSON)

        return stockDictionary
    except Exception as stockError:
        raise Exception("Error retrieving stock price", stockError)


def main():
    f = open("japi.out", "w")
    f.write("Beginning Stock Price Listing. Current Time: " +
            str(datetime.datetime.now()) + "\r\n")
    f.close()

    while True:

        symbol = input("Please enter stock ticker >> ")

        if symbol.lower() == 'quit':
            exit()
        else:
            try:
                stockInfoDict = getStockData(symbol)

                if stockInfoDict.get("Error Message") is None:

                    topNode = stockInfoDict.get("Global Quote")

                    outStr = "The current price of", symbol, "is:", topNode['05. price']

                    print(' '.join(outStr))

                    f = open("japi.out", "a")
                    f.write(' '.join(outStr) + "\r\n")
                    f.close()
                    print("Stock Quotes retrieved successfully!")

            except Exception as stockError:
                print("Error", stockError)


if __name__ == "__main__":
    main()
