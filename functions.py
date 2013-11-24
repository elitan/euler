def primeFac(n):
	arr = []

	while i < m.sqrt(n) + 1:
		while n % i == 0:
			arr.append(i)
			n = n / i
		 
		i += 1

	return arr