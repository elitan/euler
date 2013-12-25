#!/bin/py

"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def sumN(n):
	s = 0
	for nr in str(n):
		s += int(nr)
	return s

answer = 0
for a in range(0, 100):
	for b in range(0, 100):
		if sumN(pow(a,b)) > answer:
			answer = sumN(pow(a,b))
print(answer)