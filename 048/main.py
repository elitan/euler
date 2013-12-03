#!/bin/py

"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

answer = 0
for i in range(1, 1001):
	answer += pow(i, i, 10000000000)
	answer = answer % 10000000000

print(answer)