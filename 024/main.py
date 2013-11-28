#!/bin/py

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math as m

#find the closest factorial number fac that is <n
def closest(fac, n):

	over = False
	c = 1
	while not over:

		if c * m.factorial(fac) >= n:
			return (c-1, (c-1) * m.factorial(fac))
		c += 1

#append n in l. n++ for every number <n that exists in l
def appendNext(l, n):
	
	j = 0
	while j < n:

		if j in l:
			n += 1

		j += 1

	appendNextUniq(l, n)

#append n in l. if n already exists: n++
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

print(l) #The last zero will not be included.