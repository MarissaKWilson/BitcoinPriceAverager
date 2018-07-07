import binance
from coin import coin
import threading
import time


# Run every second to update prices and find average
def update_prices(coins):
    prices = binance.prices()
    for c in coins:
        price = prices.get(c.name)
        c.addPrice(price)
        # Coins have their own average function
        c.sma()
        print("Coin: " + c.name + " SMA: " + str(c.average) + " Current Price: " + price)


# Make initial coin objects, list of objects will be passed around
def initialize_coins():
    coins=[]

    # gives a dictionary which coin name as key and price as value
    prices = binance.prices()
    coinNames = list(prices.keys())
    for c in coinNames:
        # Create coin and add starting price
        tmpcoin = coin(c)
        tmpcoin.addPrice(prices.get(c))
        coins.append(tmpcoin)
    return coins

# Handles thread sleeping and prints time interval
def coinThread(coins):
    seconds=1;
    while True:
        update_prices(coins)

        # Convert seconds to minutes and seconds
        minutes=int(seconds/60)
        print_seconds=seconds%60
        print("Running for " + str(minutes) + " minutes and " + str(print_seconds) + " seconds")
        seconds+=1

        # Sleeps process for 1 second
        time.sleep(1)


if __name__=="__main__":
    coins=initialize_coins()
    threading.Thread(target=coinThread(coins)).start()