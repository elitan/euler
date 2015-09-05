# -*- coding: utf-8 -*-
"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""
import sys
sys.path.append("../")
import functions as f

def p(n, values):
	ways = [1] + [0]*n

	for value in values:
		for i in range(value, n+1):
			ways[i] += ways[i-value]
	return ways[n]


i = 10
while p(i, f.primeList(i)) < 5000:
	i += 1
print(i)