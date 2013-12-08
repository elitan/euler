#!/bin/py

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def allNr(a,b,c):
	st = ""
	st += str(a)
	st += str(b)
	st += str(c)

	try:	
		st.index("1")
		st.index("2")
		st.index("3")
		st.index("4")
		st.index("5")
		st.index("6")
		st.index("7")
		st.index("8")
		st.index("9")
	except Exception:
		return False

	if len(st) != 9:
		return False

	return True

def uniqCharInString(n):
	n = str(n)
	for i in range(0, len(n)):
		if n.count(str(n[i:i+1])) > 1:
			return False

	return True	

listOne = []	#stores c
listTwo = [] 	#sum a and b

c = 0

for a in range(1, 200):
	bmin = pow(10,8-len(str(a)))
	bmax = pow(10,9-len(str(a)))
	arg = ""

	for b in range(bmin, bmax):

		c = a * b
		print("Testing at %d x %d = %d" % (a,b,c))

		if not uniqCharInString("%d%d" % (a,b)):
			#print("Breaking at %d x %d = %d" % (a,b,c))
			break

		if allNr(a,b,c) and c not in listOne:
			print("Found %d x %d = %d" % (a, b, c))
			listOne.append(c)
			listTwo.append(a+b)

print(sum(listTwo))
