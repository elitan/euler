# -*- coding: utf-8 -*-
"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Examples
https://stackoverflow.com/questions/13300904/determine-whether-point-lies-inside-triangle
"""

import sys

fh = open('p102_triangles.txt')
#fh = open('test.txt')
c = 0
for l in fh:
	coordinates = map(float, l.replace('\n', '').split(','))
	p1 = coordinates[:2]
	p2 = coordinates[2:4]
	p3 = coordinates[4:6]

	alpha = ((p2[1] - p3[1]) * (0 - p3[0]) + (p3[0] - p2[0]) * (0 - p3[1])) / ((p2[1] - p3[1])*(p1[0] - p3[0]) + (p3[0] - p2[0])*(p1[1] - p3[1]));
	beta = ((p3[1] - p1[1])*(0 - p3[0]) + (p1[0] - p3[0])*(0 - p3[1])) / ((p2[1] - p3[1])*(p1[0] - p3[0]) + (p3[0] - p2[0])*(p1[1] - p3[1]))
	gamma = 1.0 - alpha - beta;

	if alpha > 0 and beta > 0 and gamma > 0:
		c += 1
print(c)