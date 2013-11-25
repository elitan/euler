#!/bin/py

import math as m

bigNumber = str(int(m.pow(2, 1000)))

sumv = 0
for i in bigNumber:
	sumv += int(i)

print(sumv)