"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.


---

consider 3 x 2

the matrix is:

6 	4 	2
3 	2 	1

this is the pattern for every rectangle.

so at 3 x 2 we have

6 	4 	2
3 	2 	1
----------
9 	6 	3

and 5 x 6 we have

30 	25 	20 	15 	10 	5
24 	20 	16 	12 	8 	3
18 	15 	12 	9 	6 	4
12 	10 	8 	6 	4 	2
6 	5 	4 	3 	2 	1
----------------------
90	75	60	45	30	15

x x y
gets

x! + 2*x! + ... + y*x!

triangle numbers, but insted of +1, we jump x! y number of times.

the sum of such "problem" is (n/2) * (2 * a + (n-1)*d

where n is the number of times, and d is the "jump", and a is the starting number.

No, the problem is.
for which x and y can we get closest to 2*10^6.

"""

import sys
sys.path.append("../")
import functions as f
import itertools
import math

def countTriangles(x, y):
	x = float(x)
	y = float(y)
	d = (x**2+x)/2
	return int((y/2)*((2*d)+((y-1)*d)));


xB = 0
yB = 0
low = 2*10**6

for x in range(1,100):
	for y in range(1,100):

		ctr = countTriangles(x,y)

		if abs(ctr - 2*10**6) < low:
			low = abs(ctr - 2*10**6);
			xB = x
			yB = y

print(xB,yB,low)
print(xB*yB)