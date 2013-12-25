#!/bin/py

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def sameDigits(a,b):
	return sorted(list(str(a))) == sorted(list(str(b)))

for i in range(1, 1000000):
	found = True
	for j in range(2,7):

		if not sameDigits(i, i*j):
			found = False
			break

	if found:
		print(i)
		break