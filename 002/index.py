#!/bin/py
n = 4000000
s = 0
a, b = 0, 1


while b < n:
	if b % 2 == 0:
		s += b
	a, b = b, a+b

print(s)