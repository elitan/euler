#!/bin/py

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math as m

def triangleSets(perimeter):
	cList = []
	l = []
	for a in range(1,int(perimeter/2)):
		for b in range(1, int(perimeter/2)):
			c = m.sqrt(a*a + b*b)
			if (a+b+c) == perimeter and c not in cList:
				cList.append(c)
				c = int(c)
				l.append((a,b,c))
	return l

answer = 0
for i in range(3,1001):
	lenTri = len(triangleSets(i))
	if lenTri > answer:
		print(i)
		answer = lenTri

print(answer)		