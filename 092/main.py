"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import sys
sys.path.append("../")
import functions as f
import math

def squareDigit(n):
	ret = 0
	for x in list(str(n)):
		ret += int(x)**2
	return ret;

def sqChain(n):
	global answer
	#print(n)
	if n == 89:
		answer += 1
		return 0
	if n == 1:
		return 0

	sqChain(squareDigit(n))

answer = 0
for x in range(1, 10**7):
	sqChain(x)
	#print("----")

print("Eureka!: %d" % answer)