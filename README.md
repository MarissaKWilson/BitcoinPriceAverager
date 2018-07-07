# BitcoinPriceAverager
A python program for averaging bitcoin prices.

Uses a Simple Moving Average and the Binance python API.

By default all coins refresh every second and provide an average of the past minute of prices
Coins are created as an object so in the future individual coins can have custom refresh times.

Running the program is as simple as calling navigating to the folder and calling Python BitcoinPriceAverager/src/main.py

If the program runs as expected the output will be similar to below:

Coin: NPXSBTC, SMA: 0.00000062, Current Price: 0.00000062
Coin: NPXSETH, SMA: 0.00000856, Current Price: 0.00000856
Coin: VENUSDT, SMA: 2.44460000, Current Price: 2.44460000
Coin: KEYBTC, SMA: 0.00000325, Current Price: 0.00000325
Coin: KEYETH, SMA: 0.00004559, Current Price: 0.00004559
Coin: NASBTC, SMA: 0.00067780, Current Price: 0.00067780
Coin: NASETH, SMA: 0.00953500, Current Price: 0.00953500
Coin: NASBNB, SMA: 0.32588000, Current Price: 0.32588000
Coin: MFTBTC, SMA: 0.00000241, Current Price: 0.00000241
Coin: MFTETH, SMA: 0.00003388, Current Price: 0.00003388
Coin: MFTBNB, SMA: 0.00116000, Current Price: 0.00116000
Coin: DENTBTC, SMA: 0.00000096, Current Price: 0.00000096
Coin: DENTETH, SMA: 0.00001333, Current Price: 0.00001333
Running for 0 minutes and 2 seconds