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
import sys

def isPerfectSquare(n):
	nsqrt = math.sqrt(n)
	return nsqrt == math.floor(nsqrt)

def converg(n):
	#0
	az = math.floor(math.sqrt(n))
	p = az
	p2 = p
	q = 1
	q2 = q
	k = 0 # P
	l = 1 # Q

	#print("%s^2 - %s*%s^2 = %s" % (p,n,q,p**2-n*q**2))

	#1
	k = az
	l = n - az**2
	a = math.floor( (az + k ) / l)
	p = az*a + 1
	q = a

	while p*p - n*q*q != 1:

		#print("%s^2 - %s*%s^2 = %s" % (p,n,q,p**2-n*q**2))
		ptmp = p
		qtmp = q

		# start
		k = int(a * l - k)
		l = int((n - k*k) / l)

		a = int(math.floor( (az + k ) / l))
		try:
			p = int(a*p+p2)
			q = int(a*q+q2)
		except:
			#print("DID NOT WORK...", p,q)
			break


		# ...
		p2 = ptmp
		q2 = qtmp

	return p,q

xlargest = 0
iindex = 0
for i in range(2, 1001):
	if isPerfectSquare(i):
		continue
	x,y = converg(i)
	#print(i, x, y)
	if x > xlargest:
		print("NEW RECORD", i, x)
		xlargest = x
		iindex = i

print(iindex, xlargest)

