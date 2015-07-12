# -*- coding: utf-8 -*-
"""
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""
import sys
sys.path.append("../")
import functions as f

class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return ("(%d,%d)" % (self.x, self.y))

	def __repr__(self):
		return ("(%d,%d)" % (self.x, self.y))

class CoordinateVector2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return ("[%d,%d]" % (self.x, self.y))

	def __repr__(self):
		return ("[%d,%d]" % (self.x, self.y))

def coordinates_on_line(a,b):
	return a.x == b.x or a.y == b.y

def is_right_angle_triangle(a,b,c):

	# check if same coordinate
	if a == b or a == c or b == c:
		return False

	# check if all three coordinates lay on the same line
	# if so, thay can not form a triangle
	if coordinates_on_line(a,b) and coordinates_on_line(a,c) and coordinates_on_line(c,b):
		return False

	ab = CoordinateVector2D(a.x-b.x, a.y-b.y)
	ac = CoordinateVector2D(a.x-c.x, a.y-c.y)
	bc = CoordinateVector2D(b.x-c.x, b.y-c.y)

	# check ab ac
	if ab.x*ac.x + ab.y*ac.y == 0:
		return True

	# check ab bc
	if ab.x*bc.x + ab.y*bc.y == 0:
		return True

	# check ac bc
	if ac.x*bc.x + ac.y*bc.y == 0:
		return True

	return False

"""
O = Coordinate(0,0)
P = Coordinate(6,1)
Q = Coordinate(10,3)

r = is_right_angle_triangle(O, P, Q)
print(r)

sys.exit()
"""

c = 0
size = 51

O = Coordinate(0,0)
P = Coordinate(0,0)
Q = Coordinate(0,0)


# generate coordinates

# Improve: Done do duplicates

# P
for pX in range(0, size):
	for pY in range(0, size):
		P.set(pX, pY)

		# Q
		for qX in range(0, size):
			for qY in range(0, size):
				Q.set(qX, qY)
				if is_right_angle_triangle(O, P,  Q):
					c += 1

print(c)
print(c/2) # forgive me :(