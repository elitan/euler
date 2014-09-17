#!/usr/bin/python 

"""
Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import sys
sys.path.append("../")
import functions as f
import itertools

def isPrimePairs(p, q):
	n = int(str(p) + str(q))
	m = int(str(q) + str(p))
	
	if not f.isPrime(n) or not f.isPrime(m):
		return False;
	return True

def acombos(s):

	for x in itertools.combinations(s, 2):
		if not isPrimePairs(x[0], x[1]):
			return False

	return True;

pl = f.primeList(10000000)


a, b, c, d, e = 2, 3, 5, 7, 11

maxTic = 200

while a < maxTic:
	b = 0
	while b < maxTic:
		c = 1
		while c < maxTic:
			d = 2
			while d < maxTic:
				e = 3
				while e < maxTic:

					l = [pl[a], pl[b], pl[c], pl[d], pl[e]]

					if acombos(l):

						print("yes")
						print(l)
						print("")
						sys.exit(0);
					
					e += 1
				d += 1
			c += 1
			print("C: %d" % c)
		b +=1
		print("B: %d" % b)
	a += 1
	print("A: %d" % a)

