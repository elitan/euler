"""
import sys
sys.path.append("../")
import functions as f
"""
import math as m

def primeFac(n):
	nR = n
	i = 2
	arr = []

	while i < m.sqrt(n) + 1:
		while n % i == 0:
			arr.append(i)
			n = n / i
	     
		i += 1

	arr.append(int(n))
	try:
		arr.remove(1)
	except:
		pass
	try:
		arr.remove(nR)
	except:
		pass
	return arr

def isPrime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		#print(f)
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True    


def devisors(n):
	dev = []
	dev.append(1)
	for i in range(2, int(m.ceil(n**0.5))):
		if n % i == 0:
			dev.append(i)
			dev.append(int(n/i))

	#Find some n^1/x with no decimals
	e = 2
	a = 2.5
	while a % 1 != 0 and a > 2:

		a = pow(n, 1/e)
		e += 1

	if a % 1 == 0 and a not in dev:
		dev.append(int(a))

	dev.sort()
	return dev
	
def primeList(top):
	primes = []
	a = [2] * top
	a[0] = 0
	a[1] = 0
	a[2] = 1
	p = 2

	while p < top:
		a[p] = 1

		for n in range(p*2, top, p):
			a[n] = 0
		p = findNextIndex(a, p, top)

	for p in range(0, top):
		if a[p] == 1:
			primes.append(p)

	return primes


def findNextIndex(a, n, top):
	n += 1
	try:		
		while a[n] != 2:
			n += 1
	except:
		return top

	return n

def isPalindromic(n):
	n = str(n)
	i = 0

	while i < len(n)/2:
		if n[0 + i] != n[len(n) - 1 - i]:
			
			return False
		i += 1

	return True	