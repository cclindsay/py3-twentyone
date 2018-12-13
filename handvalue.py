# BlackJack Simulation - Handvalue Function
# Cameron Lindsay, COSC 1336 021
# December 2016

#!python3

from card import card

def handvalue(hand):

	cardTotal = 0

	for card in hand.cardsInHand:
		if card.isace():
			if cardTotal < card.hival(): 
				cardTotal += card.hival() # 11 + 10 = Blackjack!
			else:
				cardTotal += card.loval() # 11 + 11 = Bust!	
		else:
			cardTotal += card.loval()

	return cardTotal