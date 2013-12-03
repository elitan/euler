#!/bin/py

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from decimal import *

def findRecurringCyckleDecimal(n):
	n = str(n)[2:]

	for i in range(3, 5000):
		if recurringCycle(n, i):
			return i-1

	return False

def recurringCycle(n, i):
	s = len(n)%i*-1

	if s != 0:
		n = n[:s]

	comp = n[0:i-1]
	#print("Comp: ", comp)

	for c in range(1, int(len(n)/i)):
		#print(n[(i-1)*c:(i-1)*c + i-1])
		if comp != n[(i-1)*c:(i-1)*c + i-1]:
			return False

	return True


highest = 0
getcontext().prec = 10000
for i in range(2, 1001):

	n = Decimal(1)/Decimal(i)

	cykel = findRecurringCyckleDecimal(n)

	if cykel > highest:
		highest = i

print(highest)
