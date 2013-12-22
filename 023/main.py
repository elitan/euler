#!/bin/py

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import sys
sys.path.append("../")
import functions as f

def isAbundant(n):
	return sum(f.devisorsSlow(n)) > n

l = [1] * 28123
an = []

for i in range(12, 28124):
	if isAbundant(i):
		an.append(i)

for a in an:
	for b in an:
		try:
			l[a+b] = 0
		except:
			pass

answer = 0
for i,c in enumerate(l):
	if c == 1:
		answer += i

print(answer)