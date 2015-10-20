"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import sys
import math as m

def isPythagoreanTriplet(a, b, c):
	return m.pow(a, 2) + m.pow(b, 2) == m.pow(c, 2)

def pythagorean_triplet(s):
	for a in range(1, s):
		for b in range(1, s):
			c = s - a - b
			if isPythagoreanTriplet(a,b,c):
				return a*b*c

r = pythagorean_triplet(1000);

print(r)
