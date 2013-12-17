#!/bin/py

"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def isPalindromic(n):
	n = str(n)
	i = 0

	while i < len(n)/2:
		if n[0 + i] != n[len(n) - 1 - i]:
			
			return False
		i += 1

	return True

def decToBinStr(n):
	return str(bin(n)[2:])	

answer = 0
for i in range(1, 1000000):
	if isPalindromic(i) and isPalindromic(decToBinStr(i)):
		answer += i

print(answer)