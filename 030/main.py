#!/bin/py



import math as m

strn = ""
sumv = 0;
answer = 0;

for a in range(0, 10):
	for b in range(0, 10):
		for c in range(0, 10):
			for d in range(0, 10):
				for e in range(0, 10):

					strn = "";
					sumv = 0;

					strn += str(a)
					strn += str(b)
					strn += str(c)
					strn += str(d)
					strn += str(e)

					sumv += m.pow(a, 5);
					sumv += m.pow(b, 5);
					sumv += m.pow(c, 5);
					sumv += m.pow(d, 5);
					sumv += m.pow(e, 5);

					if sumv == int(strn) and sumv > 1:
						answer += sumv
						#print(strn)

print(int(answer))
				