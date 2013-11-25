#!/bin/py

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math as m

def isPythagoreanTriplet(a, b, c):
	if m.pow(a, 2) + m.pow(b, 2) == m.pow(c, 2):
		return True
	else:
		return False

a = 1

while a < 1000:
	b = a+1
	while b < 1000:
		c = b+1
		while c < 1000:
			if a + b + c == 1000 and isPythagoreanTriplet(a, b, c):

				print("a: %d, b: %d, c: %d. Product: %d" % (a, b, c, (a*b*c)))
				exit(0)				
			c += 1
		b += 1
	a += 1
