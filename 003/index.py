#!/bin/py

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math as m

n = 600851475143
i = 2
arr = []

while i < m.sqrt(n) + 1:
	while n % i == 0:
		arr.append(i)
		n = n / i
     
	i += 1

arr.append(int(n))

print(arr[-1])