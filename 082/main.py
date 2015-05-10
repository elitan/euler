# -*- coding: utf-8 -*-
"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

131,673,234,103,18
201,96,342,965,150
630,803,746,422,11
537,699,497,121,956
805,732,524,37,311

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

# node class
class Node:
	def __init__(self, x, y, weight):
		self.weight = int(weight)
		self.cost = 10**1000000
		self.x = int(x)
		self.y = int(y)
		self.originateX = -1
		self.originateY = -1
		self.added = False

	def addNode(self, node):
		self.nodes.append(node)

	def __repr__(self):
		return "Y: %s, X: %s\nweight: %d, cost: %d\noriginY: %d, originX: %d" % (self.y, self.x, self.weight, self.cost, self.originateY, self.originateX)

def orderO(o):
	return o.sort(key = lambda x: x.cost)

def checkNextNode(nextNode, currentNode, o):
	if nextNode.cost > currentNode.cost + nextNode.weight:
		nextNode.cost = currentNode.cost + nextNode.weight
		nextNode.originateX = currentNode.x
		nextNode.originateY = currentNode.y

	if not nextNode.added:
		nextNode.added = True
		o.append(nextNode)

lowest = float("inf")
fname = "test.txt"
fname = "p082_matrix.txt"
for i in range(sum(1 for line in open(fname))):

	fh = open(fname)
	arr = []

	for y, line in enumerate(fh):
		l = []
		for x, weight in enumerate(line.replace('\n', '').split(',')):
			l.append(Node(x, y, weight))
		arr.append(l)

	# open nodes (un done)
	o = []

	# init first node
	arr[i][0].cost = arr[i][0].weight
	o.append(arr[i][0])

	while o:
		node = o.pop(0)

		# base case
		if node.x == len(arr)-1:
			o = []
			continue

		# check right node
		if node.x+1 < len(arr):
			nextNode = arr[node.y][node.x+1]
			checkNextNode(nextNode, node, o)

		# check top node
		if node.y-1 >= 0:
			nextNode = arr[node.y-1][node.x]
			checkNextNode(nextNode, node, o)

		# check bottom node
		if node.y+1 < len(arr):
			nextNode = arr[node.y+1][node.x]
			checkNextNode(nextNode, node, o)

		# order open nodes
		orderO(o)

	if node.cost < lowest:
		lowest = node.cost
	fh.close()
	

print(lowest)