import math

def hcf(x, y):
	"""This function takes two
	integers and returns the H.C.F"""

	# choose the smaller number
	if x > y:
		smaller = y
	else:
		smaller = x
	for i in range(1,smaller + 1):
		if((x % i == 0) and (y % i == 0)):
			hcf = i
	return hcf

dhigh = 1000000
nn = 1
dd = dhigh
for d in range(dhigh+1, 1, -1):
	for n in range(d*nn/d, d*3/7+1):
	#for n in range(1, d*3/7+1):
		if math.fabs(d*3-n*7) == 1 and hcf(d,n) == 1:
			#print("%s/%s" % (n,d))
			dd = d
			nn = n
print(nn, dd)
