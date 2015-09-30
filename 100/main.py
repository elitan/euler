# -*- coding: utf-8 -*-
"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""
import sys
sys.path.append("../")
import functions as f


k = 10**12
s = (k * (k-1)) / 2

b = 1
while (b * b) - b < s:
	a = (b * b) - b
	if a % 10000000 == 0:
		print(a)
		print(s)
	b += 1
