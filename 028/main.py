#!/bin/py

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


9, 25, 49 == 3^2, 5^2, 7^2. top right diagonal.

For every loop get the cordners. First loop:

3^2 + 3^2-2 + 3^2-4 + 3^2-8 = 4*3^2 - 12
5^2 + 5^2-4 + 5^2-8 + 5^2-12 = 4*5^2 - 24
etc...
"""

import math as m

a = 3;
i = 1;
s = 1; 	#Skip middle. Its one mkay?
while a <= 1001:
	s += 4 * m.pow(a,2) - i*12
	a += 2
	i += 1

print(int(s))