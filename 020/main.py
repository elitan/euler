#!/bin/py

import math as m

sumv = 0
for i in str(m.factorial(100)):
	sumv += int(i)

print(sumv)