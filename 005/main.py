#!/bin/py

import math as m

n = 0;
count = 0
found = False

print("Starting...");
#exit(0)

while not found:

	n += 20
	ok = True
	i = 1
	
	while ok and i < 21:
		if n%i != 0:
			ok = False
		i += 1

	if ok:
		found = True


print(n);