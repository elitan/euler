#!/usr/bin/python

"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

c = 0
for i in range(1, 100):
	for j in range(1, 100):
		if len(str(i**j)) == j:
			#print("%i^%i = %i (%s)" % (i, j, i**j, len(str(i**j))))
			c += 1
		else:
			#print("%i^%i = %i (%s)" % (i, j, i**j, len(str(i**j))))
			pass
print(c)