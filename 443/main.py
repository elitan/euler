from fractions import gcd
def g(n):
	s = 13
	i = 4
	while i < n:
		if i % 10**7 == 0:
			print(i)
		s += gcd(i+1, s)
		i += 1
	return s
print(g(10**15))