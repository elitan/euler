import math
import sys
import gmpy
"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""

def almostEqualTriArea(x, y):
	a = int(math.pow(x, 2))
	b = int(math.pow((y/2),2))
	ps = a-b
	if gmpy.is_square(ps):
		print("Found side:", x)
		return x+x+y
	return 0

def almostEqualTriAreaHandler(x):
	s = 0
	s += almostEqualTriArea(x, x+1)
	s += almostEqualTriArea(x, x-1)
	return s

i = 5
s = 0
while 3*i+1 < 10**int(sys.argv[1]): 
	res = almostEqualTriAreaHandler(i)
	if res > 0:
		s += res
		print("current sum:", s)
		print("")
	i += 2
print("Answer:", s)