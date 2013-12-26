#!/bin/py

"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

import sys
import itertools
sys.path.append("../")
sys.stdout.flush()
import functions as f


def perm(k,n):

	initP = ""
	newL = []

	for i in range(k):
		initP += "1"
	for i in range(0, len(str(n))-k):
		initP += "0"

	t = itertools.permutations(initP)

	for n in t:
		newL.append(n)

	newL = list(set(newL))
	return newL

"""
i = the number that will be the replacer
l = list that explains where we should replace numbers.
n = number that we will work with.
"""
def replace(i, l, n):
	newN = ""
	n = [int(x) for x in str(n)]
	for a,b in enumerate(n):
		if int(l[a]):
			newN += str(i)
		else:
			newN += str(b)
	newN = int(newN)
	return newN


pl = f.primeList(1000000)
low = 999999999

for p in pl:
	#print("Testing prime: %d" % p)
	for i in range(1, len(str(p))):
		lists = perm(i, p)
		for l in lists:
			#print("### %d ###" % p)
			c = 0
			cc = 0
			for j in range(0,10):
				cc += 1
				#print(j,l,p)
				primeTest = replace(j,l,p)
				if len(str(primeTest)) == len(str(p)) and f.isPrime(primeTest):
					c += 1
					#	print("%d:%d. Prime found: %d" % (c, cc, replace(j,l,p)))
				if cc-c > 2:
					break
			if c == 8:
				#print("PRIME: %d, nr: %d" % (p, c))
				for j in range(0,10):
					#print(j,l,p)
					primeTest = replace(j,l,p)
					if f.isPrime(primeTest):
						print(primeTest)
						exit(0)		