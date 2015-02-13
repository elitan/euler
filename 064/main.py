#!/bin/python

"""
to long...
"""

import math

def isOddDecimals(S):

	aZero = math.floor(math.sqrt(S))

	if math.sqrt(S) == aZero:
		return False

	a = aZero
	m = 0
	d = 1
	c = 0

	while a != 2*aZero:

		m = (d * a) - m
		d = (S - m*m) / d
		
		if d == 0:
			print(S, m, d)

		a = math.floor((aZero+m) / d)

		c += 1

	return c % 2 == 1


c = 0
for i in range(2, 10000):

	if isOddDecimals(i):
		c += 1
print(c)
