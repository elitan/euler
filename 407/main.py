# -*- coding: utf-8 -*-
"""
If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a2 ≡ a (mod n).
So M(6) = 4.

Find SUMM(n) for 1 ≤ n ≤ 107.
"""

import math

def isPrime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		#print(f)
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True  

def m(n):
	if isPrime(n):
		return 1
	a = n-1
	nsqrt = math.sqrt(n)
	#while a*(a-1) % n != 0 and a > nsqrt:
	while pow(a,2,n) != a:
		print("%s = %s %% %s (%s)" % (a**2, a, pow(a,2,n), n))
		a -= 1
	#if a <= nsqrt:
		#return 1
	print("FOUND: %s = %s %% %s (%s)" % (a**2, a, pow(a,2,n), n))
	return a

for i in range(1,10):
	m(i)