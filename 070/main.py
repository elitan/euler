# -*- coding: utf-8 -*-

"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

import sys
sys.path.append("../")
import functions as f
import fractions
import itertools

def phi(n):
	amount = 0
	for k in range(1, n + 1):
		if fractions.gcd(n, k) == 1:
			amount += 1
	return amount

def isPermutation(n,m):
	nstr = str(n)
	mstr = str(m)
	if len(nstr) == len(mstr):
		nl = list(nstr)
		ml = list(mstr)
		nl.sort()
		ml.sort()
		return nl == ml
	return False

pl = f.primeList(10**7)
print(pl)
