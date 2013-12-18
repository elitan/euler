#!/bin/py

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools
perm = itertools.permutations(list("0123456789"))

def intListToNr(l):
	return int(''.join(map(str,l)))

def isSubStringDiv(n):
	n = str(n)
	c = n[1:2] + n[2:3] + n[3:4]
	if int(c) % 2 != 0:
		return False
	c = n[2:3] + n[3:4] + n[4:5]
	if int(c) % 3 != 0:
		return False
	c = n[3:4] + n[4:5] + n[5:6]
	if int(c) % 5 != 0:
		return False
	c = n[4:5] + n[5:6] + n[6:7]
	if int(c) % 7 != 0:
		return False
	c = n[5:6] + n[6:7] + n[7:8]
	if int(c) % 11 != 0:
		return False
	c = n[6:7] + n[7:8] + n[8:9]
	if int(c) % 13 != 0:
		return False
	c = n[7:8] + n[8:9] + n[9:10]
	if int(c) % 17 != 0:
		return False
	return True
answer = 0
for a in perm:
	if isSubStringDiv(intListToNr(a)):
		answer += intListToNr(a)

print(answer)