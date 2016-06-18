# -*- coding: utf-8 -*-
"""
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
"""
import sys
sys.path.append("../")
import functions as f

def is_sum(a,b):
    return sum(map(int, list(str(a)))) == b

n = 2
an = 0
seq = []
while an < 100:
    x = 1
    nex = False
    while not nex:
        a = n**x
        alen = len(str(a))
        if alen < 2:
            pass
        elif alen > n * 2:
            nex = True
        elif is_sum(a, n):
            an += 1
            #print(an, "%d ** %d = %d" % (n, x, a))
            seq.append(a)
        x += 1

    n += 1

print(seq[29])
