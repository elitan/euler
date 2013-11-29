#!/bin/py

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import math as m

def isLeapYear(y):
	if (y % 4 == 0 and y % 100 != 0) or (y % 4 == 0 and y % 400 == 0):
		return True
	else:
		return False

def daysOfMonth(m, year):
	if m == 1:
		return 31
	elif m == 2:
		if isLeapYear(year):
			return 29
		else:
			return 28
	elif m == 3:
		return 31
	elif m == 4:
		return 30
	elif m == 5:
		return 31
	elif m == 6:
		return 30
	elif m == 7:
		return 31
	elif m == 8:
		return 31
	elif m == 9:
		return 30
	elif m == 10:
		return 31
	elif m == 11:
		return 30
	elif m == 12:
		return 31


startDay = 1 	#1 jan 1901 == thusday = 1
days = 0
sundays = 0
for year in range(1901, 2001):
		for m in range(1, 13):

			days = daysOfMonth(m, year)
			startDay = ((days % 7) + startDay) % 7
			if startDay == 6:
				sundays += 1

print(sundays)






