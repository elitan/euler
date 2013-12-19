#!/bin/py

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import sys
sys.path.append("../")
import functions as f
import itertools

def isPerm(a,b,c):
	perm = itertools.permutations(list(str(a)))

	f1,f2 = False, False
	for p in perm:
		if int(''.join(map(str,p))) == b:
			f1 = True
		if int(''.join(map(str,p))) == c:
			f2 = True

	if f1 and f2:
		return True
	return False

pl = f.primeList(10000)

for i, pA in enumerate(pl):
	if pA > 999:
		for iB in range(i+1, len(pl)):
			pC = 2 * pl[iB] - pA
			if pC in pl and isPerm(pA, pl[iB], pC):
				print("%d%d%d (%d)" % (pA, pl[iB], pC, pl[iB] - pA))