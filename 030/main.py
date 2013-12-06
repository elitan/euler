#!/bin/py

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import math as m

def fivePowSum(n):

	s = 0
	for i in str(n):
		s += m.pow(float(i), 5)

		if s > n:
			break

	if s == n:
		return 1
	else:
		return 0

answer = 0
for i in range(10, 1000000):
	if(fivePowSum(i)):
		answer += i
		#print(i)

print(answer)