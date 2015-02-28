for i in range(0, 10):
	fh = open('p079_keylog.txt')
	n = str(i)
	left = list()
	right = list()
	for line in fh:
		nr = line.replace('\n', '')
		if n in nr:
			split = nr.split(n)
			#check left
			for k in split[0]:
				if k not in left:
					left.append(k)
			#check right
			for k in split[1]:
				if k not in right:
					right.append(k)
	print(n)
	print(left)
	print(right)
	fh.close()