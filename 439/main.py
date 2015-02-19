import sys
import math as m

def d(n):	
	if n == 1:
		return 1
	s = 1
	s += n
	for i in range(2, int(m.ceil(n**0.5))):
		if n % i == 0:
			s += i
			s += int(n/i)

	if m.sqrt(n) == m.floor(m.sqrt(n)):
		s += m.sqrt(n)

	return int(s)

def s(n):
	sum = 0
	#over diagonal
	for i in range(1, n+1):
		for j in range(i+1, n+1):
			#print("i: %s, j: %s, d(%s) = %s" % (i, j, (i*j), d(i*j)))
			sum += d(i*j)
	sum *= 2

	#diagonal
	for i in range(1, n+1):
			sum += d(i*i)

	return sum


print(s(3))