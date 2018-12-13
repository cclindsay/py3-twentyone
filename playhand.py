# BlackJack Simulation - Playhand Class
# Cameron Lindsay, COSC 1336 021
# December 2016

#!python3

import random
import handvalue
from card import card
from deck import deck
from hand import hand

def PlayHand(): # Plays a single hand of blackjack -- No real gambling required!

	print()
	print('Starting a new round of Blackjack...')

	gameDeck = deck() # Deck object shuffles itself upon init...
	playerHand = hand()
	dealerHand = hand()
	playerHit = True
	# dealerHit = True # Currently Unused
	dealerThreshold = random.randint(16, 19) # Just a fun little logic tweak.

	gameDeck.shuffle() # Shuffled twice; extra nice...

	print('Dealing two cards each...')
	print()

	print('You are dealt the', playerHand.hit(gameDeck)) # I was going to iterate this with a loop
	dealerHand.hit(gameDeck) # But I don't think I can show the dealer's top card in a loop

	print('You are dealt the', playerHand.hit(gameDeck))

	print()
	print("Dealer's Top Card Showing:")
	print(dealerHand.hit(gameDeck)) # I hope that works; maybe we should use a dedicated 'top card' method?
	print()

	if dealerHand.blackjack():
		print('The Dealer was dealt a Blackjack! Ugh!')
		print("The Dealer's Hand:")
		dealerHand.Print()
		print("Dealer's Hand Value:", dealerHand.value())
		print('Better Luck Next Hand!')
		return False

	while playerHit:
		print('Your Hand:')
		playerHand.Print()
		print("Your Hand's Value:", playerHand.value())
		print()
		if playerHand.blackjack():
			print('Blackjack! It must be your lucky day!')
			return True
		choice = str(input('\a Would you like to Hit, or Stay? (Y/N) '))
		if choice[0].upper() in ('Y', 'H'):
			print()
			print('You hit, drawing the', playerHand.hit(gameDeck))
			print()
			if playerHand.have21():
				print('A Perfect 21! You must feel pretty lucky, huh?')
				playerHand.Print()
				print("Your Hand's Value:", playerHand.value())
				return True
			elif playerHand.bust():
				print('You bust! Sorry, friend. Better luck next time!')
				playerHand.Print()
				print("Your Hand's Value:", playerHand.value())
				return False
		else:
			print()
			playerHit = False
			print("You've chosen to stand at", playerHand.value())
			print()
		if dealerHand.value() < dealerThreshold: # It's not fun if you know what the dealer will do.
			print('Dealer hits, drawing the', dealerHand.hit(gameDeck)) 
			if dealerHand.have21():
				print('The Dealer hit 21! Tough Luck!')
				print("The Dealer's Hand:")
				dealerHand.Print()
				print("Dealer's Hand Value:", dealerHand.value())
				return False
			elif dealerHand.bust():
				print('The Dealer went bust! Sweet Revenge!')
				print("The Dealer's Hand:")
				dealerHand.Print()
				print("Dealer's Hand Value:", dealerHand.value())
				return True
		else:
			print('The Dealer has chosen to stay...')
		print()
# Complete Turn, Before Standing

	while not playerHit: # Dealer finishes playing up to final value
		if dealerHand.value() < dealerThreshold:
			print('Dealer hits, drawing the', dealerHand.hit(gameDeck))
			if dealerHand.have21():
				print('The Dealer hit 21! Tough Luck!')
				print("The Dealer's Hand:")
				dealerHand.Print()
				print("Dealer's Hand Value:", dealerHand.value())
				return False
			elif dealerHand.bust():
				print('The Dealer went bust! Sweet Revenge!')
				print("The Dealer's Hand:")
				dealerHand.Print()
				print("Dealer's Hand Value:", dealerHand.value())
				return True
		else: # Final Decision Suite
			if dealerHand.value() > playerHand.value():
				print("The Dealer Won. Oh well, them's the breaks...")
				print()
				print("The Dealer's Hand:")
				dealerHand.Print()
				print("Dealer's Hand Value:", dealerHand.value())
				print()
				print("Your Hand:")
				playerHand.Print()
				print("Your Hand's Value:", playerHand.value())
				return False

			if dealerHand.value() < playerHand.value():
				print("You beat the dealer! Not too shabby!")
				print()
				print("The Dealer's Hand:")
				dealerHand.Print()
				print("Dealer's Hand Value:", dealerHand.value())
				print()
				print("Your Hand:")
				playerHand.Print()
				print("Your Hand's Value:", playerHand.value())
				return True

			if dealerHand.value() == playerHand.value():
				print("A Tie?! This is why they say 'The House Always Wins'...")
				print()
				print("The Dealer's Hand:")
				dealerHand.Print()
				print("Dealer's Hand Value:", dealerHand.value())
				print()
				print("Your Hand:")
				playerHand.Print()
				print("Your Hand's Value:", playerHand.value())
				return False
		print()
# Complete Turn, After Standing

# I wonder if that's how the Jack of Spades and the Jack of Clubs each lost an eye...