# -*- coding: utf-8 -*-
"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
from decimal import *
import sys


getcontext().prec = 102
answer = 0
i = 2
while i < 100:

	if int(i**0.5) == i**0.5:
		i += 1
		continue

	a = str(Decimal(i).sqrt())[:101]
	a = a.replace('.', '')
	#a = str(Decimal(i) ** Decimal('0.5'))[:101]

	for n in a:
		answer += int(n)
	#sys.exit()
	print(i, answer)
	i += 1

print(answer)