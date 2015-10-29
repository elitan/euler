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

def usePlus(i):
	i = i % 4
	return i == 0 or i == 3

def p(n, i):
	if n - gpnlist[i] < 0:
		return 0
	else:
		print("#######")
		print("n", n)
		print("i", i)
		print("gpnlist[i]", gpnlist[i])
		print("plist", plist)
		print(plist[n-gpnlist[i]])
		if usePlus(i):
			print("+")
			return plist[n-gpnlist[i]] + p(n, i+1)
		else:
			print("-")
			return plist[n-gpnlist[i]] - p(n, i+1)

# p(0)
plist = [1]
gpnlist = []

for i in range(1,10):
	gpnlist.append(gpn(i))
	gpnlist.append(gpn(-i))

for n in range(1, 6):
	print("NEW NNNNNNNNNNNN")
	res = p(n, 0)
	plist.append(res)
	print("RES:", n, res)

print(plist)