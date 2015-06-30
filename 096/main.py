"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
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


def solveSimple(sudo):
	reRun = True
	while reRun:
		reRun = False
		for row,r in enumerate(sudo):
			for col,node in enumerate(r):
				#print(node)
				r = node.possibleNumbers(sudo) 
				if not r:
					#printSudo(sudo)
					#sys.exit();
					return False
					#print("do again!")
					reRun = True

				#print(node)
				#print("")
				#time.sleep(0.4)
				#sys.exit()
	print(r)
	#print("We need to backtrack this sudoku!");
	return True # no solution found?

def solveSudoko(sudo, rowStart = 0, colStart = 0):
	for row in range(rowStart, 9):
		for col in range(colStart, 9):
			print("######")
			print(row, col)
			print("######")
			r = solveSimple(sudo)
			current_node = sudo[row][col]
			print(row, col, r)

			if current_node.len() == 1:
				continue

			if not r:
				printSudo(sudo)
				print(current_node)
				return False

			#time.sleep(.5)

				
			for c in current_node.getPossible():
				print("Currently on")
				print(row, col, c, current_node.getPossible())
				sudo[row][col] = Node(c, row, col)
				r = solveSudoko(copy.deepcopy(sudo))
				print("r was " , r)
				if not r:
					print("false")
					printSudo(sudo)
					#sys.exit()					
					print("continue 2")
					continue
	printSudo(sudo)


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
	print("done??")
	sys.exit()