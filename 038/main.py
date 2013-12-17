#!/bin/py

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def isPandigital(n):
	n = str(n)

	if '0' in n:
		return False

	temp = []
	for c in n:
		if c in temp:
			return False
		else:
			temp.append(c)
	return True

def pandigitalMultiples(n):
	allNr = list("123456789")
	i = 1
	s = ""

	while len(s) < 9:

		s += str(n*i)
		i += 1
		#print(s)

	if len(s) != 9:
		return False
	elif isPandigital(s):
		return int(s)
	else:
		return False

m = 0

for i in range(0, 9876):

	n = pandigitalMultiples(i)
	if n != False and n > m:
		m = n

print(m)