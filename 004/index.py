#!/bin/py

import math as m

def isPalindromic(n):
	ret = False
	n = str(n)
	i = 0

	if len(n)%2 == 0 and len(n) >= 2:

		ret = True
		while i < len(n)/2 and ret:
			if n[0 + i] != n[len(n) - 1 - i]:
				
				ret = False
			i += 1

	return ret

largest = 0

for i in range(100, 999):
	for j in range(100, 999):

		k = i * j
		if isPalindromic(k):
			if k > largest:
				largest = k
print(largest)