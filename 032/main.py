#!/bin/py

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import itertools

def intListToNr(l):
	return int(''.join(map(str,l)))


perm = itertools.permutations([1,2,3,4,5,6,7,8,9])

tempL = []
answer = 0

for span in range(5,10):
	print(span)
	for a in perm:
		for i in range(1,span):
			#print(a[0:2], a[2:3], a)
			x = intListToNr(a[0:i])
			y = intListToNr(a[i:span])
			s = intListToNr(a[span:10])
			z = x*y
			if(s == z and s not in tempL):
				print(a[0:i], a[i:span], a[span:10])
				print(x,y,z)
				tempL.append(s)
				answer += s

print(answer)