#!/bin/py

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def fracTest(t,n):
	s = t/n

	t,n = str(t),str(n)
	if '0' in t or '0' in n:
		return False

	#print(t,n,s, int(t[:1]) / int(n[:1]), int(t[:1]) / int(n[1:2]), int(t[1:2]) / int(n[:1]), int(t[1:2]) / int(n[1:2]))

	if t[:1] == n[:1] and s == (int(t[1:2]) / int(n[1:2])):
		return True
	elif t[:1] == n[1:2] and s == (int(t[1:2]) / int(n[:1])):
		return True
	elif t[1:2] == n[:1] and s == (int(t[:1]) / int(n[1:2])):
		return True
	elif t[1:2] == n[1:2] and s == (int(t[:1]) / int(n[:1])):
		return True
	return False


st = 1
sn = 1
for t in range(11, 100):
	for n in range(t, 100):

		if (t%10 != 0 or n%10 != 0) and t != n:
			if fracTest(t,n):
				st *= t
				sn *= n
				#print(t,n)

print(st/sn) #1/100. Answer is 100