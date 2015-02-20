# -*- coding: utf-8 -*-
"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

"""

import math
import sys
import re

def match(n):
	a = re.compile("^1[0-9]2[0-9]3[0-9]4[0-9]5[0-9]6[0-9]7[0-9]8[0-9]9$")
	return a.match(str(n))

x = 100000003 #int(math.sqrt(10203040506070809))
while x < 138902662:
	if match(x*x):
		print("FOUND: %s" % (x*10))
		sys.exit()
	x += 10

x = 100000007 #int(math.sqrt(10203040506070809))
while x < 138902662:
	if match(x*x):
		print("FOUND: %s" % (x*10))
		sys.exit()
	x += 10

print("FOUND: %s" % (x*10))
