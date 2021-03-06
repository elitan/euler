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

	if n != nR:
		arr.append(int(n))

	try:
		arr.remove(1)
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


def divisors(n):
	div = []
	div.append(1)
	for i in range(2, int(m.ceil(n**0.5))):
		if n % i == 0:
			div.append(i)
			div.append(int(n/i))

	if m.sqrt(n) == m.floor(m.sqrt(n)):
		div.append(m.sqrt(n))

	div.sort()
	return div
	
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
	return n == str(n[::-1])