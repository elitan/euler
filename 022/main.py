#!/bin/py

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