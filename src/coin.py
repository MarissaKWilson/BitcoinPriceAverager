class coin():

    def __init__(self, name):
        self.name=name
        self.prices=[]
        self.average = 0.0
        self.refresh_interval=1.0

    # Adds prices to the list of prices
    # removes the oldest price after 60 prices have been added
    def add_price(self, price):
        self.prices.append(price)
        if (len(self.prices)) > 60:
            self.prices.pop(0)

    # Simple Moving Average function
    # Finds the average for the number of items currently in the list
    def sma(self):
        total=0.0
        for p in self.prices:
            total+=float(p)
        self.average = total/len(self.prices)
