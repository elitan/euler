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

"""

# https://en.wikipedia.org/wiki/Partition_(number_theory)
https://en.wikipedia.org/wiki/Pentagonal_number

p(n) = p(n-1) + p(n-2) + p(n-5)

where 1,2,5 are generalized pentagonal numbers.

"""

import sys

def gpn(n):
	return (3 * n * n - n) / 2

def p(n, i):
	if n - gpnlist[i] < 0:
		return 0
	else:
		if i % 4 <= 1: # use plus
			return plist[n-gpnlist[i]] + p(n, i+1)
		else:
			return -1 * plist[n-gpnlist[i]] + p(n, i+1)

# p(0)
plist = [1]
gpnlist = []

for i in range(1,100000):
	gpnlist.append(gpn(i))
	gpnlist.append(gpn(-i))

n = 1
pn = 1
while pn % 10**6 != 0:
	pn = p(n, 0)
	plist.append(pn)
	n += 1

print(n-1)