"""
In the following equation x, y, and n are positive integers.

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.

xy / (x+y) = n.

1 + 1 = n
x   y

y * n = k

k % y-1 == 0

"""
import sys
import time

def isDenominator(denumerator, n):
	numerator = denumerator * n
	return numerator % (denumerator - 1) == 0

def find_next_n(n, h, saved_set):
	#print("in find_next_n")
	#print(n, h)
	for prev in saved_set:
		n_tmp = n + prev
		s = 0
		for d in range(2, n_tmp):
			if isDenominator(d,n_tmp):
				s += 1
		if s > h:
			saved_set.add(n_tmp)
			#print(n_tmp, s)
			return s, n_tmp

n = 6
h = 0
saved_set = set()
saved_set.add(n)
while h < 1000:
	print(n, h)
	h, n = find_next_n(n, h, saved_set)
	#time.sleep(0.5)