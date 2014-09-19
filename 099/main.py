"""
CComparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import sys
sys.path.append("../")
import functions as f
import math

print("start")

currentHighest = 0
answer = 0
for i, line in enumerate(open('p099_base_exp.txt'), start=1):

	nr = int(line.split(',')[1]) * math.log(int(line.split(',')[0]))
	
	if  nr > currentHighest:
		currentHighest = nr
		answer = i

print(answer)