import math
import sys
import gmpy
"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""

def almostEqualTri(x, y):
	if gmpy.is_square(x**2-(y/2)**2):
		print("found %d" % x)
		return x+x+y
	return 0

def almostEqualTriHandler(x):
	return almostEqualTri(x, x+1) + almostEqualTri(x, x-1)

i = 5
s = 0
while 3*i+1 < 10**int(sys.argv[1]): 
	r = almostEqualTriHandler(i)
	if r > 0:
		s += r
		print("current sum: %d" % s)
		print("")
	i += 2
print("Answer: %d" % s)