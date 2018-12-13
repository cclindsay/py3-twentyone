# BlackJack Simulation - Deck Class
# Cameron Lindsay, COSC 1336 021
# December 2016

#!python3

from card import card

class deck:

	def __init__(self):

		self.cardsInDeck = [] # Initialized blank deck to hold cards upon instancing

		for suit in card.suits:
			for name in card.names:
				self.cardsInDeck.append(card(name, suit))

		self.shuffle() # Surely we're not just starting with an unshuffled deck...

	def Print(self):
		for card in self.cardsInDeck:
			print(card)

	def deal(self):
		return self.cardsInDeck.pop(0) # ...goes the house. Dealer busts!

	def shuffle(self):
		import random
		random.shuffle(self.cardsInDeck)

	def stack(self): # Unused, allows simulated "dealer" to "cheat"
		self.cardsInDeck.sort(key = card.loval) # "Stacks" the deck; Aces on top
		return True # Catch this output to detect "cheating"