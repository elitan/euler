"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

(added extra bottom row)
"""

"""
Solved using backtracking method. Find all possibilitys and start testing lowest set. if wrong path, backtrack.
"""


import sys
import time
import copy

# global variable
fullNrSet = set()
for i in range(1,10): fullNrSet.add(i)

class Node():
	def __init__(self, number, row, col):
		self.possible = set()
		self.row = row
		self.col = col

		self.possible.add(number)


	def done(self):
		return 0 not in self.possible and len(self.possible) == 1


	def newSet(self, s):
		self.possible = s


	def len(self):
		return len(self.possible)


	def getPossible(self):
		return self.possible


	def number(self):
		if not self.done():
			return False
		x = self.possible.pop()
		self.possible.add(x)
		return x


	def possibleNumbers(self, sudo):
		global fullNrSet

		if self.done():
			return True

		foundNr = set()
		# check row
		for i in range(0,9):
			n = sudo[self.row][i]
			if n != self and n.done():
				foundNr.add(n.number())
		# check col
		for i in range(0,9):
			n = sudo[i][self.col]
			if n != self and n.done():
				foundNr.add(n.number())
		# check inside square
		rowStart = self.row - (self.row % 3)
		colStart = self.col - (self.col % 3)
		for r in range(rowStart, rowStart+3):
			for c in range(colStart, colStart+3):
				n = sudo[r][c]
				if n != self and n.done():
					foundNr.add(n.number())
		if self.possible != (fullNrSet - foundNr) and len(fullNrSet - foundNr) != 0:
			self.newSet(fullNrSet - foundNr)
			return True
		elif len(fullNrSet - foundNr) == 0:
			print("FULL EXIT, GO BACK")
			return False
		return True


	def __str__(self):
		return "%s, row: %s, col: %s" % (repr(self.possible), self.row, self.col)


"""
tn = Node(0, 0, 0)
if tn.done():
	print("yes")
print(tn)
sys.exit()
"""

def printSudo(sudo):
	for row in range(0, 9):
		for col in range(0, 9):
			sys.stdout.write("%s \t" % sudo[row][col].getPossible())
		sys.stdout.write("\n")

def checkSudo(sudo):

	#print("#########")
	#print("Checking")
	#sudo[0][0] = Node(3,0,0)
	#printSudo(sudo)
	#print("#########")
	# check simle len
	for row in range(0, 9):
		for col in range(0, 9):
			if sudo[row][col].len() != 1:
				print(sudo[row][col].len())
				print("F 1")
				return False

	# check row
	for row in range(0, 9):
		s = set()
		for col in range(0, 9):
			if sudo[row][col].number() in s:
				print(row, col)
				print("F 2")
				return False
			s.add(sudo[row][col].number())

	#check col
	for col in range(0, 9):
		s = set()
		for row in range(0, 9):
			if sudo[row][col].number() in s:
				print("F 2")
				return False
			s.add(sudo[row][col].number())

	for row in range(0, 9, 3):
		for col in range(0, 9, 3):
			s = set()
			for rowIn in range(0, 3):
				for colIn in range(0, 3):
					if sudo[row+rowIn][col+colIn].number() in s:
						print("F 2")
						return False
					s.add(sudo[row][col].number())			

	return True
	#check squares

def possibleNumbers(sudo, row, col):
	global fullNrSet

	self = sudo[row][col]
	if sudo[row][col].done():
		return 1

	foundNr = set()
	# check row
	for i in range(0,9):
		n = sudo[row][i]
		if n != self and n.done():
			foundNr.add(n.number())
	# check col
	for i in range(0,9):
		n = sudo[i][col]
		if n != self and n.done():
			foundNr.add(n.number())
	# check inside square
	rowStart = row - (row % 3)
	colStart = col - (col % 3)
	for r in range(rowStart, rowStart+3):
		for c in range(colStart, colStart+3):
			n = sudo[r][c]
			if n != self and n.done():
				foundNr.add(n.number())
	if self.possible != (fullNrSet - foundNr) and len(fullNrSet - foundNr) != 0:
		self.newSet(fullNrSet - foundNr)
		return 2 # new poss
	elif len(fullNrSet - foundNr) == 0:
		return 3 # wrong, backtrack
	return 1 #no changes where made

def solveSimple(sudo):
	reRun = True
	while reRun:
		reRun = False
		for row,r in enumerate(sudo):
			for col,node in enumerate(r):
				#print(node)
				r = possibleNumbers(sudo, row, col) 
				if r == 3:
					return False # backtrack
				if r != 1:
					reRun = True # something changed, lets make sure we do possibleNumbers again
	return True # no solution found, try next set

def solveSudoko(sudo, depth = 0):
	r = solveSimple(sudo)
	if not r:
		return r, None

	# find the node with smallest set
	rowLow, colLow, low = 0, 0, 11
	for row in range(0, 9):
		for col in range(0, 9):
			n_len = sudo[row][col].len()
			if n_len > 1 and n_len < low:
				rowLow = row
				colLow = col
				low = n_len

	# if just one item in each node
	if low == 11:
		if checkSudo(sudo):
			return True, sudo # win
		else:
			return False, None

	row = rowLow
	col = colLow
	for i, c in enumerate(sudo[row][col].possible):
		sudoTmp = copy.deepcopy(sudo)
		sudoTmp[row][col] = Node(c, row, col)
		r = solveSudoko(sudoTmp, depth+1)
		if r[0]:
			return True, r[1]

	return False, None
		

# parse text
c = 0
sudoArr = []
sudokuTmp = []

for l in open("p096_sudoku.txt", "r"):
	l = l.replace("\n", "")
	c += 1

	if l[:4] == "Grid":
		c = 0
		sudoArr.append(sudokuTmp)
		sudokuTmp = []
	else:
		arrTmp = []
		for col, n in enumerate(list(l)):
			arrTmp.append(Node(int(n), c-1, col))
		sudokuTmp.append(arrTmp)
sudoArr.pop(0)

# solve soduko
c = 0
for i, sudo in enumerate(sudoArr):
	r, sudoTmp = solveSudoko(sudo)
	print("%d solved" % (i+1))
	nr = int("%d%d%d" % (sudoTmp[0][0].number(), sudoTmp[0][1].number(), sudoTmp[0][2].number()))
	print(nr)
	
	c += int("%d%d%d" % (sudoTmp[0][0].number(), sudoTmp[0][1].number(), sudoTmp[0][2].number()))
		
	#raw_input("next")
	#sys.exit()
print(c)