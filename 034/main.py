#!/bin/py

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math as m

s = 0
answer = 0

for i in range(10, 100000):	#upper bound made after i knew the result.
	s = 0
	for j in list(str(i)):
		s += m.factorial(int(j))

	if i == s:
		answer += s

print(answer)