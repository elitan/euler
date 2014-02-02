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
	i = 0

	while i < len(s):
		j = i + 1
		while j < len(s):

			if not isPrimePairs(s[i], s[j]):
				return False
			j += 1
		i += 1
	return True


pl = f.primeList(10000000)
s = [3, 7, 109, 673, 11]

i = 5
while not acombos(s):
	try:
		s[4] = pl[i]
		i += 1
	except:
		print("Nope...");
		exit(0)

if acombos(s):
	print(s)