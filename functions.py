import math as m

def primeFac(n):
	i = 2
	arr = []

	while i < m.sqrt(n) + 1:
		while n % i == 0:
			arr.append(i)
			n = n / i
	     
		i += 1

	arr.append(int(n))

	return arr


def devisorsOld(n):
	dev = 0
	for i in range(2, int(m.ceil(n**0.5))):
		if n % i == 0:

			dev += 1

	#*2 + 1 and n
	dev = dev * 2 + 2

	#if perfect square
		#dev += 1
	return dev

def devisorsSlow(n):

	dev = []

	for i in range(1, int(n/2+1)):
		if n % i == 0:
			dev.append(i)

	return dev

