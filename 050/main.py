#!/bin/py

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import sys
sys.path.append("../")
sys.stdout.flush()
import functions as f

limit = 1000000
pl = f.primeList(limit)
t = []

i = 0
j = 0
mL = 0
mV = 0

for i in range(0, len(pl)):
	for j in range(i+1, len(pl)):
		s = sum(pl[i:j])
		if s > limit:
			break
		if f.isPrime(s) and s < limit and j-i > mL:
			t.append(sum(pl[i:j]))
			mL = j-i
			mV = sum(pl[i:j])

print(t)
print(mL)
print(mV)
