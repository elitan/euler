# -*- coding: utf-8 -*-
"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

import sys
import math
import time

def devisors(n):
	s = 1
	for i in range(2, int(math.ceil(n**0.5))):
		if n % i == 0:
			s += i
			s += int(n/i)
	if math.sqrt(n) == math.floor(math.sqrt(n)):
		s += math.sqrt(n)
	return s

i = 10
longest_c = 0
bad_set = set()

while i < 10**6:
	tmp_i = i
	current_chain = set()
	c = 0
	chain = False
	while True:
		# next link in chain
		tmp_i = int(devisors(tmp_i))

		# not a good road
		if tmp_i in bad_set or tmp_i == 1 or tmp_i > 10**6:
			for number in current_chain:
				bad_set.add(number)
			break
		# inner loop
		if tmp_i in current_chain:
			break

		# all good, continue
		current_chain.add(tmp_i)
		c += 1

		# if we got back to where we started we found a chain
		if tmp_i == i:
			chain = True
			break

	# if the loop broke with a chain, find lowest value
	if chain and c > longest_c:
		longest_c = c
		print("New high score!!")
		print("i: %d, c: %d" % (i, c))
		# find smallest memeber of current_chain
		low = current_chain.pop()
		for number in current_chain:
			if number < low:
				low = number
		print("Smallest element: %d" % low)
	i += 1