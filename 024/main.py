#!/bin/py

import math as m

def closest(fac, n):

	over = False
	c = 1
	while not over:

		if c * m.factorial(fac) >= n:
			return (c-1, (c-1) * m.factorial(fac))
		c += 1

def appendNext(l1, l2, n):
	
	l1.append(n)

n = 1000000
l1 = []
l2 = []

for i in range(9, 0, -1):
	res = closest(i, n)
	n = n - res[1]
	print(res[0])
	appendNext(l1, l2, res[0])

print(l1)