# -*- coding: utf-8 -*-
"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""

"""

x = 21

total_disks = x + (x - 1)
total_disks = x**2 - x

tdsqrt = sqrt(total_disks)
y = ceil(tdsqrt) * floor(tdsqrt)

if y * 2 == total_disks:
	match



"""
import sys
import math
sys.path.append("../")
import functions as f

def main():

	i = 10

	while True:


		x = i * (i - 1)
		x2 = x * 2
		y = int(math.ceil(math.sqrt(x2)) * math.floor(math.sqrt(x2)))

		if x2 == y:
			print('match!')
			print(i)
			print(x, y)

			print('balls: ', math.ceil(math.sqrt(x2)) + math.floor(math.sqrt(x2)) )

		i += 1

if __name__ == '__main__':
	main()
