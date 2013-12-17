#!/bin/py

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import sys
sys.path.append("../")
import functions as f

def isTruncatablePrime(n):
	n = str(n)
	if ('2' in n or '4' in n or '6' in n or '8' in n) and len(n) > 2:
		return False
	for a in range(1, len(n)):
		if not f.isPrime(int(n[0:a])):
			return False;
		if not f.isPrime(int(n[a:len(n)])):
			return False;
	return True

pl = f.primeList(1000000)

answer = 0
for p in pl:
	if isTruncatablePrime(p) and p > 7:
		answer += p

print(answer)
