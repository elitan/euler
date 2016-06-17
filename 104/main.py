# -*- coding: utf-8 -*-
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.


1 1 2 3 5 8 12
"""
import sys
import time
sys.path.append("../")
import functions as f

correct_set = set(list("123456789"))
def is_pandigital(n):
    global correct_set
    return set(n) == correct_set


f1 = 1
f2 = 1
fn = 2
n = 3
found = False
while not found:
    fn = f1 + f2
    if is_pandigital(str(fn)[0:9]) and is_pandigital(str(fn)[-9:]):
        print(n)
        found = True
        sys.exit()
    f1 = f2
    f2 = fn
    n += 1

