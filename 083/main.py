# -*- coding: utf-8 -*-
"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

131,673,234,103,18
201,96,342,965,150
630,803,746,422,11
537,699,497,121,956
805,732,524,37,331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
"""

import sys

# node class
class Node:
	def __init__(self, x, y, weight):
		self.weight = int(weight)
		self.cost = 10*100000
		self.x = int(x)
		self.y = int(y)
		self.originateX = -1
		self.originateY = -1
		self.added = False
		self.done = False
		self.nodes = []

	def addNode(self, node):
		self.nodes.append(node)

	def __repr__(self):
		return "Y: %s, X: %s\nweight: %d, cost: %d, done: %s\noriginY: %d, originX: %d\n\n" % (self.y, self.x, self.weight, self.cost, self.done, self.originateY, self.originateX)

def orderO(o):
	return o.sort(key = lambda x: x.cost)

# initiate
fh = open('test.txt')
fh = open('p083_matrix.txt')
arr = []
arr2 = []

for y, line in enumerate(fh):
	l = []
	for x, weight in enumerate(line.replace('\n', '').split(',')):
		l.append(Node(x, y, weight))
	arr.append(l)

# open nodes (un done)
o = []

# init first node
arr[0][0].cost = arr[0][0].weight
arr[0][0].added = True
o.append(arr[0][0])

while o:
	node = o.pop(0)

	if node.x == len(arr)-1 and node.y == len(arr)-1:
		o = []
		continue

	# right
	try:
		right = arr[node.y][node.x+1]
		rightExists = True
	except:
		rightExists = False

	if rightExists:
		if right.cost > node.cost + right.weight:
			right.cost = node.cost + right.weight
			right.originateX = node.x
			right.originateY = node.y

		if not right.added:
			right.added = True
			o.append(right)

	# left
	if node.x-1 >= 0:
		left = arr[node.y][node.x-1]
		leftExists = True
	else:
		leftExists = False

	if leftExists:
		if left.cost > node.cost + left.weight:
			left.cost = node.cost + left.weight
			left.originateX = node.x
			left.originateY = node.y

		if not left.added:
			left.added = True
			o.append(left)

	# bottom
	try:
		bottom = arr[node.y+1][node.x]
		bottomExists = True
	except:
		bottomExists = False

	if bottomExists:
		if bottom.cost > node.cost + bottom.weight:
			bottom.cost = node.cost + bottom.weight
			bottom.originateX = node.x
			bottom.originateY = node.y

		if not bottom.added:
			bottom.added = True
			o.append(bottom)

	# top
	if node.y-1 >= 0:
		top = arr[node.y-1][node.x]
		topExists = True
	else:
		topExists = False

	if topExists:
		if top.cost > node.cost + top.weight:
			top.cost = node.cost + top.weight
			top.originateX = node.x
			top.originateY = node.y

		if not top.added:
			top.added = True
			o.append(top)


	orderO(o)

# end


print(arr[len(arr)-1][len(arr)-1])