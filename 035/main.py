#!/bin/py

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import sys
sys.path.append("../")
import functions as f

#Sieve of Eratosthenes
def primeList(top):
	primes = []
	a = [2] * top
	a[0] = 0
	a[1] = 0
	a[2] = 1
	p = 2

	while p < top:
		a[p] = 1

		for n in range(p*2, top, p):
			a[n] = 0
		p = findNextIndex(a, p, top)

	for p in range(0, top):
		if a[p] == 1:
			primes.append(p)

	return primes


def findNextIndex(a, n, top):
	n += 1
	try:		
		while a[n] != 2:
			n += 1
	except:
		return top

	return n

def circularPrime(p):
	if '0' in str(p):
		return False

	for n in range(0, len(str(p))-1):
		p = nextCircularNumber(p)
		if not f.isPrime(p):
			return False

	return True

def nextCircularNumber(n):
	l = list(str(n))
	nl = [0] * len(l)
	
	for index, n in enumerate(l):
		nl[index - 1 % len(l)] = n

	return int(''.join(nl))

answer = 0
pL = primeList(1000000)

for p in pL:
	if circularPrime(p):
		print(p)
		answer += 1

print("Correct answer is: %d" % answer)