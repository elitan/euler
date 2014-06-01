#!/usr/bin/python

"""

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

"""

import sys

def cardValue(card):

	value = card[0:1]

	try:
		value = int(value)
		return value
	except:
		if value == "T":
			return 10
		elif value == "J":
			return 11
		elif value == "Q":
			return 12
		elif value == "K":
			return 13
		elif value == "A":
			return 14

############

def sameKind(pokerhand, num):
	m = 0
	for i in range(0,len(pokerhand)):
		s = 0
		for j in range(0, len(pokerhand)):
			if cardValue(pokerhand[i]) == cardValue(pokerhand[j]):
				s += 1
		if s == num:
			return True, cardValue(pokerhand[i])
	return False

def sortPokerHand(hand):
	newHand = []

	for k in range(0, len(hand)):
		index = 0
		m = 15
		for i, card in enumerate(hand):
			if cardValue(card) < m:
				m = cardValue(card)
				index = i
		newHand.append(hand[index])
		hand.pop(index)
	return newHand

############

def isRoyalStrightFlush(pokerhand):
	suit = pokerhand[0][1:2]
	for card in pokerhand:
		if card[1:2] != suit:
			return False
		if cardValue(card[0:1]) < 10:
			return False 
	return True, 9 * 10**10

def isStrightFlush(pokerhand):
	suit = pokerhand[0][1:2]
	for card in pokerhand:
		if card[1:2] != suit:
			return False

	for i in range(0, 3):
		value = cardValue(pokerhand[i])
		if cardValue(pokerhand[i])+1 != cardValue(pokerhand[i+1]):
			return False
	return True, 8 * 10**10 + cardValue(pokerhand[0]) * 10**8

def isFourOfAKind(pokerhand):
	if sameKind(pokerhand, 4):
		if cardValue(pokerhand[0]) == cardValue(pokerhand[1]):
			return True, 7 * 10**10 + cardValue(pokerhand[0]) * 10**8 + cardValue(pokerhand[4]) * 10**6
		else:
			return True, 7 * 10**10 + cardValue(pokerhand[4]) * 10**8 + cardValue(pokerhand[0]) * 10**6
	return False

def isFullHouse(pokerhand):
	if sameKind(pokerhand, 2) and sameKind(pokerhand, 3):
		return True,6 * 10**10 + sameKind(pokerhand, 3)[1] * 10**8 + sameKind(pokerhand, 2)[1] * 10**6
	return False

def isFlush(pokerhand):
	suit = pokerhand[0][1:2]
	for card in pokerhand:
		if card[1:2] != suit:
			return False
	return True, 5 * 10**10 + cardValue(pokerhand[0]) * 10**8

def isStright(pokerhand):
	for i in range(0, 4):
		value = cardValue(pokerhand[i])
		if cardValue(pokerhand[i])+1 != cardValue(pokerhand[i+1]):
			return False
	return True, 4 * 10**10 + cardValue(pokerhand[0]) * 10**8

def isThreeOfAKind(pokerhand):
	if sameKind(pokerhand, 3):
		if cardValue(pokerhand[0]) == cardValue(pokerhand[1]):
			return True, 3 * 10**10 + cardValue(pokerhand[0]) * 10**8 + cardValue(pokerhand[4]) * 10**6 + cardValue(pokerhand[3]) * 10**4
		elif cardValue(pokerhand[3]) == cardValue(pokerhand[4]):
			return True, 3 * 10**10 + cardValue(pokerhand[4]) * 10**8 + cardValue(pokerhand[1]) * 10**6 + cardValue(pokerhand[0]) * 10**4
		else:
			return True, 3 * 10**10 + cardValue(pokerhand[2]) * 10**8 + cardValue(pokerhand[4]) * 10**6 + cardValue(pokerhand[0]) * 10**4
	return False

def isTwoPair(pokerhand):

	tempPokerhand = pokerhand[:]
	
	value = 2 * 10**10

	#Find single card
	cardIndex = 0
	for i in range(0,len(tempPokerhand)):
		s = 0
		for j in range(0, len(tempPokerhand)):
			if cardValue(tempPokerhand[i]) != cardValue(tempPokerhand[j]):
				s += 1
		if s == 4:
			value += cardValue(tempPokerhand[i]) * 10**4
			cardIndex = i

	tempPokerhand.pop(cardIndex)

	#Check if last 4 cards are double pairs
	if cardValue(tempPokerhand[0]) == cardValue(tempPokerhand[1]) and cardValue(tempPokerhand[2]) == cardValue(tempPokerhand[3]):
		#Find first pair
		value += cardValue(tempPokerhand[0]) * 10**6
		#Find second pair
		value += cardValue(tempPokerhand[2]) * 10**8
		return True, value
	else:
		return False

def isPairHelpFunction(pokerhand):
	cardIndex = 0
	for i in range(0,len(pokerhand)):
		s = 0
		for j in range(0, len(pokerhand)):
			if cardValue(pokerhand[i]) == cardValue(pokerhand[j]) and i != j:
				return True, i
	return False

def isPair(pokerhand):

	value = 1 * 10**10
	tempPokerhand = pokerhand[:]
	#Find single card

	res = isPairHelpFunction(tempPokerhand)
	if res:
		value += cardValue(tempPokerhand[res[1]]) * 10**8
		tempPokerhand.pop(res[1])
		tempPokerhand.pop(res[1])

		power = 6
		for i, card in enumerate(reversed(tempPokerhand)):
			value += cardValue(card) * 10**power
			power -= 2
		return 	True, value

	return False

def isHighCard(pokerhand):
	#This will always return true

	value = 0 # * 10**10
	power = 8
	for i, card in enumerate(reversed(pokerhand)):
		value += cardValue(card) * 10**power
		power -= 2
	return True, value

def pokerhandToPoints(pokerhand):
	if isRoyalStrightFlush(pokerhand):
		#print("royal stright flush")
		return isRoyalStrightFlush(pokerhand)[1]
	elif isStrightFlush(pokerhand):
		#print("Stright flush")
		return isStrightFlush(pokerhand)[1]
	elif isFourOfAKind(pokerhand):
		#print("Four of a kind")
		return isFourOfAKind(pokerhand)[1]
	elif isFullHouse(pokerhand):
		#print("Full house")
		return isFullHouse(pokerhand)[1]
	elif isFlush(pokerhand):
		#print("Flush")
		return isFlush(pokerhand)[1]
	elif isStright(pokerhand):
		#print("Stright")
		return isStright(pokerhand)[1]
	elif isThreeOfAKind(pokerhand):
		#print("Three of a kind")
		return isThreeOfAKind(pokerhand)[1]
	elif isTwoPair(pokerhand):
		#print("Two pairs")
		return isTwoPair(pokerhand)[1]
	elif isPair(pokerhand):
		#print("Pair!")
		return isPair(pokerhand)[1]
	else:
		#print("some high card..")
		return isHighCard(pokerhand)[1]


h1win = 0
h2wins = 0

lines = open('poker.txt', 'r')
for line in lines:
	h1 = sortPokerHand(line[:-1].split()[0:5])
	h2 = sortPokerHand(line[:-1].split()[5:10])
	
	#print("-- Lets find out what we got --")
	#print("H1:")
	#print(h1)
	#print("H2:")
	#print(h2)

	h1points = pokerhandToPoints(h1)
	h2points = pokerhandToPoints(h2)

	if h1points > h2points:
		#print("Winner: H1")
		h1win += 1
	elif h1points < h2points:
		h2wins += 1
		#print("Winner: H2")
		pass
	else:
		print("Tie??")

	#sys.exit()

lines.close()

print(h1win)