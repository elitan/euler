# -*- coding: utf-8 -*-
"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""
import math

def hcf(x, y):
	"""This function takes two
	integers and returns the H.C.F"""

	# choose the smaller number
	if x > y:
		smaller = y
	else:
		smaller = x
	for i in range(1,smaller + 1):
		if((x % i == 0) and (y % i == 0)):
			hcf = i
	return hcf

dhigh = 1000000
nn = 1
dd = dhigh
for d in range(dhigh+1, 1, -1):
	for n in range(d*nn/d, d*3/7+1):
	#for n in range(1, d*3/7+1):
		if math.fabs(d*3-n*7) == 1 and hcf(d,n) == 1:
			#print("%s/%s" % (n,d))
			dd = d
			nn = n
print(nn, dd)
