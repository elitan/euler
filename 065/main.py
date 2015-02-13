#!/bin/python
# -*- coding: utf-8 -*-

"""
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

täljare = numerator
nämnare = denumerator

"""

import math

def getFractionRecursion(l, numerator, denumerator):

	if len(l) == 1:
		return numerator, denumerator

	numerator, denumerator = denumerator, numerator
	numerator = (l[-2]*denumerator) + numerator
	return getFractionRecursion(l[:-1], numerator, denumerator)

def getFraction(l):

	return getFractionRecursion(l, l[-1], 1)

def eList(n):

	l = list();
	l.append(2)

	i = 1

	while len(l) < n:
		l.append(1)
		l.append(2*i)
		l.append(1)
		i += 1

	return l[:n]

el = eList(100)

fract = getFraction(el)

print(sum(map(int, str(fract[0]))))