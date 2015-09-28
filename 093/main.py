# -*- coding: utf-8 -*-
"""
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a &lt; b &lt c &lt d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
"""
import sys
import itertools
import time

sys.path.append("../")
import functions as f

def perm_parenthesis(s):
	ret_array = []

	ret_array.append(("%s" % s))

	ret_tmp = "(((%s)%s)%s)" % (s[0:7], s[7:11], s[11:])
	ret_array.append(ret_tmp)

	ret_tmp = "(%s)%s(%s)" % (s[0:7], s[7:8], s[8:])
	ret_array.append(ret_tmp)

	ret_tmp = "(%s)%s" % (s[0:11], s[11:])
	ret_array.append(ret_tmp)

	return ret_array


perm_numbers = list(itertools.combinations([str(float(i)) for i in range(1, 10)], 4))

sum_set = set()
highest = 0
highest_numbers = 0;
highest_sum_set = 0;

for n in perm_numbers:
	#n = [4.0, 5.0, 6.0, 8.0]
	sum_set = set()
	for number in itertools.permutations(n):
		comb_with_replacement_operators = itertools.combinations_with_replacement("*/+-", 3)
		for op in comb_with_replacement_operators:
			perm_operators = set(itertools.permutations(list(op)))
			for operator in perm_operators:
				# create string of numbers and operators
				s = ""
				s += "%s%s" % (number[0], operator[0])
				s += "%s%s" % (number[1], operator[1])
				s += "%s%s" % (number[2], operator[2])
				s += "%s" % (number[3])
				for perm in perm_parenthesis(s):
					try:
						res_tmp = eval(perm)
						if res_tmp == int(res_tmp):
							sum_set.add(abs(int(round(eval(perm)))))
					except:
						pass
	
	i = 1
	while i in sum_set:
		i += 1
	if i-1 > highest:
		highest = i-1
		highest_numbers = [int(float(i)) for i in list(n)]
		highest_sum_set = sum_set
		print(highest)
		print(highest_numbers)
		print(highest_sum_set)