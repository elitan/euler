# -*- coding: utf-8 -*-
"""
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

import sys
import re
sys.path.append("../")
import functions as f

rome_lookup = dict(
				I=1, 
				II=2, 
				III=3, 
				IV=4, 
				V=5, 
				VI=6,
				VII=7,
				VIII=8,
				IX=9,
				X=10,
				XX=20,
				XXX=30,
				XL=40,
				L=50,
				LX=60,
				LXX=70,
				LXXX=80,
				XC=90,
				C=100,
				CC=200,
				CCC=300,
				CD=400,
				D=500,
				DC=600,
				DCC=700,
				DCCC=800,
				CM=900,
				M=1000
				)
def lookup_int_to_roman(n):
	for k,v in rome_lookup.items():
		if n == v:
			return k
	return ""

def lookup_roman_to_int(r):
	try:
		return rome_lookup[r]
	except:
		return 0

def int_to_roman(n):
	s = ""
	# 1000
	for i in range(0, n/1000):
		s += "M"
	n -= n/1000*1000

	# 100
	s += lookup_int_to_roman(n/100*100)
	n -= n/100*100

	# 10 
	s += lookup_int_to_roman(n/10*10)
	n -= n/10*10

	# 1
	s += lookup_int_to_roman(n)

	return s

pattern = '^(M{0,4})(CM|CD|D?C{0,4})(XC|XL|L?X{0,4})(IX|IV|V?I{0,4})$'

fh = open('p089_roman.txt', 'r')

answer = 0

for l in fh:
	roman = l.replace('\n', '')
	match = re.search(pattern, roman)

	n = 0
	#print(roman)
	#print(match.groups())
	for m in match.groups():
		if m:
			#print(m)
			r = lookup_roman_to_int(m)
			if r:
				n += r
			else:
				# check two charts at the time, and then one char at a time
				r = True
				i = 0
				while r:
					r = lookup_roman_to_int(m[i:i+2])
					if r:
						n += r
						i += 2
				r = True
				while r:
					r = lookup_roman_to_int(m[i:i+1])
					if r:
						n += r
						i += 1
	answer += len(roman) - len(int_to_roman(n))

print(answer)