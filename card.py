# BlackJack Simulation - Card Class
# Cameron Lindsay, COSC 1336 021
# December 2016

#!python3

class card: # Note to Self: add support for Jokers? Later.

	suits = ('spades', 'hearts', 'clubs', 'diamonds')
	names = ('ace', 'two', 'three', 'four', 'five', 'six', 'seven',\
	 'eight', 'nine', 'ten', 'jack', 'queen', 'king')

	def __init__(self, name, suit):
		self.name = name
		self.suit = suit

	def __str__(self): # Looks fancy when you throw a .title() on it~
		self.printName = self.name.title()+' of '+self.suit.title()
		return self.printName

	def isace(self):
		if self.name == 'ace':
			return True
		return False

	def loval(self):
		values = {'ace':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,\
		 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10}
		return values[self.name]

	def hival(self):
		if self.isace():
			return (self.loval() + 10)
		return self.loval()

	def getsuit(self):
		return self.suit

	def getname(self):
		return self.name