#!/bin/py

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import math as m

def isTriangleNum(n):
	return m.sqrt((2 * n) + 1/4) % 1 == 0.5

def ucToDec(c):
	return ord(c) - ord('A') + 1

l = []
s = 0
answer = 0
with open("words.txt") as f:
	for line in f:
		l = line[1:-1].split('","')

for w in l:
	s = 0
	for c in list(w):
		s += ucToDec(c)

	if isTriangleNum(s):
		answer += 1

print(answer)