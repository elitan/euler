#!/bin/py

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

import sys
sys.path.append("../")
import functions as f

mV = 4
found = False
i = 2
while not found:
	i += 1
	if len(list(set(f.primeFac(i)))) == mV:
		#print("1: %d" % i)
		#print(f.primeFac(i))
		found = True
		for j in range (1,mV):
			#print("1.%d: %d" % (j, i+j))
			#print(f.primeFac(i+j))
			if len(list(set(f.primeFac(i+j)))) != mV:
				found = False
				break
print(i)
