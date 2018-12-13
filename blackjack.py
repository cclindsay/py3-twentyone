# BlackJack Simulation - Main User Interface
# Cameron Lindsay, COSC 1336 021
# December 2016

#!python3

def main():

	import playhand

	title()

	playAgain = True
	winCount = 0
	lossCount = 0
	gameCount = 0

	while playAgain:
		if playhand.PlayHand():
			winCount += 1
		else:
			lossCount += 1

		gameCount += 1

		choice = str(input('Would you like to play another hand? (Y/N)'))

		if choice[0].upper() != 'Y':
			playAgain = False

	winPercent = int((float(winCount) / float(gameCount)) * 100.0)

	print('That was a fun game! Thank you for playing!')
	print()
	print('Here are you Game Stats:')
	print()
	print('Total Games Played:', gameCount)
	print('Games Won:', winCount)
	print('Games Lost:', lossCount)
	print()
	print('Percentage of Games Won:', str(winPercent)+'%')

	if gameCount >= 5:
		if winPercent > 25:
			print('Wow, you had a solid streak there!')
		if winPercent > 50:
			print("Lady Luck is really on your side, isn't she?")
		if winPercent > 75:
			print('Were you counting cards or something??!')

def title():

	titles = []
	titles.append('Welcome to Python3 BlackJack, by Cameron')
	titles.append('An ACC COSC 1336 Fall 2016 Production!')

	# padCount = 0 # Not used, currently using hard-coded spacing

	print('/'+('-'*78)+'\\')
	print('|'+('\\/'*39)+'|')
	fillGen(4)
	print('|'+('/\\'*8), ' '*44, ('/\\'*8)+'|')
	print('|'+('\\/'*8), ' '*44, ('\\/'*8)+'|')
	print('|'+('/\\'*8), ' ', titles[0],' ', ('/\\'*8)+'|')
	print('|'+('\\/'*8), ' '*44, ('\\/'*8)+'|')
	fillGen(4)
	print('|'+('/\\'*8), ' '*44, ('/\\'*8)+'|')
	print('|'+('\\/'*8), '  ', titles[1], '  ', ('\\/'*8)+'|')
	print('|'+('/\\'*8), ' '*44, ('/\\'*8)+'|')
	print('|'+('\\/'*8), ' '*44, ('\\/'*8)+'|')
	fillGen(4)
	print('|'+('/\\'*39)+'|')
	print('\\'+('-'*78)+'/')


def fillGen(count):

	for line in range(count):
		if line % 2 == 0:
			print('|'+('/\\'*39)+'|')
		else:
			print('|'+('\\/'*39)+'|')

main()