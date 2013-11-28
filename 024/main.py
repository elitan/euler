#!/bin/py

import math as m

def closest(fac, n):

	over = False
	c = 1
	while not over:

		if c * m.factorial(fac) >= n:
			return (c-1, (c-1) * m.factorial(fac))
		c += 1

def appendNext(l, n):
	
	j = 0
	while j < n:

		if j in l:
			n += 1

		j += 1

	appendNextUniq(l, n)

def appendNextUniq(l, n):
	if n in l:
		appendNextUniq(l, n+1)
	else:
		l.append(n)

n = 1000000
l = []

for i in range(9, 0, -1):
	res = closest(i, n)
	n = n - res[1]
	appendNext(l, res[0])

print(l)