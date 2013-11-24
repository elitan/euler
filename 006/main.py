#!/bin/py

import math as m

sumf = 0
suml = 0

for i in range(1, 101):

	sumf += pow(i, 2)

for i in range(1, 101):

	suml += i

suml = pow(suml, 2)

print(suml - sumf)