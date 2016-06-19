# -*- coding: utf-8 -*-
"""
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.
"""
import sys
import time
import math
sys.path.append("../")
import functions as f

def find_pal_sum(x, y, nlist, palsum):
    s = 0
    # add consecutively squares
    for z in range(x, y):
        s += nlist[z]
        if s > highest:
            return False
    # check if palindrome
    if f.isPalindromic(str(s)):
        palsum.add(s)
        return True
    return False
    

highest = 10**8
h = int(math.ceil(math.sqrt(highest)))
c = 0
palsum = set()

# generate all squares
nlist = []
for i in range(1, h+1):
    nlist.append(i**2)

# go through all squares consecutively
for x in range(len(nlist)):
    for y in range(x+2, len(nlist)):
        find_pal_sum(x, y, nlist, palsum)

print(len(palsum))
print(sum(palsum)) #answer
