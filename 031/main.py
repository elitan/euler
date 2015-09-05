#!/bin/py

"""
In England the currency is made up of pound, , and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).
It is possible to make 2 in the following way:

1x1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 2 be made using any number of coins?
"""

#https://www.youtube.com/watch?v=_fgjrs570YE

target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1] + [0]*target

for coin in coins:
	for i in range(coin, target+1):
		ways[i] += ways[i-coin]
print(ways[target])