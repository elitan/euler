"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
import sys
import time

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


	def nrExists(self, n):
		return n in self.possible

	def newSet(self, s):
		self.possible = s

	def add(self, n):
		self.possible.add(n)


	def remove(self, n):
		self.possible.remove(n)


	def number(self):
		if not self.done():
			return False
		x = self.possible.pop()
		self.possible.add(x)
		return x


	def possibleNumbers(self, sudo):
		global fullNrSet

		if self.done():
			return False

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
		if self.possible != (fullNrSet - foundNr):
			print("new set")
			self.newSet(fullNrSet - foundNr)
			return True
		return False


	def __str__(self):
		return "%s, row: %s, col: %s" % (repr(self.possible), self.row, self.col)


"""
tn = Node(0, 0, 0)
if tn.done():
	print("yes")
print(tn)
sys.exit()
"""


def solveSudoko(sudo):
	reRun = True
	while reRun:
		print("ss")
		reRun = False
		for row,r in enumerate(sudo):
			for col,node in enumerate(r):
				print(node)
				if node.possibleNumbers(sudo):
					print("do again!")
					reRun = True

				print(node)
				print("")
				#time.sleep(0.4)
				#sys.exit()


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
for sudo in sudoArr:
	solveSudoko(sudo)
	sys.exit()