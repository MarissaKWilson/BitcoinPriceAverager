from BitcoinPriceAverager.src.coin import coin


def test_coin():
    tcoin = coin("TestCoin")
    test_add_price(tcoin)
    test_average(tcoin)
    test_add_price(tcoin)

# Tests if prices add to list correctly
# Also tests if list maxes out correctly
def test_add_price(tcoin):
    start_size=len(tcoin.prices)
    tcoin.add_price(.01234565)
    end_size=len(tcoin.prices)
    # Added 1 successfully
    if (start_size+1)==end_size:
        print("Add Price Test Passed")
    # List was already max size
    elif start_size==60 & end_size==60:
        print("Add Price Test Passed")
    else:
        print("Add Price Test Failed")

# Tests averaging function on coin
def test_average(tcoin):
    price=0.01238200
    prices=[]
    totalprice=0.0
    while len(prices) < 60:
        prices.append(price)
        tcoin.add_price(price)
        totalprice += price
        price += 0.00001
    averageprice=totalprice/60
    tcoin.sma()
    if averageprice == tcoin.average:
        print("Average Test Passed")
    else:
        print("Average Test Failed")


if __name__=="__main__":
    test_coin()