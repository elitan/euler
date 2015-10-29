# -*- coding: utf-8 -*-
"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""
import sys
sys.path.append("../")
import functions as f

# s = k^2 - k
def findB(s):
	b = 1
	while (b*b - b) * 2 < s:
		b+=1
	return (b*b - b) * 2 == s, b

k = 15

while k < 2500000:
	res = findB(k*k-k)
	if res[0]:
		print(res[1], k)
	k += 1

