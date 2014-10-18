"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""

def onlyOddDigits(n):
	for d in str(n):
		if int(d) % 2 == 0:
			return False;
	return True;

def isReversable(n):
	if n % 10 != 0:
		return onlyOddDigits(n + int(str(n)[::-1]))
	else:
		return False

i = 0;
r = 0;

while i < 10**9:

	if isReversable(i):
		#print(i)
		r += 1
	i += 1

print(r)