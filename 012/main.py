#!/bin/py
import math as m

def devisors(n):

	dev = 0
	for i in range(2, int(m.ceil(n**0.5))):
		if n % i == 0:

			dev += 1

	#*2 + 1 and n
	dev = dev * 2 + 2

	#if perfect square
		#dev += 1
	return dev


maxDevisors = 500
largest = 0
value = 0
i = 10
while largest < 500:

	i += 1
	n = 0
	for x in range(1, i+1):
		n += x

	devTemp = devisors(n)
	if devTemp > largest:
		largest = devTemp
		value = n

print("Winner: %d, devisors: %d" % (value, largest))
