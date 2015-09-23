"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

# https://en.wikipedia.org/wiki/Partition_(number_theory)

def p(n):
	available_value = list(xrange(n+1))[1:]
	ways = [1] + [0]*n

	for value in available_value:
		for i in range(value, n+1):
			ways[i] += ways[i-value]
	return ways[n]

i = 5500

while p(i) % 10**6 != 0:
	i += 1
	print(i)