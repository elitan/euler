"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

import sys

target = 100
available_value = list(xrange(target))[1:]
ways = [1] + [0]*target

for value in available_value:
	for i in range(value, target+1):
		ways[i] += ways[i-value]
print(ways[target])