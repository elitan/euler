"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

import sys
sys.path.append("../")
import functions as f
import itertools
import copy

# global
count = 0

def minimize(nl, m=0):
	global count

	nnl = copy.deepcopy(nl)
	if len(nnl) < 2:
		return False

	while len(nnl) >= m+2:
		nnl[m] += nnl[m+1]
		del nnl[m+1]
		
		if m == 0 or nnl[m] <= nnl[m-1]:
			print(nnl)
			count += 1
			minimize(nnl, m+1)

n = int(sys.argv[1])
nl = list()

# prepare list
for i in range(0, n):
	nl.append(1)

minimize(nl)

print(count)