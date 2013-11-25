#!/bin/py

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math as m

n = 0;
count = 0
found = False

print("Starting...");
#exit(0)

while not found:

	n += 20
	ok = True
	i = 1
	
	while ok and i < 21:
		if n%i != 0:
			ok = False
		i += 1

	if ok:
		found = True


print(n);