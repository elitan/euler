"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

import sys
sys.path.append("../")
sys.stdout.flush()
import functions as f

def bouncy(nr):
	pd = False
	ud = 0;

	if len(str(nr)) <= 2:
		return False

	for d in str(nr):
		if pd != False:
			if ud == 0:
				if d > pd:
					ud = 1;
				elif d < pd:
					ud = -1;
			else:
				if ud == 1 and d < pd:
					return True;
				elif ud == -1 and d > pd:
					return True;

		pd = d;
	return False;

i = 0;
b = float(0);

while(True):

	if bouncy(i):
		b += 1
		print(i)
		if (b/i) == 0.99:
			sys.exit()


	i += 1

