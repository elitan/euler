"""
Guess I should have a lookup table. But it runs under 3 min so meeh
"""
import math
import sys

def trans(n):
	s = 0
	for i in list(str(n)):
		s += math.factorial(int(i));
	return s

def nrOfChains(n):
	l = []
	s = 0
	while n not in l:
		s += 1
		l.append(n)
		n = trans(n)
		if s > 60:
			return 61
	return s

s = 0
for i in range(1, 10**6):
	if i % 10**4 == 0:
		print(i)
	noc = nrOfChains(i)
	if noc == 60:
		s += 1
print(s)