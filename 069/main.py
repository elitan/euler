
import sys
sys.path.append("../")
import functions as f
import itertools

import fractions

def phi(n):

	pf = f.primeFac(n)

	if len(pf) == 0:
		return n - 1;

	ans = 1
	while pf:
		ans *= (pf[0] ** pf.count(pf[0])) * (1 - (1/float(pf[0])))
		#remove all values p
		pf = [x for x in pf if x != pf[0]]

	return int(ans)

high = 0
highN = 0
for n in range(2, 1000000):

	npn = n / float(phi(n))
	if npn > high:
		print("YEA")
		high = npn
		highN = n
		print(n, phi(n), npn)

print(highN)