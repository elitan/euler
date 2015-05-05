# -*- coding: utf-8 -*-
"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""
def farey(n):
    """Python function to print the nth Farey sequence, either ascending or descending."""
    a, b, c, d = 0, 1,  1  , n     # (*)
    #print "%d/%d" % (a,b)
    s = 0
    while c <= n:
        k = (n + b)/d
        a, b, c, d = c, d, k*c - a, k*d - b
        s += 1
        #print "%d/%d" % (a,b)
    return s-1

f = farey(10**5)

print(f)
