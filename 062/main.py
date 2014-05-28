#!/usr/bin/python

"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import sys

arr = []
i = 1

while True:
	add = True	
	a = [int(char) for char in str(i**3)]
	key = sorted(a)

	for j,c in enumerate(arr):
		if c[0] == key:
			arr[j][1] = arr[j][1] + 1
			if arr[j][1] == 5:
				print(arr[j][2])
				sys.exit(0)
			add = False
		else:
			add = True;

	if add:
		arr.append([key,1, i**3])

	i += 1
