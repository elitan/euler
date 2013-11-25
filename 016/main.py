#!/bin/py

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import math as m

bigNumber = str(int(m.pow(2, 1000)))

sumv = 0
for i in bigNumber:
	sumv += int(i)

print(sumv)