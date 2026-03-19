prices = {}
prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3
print(prices)
stock = {}
stock["pear"] = 15
stock["banana"] = 6
stock["apple"] = 10
stock["orange"] = 32
for item in prices:
    print(item)
    print("Price: {}".format(prices[item]))
    print("Price: {}".format(stock[item]))
    print("--")