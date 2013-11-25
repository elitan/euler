#!/bin/py

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
https://projecteuler.net/project/images/p_015.gif
How many such routes are there through a 20×20 grid?
"""

import math as m

#Pascal's triangle
print(m.factorial(2*20) / m.pow(m.factorial(20), 2))