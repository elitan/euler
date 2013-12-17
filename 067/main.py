#!/bin/py

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
triangle = []

with open("data.txt") as f:
    for index, line in enumerate(f):
    	triangle.append(list(map(int, line.split())))

for i1 in range(len(triangle)-2, -1, -1):
	for i2, n in enumerate(triangle[i1]):
		#print("%d check for max in 1: %d and 2: %d. Should be %d" % (triangle[i1][i2], triangle[i1+1][i2], triangle[i1+1][i2+1], max(triangle[i1+1][i2], triangle[i1+1][i2+1])+int(triangle[i1][i2])))
		triangle[i1][i2] = max(triangle[i1+1][i2], triangle[i1+1][i2+1]) + triangle[i1][i2]

print(triangle)	