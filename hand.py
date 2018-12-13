# BlackJack Simulation - Hand Class
# Cameron Lindsay, COSC 1336 021
# December 2016

#!python3

import handvalue
from deck import deck

class hand:

	def __init__(self):
		self.cardsInHand = [] # Initialized blank list for cards in hand. Two in the hand...

	def hit(self, deck):
		self.cardsInHand.append(deck.deal()) # ...is worth one in the deck, I suppose
		return self.cardsInHand[-1] # Missed this bit the first time. No way to show dealer's top card without it.

	def value(self):
		return handvalue.handvalue(self)

	def Print(self):
		for card in self.cardsInHand:
			print(card)

	def bust(self):
		if self.value() > 21:
			return True
		return False

	def blackjack(self): # There's no saving grace... 
		if len(self.cardsInHand) == 2:
			if self.value() == 21:
				return True
		return False

	def have21(self): # ...quite like an Ace and a Face
		if self.value() == 21:
			return True
		return False