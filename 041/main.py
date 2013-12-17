#!/bin/py

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import sys
sys.path.append("../")
import functions as f
import itertools

t = 0
n = list("1")

while len(n) < 10:
	perm = itertools.permutations(n)

	for nr in perm:
		t = int(''.join(map(str,nr)))
		if f.isPrime(t):
			answer = t
	n.append(len(n)+1)

print(answer)