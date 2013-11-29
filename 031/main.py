#!/bin/py

"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

#Im not extremly proud of this.. But it works.

import sys
sys.stdout.flush()

sumv = 0
i = 0

for a in range(200, -1, -1): #1p
	if a*1 < 200:
		for b in range(100, -1, -1): #2p
			if a*1 + b*2 < 200:
				for c in range(40, -1, -1): #5p
					if a*1 + b*2 + c*5 < 200:
						for d in range(20, -1, -1): #10p	
							if a*1 + b*2 + c*5 + d*10 < 200:
								for e in range(10, -1, -1): #20p
									if a*1 + b*2 + c*5 + d*10 + e*20 < 200:
										for f in range(4, -1, -1): #50p
											if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 < 200:
												for g in range(2, -1, -1): #100p
													if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 < 200:
														for h in range(1, -1, -1): #200p
															if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200 == 200:
																i += 1
													elif a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 == 200:
														i +=1
											elif a*1 + b*2 + c*5 + d*10 + e*20 + f*50 == 200:
												i += 1
									elif a*1 + b*2 + c*5 + d*10 + e*20 == 200:
										i+=1
							elif a*1 + b*2 + c*5 + d*10 == 200:
								i+=1
					elif a*1 + b*2 + c*5 == 200:
						i += 1
			elif a*1 + b*2 == 200:
				i += 1
	elif a*1 == 200:
		i += 1


print(i)									