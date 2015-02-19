from fractions import gcd

def g(n):
	s = 13
	i = 4
	while i < n:
		s += gcd(i+1, s)
		i += 1
	return s

g(10**7)