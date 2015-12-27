# -*- coding: utf-8 -*-
"""
A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
"""
import sys
sys.path.append("../")
import functions as f
import math
import itertools

target = 10**8
pl = f.primeList(int(target / 2))

#sys.exit()

s = 0
for i in xrange(0, len(pl)):
	#print("current list: ", pl[i:i+1], pl[i:])
	c = 0
	for a,b in itertools.product(pl[i:i+1], pl[i:]):
		if a * b < target:
			#print(a,b)
			s += 1
		else:
			if c == 0:
				print(s)
				sys.exit()
			break
		c += 1
print(s)