import itertools
import sys

def trans(ss):
	low = 100
	lowindex = 0
	for i, n in enumerate(ss[::3]):
		if n < low:
			low = n
			lowindex = i
	if lowindex != 0:
		start = lowindex*3
		i = 0
		nl = list()
		sslen = len(ss)
		while i < len(ss):
			nl.append(ss[(start+i) % sslen])
			i += 1
		return nl
	return ss

high = 0
nr = [1,2,3,4,5,6,7,8,9,10]
a = 0
for perm in itertools.permutations(nr):
	ss = [perm[0], perm[1], perm[2], perm[3], perm[2], perm[4], perm[5], perm[4], perm[6], perm[7], perm[6], perm[8], perm[9], perm[8], perm[1]]
	
	a = sum(ss[0:3])
	b = sum(ss[3:6])
	c = sum(ss[6:9])
	d = sum(ss[9:12])
	e = sum(ss[12:15])

	if a == b and a == c and a == d and a == e:
		ss = trans(ss)
		nr = int(''.join(map(str, ss)))
		if nr > high and len(str(nr)) == 16:
			high = nr
print(high)