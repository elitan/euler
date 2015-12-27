# -*- coding: utf-8 -*-
"""
Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""
import sys
sys.path.append("../")
import functions as f

s = 0
target = 10**7
prev_div = 0
for i in xrange(1, target):
	cur_div = len(f.primeFac(i))
	if prev_div == cur_div:
		#print(i-1, i)
		s += 1
	prev_div = cur_div
print(s)



