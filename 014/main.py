#!/bin/py

def newNumber(n):

	if n % 2 == 0:
		return n/2

	else:
		return (3 * n) + 1

largest = 0
count = 0
for i in range(1, 1000000):
	
	x = i
	c = 1
	while x != 1:

		x = newNumber(x)
		c += 1
	if c > count:
		count = c
		largest = i

print("Number: %d, Count: %d" % (largest, count))
