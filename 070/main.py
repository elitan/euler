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

def transformPrime(primeList):
	pl = list()

	for p in primeList:
		found = False
		for k in pl:
			if p == k[0]:
				k[1] += 1
				found = True
		if not found:
			pl.append([p,1])
	return pl

def phi(pl):
	s = 1
	for p in pl:
		s *= (p[0]**p[1]) - (p[0]**(p[1]-1))
	return s

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

#pl = f.primeList(10**7)
#print(pl)


"""
create primeFac function: primeFac2(n, pl).

return list type: [[2,3],[3,1]] for 2^3 * 3^1

ezpz calculate phi.

phi(2^3 * 3^1) = phi(2^3) * phi(3^1) = (2^3 - 2^2) * (3^1-3^0) = (8-4)*(3-1) = 4*2 = 8
"""
m = 10**6
iindex = 0
for i in range(2, 10**7):
	phiTmp = phi(transformPrime(f.primeFac(i)))
	ratTmp = float(i) / phiTmp

	if ratTmp < m and isPermutation(i, phiTmp):
		m = ratTmp
		iindex = i
		print("New record!", i, phiTmp, ratTmp)