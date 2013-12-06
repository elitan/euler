#!/bin/py



import math as m

def fivePowSum(n):

	s = 0
	for i in str(n):
		s += m.pow(float(i), 5)

		if s > n:
			break

	if s == n:
		return 1
	else:
		return 0

answer = 0
for i in range(10, 1000000):
	if(fivePowSum(i)):
		answer += i
		#print(i)

print(answer)