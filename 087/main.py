# -*- coding: utf-8 -*-

import sys
import time
import math
from sets import Set

sys.path.append("../")
import functions as f

limit = 50*10**6

pl = f.primeList(int(math.sqrt(limit)))

# initz
aarr = []
barr = []
carr = []
for prime in pl:
	square =  prime**2
	cube = prime**3
	pfourth = prime**4

	aarr.append(square)
	barr.append(cube)
	carr.append(pfourth)

# start
savedNumbers = Set()
counter = 0

for c in carr:
	if c > limit:
		break
	for b in barr:
		if (b+c) > limit:
			break
		for a in aarr:
			if (a+b+c) > limit:
				break
			if a+b+c < limit and (a+b+c) not in savedNumbers:
				savedNumbers.add(a+b+c)
				counter += 1


print("answer: %d" % (counter))