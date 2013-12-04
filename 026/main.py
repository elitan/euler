#!/bin/py

from decimal import *

def recurringCycleDecimal(n):
	n = str(n)[2:]
	return n



getcontext().prec = 600

n = Decimal(1)/Decimal(7)
n = recurringCycleDecimal(n)
print(n)
exit(0)