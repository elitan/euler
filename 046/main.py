#!/bin/py

"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import sys
sys.path.append("../")
import functions as f

def isGoldbachNr(n, l):
	for prime in l:
		if prime > n:
			return False
		#print(prime)
		i = 0
		found = False
		while not found:
			i += 1
			#print("Testing n: %d prime: %d, i: %d. 2*i^2:%d" % (n, prime, i, (2*pow(i,2))))
			if prime + 2*pow(i,2) > n:
				break
			elif n == prime + 2*pow(i,2):
				#print("Found: %d, %d" % (prime, i))
				return True

maxV = 10000
l = f.primeList(maxV)

answer = 0
for n in range(2, maxV):
	if n not in l and n % 2 == 1:
		if not isGoldbachNr(n,l):
			answer = n
			break

print(answer)
