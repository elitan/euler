
import sys
sys.path.append("../")
import functions as f
import itertools

def triangle(n):
	return n * (n + 1) / 2

def square(n):
	return n**2

def pentagonal(n):
	return n * (3 * n - 1) / 2

def hexagonal(n):
	return n * (2 * n - 1)

def heptagonal(n):
	return n * (5 * n - 3) / 2

def octagonal(n):
	return n * (3 * n - 2)

def getP(n, c):
	if c == 0:
		return triangle(n)
	elif c == 1:
		return square(n)
	elif c == 2:
		return pentagonal(n)
	elif c == 3:
		return hexagonal(n)
	elif c == 4:
		return heptagonal(n)
	elif c == 5:
		return octagonal(n)

# Check if there exists two numb
def cyclickCheck(l, q):
	if not l:
		return True
	if str(l[-1])[2:] == str(q)[:2]:
		return True
	return False

# final check
def cyclickCheckLast(l):
	if not l:
		return True
	if str(l[0])[:2] == str(l[-1])[2:]:
		return True
	return False

#taken referse to c in getP()

def rec(l, taken):

	for x in range(0, 6):
		if x not in taken:

			go = True
			n = 1
			while go:
				p = getP(n, x)

				if len(str(p)) == 4 and cyclickCheck(l, p):
					l.append(p)
					taken.append(x)

					if len(taken) == 6:
						if cyclickCheckLast(l):
							print(l)
							print(sum(l))
							sys.exit()

						l.pop()
						taken.pop()

						if len(str(p)) > 4:
							go = False
					else:
						rec(l, taken)
						l.pop()
						taken.pop()

				elif len(str(p)) > 4:
					go = False

				n += 1

rec(list(), list())