#!/bin/py

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math as m

def isPrime(n):

	if n == 2:
		return True

	if n % 2 == 0:
		return False

	for i in range(3, int(m.sqrt(n))+1):
		if n % i == 0:
			return False

	return True

primesum = 0
for i in range(2, 2000000):
	if isPrime(i):
		primesum += i

print(primesum)