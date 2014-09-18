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

def checkListForPairs(l):
	for x in range(0, len(l)-1):
		if not isPrimePairs(l[x], l[-1]):
			return False;

	return True;

def recF(l, d):

	global c

	ls = list(l)
	ls.append(pl[d])

	#basecase
	if d == 5:
		print("FOUND IT")
		print(ls[:-1])
		print("sum: %d" % sum(ls[:-1]))
		print("C: %d" % c)
		sys.exit()
		return 0
	
	for x in range(d, len(pl)):
		c += 1
		ls[-1] = pl[x]
		#print(l, x)
		if checkListForPairs(ls):

			recF(ls, d+1)

pl = f.primeList(9000)
l = list()

c = 0
recF(l, 0)
print("found nothing. c: %d" % c)