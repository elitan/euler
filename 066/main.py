# -*- coding: utf-8 -*-
'''
Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×2^2 = 1
22 – 3×1^2 = 1
92 – 5×4^2 = 1
52 – 6×2^2 = 1
82 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

http://mathworld.wolfram.com/PellEquation.html
https://en.wikipedia.org/wiki/Pell%27s_equation
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Pell.27s_equation

'''

import math

def alist(S):

	aZero = math.floor(math.sqrt(S))
	if math.sqrt(S) == aZero:
		return False

	# initiate
	a = aZero
	m = 0
	d = 1
	c = 0
	l = list()
	l.append(a)

	while a != 2*aZero:
		m = (d * a) - m
		d = (S - m*m) / d
		a = math.floor((aZero+m) / d)
		c += 1
		l.append(a)

	return l

def isPerfectSquare(n):
	return math.sqrt(n) == math.floor(math.sqrt(n))

def contFraction(n, dalist):
	

largestx = 0
dindex = 0

for d in range(2, 1001):

	if isPerfectSquare(d):
		continue

	dalist = alist(d)
	print(dalist)

		

print(largestx, dindex)
