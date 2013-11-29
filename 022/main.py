#!/bin/py

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def valueOfChar(c):
	return ord(c)-64 	#ascii value - 64. A = 65 in ASCII

def sumOfString(foo):
	sumv = 0
	for i in foo:
		sumv += valueOfChar(i)

	return sumv

l = []
with open ("names.txt", "r") as myfile:
    data=myfile.read()

#Remove first and last "
data = data[1:-1]

#Split to list
l = data.split('","')
l.sort()

#Lets start the counting
sumv = 0
count = 0
for i in l:
	count += 1
	sumv += count * sumOfString(i)
	
print(sumv)