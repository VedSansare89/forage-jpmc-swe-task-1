import json
import random
import urllib.request
import time

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

prices = {}  # Dictionary to store stock prices


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Taking the average of bid and ask prices
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Storing the price in the prices dictionary
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        if 'ABC' in prices and 'DEF' in prices:  # Checking if both stocks are present in the prices dictionary
            ratio = getRatio(prices['ABC'], prices['DEF'])
            print("Ratio %s" % ratio)
        else:
            print("Unable to calculate ratio, data missing")

        time.sleep(1)  # Sleep for 1 second before querying again

