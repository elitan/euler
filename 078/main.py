"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

# https://en.wikipedia.org/wiki/Partition_(number_theory)
# http://mathworld.wolfram.com/Partition.html

import sys

def p(n):
	available_value = list(xrange(n+1))[1:]
	ways = [1] + [0]*n

	for value in available_value:
		for i in range(value, n+1):
			ways[i] += ways[i-value]
	return ways[n]

class Memoize:
    """decorator to memoise a function"""
    def __init__(self, f):
        self.f = f
        self.cache = {}
 
    def __call__(self, *args):
        if not args in self.cache:
            self.cache[args] = self.f(*args)
        return self.cache[args]
 
@Memoize
def bigp(n):    
    if n < 0:
        return 0
    if n == 0:
        return 1
     
    # run k from n to 1 to avoid excessive recursion depth
    return sum((-1) ** (k + 1) * (bigp(n - k * (3 * k - 1) / 2) + bigp(n - k * (3 * k + 1) / 2)) for k in range(n,0,-1))

limit = 1
i = 9
while limit < 100000:
	limit *= 10
	while p(i) % limit != 0:
		i += 10
		print(i)
		#print(i)

	print(limit)
	print(i)
	print(p(i))
	print("")
#print bigp(1000)

sys.exit()

limit = 1
i = 1
while limit < 100000:
	limit *= 10
	while p(i) % limit != 0:
		i += 1
		#print(i)

	print(limit)
	print(i)
	print(p(i))